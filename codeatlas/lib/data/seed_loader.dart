// lib/data/seed_loader.dart — Validates content.json and seeds/upgrades database.
//
// Responsibilities:
// 1. Parse and validate the content package (format_version, IDs, references,
//    enums, field content, code examples, quiz options, graph acyclicity).
// 2. Atomic seed on fresh database within a single transaction.
// 3. Idempotent upgrade: compare content_version, update changed records,
//    mark removed IDs as inactive. Never touch progress/notes/paths.
// 4. Rollback on any failure; leave old valid database intact.

import 'dart:convert';

import 'package:flutter/services.dart' show rootBundle;
import 'package:sqflite/sqflite.dart';

import 'models.dart';

/// Supported format_version for the JSON parser.
const int kSupportedFormatVersion = 1;

/// Result of a seed/upgrade operation.
class SeedResult {
  final bool success;
  final String? error;
  final int categoriesCount;
  final int topicsCount;
  final int quizzesCount;

  const SeedResult({
    required this.success,
    this.error,
    this.categoriesCount = 0,
    this.topicsCount = 0,
    this.quizzesCount = 0,
  });
}

enum VersionAction { initialSeed, skipEqual, upgradeHigher, rejectDowngrade }

/// Parsed and validated content package, ready to be written to database.
class ContentPackage {
  final int formatVersion;
  final int contentVersion;
  final String dataset;
  final String locale;
  final List<Category> categories;
  final List<Topic> topics;
  final List<Quiz> quizzes;

  const ContentPackage({
    required this.formatVersion,
    required this.contentVersion,
    required this.dataset,
    required this.locale,
    required this.categories,
    required this.topics,
    required this.quizzes,
  });

  factory ContentPackage.fromJson(Map<String, dynamic> data) =>
      SeedLoader.parseAndValidate(data);
}

class SeedLoader {
  final Database db;

  SeedLoader(this.db);

  /// Determine the appropriate action based on package and existing content versions.
  static VersionAction determineVersionAction(
    int packageVersion,
    int? existingVersion,
  ) {
    if (existingVersion == null) return VersionAction.initialSeed;
    if (packageVersion < existingVersion) return VersionAction.rejectDowngrade;
    if (packageVersion == existingVersion) return VersionAction.skipEqual;
    return VersionAction.upgradeHigher;
  }

  /// Load, validate, and seed/upgrade from bundled asset.
  Future<SeedResult> loadFromAsset() async {
    try {
      final jsonString = await rootBundle.loadString(
        'assets/content/content.json',
      );
      final data = jsonDecode(jsonString) as Map<String, dynamic>;
      return await seedFromMap(data);
    } catch (e) {
      return SeedResult(success: false, error: 'Gagal memuat konten: $e');
    }
  }

  /// Seed or upgrade from a parsed JSON map. Useful for testing.
  Future<SeedResult> seedFromMap(Map<String, dynamic> data) async {
    // 1. Parse and validate the package
    final ContentPackage package;
    try {
      package = parseAndValidate(data);
    } catch (e) {
      return SeedResult(success: false, error: 'Validasi gagal: $e');
    }

    // 2. Check current content_version
    final existing = await _getCurrentMeta();
    final action = determineVersionAction(
      package.contentVersion,
      existing?.contentVersion,
    );

    if (action == VersionAction.rejectDowngrade) {
      return SeedResult(
        success: false,
        error:
            'Downgrade versi konten ditolak '
            '(saat ini: ${existing!.contentVersion}, paket: ${package.contentVersion})',
        categoriesCount: 0,
        topicsCount: 0,
        quizzesCount: 0,
      );
    }

    if (action == VersionAction.skipEqual) {
      // Same version: do not rewrite content
      return const SeedResult(
        success: true,
        categoriesCount: 0,
        topicsCount: 0,
        quizzesCount: 0,
      );
    }

    if (action == VersionAction.upgradeHigher) {
      // Higher version: perform atomic upgrade within transaction
      try {
        await db.transaction((txn) async {
          await _upgrade(txn, package);
        });
        return SeedResult(
          success: true,
          categoriesCount: package.categories.length,
          topicsCount: package.topics.length,
          quizzesCount: package.quizzes.length,
        );
      } catch (e) {
        return SeedResult(
          success: false,
          error: 'Gagal memperbarui konten (rollback aman): $e',
        );
      }
    }

    // 3. Fresh install: insert all data in a single transaction
    try {
      await db.transaction((txn) async {
        await _freshSeed(txn, package);
      });
      return SeedResult(
        success: true,
        categoriesCount: package.categories.length,
        topicsCount: package.topics.length,
        quizzesCount: package.quizzes.length,
      );
    } catch (e) {
      return SeedResult(
        success: false,
        error: 'Gagal menyimpan konten ke database: $e',
      );
    }
  }

