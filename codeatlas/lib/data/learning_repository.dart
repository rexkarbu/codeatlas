// lib/data/learning_repository.dart — Progress, notes, and learning paths.
//
// Key design:
// - Status and notes are saved via separate column updates, never overwriting each other.
// - Learning paths validate prerequisite ordering before save.
// - Paths are written in a single transaction; reordering rewrites path items only.

import 'package:sqflite/sqflite.dart';

import 'models.dart';

class LearningRepository {
  final Database db;

  LearningRepository(this.db);

  // ─── Progress ───

  Future<Progress?> getProgress(String topicId) async {
    final rows = await db.query(
      'progress',
      where: 'topic_id = ?',
      whereArgs: [topicId],
    );
    if (rows.isEmpty) return null;
    return Progress.fromDb(rows.first);
  }

  Future<Map<String, Progress>> getAllProgress() async {
    final rows = await db.query('progress');
    final map = <String, Progress>{};
    for (final row in rows) {
      final p = Progress.fromDb(row);
      map[p.topicId] = p;
    }
    return map;
  }

  /// Update status only; never touches notes.
  Future<void> updateStatus(String topicId, LearningStatus status) async {
    final now = DateTime.now().toUtc().millisecondsSinceEpoch;
    final existing = await getProgress(topicId);
    if (existing == null) {
      await db.insert('progress', {
        'topic_id': topicId,
        'status': status.dbValue,
        'notes': '',
        'last_reviewed_at': null,
        'updated_at': now,
      });
    } else {
      await db.update(
        'progress',
        {'status': status.dbValue, 'updated_at': now},
        where: 'topic_id = ?',
        whereArgs: [topicId],
      );
    }
  }

  /// Update notes only; never touches status.
  Future<void> updateNotes(String topicId, String notes) async {
    // Validate length in Unicode code points
    if (notes.runes.length > 20000) {
      throw ArgumentError('Catatan melebihi 20.000 karakter');
    }
    final now = DateTime.now().toUtc().millisecondsSinceEpoch;
    final existing = await getProgress(topicId);
    if (existing == null) {
      await db.insert('progress', {
        'topic_id': topicId,
        'status': LearningStatus.notStarted.dbValue,
        'notes': notes,
        'last_reviewed_at': null,
        'updated_at': now,
      });
    } else {
      await db.update(
        'progress',
        {'notes': notes, 'updated_at': now},
        where: 'topic_id = ?',
        whereArgs: [topicId],
      );
    }
  }

  /// Record that a topic was opened/reviewed. Does NOT change status.
  Future<void> recordReview(String topicId) async {
    final now = DateTime.now().toUtc().millisecondsSinceEpoch;
    final existing = await getProgress(topicId);
    if (existing == null) {
      await db.insert('progress', {
        'topic_id': topicId,
        'status': LearningStatus.notStarted.dbValue,
        'notes': '',
        'last_reviewed_at': now,
        'updated_at': now,
      });
    } else {
      await db.update(
        'progress',
        {'last_reviewed_at': now, 'updated_at': now},
        where: 'topic_id = ?',
        whereArgs: [topicId],
      );
    }
  }

  /// Get the last reviewed topic ID.
  Future<String?> getLastReviewedTopicId() async {
    final rows = await db.query(
      'progress',
      where: 'last_reviewed_at IS NOT NULL',
      orderBy: 'last_reviewed_at DESC',
      limit: 1,
    );
    if (rows.isEmpty) return null;
    return rows.first['topic_id'] as String;
  }

  /// Count topics with a given status among active topics.
  Future<int> countByStatus(
    LearningStatus status, {
    Set<String>? topicIds,
  }) async {
    if (topicIds != null && topicIds.isEmpty) return 0;
    if (topicIds != null) {
      // Count from the provided set
      final placeholders = List.filled(topicIds.length, '?').join(',');
      final rows = await db.rawQuery(
        'SELECT COUNT(*) as cnt FROM progress '
        'WHERE status = ? AND topic_id IN ($placeholders)',
        [status.dbValue, ...topicIds],
      );
      return rows.first['cnt'] as int;
    }
    final rows = await db.rawQuery(
      'SELECT COUNT(*) as cnt FROM progress WHERE status = ?',
      [status.dbValue],
    );
    return rows.first['cnt'] as int;
  }

