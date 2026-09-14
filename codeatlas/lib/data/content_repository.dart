// lib/data/content_repository.dart — Read-only queries for content, search,
// relations, quizzes, and comparison groups.

import 'package:sqflite/sqflite.dart';

import 'models.dart';

class ContentRepository {
  final Database db;

  // In-memory catalog cache loaded once after seed.
  List<Category>? _categoriesCache;
  List<Topic>? _topicsCache;

  ContentRepository(this.db);

  void clearCache() {
    _categoriesCache = null;
    _topicsCache = null;
  }

  // ─── Categories ───

  Future<List<Category>> getAllCategories() async {
    if (_categoriesCache != null) return _categoriesCache!;
    final rows = await db.query('categories', orderBy: 'sort_order ASC');
    _categoriesCache = rows.map((r) => Category.fromDb(r)).toList();
    return _categoriesCache!;
  }

  Future<List<Category>> getCategoriesByLayer(ContentLayer layer) async {
    final all = await getAllCategories();
    return all.where((c) => c.layer == layer).toList();
  }

  Future<List<Category>> getGroupCategories(ContentLayer layer) async {
    final all = await getAllCategories();
    return all
        .where((c) => c.layer == layer && c.kind == CategoryKind.group)
        .toList();
  }

  Future<List<Category>> getDomainsByGroup(String groupId) async {
    final all = await getAllCategories();
    return all
        .where((c) => c.kind == CategoryKind.domain && c.parentId == groupId)
        .toList();
  }

  // ─── Topics ───

  Future<List<Topic>> getAllActiveTopics() async {
    if (_topicsCache != null) return _topicsCache!;
    final rows = await db.query(
      'topics',
      where: 'is_active = 1',
      orderBy: 'sort_order ASC',
    );
    _topicsCache = rows.map((r) => Topic.fromDb(r)).toList();
    return _topicsCache!;
  }

  Future<List<Topic>> getTopicsByCategory(String categoryId) async {
    final all = await getAllActiveTopics();
    return all.where((t) => t.categoryId == categoryId).toList();
  }

  Future<List<Topic>> getTopicsByLayer(ContentLayer layer) async {
    final categories = await getCategoriesByLayer(layer);
    final catIds = categories.map((c) => c.id).toSet();
    final all = await getAllActiveTopics();
    return all.where((t) => catIds.contains(t.categoryId)).toList();
  }

  Future<Topic?> getTopicById(String id) async {
    final rows = await db.query('topics', where: 'id = ?', whereArgs: [id]);
    if (rows.isEmpty) return null;
    final topic = Topic.fromDb(rows.first);

    // Load relations
    final prereqs = await db.query(
      'topic_prerequisites',
      where: 'topic_id = ?',
      whereArgs: [id],
    );
    final related = await db.query(
      'topic_related',
      where: 'topic_id = ?',
      whereArgs: [id],
    );

    return topic.copyWith(
      prerequisiteIds: prereqs
          .map((r) => r['prerequisite_id'] as String)
          .toList(),
      relatedTopicIds: related
          .map((r) => r['related_topic_id'] as String)
          .toList(),
    );
  }

  /// Get topics that directly require this topic as a prerequisite.
  Future<List<String>> getDependentTopicIds(String topicId) async {
    final rows = await db.query(
      'topic_prerequisites',
      where: 'prerequisite_id = ?',
      whereArgs: [topicId],
    );
    return rows.map((r) => r['topic_id'] as String).toList();
  }

  /// Get all prerequisite IDs transitively.
  Future<Set<String>> getTransitivePrerequisites(String topicId) async {
    final result = <String>{};
    final visited = <String>{};
    final queue = <String>[topicId];

    while (queue.isNotEmpty) {
      final current = queue.removeLast();
      if (!visited.add(current)) continue;

      final rows = await db.query(
        'topic_prerequisites',
        where: 'topic_id = ?',
        whereArgs: [current],
      );
      for (final row in rows) {
        final prereqId = row['prerequisite_id'] as String;
        result.add(prereqId);
        queue.add(prereqId);
      }
    }
    return result;
  }

  /// Build prerequisite graph for all active topics.
  Future<Map<String, List<String>>> getPrerequisiteGraph() async {
    final rows = await db.rawQuery('''
      SELECT tp.topic_id, tp.prerequisite_id
      FROM topic_prerequisites tp
      JOIN topics t ON t.id = tp.topic_id AND t.is_active = 1
      JOIN topics t2 ON t2.id = tp.prerequisite_id AND t2.is_active = 1
    ''');
    final graph = <String, List<String>>{};
    for (final row in rows) {
      final topicId = row['topic_id'] as String;
      final prereqId = row['prerequisite_id'] as String;
      graph.putIfAbsent(topicId, () => []).add(prereqId);
    }
    return graph;
  }

  // ─── Search ───
  // ponytail: linear scan for ~99 articles; use FTS when search doesn't meet target.