  // ─── Parsing & Validation ───

  static ContentPackage parseAndValidate(Map<String, dynamic> data) {
    // Format version
    final formatVersion = data['format_version'] as int? ?? 0;
    if (formatVersion != kSupportedFormatVersion) {
      throw FormatException(
        'format_version $formatVersion tidak didukung '
        '(didukung: $kSupportedFormatVersion)',
      );
    }

    final contentVersion = data['content_version'] as int? ?? 0;
    if (contentVersion <= 0) {
      throw FormatException('content_version harus > 0');
    }

    final dataset = data['dataset'] as String? ?? '';
    if (!['reference', 'production'].contains(dataset)) {
      throw FormatException('dataset tidak valid: $dataset');
    }

    final locale = data['locale'] as String? ?? '';
    if (locale.isEmpty) throw FormatException('locale tidak boleh kosong');

    // Parse categories
    final categoriesRaw = data['categories'] as List<dynamic>? ?? [];
    final categories = categoriesRaw
        .map((e) => Category.fromJson(e as Map<String, dynamic>))
        .toList();

    // Parse topics
    final topicsRaw = data['topics'] as List<dynamic>? ?? [];
    final topics = topicsRaw
        .map((e) => Topic.fromJson(e as Map<String, dynamic>))
        .toList();

    // Parse quizzes
    final quizzesRaw = data['quizzes'] as List<dynamic>? ?? [];
    final quizzes = quizzesRaw
        .map((e) => Quiz.fromJson(e as Map<String, dynamic>))
        .toList();

    // ─── Cross-reference validation ───

    final categoryIds = categories.map((c) => c.id).toSet();
    final topicIds = topics.map((t) => t.id).toSet();

    // Check duplicate category IDs
    if (categoryIds.length != categories.length) {
      final seen = <String>{};
      for (final c in categories) {
        if (!seen.add(c.id)) {
          throw FormatException('Duplikasi category ID: ${c.id}');
        }
      }
    }

    // Check duplicate topic IDs
    if (topicIds.length != topics.length) {
      final seen = <String>{};
      for (final t in topics) {
        if (!seen.add(t.id)) {
          throw FormatException('Duplikasi topic ID: ${t.id}');
        }
      }
    }

    // Check duplicate quiz IDs
    final quizIds = quizzes.map((q) => q.id).toSet();
    if (quizIds.length != quizzes.length) {
      final seen = <String>{};
      for (final q in quizzes) {
        if (!seen.add(q.id)) {
          throw FormatException('Duplikasi quiz ID: ${q.id}');
        }
      }
    }

    // Validate category hierarchy
    for (final cat in categories) {
      if (cat.kind == CategoryKind.group) {
        if (cat.parentId != null) {
          throw FormatException('Group category ${cat.id} harus parentId null');
        }
      } else {
        // domain
        if (cat.parentId == null) {
          throw FormatException('Domain category ${cat.id} harus punya parent');
        }
        if (cat.layer != ContentLayer.ecosystem) {
          throw FormatException(
            'Domain category ${cat.id} harus berlapis ecosystem',
          );
        }
        if (!categoryIds.contains(cat.parentId)) {
          throw FormatException(
            'Category ${cat.id}: parent ${cat.parentId} tidak ditemukan',
          );
        }
        final parent = categories.firstWhere((c) => c.id == cat.parentId);
        if (parent.kind != CategoryKind.group) {
          throw FormatException(
            'Category ${cat.id}: parent ${cat.parentId} bukan group',
          );
        }
        if (parent.layer != cat.layer) {
          throw FormatException('Category ${cat.id}: parent layer berbeda');
        }
      }
    }

    // Validate topics reference valid categories
    for (final topic in topics) {
      if (!categoryIds.contains(topic.categoryId)) {
        throw FormatException(
          'Topic ${topic.id}: category ${topic.categoryId} tidak ditemukan',
        );
      }
      final cat = categories.firstWhere((c) => c.id == topic.categoryId);
      // Fundamental topics must belong to fundamental group categories
      if (topic.id.startsWith('f-') && cat.layer != ContentLayer.fundamentals) {
        throw FormatException(
          'Topic ${topic.id}: fundamental topic pada category non-fundamental',
        );
      }
    }

    // Validate prerequisite references
    for (final topic in topics) {
      for (final prereqId in topic.prerequisiteIds) {
        if (prereqId == topic.id) {
          throw FormatException(
            'Topic ${topic.id}: self-reference pada prerequisites',
          );
        }
        if (!topicIds.contains(prereqId)) {
          throw FormatException(
            'Topic ${topic.id}: prerequisite $prereqId tidak ditemukan',
          );
        }
        if (topic.prerequisiteIds.where((id) => id == prereqId).length > 1) {
          throw FormatException(
            'Topic ${topic.id}: duplikasi prerequisite $prereqId',
          );
        }
      }
    }

    // Validate related references
    for (final topic in topics) {
      for (final relId in topic.relatedTopicIds) {
        if (relId == topic.id) {
          throw FormatException(
            'Topic ${topic.id}: self-reference pada related_topic_ids',
          );
        }
        if (!topicIds.contains(relId)) {
          throw FormatException(
            'Topic ${topic.id}: related $relId tidak ditemukan',
          );
        }
      }
    }

    // Detect prerequisite cycles using DFS with coloring
    _detectCycles(topics);

    // Validate quiz references
    for (final quiz in quizzes) {
      if (!topicIds.contains(quiz.topicId)) {
        throw FormatException(
          'Quiz ${quiz.id}: topic ${quiz.topicId} tidak ditemukan',
        );
      }
      // Active quizzes should reference active topics
      if (quiz.isActive) {
        final topic = topics.firstWhere((t) => t.id == quiz.topicId);
        if (!topic.isActive) {
          throw FormatException(
            'Quiz ${quiz.id}: merujuk topic inactive ${quiz.topicId}',
          );
        }
      }
    }

    // Validate code example uniqueness per (topic, comparison_key, language)
    for (final topic in topics) {
      final seen = <String>{};
      for (final ex in topic.codeExamples) {
        if (ex.comparisonKey != null) {
          final key = '${topic.id}|${ex.comparisonKey}|${ex.language}';
          if (!seen.add(key)) {
            throw FormatException(
              'Topic ${topic.id}: duplikasi (comparison_key=${ex.comparisonKey}, '
              'language=${ex.language})',
            );
          }
        }
      }
    }

    // Production dataset checks
    if (dataset == 'production') {
      _validateProductionDataset(categories, topics, quizzes);
    }

    return ContentPackage(
      formatVersion: formatVersion,
      contentVersion: contentVersion,
      dataset: dataset,
      locale: locale,
      categories: categories,
      topics: topics,
      quizzes: quizzes,
    );
  }

