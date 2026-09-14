// lib/data/app_database.dart — SQLite schema, connection, and migrations.

import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart' as p;

/// Database version for schema migrations (separate from content_version).
const int kDatabaseVersion = 2;

class AppDatabase {
  static Database? _db;

  /// Get or open the database singleton.
  static Future<Database> get database async {
    if (_db != null) return _db!;
    _db = await _openDatabase();
    return _db!;
  }

  /// Close the database (for testing).
  static Future<void> close() async {
    await _db?.close();
    _db = null;
  }

  /// Open database with a specific path (for testing).
  static Future<Database> openWithPath(String path) async {
    _db = await openDatabase(
      path,
      version: kDatabaseVersion,
      onConfigure: _onConfigure,
      onCreate: _onCreate,
      onUpgrade: _onUpgrade,
    );
    return _db!;
  }

  static Future<Database> _openDatabase() async {
    final dbPath = await getDatabasesPath();
    final path = p.join(dbPath, 'codeatlas.db');
    return openDatabase(
      path,
      version: kDatabaseVersion,
      onConfigure: _onConfigure,
      onCreate: _onCreate,
      onUpgrade: _onUpgrade,
    );
  }

  /// Enable foreign keys on every connection before any transaction.
  static Future<void> _onConfigure(Database db) async {
    await db.execute('PRAGMA foreign_keys = ON');
  }

  /// Create all tables on fresh install.
  static Future<void> _onCreate(Database db, int version) async {
    await db.execute('''
      CREATE TABLE categories (
        id TEXT PRIMARY KEY NOT NULL,
        parent_id TEXT REFERENCES categories(id) ON DELETE RESTRICT,
        layer TEXT NOT NULL CHECK (layer IN ('fundamentals', 'ecosystem')),
        kind TEXT NOT NULL CHECK (kind IN ('group', 'domain')),
        title TEXT NOT NULL CHECK (length(trim(title)) > 0),
        description TEXT NOT NULL CHECK (length(trim(description)) > 0),
        sort_order INTEGER NOT NULL CHECK (sort_order >= 0),
        CHECK ((kind = 'group' AND parent_id IS NULL)
          OR (kind = 'domain' AND parent_id IS NOT NULL AND layer = 'ecosystem')),
        CHECK (parent_id IS NULL OR parent_id <> id)
      )
    ''');

    await db.execute('''
      CREATE TABLE topics (
        id TEXT PRIMARY KEY NOT NULL,
        category_id TEXT NOT NULL REFERENCES categories(id) ON DELETE RESTRICT,
        title TEXT NOT NULL CHECK (length(trim(title)) > 0),
        level TEXT NOT NULL CHECK (level IN ('beginner', 'intermediate', 'advanced')),
        summary TEXT NOT NULL CHECK (length(trim(summary)) > 0),
        explanation_simple TEXT NOT NULL CHECK (length(trim(explanation_simple)) > 0),
        explanation_technical TEXT NOT NULL CHECK (length(trim(explanation_technical)) > 0),
        code_examples_json TEXT NOT NULL,
        why_vibecoding_matters TEXT NOT NULL CHECK (length(trim(why_vibecoding_matters)) > 0),
        problem_context TEXT NOT NULL DEFAULT '',
        misconceptions_json TEXT NOT NULL DEFAULT '[]',
        when_to_use TEXT NOT NULL DEFAULT '',
        reflection_questions_json TEXT NOT NULL DEFAULT '[]',
        keywords_json TEXT NOT NULL,
        estimated_minutes INTEGER NOT NULL CHECK (estimated_minutes > 0),
        sort_order INTEGER NOT NULL CHECK (sort_order >= 0),
        is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1))
      )
    ''');

    await db.execute('''
      CREATE TABLE topic_prerequisites (
        topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        prerequisite_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        PRIMARY KEY (topic_id, prerequisite_id),
        CHECK (topic_id <> prerequisite_id)
      )
    ''');

    await db.execute('''
      CREATE TABLE topic_related (
        topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        related_topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        PRIMARY KEY (topic_id, related_topic_id),
        CHECK (topic_id <> related_topic_id)
      )
    ''');

    await db.execute('''
      CREATE TABLE progress (
        topic_id TEXT PRIMARY KEY NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        status TEXT NOT NULL DEFAULT 'not_started'
          CHECK (status IN ('not_started', 'in_progress', 'understood')),
        notes TEXT NOT NULL DEFAULT '' CHECK (length(notes) <= 20000),
        last_reviewed_at INTEGER CHECK (last_reviewed_at IS NULL OR last_reviewed_at >= 0),
        updated_at INTEGER NOT NULL CHECK (updated_at >= 0)
      )
    ''');

    await db.execute('''
      CREATE TABLE quizzes (
        id TEXT PRIMARY KEY NOT NULL,
        topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        type TEXT NOT NULL CHECK (type IN ('language', 'concept')),
        level TEXT NOT NULL CHECK (level IN ('beginner', 'intermediate', 'advanced')),
        prompt TEXT NOT NULL CHECK (length(trim(prompt)) > 0),
        snippet TEXT NOT NULL CHECK (length(trim(snippet)) > 0),
        snippet_language TEXT NOT NULL,
        options_json TEXT NOT NULL,
        correct_option_id TEXT NOT NULL,
        explanation TEXT NOT NULL CHECK (length(trim(explanation)) > 0),
        is_active INTEGER NOT NULL DEFAULT 1 CHECK (is_active IN (0, 1))
      )
    ''');

    await db.execute('''
      CREATE TABLE learning_paths (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL CHECK (length(trim(name)) BETWEEN 1 AND 100),
        goal TEXT NOT NULL CHECK (goal IN ('general', 'flutter', 'web', 'backend', 'data', 'custom')),
        created_at INTEGER NOT NULL CHECK (created_at >= 0),
        updated_at INTEGER NOT NULL CHECK (updated_at >= created_at)
      )
    ''');

    await db.execute('''
      CREATE TABLE learning_path_items (
        path_id INTEGER NOT NULL REFERENCES learning_paths(id) ON DELETE CASCADE,
        topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
        position INTEGER NOT NULL CHECK (position >= 0),
        PRIMARY KEY (path_id, topic_id),
        UNIQUE (path_id, position)
      )
    ''');

    await db.execute('''
      CREATE TABLE content_meta (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        content_version INTEGER NOT NULL CHECK (content_version > 0),
        dataset TEXT NOT NULL CHECK (dataset IN ('reference', 'production')),
        locale TEXT NOT NULL
      )
    ''');

    // Indexes
    await db.execute('CREATE INDEX topics_category_idx ON topics(category_id)');
    await db.execute(
      'CREATE INDEX prerequisites_reverse_idx ON topic_prerequisites(prerequisite_id)',
    );
    await db.execute('CREATE INDEX quizzes_topic_idx ON quizzes(topic_id)');
  }

  /// Handle schema upgrades.
  static Future<void> _onUpgrade(
    Database db,
    int oldVersion,
    int newVersion,
  ) async {
    if (oldVersion < 2) {
      await db.execute(
        "ALTER TABLE topics ADD COLUMN problem_context TEXT NOT NULL DEFAULT ''",
      );
      await db.execute(
        "ALTER TABLE topics ADD COLUMN misconceptions_json TEXT NOT NULL DEFAULT '[]'",
      );
      await db.execute(
        "ALTER TABLE topics ADD COLUMN when_to_use TEXT NOT NULL DEFAULT ''",
      );
      await db.execute(
        "ALTER TABLE topics ADD COLUMN reflection_questions_json TEXT NOT NULL DEFAULT '[]'",
      );
    }
  }
}