  Future<List<Topic>> search(
    String query, {
    ContentLayer? layer,
    String? categoryId,
    Difficulty? level,
  }) async {
    final allTopics = await getAllActiveTopics();
    final allCategories = await getAllCategories();
    final catIds = layer != null
        ? allCategories.where((c) => c.layer == layer).map((c) => c.id).toSet()
        : null;

    final categoryChildIds = <String, Set<String>>{};
    for (final c in allCategories) {
      if (c.parentId != null) {
        categoryChildIds.putIfAbsent(c.parentId!, () => {}).add(c.id);
      }
    }

    var filtered = allTopics.where((t) {
      if (catIds != null && !catIds.contains(t.categoryId)) return false;
      if (categoryId != null) {
        final matchesDirect = t.categoryId == categoryId;
        final matchesGroup =
            categoryChildIds[categoryId]?.contains(t.categoryId) ?? false;
        if (!matchesDirect && !matchesGroup) return false;
      }
      if (level != null && t.level != level) return false;
      return true;
    });

    if (query.trim().isEmpty) {
      return filtered.toList();
    }

    final tokens = query
        .toLowerCase()
        .split(RegExp(r'\s+'))
        .where((s) => s.isNotEmpty);

    final results = <_SearchResult>[];
    for (final topic in filtered) {
      final searchable = [
        topic.title,
        topic.summary,
        topic.explanationSimple,
        topic.explanationTechnical,
        topic.whyVibecodingMatters,
        ...topic.keywords,
      ].join(' ').toLowerCase();

      final titleLower = topic.title.toLowerCase();

      if (tokens.every((token) => searchable.contains(token))) {
        // Scoring: exact title match first, then prefix, then rest
        int score = 0;
        final queryLower = query.toLowerCase().trim();
        if (titleLower == queryLower) {
          score = 3;
        } else if (titleLower.startsWith(queryLower)) {
          score = 2;
        } else if (titleLower.contains(queryLower)) {
          score = 1;
        }
        results.add(_SearchResult(topic: topic, score: score));
      }
    }

    results.sort((a, b) {
      final scoreCompare = b.score.compareTo(a.score);
      if (scoreCompare != 0) return scoreCompare;
      return a.topic.sortOrder.compareTo(b.topic.sortOrder);
    });

    return results.map((r) => r.topic).toList();
  }

  // ─── Quizzes ───

  Future<List<Quiz>> getActiveQuizzes({
    QuizType? type,
    ContentLayer? layer,
    Difficulty? level,
  }) async {
    final rows = await db.query('quizzes', where: 'is_active = 1');
    var quizzes = rows.map((r) => Quiz.fromDb(r)).toList();

    if (type != null) {
      quizzes = quizzes.where((q) => q.type == type).toList();
    }
    if (level != null) {
      quizzes = quizzes.where((q) => q.level == level).toList();
    }
    if (layer != null) {
      final allCategories = await getAllCategories();
      final catIds = allCategories
          .where((c) => c.layer == layer)
          .map((c) => c.id)
          .toSet();
      final allTopics = await getAllActiveTopics();
      final layerTopicIds = allTopics
          .where((t) => catIds.contains(t.categoryId))
          .map((t) => t.id)
          .toSet();
      quizzes = quizzes
          .where((q) => layerTopicIds.contains(q.topicId))
          .toList();
    }
    return quizzes;
  }

  // ─── Comparison Groups ───

  /// Returns comparison groups with 2+ languages, keyed by (topic_id, comparison_key).
  Future<List<ComparisonGroup>> getComparisonGroups() async {
    final allTopics = await getAllActiveTopics();
    final groups = <String, ComparisonGroup>{};

    for (final topic in allTopics) {
      for (final ex in topic.codeExamples) {
        if (ex.comparisonKey == null) continue;
        final key = '${topic.id}|${ex.comparisonKey}';
        groups.putIfAbsent(
          key,
          () => ComparisonGroup(
            topicId: topic.id,
            topicTitle: topic.title,
            comparisonKey: ex.comparisonKey!,
            examples: [],
          ),
        );
        groups[key]!.examples.add(ex);
      }
    }

    // Only return groups with 2+ languages
    return groups.values
        .where((g) => g.examples.map((e) => e.language).toSet().length >= 2)
        .toList();
  }

  /// Get available languages across all comparison groups.
  Future<Set<String>> getComparisonLanguages() async {
    final groups = await getComparisonGroups();
    final languages = <String>{};
    for (final g in groups) {
      for (final ex in g.examples) {
        languages.add(ex.language);
      }
    }
    return languages;
  }

  // ─── Content Meta ───

  Future<ContentMeta?> getContentMeta() async {
    final rows = await db.query('content_meta', where: 'id = 1');
    if (rows.isEmpty) return null;
    return ContentMeta.fromDb(rows.first);
  }

  /// Count of active topics.
  Future<int> getActiveTopicCount() async {
    final result = await db.rawQuery(
      'SELECT COUNT(*) as cnt FROM topics WHERE is_active = 1',
    );
    return result.first['cnt'] as int;
  }

  /// Count of active topics by layer.
  Future<int> getActiveTopicCountByLayer(ContentLayer layer) async {
    final categories = await getCategoriesByLayer(layer);
    final catIds = categories.map((c) => c.id).toSet();
    final topics = await getAllActiveTopics();
    return topics.where((t) => catIds.contains(t.categoryId)).length;
  }
}

class _SearchResult {
  final Topic topic;
  final int score;
  _SearchResult({required this.topic, required this.score});
}

class ComparisonGroup {
  final String topicId;
  final String topicTitle;
  final String comparisonKey;
  final List<CodeExample> examples;

  ComparisonGroup({
    required this.topicId,
    required this.topicTitle,
    required this.comparisonKey,
    required this.examples,
  });
}