  /// Detect cycles in prerequisite graph using DFS three-color marking.
  static void _detectCycles(List<Topic> topics) {
    // white=0, gray=1, black=2
    final color = <String, int>{};
    final adj = <String, List<String>>{};

    for (final t in topics) {
      color[t.id] = 0;
      adj[t.id] = t.prerequisiteIds;
    }

    void dfs(String u) {
      color[u] = 1; // gray - visiting
      for (final v in adj[u] ?? []) {
        if (color[v] == 1) {
          throw FormatException('Siklus prasyarat terdeteksi: $u → $v');
        }
        if (color[v] == 0) {
          dfs(v);
        }
      }
      color[u] = 2; // black - done
    }

    for (final t in topics) {
      if (color[t.id] == 0) {
        dfs(t.id);
      }
    }
  }

  /// Additional checks for production dataset.
  static void _validateProductionDataset(
    List<Category> categories,
    List<Topic> topics,
    List<Quiz> quizzes,
  ) {
    // All 47 fundamental topic IDs must be present
    const fundamentalIds = [
      'f-programming-logic',
      'f-variables-data-types',
      'f-operators',
      'f-conditionals',
      'f-loops',
      'f-functions',
      'f-scope',
      'f-type-system',
      'f-recursion',
      'f-data-structures',
      'f-algorithms',
      'f-big-o',
      'f-oop',
      'f-functional-programming',
      'f-clean-code',
      'f-design-patterns',
      'f-software-architecture',
      'f-error-handling',
      'f-debugging',
      'f-testing',
      'f-memory',
      'f-references',
      'f-input-output',
      'f-file-system',
      'f-operating-system',
      'f-modules-packages',
      'f-dependencies',
      'f-build-compilation',
      'f-runtime',
      'f-git',
      'f-terminal',
      'f-networking',
      'f-http-web',
      'f-apis',
      'f-serialization',
      'f-databases',
      'f-sql',
      'f-data-modeling',
      'f-auth',
      'f-security',
      'f-concurrency',
      'f-async',
      'f-deployment',
      'f-logging-monitoring',
      'f-sdlc-agile',
      'f-documentation',
      'f-computer-science',
    ];

    const ecosystemDomainIds = [
      'e-languages',
      'e-compilers',
      'e-runtime',
      'e-package-managers',
      'e-build-tools',
      'e-frameworks',
      'e-libraries',
      'e-orm',
      'e-frontend',
      'e-backend',
      'e-mobile',
      'e-desktop',
      'e-games',
      'e-embedded',
      'e-graphics',
      'e-databases',
      'e-api-communication',
      'e-message-brokers',
      'e-caching',
      'e-dsa',
      'e-paradigms',
      'e-system-programming',
      'e-computer-science',
      'e-architecture',
      'e-patterns',
      'e-distributed',
      'e-networking',
      'e-operating-systems',
      'e-shells',
      'e-web-servers',
      'e-cloud',
      'e-iac',
      'e-orchestration',
      'e-testing',
      'e-debugging',
      'e-security',
      'e-cybersecurity',
      'e-accessibility',
      'e-devops',
      'e-observability',
      'e-production',
      'e-developer-tools',
      'e-data-engineering',
      'e-data-science',
      'e-ai-ml',
      'e-version-control',
      'e-engineering-process',
      'e-ui-ux',
      'e-technical-docs',
      'e-localization',
      'e-blockchain',
      'e-open-source',
    ];

    final activeTopicIds = topics
        .where((t) => t.isActive)
        .map((t) => t.id)
        .toSet();

    for (final id in fundamentalIds) {
      if (!activeTopicIds.contains(id)) {
        throw FormatException(
          'Production: fundamental topic $id tidak ditemukan atau inactive',
        );
      }
    }

    for (final domainId in ecosystemDomainIds) {
      final overviewId = '$domainId-overview';
      if (!activeTopicIds.contains(overviewId)) {
        throw FormatException(
          'Production: ecosystem overview $overviewId tidak ditemukan atau inactive',
        );
      }
    }

    // Check domain categories exist
    final catIds = categories.map((c) => c.id).toSet();
    for (final domainId in ecosystemDomainIds) {
      if (!catIds.contains(domainId)) {
        throw FormatException(
          'Production: domain category $domainId tidak ditemukan',
        );
      }
    }

    // Quiz minimums: 10+ language, 20+ concept, 15+ different topics
    final activeQuizzes = quizzes.where((q) => q.isActive).toList();
    final languageQuizzes = activeQuizzes
        .where((q) => q.type == QuizType.language)
        .length;
    final conceptQuizzes = activeQuizzes
        .where((q) => q.type == QuizType.concept)
        .length;
    if (languageQuizzes < 10) {
      throw FormatException(
        'Production: butuh minimal 10 kuis bahasa, ada $languageQuizzes',
      );
    }
    if (conceptQuizzes < 20) {
      throw FormatException(
        'Production: butuh minimal 20 kuis konsep, ada $conceptQuizzes',
      );
    }
    final quizTopics = activeQuizzes.map((q) => q.topicId).toSet();
    if (quizTopics.length < 15) {
      throw FormatException(
        'Production: kuis harus mencakup minimal 15 topik berbeda, ada ${quizTopics.length}',
      );
    }

    // Comparison groups: minimum 9
    final comparisonGroups = <String>{};
    for (final topic in topics.where((t) => t.isActive)) {
      for (final ex in topic.codeExamples) {
        if (ex.comparisonKey != null) {
          comparisonGroups.add('${topic.id}|${ex.comparisonKey}');
        }
      }
    }
    // Count groups with 2+ languages
    final groupLanguages = <String, Set<String>>{};
    for (final topic in topics.where((t) => t.isActive)) {
      for (final ex in topic.codeExamples) {
        if (ex.comparisonKey != null) {
          final key = '${topic.id}|${ex.comparisonKey}';
          groupLanguages.putIfAbsent(key, () => {}).add(ex.language);
        }
      }
    }
    final validGroups = groupLanguages.entries
        .where((e) => e.value.length >= 2)
        .length;
    if (validGroups < 9) {
      throw FormatException(
        'Production: butuh minimal 9 kelompok perbandingan, ada $validGroups',
      );
    }
  }

