"""Check the specification's real JSON, SQLite schema, and embedded copies.

Run: python docs/validate_reference.py
This checks reference artifacts, not a Flutter implementation or snippet execution.
"""

import json
import re
import sqlite3
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    sample_text = (root / "content-sample.json").read_text(encoding="utf-8")
    sql = (root / "schema.sql").read_text(encoding="utf-8")
    prompt = (root / "codeatlas-antigravity-prompt.md").read_text(encoding="utf-8")
    sample = json.loads(sample_text)
    assert sample["format_version"] == sample["content_version"] == 1
    assert sample["dataset"] == "reference" and sample["locale"] == "id-ID"
    assert f"```json\n{sample_text.rstrip()}\n```" in prompt, "JSON embed differs"
    assert f"```sql\n{sql.rstrip()}\n```" in prompt, "SQL embed differs"

    manifests = []
    for start, end, prefix, expected in [
        ("### 2.1", "### 2.2", "f-", 47),
        ("### 2.2", "## 3.", "e-", 52),
    ]:
        section = prompt.split(start, 1)[1].split(end, 1)[0]
        rows = [line for line in section.splitlines() if line.startswith(f"| {prefix}")]
        assert len(rows) == 12, (prefix, "group count")
        ids = []
        for row in rows:
            columns = row.split("|")
            item_ids = re.findall(r"`([a-z0-9-]+)`:", columns[4])
            assert len(item_ids) == int(columns[3]), row
            ids.extend(item_ids)
        assert len(ids) == len(set(ids)) == expected, (prefix, "item count")
        manifests.append(set(ids))
    production_ids = manifests[0] | {f"{domain}-overview" for domain in manifests[1]}
    assert len(production_ids) == 99
    presets = prompt.split("| Goal |", 1)[1].split("Algoritma:", 1)[0]
    assert set(re.findall(r"`([fe]-[a-z0-9-]+)`", presets)) <= production_ids

    categories = {item["id"]: item for item in sample["categories"]}
    topics = {item["id"]: item for item in sample["topics"]}
    assert len(categories) == len(sample["categories"]) == 1
    assert len(topics) == len(sample["topics"]) == 3
    assert set(topics) <= manifests[0]
    for category in categories.values():
        assert category["layer"] == "fundamentals"
        assert category["kind"] == "group" and category["parent_id"] is None
    for topic in topics.values():
        assert topic["category_id"] in categories
        for field in ("prerequisite_ids", "related_topic_ids"):
            refs = topic[field]
            assert len(refs) == len(set(refs))
            assert set(refs) <= topics.keys() and topic["id"] not in refs
        assert topic["related_topic_ids"] and topic["code_examples"]
        assert {example["language"] for example in topic["code_examples"]} == {
            "typescript", "python", "dart"
        }
        pairs = []
        for example in topic["code_examples"]:
            assert all(isinstance(example[key], str) and example[key].strip()
                       for key in ("language", "label", "code", "explanation"))
            assert len(example["code"].splitlines()) <= 15
            pairs.append((example["comparison_key"], example["language"]))
        assert len(pairs) == len(set(pairs))

    # Topological elimination checks the actual reference graph without running code snippets.
    remaining = set(topics)
    while remaining:
        ready = {key for key in remaining
                 if not set(topics[key]["prerequisite_ids"]) & remaining}
        assert ready, f"Prerequisite cycle: {remaining}"
        remaining -= ready

    quizzes = sample["quizzes"]
    assert len({quiz["id"] for quiz in quizzes}) == len(quizzes) == 3
    assert {quiz["type"] for quiz in quizzes} == {"language", "concept"}
    for quiz in quizzes:
        assert quiz["topic_id"] in topics
        option_ids = [option["id"] for option in quiz["options"]]
        assert len(option_ids) == len(set(option_ids)) == 4
        assert len({option["text"] for option in quiz["options"]}) == 4
        assert quiz["correct_option_id"] in option_ids

    database = sqlite3.connect(":memory:")
    database.executescript(sql)
    assert database.execute("PRAGMA foreign_keys").fetchone() == (1,)

    def insert(table, record):
        allowed = {row[1] for row in database.execute(f"PRAGMA table_info({table})")}
        assert set(record) <= allowed, (table, set(record) - allowed)
        columns = ", ".join(record)
        parameters = ", ".join("?" for _ in record)
        database.execute(f"INSERT INTO {table} ({columns}) VALUES ({parameters})",
                         tuple(record.values()))

    with database:
        for category in categories.values():
            insert("categories", category)
        for topic in topics.values():
            row = dict(topic)
            row.pop("prerequisite_ids")
            row.pop("related_topic_ids")
            for field in ("code_examples", "keywords"):
                row[f"{field}_json"] = json.dumps(row.pop(field), ensure_ascii=False)
            insert("topics", row)
        for topic in topics.values():
            for prerequisite in topic["prerequisite_ids"]:
                insert("topic_prerequisites", {"topic_id": topic["id"],
                                               "prerequisite_id": prerequisite})
            for related in topic["related_topic_ids"]:
                insert("topic_related", {"topic_id": topic["id"],
                                         "related_topic_id": related})
        for quiz in quizzes:
            row = dict(quiz)
            row["options_json"] = json.dumps(row.pop("options"), ensure_ascii=False)
            insert("quizzes", row)
        insert("content_meta", {"id": 1, "content_version": 1,
                                "dataset": "reference", "locale": "id-ID"})
        insert("progress", {"topic_id": "f-programming-logic", "status": "understood",
                            "notes": "Urutan perlu diperiksa.", "updated_at": 1})
        insert("learning_paths", {"id": 1, "name": "Dasar", "goal": "custom",
                                  "created_at": 1, "updated_at": 1})
        insert("learning_path_items", {"path_id": 1, "topic_id": "f-programming-logic",
                                       "position": 0})
    assert database.execute("PRAGMA foreign_key_check").fetchall() == []

    for statement, parameters in [
        ("UPDATE progress SET status = ?", ("completed",)),
        ("UPDATE progress SET notes = ?", ("x" * 20001,)),
        ("INSERT INTO topic_prerequisites VALUES (?, ?)", ("f-operators", "missing")),
        ("INSERT INTO topic_prerequisites VALUES (?, ?)", ("f-operators", "f-operators")),
        ("DELETE FROM topics WHERE id = ?", ("f-programming-logic",)),
        ("INSERT INTO learning_path_items VALUES (?, ?, ?)",
         (1, "f-operators", 0)),
    ]:
        try:
            with database:
                database.execute(statement, parameters)
        except sqlite3.IntegrityError:
            pass
        else:
            raise AssertionError(f"Constraint not enforced: {statement}")
    with database:
        database.execute("UPDATE topics SET title = ? WHERE id = ?",
                         ("Logika Pemrograman", "f-programming-logic"))
        database.execute("DELETE FROM learning_paths WHERE id = 1")
    assert database.execute("SELECT count(*) FROM learning_path_items").fetchone() == (0,)
    assert database.execute("SELECT status, notes FROM progress").fetchone() == (
        "understood", "Urutan perlu diperiksa."
    )
    assert database.execute("PRAGMA integrity_check").fetchone() == ("ok",)
    database.close()
    print("PASS: 47 fundamental + 52 domain/overview; all preset IDs valid.")
    print("PASS: 3 reference topics, 9 snippets, 3 quizzes, references and DAG valid.")
    print("PASS: SQLite import, constraints, retained progress, and embedded copies.")
    print("Scope: specification artifacts only; Flutter and snippet execution not tested.")


if __name__ == "__main__":
    main()
