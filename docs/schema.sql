-- Skema SQLite v1. Aktifkan foreign_keys pada setiap koneksi sebelum transaksi.
PRAGMA foreign_keys = ON;

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
);

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
);

CREATE TABLE topic_prerequisites (
  topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
  prerequisite_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
  PRIMARY KEY (topic_id, prerequisite_id),
  CHECK (topic_id <> prerequisite_id)
);

CREATE TABLE topic_related (
  topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
  related_topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
  PRIMARY KEY (topic_id, related_topic_id),
  CHECK (topic_id <> related_topic_id)
);

CREATE TABLE progress (
  topic_id TEXT PRIMARY KEY NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
  status TEXT NOT NULL DEFAULT 'not_started'
    CHECK (status IN ('not_started', 'in_progress', 'understood')),
  notes TEXT NOT NULL DEFAULT '' CHECK (length(notes) <= 20000),
  last_reviewed_at INTEGER CHECK (last_reviewed_at IS NULL OR last_reviewed_at >= 0),
  updated_at INTEGER NOT NULL CHECK (updated_at >= 0)
);

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
);

CREATE TABLE learning_paths (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL CHECK (length(trim(name)) BETWEEN 1 AND 100),
  goal TEXT NOT NULL CHECK (goal IN ('general', 'flutter', 'web', 'backend', 'data', 'custom')),
  created_at INTEGER NOT NULL CHECK (created_at >= 0),
  updated_at INTEGER NOT NULL CHECK (updated_at >= created_at)
);

CREATE TABLE learning_path_items (
  path_id INTEGER NOT NULL REFERENCES learning_paths(id) ON DELETE CASCADE,
  topic_id TEXT NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
  position INTEGER NOT NULL CHECK (position >= 0),
  PRIMARY KEY (path_id, topic_id),
  UNIQUE (path_id, position)
);

CREATE TABLE content_meta (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  content_version INTEGER NOT NULL CHECK (content_version > 0),
  dataset TEXT NOT NULL CHECK (dataset IN ('reference', 'production')),
  locale TEXT NOT NULL
);

CREATE INDEX topics_category_idx ON topics(category_id);
CREATE INDEX prerequisites_reverse_idx ON topic_prerequisites(prerequisite_id);
CREATE INDEX quizzes_topic_idx ON quizzes(topic_id);