  // ─── Database operations ───

  Future<ContentMeta?> _getCurrentMeta() async {
    final rows = await db.query('content_meta', where: 'id = 1');
    if (rows.isEmpty) return null;
    return ContentMeta.fromDb(rows.first);
  }

  /// Fresh seed: insert everything in order within a transaction.
  Future<void> _freshSeed(Transaction txn, ContentPackage pkg) async {
    // Insert group categories first (parent_id = null)
    final groups = pkg.categories
        .where((c) => c.kind == CategoryKind.group)
        .toList();
    for (final cat in groups) {
      await txn.insert('categories', cat.toDbMap());
    }

    // Then domain categories (parent_id references group)
    final domains = pkg.categories
        .where((c) => c.kind == CategoryKind.domain)
        .toList();
    for (final cat in domains) {
      await txn.insert('categories', cat.toDbMap());
    }

    // Insert all topics
    for (final topic in pkg.topics) {
      await txn.insert('topics', topic.toDbMap());
    }

    // Insert prerequisite edges
    for (final topic in pkg.topics) {
      for (final prereqId in topic.prerequisiteIds) {
        await txn.insert('topic_prerequisites', {
          'topic_id': topic.id,
          'prerequisite_id': prereqId,
        });
      }
    }

    // Insert related edges
    for (final topic in pkg.topics) {
      for (final relId in topic.relatedTopicIds) {
        await txn.insert('topic_related', {
          'topic_id': topic.id,
          'related_topic_id': relId,
        });
      }
    }

    // Insert quizzes
    for (final quiz in pkg.quizzes) {
      await txn.insert('quizzes', quiz.toDbMap());
    }

    // Insert content_meta last
    await txn.insert('content_meta', {
      'id': 1,
      'content_version': pkg.contentVersion,
      'dataset': pkg.dataset,
      'locale': pkg.locale,
    });
  }

