// test/data_migration_backup_test.dart — Unit test for user data preservation & backup format.
import 'package:flutter_test/flutter_test.dart';
import 'package:codeatlas/data/learning_repository.dart';
import 'package:sqflite/sqflite.dart';

class FakeDatabase implements Database {
  final Map<String, List<Map<String, dynamic>>> tables = {
    'progress': [],
    'learning_paths': [],
    'learning_path_items': [],
    'topics': [
      {'id': 'topic-1'},
      {'id': 'topic-2'},
    ],
  };

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Map<String, Object?>>> query(
    String table, {
    bool? distinct,
    List<String>? columns,
    String? where,
    List<Object?>? whereArgs,
    String? groupBy,
    String? having,
    String? orderBy,
    int? limit,
    int? offset,
  }) async {
    final list = tables[table] ?? [];
    if (whereArgs != null && whereArgs.isNotEmpty) {
      if (where!.contains('id = ?')) {
        return list.where((r) => r['id'] == whereArgs.first).toList();
      }
      if (where.contains('topic_id = ?')) {
        return list.where((r) => r['topic_id'] == whereArgs.first).toList();
      }
      if (where.contains('path_id = ?')) {
        return list.where((r) => r['path_id'] == whereArgs.first).toList();
      }
    }
    return list;
  }

  @override
  Future<T> transaction<T>(
    Future<T> Function(Transaction txn) action, {
    bool? exclusive,
  }) async {
    final fakeTxn = FakeTransaction(this);
    return action(fakeTxn);
  }
}

class FakeTransaction implements Transaction {
  final FakeDatabase db;
  FakeTransaction(this.db);

  @override
  dynamic noSuchMethod(Invocation invocation) => super.noSuchMethod(invocation);

  @override
  Future<List<Map<String, Object?>>> query(
    String table, {
    bool? distinct,
    List<String>? columns,
    String? where,
    List<Object?>? whereArgs,
    String? groupBy,
    String? having,
    String? orderBy,
    int? limit,
    int? offset,
  }) async {
    return db.query(table, where: where, whereArgs: whereArgs);
  }

  @override
  Future<int> insert(
    String table,
    Map<String, Object?> values, {
    String? nullColumnHack,
    ConflictAlgorithm? conflictAlgorithm,
  }) async {
    final list = db.tables[table] ?? [];
    final map = Map<String, dynamic>.from(values);
    if (table == 'learning_paths' && !map.containsKey('id')) {
      map['id'] = list.length + 1;
    }
    list.removeWhere((item) {
      if (table == 'progress') return item['topic_id'] == map['topic_id'];
      return false;
    });
    list.add(map);
    return (map['id'] as int?) ?? 1;
  }
}

void main() {
  test('exportUserData formats payload correctly', () async {
    final fakeDb = FakeDatabase();
    fakeDb.tables['progress']!.add({
      'topic_id': 'topic-1',
      'status': 'understood',
      'notes': 'Catatan uji penting.',
      'last_reviewed_at': 1700000000000,
      'updated_at': 1700000000000,
    });

    final repo = LearningRepository(fakeDb);
    final backup = await repo.exportUserData();

    expect(backup['format'], equals('codeatlas_user_backup_v1'));
    expect(backup['exported_at'], isNotNull);
    final progressList = backup['progress'] as List;
    expect(progressList.length, equals(1));
    expect(progressList.first['topic_id'], equals('topic-1'));
    expect(progressList.first['notes'], equals('Catatan uji penting.'));
  });

  test('importUserData correctly imports backup data', () async {
    final fakeDb = FakeDatabase();
    final repo = LearningRepository(fakeDb);

    final backupPayload = {
      'format': 'codeatlas_user_backup_v1',
      'exported_at': '2026-09-14T12:00:00.000Z',
      'progress': [
        {
          'topic_id': 'topic-1',
          'status': 'understood',
          'notes': 'Catatan berhasil dipulihkan.',
          'last_reviewed_at': null,
          'updated_at': 1700000001000,
        },
        {
          'topic_id': 'topic-2',
          'status': 'in_progress',
          'notes': 'Catatan kedua.',
          'last_reviewed_at': null,
          'updated_at': 1700000002000,
        },
      ],
      'learning_paths': [
        {
          'name': 'Jalur Penting',
          'goal': 'custom',
          'topics': ['topic-1', 'topic-2'],
        },
      ],
    };

    final imported = await repo.importUserData(backupPayload);
    expect(imported, equals(2));
    expect(fakeDb.tables['progress']!.length, equals(2));
    expect(fakeDb.tables['learning_paths']!.length, equals(1));
  });

  test('importUserData rejects unrecognized backup format', () async {
    final fakeDb = FakeDatabase();
    final repo = LearningRepository(fakeDb);

    expect(
      () => repo.importUserData({'format': 'invalid_format'}),
      throwsA(isA<FormatException>()),
    );
  });
}