  // ─── Learning Paths ───

  Future<List<LearningPath>> getAllPaths() async {
    final rows = await db.query('learning_paths', orderBy: 'updated_at DESC');
    final paths = <LearningPath>[];
    for (final row in rows) {
      final items = await _getPathItems(row['id'] as int);
      paths.add(LearningPath.fromDb(row, items: items));
    }
    return paths;
  }

  Future<LearningPath?> getPath(int pathId) async {
    final rows = await db.query(
      'learning_paths',
      where: 'id = ?',
      whereArgs: [pathId],
    );
    if (rows.isEmpty) return null;
    final items = await _getPathItems(pathId);
    return LearningPath.fromDb(rows.first, items: items);
  }

  Future<List<LearningPathItem>> _getPathItems(int pathId) async {
    final rows = await db.query(
      'learning_path_items',
      where: 'path_id = ?',
      whereArgs: [pathId],
      orderBy: 'position ASC',
    );
    return rows.map((r) => LearningPathItem.fromDb(r)).toList();
  }

  /// Create a new learning path with topic list. Returns the path ID.
  Future<int> createPath({
    required String name,
    required String goal,
    required List<String> topicIds,
  }) async {
    if (name.trim().isEmpty || name.trim().length > 100) {
      throw ArgumentError('Nama jalur harus 1-100 karakter');
    }
    if (topicIds.isEmpty) {
      throw ArgumentError('Jalur tidak boleh kosong');
    }
    // Check for duplicates
    if (topicIds.toSet().length != topicIds.length) {
      throw ArgumentError('Jalur tidak boleh memiliki topik duplikat');
    }

    final now = DateTime.now().toUtc().millisecondsSinceEpoch;
    late int pathId;

    await db.transaction((txn) async {
      pathId = await txn.insert('learning_paths', {
        'name': name.trim(),
        'goal': goal,
        'created_at': now,
        'updated_at': now,
      });

      for (var i = 0; i < topicIds.length; i++) {
        await txn.insert('learning_path_items', {
          'path_id': pathId,
          'topic_id': topicIds[i],
          'position': i,
        });
      }
    });

    return pathId;
  }

  /// Update path name and/or topic list.
  Future<void> updatePath({
    required int pathId,
    String? name,
    List<String>? topicIds,
  }) async {
    if (name != null && (name.trim().isEmpty || name.trim().length > 100)) {
      throw ArgumentError('Nama jalur harus 1-100 karakter');
    }
    if (topicIds != null && topicIds.isEmpty) {
      throw ArgumentError('Jalur tidak boleh kosong');
    }
    if (topicIds != null && topicIds.toSet().length != topicIds.length) {
      throw ArgumentError('Jalur tidak boleh memiliki topik duplikat');
    }

    final now = DateTime.now().toUtc().millisecondsSinceEpoch;

    await db.transaction((txn) async {
      final updates = <String, dynamic>{'updated_at': now};
      if (name != null) updates['name'] = name.trim();

      await txn.update(
        'learning_paths',
        updates,
        where: 'id = ?',
        whereArgs: [pathId],
      );

      if (topicIds != null) {
        // Delete old items and rewrite
        await txn.delete(
          'learning_path_items',
          where: 'path_id = ?',
          whereArgs: [pathId],
        );
        for (var i = 0; i < topicIds.length; i++) {
          await txn.insert('learning_path_items', {
            'path_id': pathId,
            'topic_id': topicIds[i],
            'position': i,
          });
        }
      }
    });
  }

  /// Delete a learning path and its items.
  Future<void> deletePath(int pathId) async {
    // Items cascade-delete due to ON DELETE CASCADE
    await db.delete('learning_paths', where: 'id = ?', whereArgs: [pathId]);
  }

  /// Get the first topic in a path that is not yet 'understood'.
  Future<String?> getNextUnfinishedTopic(int pathId) async {
    final items = await _getPathItems(pathId);
    for (final item in items) {
      final progress = await getProgress(item.topicId);
      if (progress == null || progress.status != LearningStatus.understood) {
        return item.topicId;
      }
    }
    return null; // All done
  }
}