  /// Upgrade existing content without touching user data (progress, notes, paths).
  Future<void> _upgrade(Transaction txn, ContentPackage pkg) async {
    final newTopicIds = pkg.topics.map((t) => t.id).toSet();
    final newQuizIds = pkg.quizzes.map((q) => q.id).toSet();

    // Upsert categories: groups first, then domains
    final groups = pkg.categories
        .where((c) => c.kind == CategoryKind.group)
        .toList();
    for (final cat in groups) {
      await _upsertCategory(txn, cat);
    }
    final domains = pkg.categories
        .where((c) => c.kind == CategoryKind.domain)
        .toList();
    for (final cat in domains) {
      await _upsertCategory(txn, cat);
    }

    // Upsert topics
    for (final topic in pkg.topics) {
      await _upsertTopic(txn, topic);
    }

    // Refresh prerequisite edges for active topics
    for (final topic in pkg.topics) {
      await txn.delete(
        'topic_prerequisites',
        where: 'topic_id = ?',
        whereArgs: [topic.id],
      );
      for (final prereqId in topic.prerequisiteIds) {
        await txn.insert('topic_prerequisites', {
          'topic_id': topic.id,
          'prerequisite_id': prereqId,
        });
      }
    }

    // Refresh related edges for active topics
    for (final topic in pkg.topics) {
      await txn.delete(
        'topic_related',
        where: 'topic_id = ?',
        whereArgs: [topic.id],
      );
      for (final relId in topic.relatedTopicIds) {
        await txn.insert('topic_related', {
          'topic_id': topic.id,
          'related_topic_id': relId,
        });
      }
    }

    // Upsert quizzes
    for (final quiz in pkg.quizzes) {
      await _upsertQuiz(txn, quiz);
    }

    // Mark missing topics as inactive (don't delete, preserve user data)
    final existingTopicIds = (await txn.query(
      'topics',
      columns: ['id'],
    )).map((r) => r['id'] as String).toSet();
    for (final existingId in existingTopicIds) {
      if (!newTopicIds.contains(existingId)) {
        await txn.update(
          'topics',
          {'is_active': 0},
          where: 'id = ?',
          whereArgs: [existingId],
        );
      }
    }

    // Mark missing quizzes as inactive
    final existingQuizIds = (await txn.query(
      'quizzes',
      columns: ['id'],
    )).map((r) => r['id'] as String).toSet();
    for (final existingId in existingQuizIds) {
      if (!newQuizIds.contains(existingId)) {
        await txn.update(
          'quizzes',
          {'is_active': 0},
          where: 'id = ?',
          whereArgs: [existingId],
        );
      }
    }

    // Update content_meta
    await txn.update('content_meta', {
      'content_version': pkg.contentVersion,
      'dataset': pkg.dataset,
      'locale': pkg.locale,
    }, where: 'id = 1');
  }

  Future<void> _upsertCategory(Transaction txn, Category cat) async {
    final existing = await txn.query(
      'categories',
      where: 'id = ?',
      whereArgs: [cat.id],
    );
    if (existing.isEmpty) {
      await txn.insert('categories', cat.toDbMap());
    } else {
      await txn.update(
        'categories',
        cat.toDbMap()..remove('id'),
        where: 'id = ?',
        whereArgs: [cat.id],
      );
    }
  }

  Future<void> _upsertTopic(Transaction txn, Topic topic) async {
    final existing = await txn.query(
      'topics',
      where: 'id = ?',
      whereArgs: [topic.id],
    );
    if (existing.isEmpty) {
      await txn.insert('topics', topic.toDbMap());
    } else {
      await txn.update(
        'topics',
        topic.toDbMap()..remove('id'),
        where: 'id = ?',
        whereArgs: [topic.id],
      );
    }
  }

  Future<void> _upsertQuiz(Transaction txn, Quiz quiz) async {
    final existing = await txn.query(
      'quizzes',
      where: 'id = ?',
      whereArgs: [quiz.id],
    );
    if (existing.isEmpty) {
      await txn.insert('quizzes', quiz.toDbMap());
    } else {
      await txn.update(
        'quizzes',
        quiz.toDbMap()..remove('id'),
        where: 'id = ?',
        whereArgs: [quiz.id],
      );
    }
  }
}
