"""Generate and validate production content.json for CodeAtlas.
Integrates 76 categories, 99 topics (47 fundamentals + 52 ecosystem overviews),
36 quizzes, and 10 multi-language comparison groups.
"""

import json
import sqlite3
import sys
from pathlib import Path

# Add scripts folder to sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from data_categories import CATEGORIES
from data_fundamentals import FUNDAMENTAL_TOPICS
from data_ecosystem import ECOSYSTEM_TOPICS
from data_quizzes import QUIZZES


def validate_and_generate():
    print("--- Starting CodeAtlas Content Generation & Validation ---")
    
    # 1. Basic counts
    all_topics = FUNDAMENTAL_TOPICS + ECOSYSTEM_TOPICS
    print(f"Categories count: {len(CATEGORIES)}")
    print(f"Topics count: {len(all_topics)} ({len(FUNDAMENTAL_TOPICS)} fundamentals + {len(ECOSYSTEM_TOPICS)} ecosystem)")
    print(f"Quizzes count: {len(QUIZZES)}")
    
    assert len(CATEGORIES) == 76, f"Expected 76 categories, got {len(CATEGORIES)}"
    assert len(all_topics) == 99, f"Expected 99 topics, got {len(all_topics)}"
    assert len(FUNDAMENTAL_TOPICS) == 47, f"Expected 47 fundamental topics, got {len(FUNDAMENTAL_TOPICS)}"
    assert len(ECOSYSTEM_TOPICS) == 52, f"Expected 52 ecosystem topics, got {len(ECOSYSTEM_TOPICS)}"
    assert len(QUIZZES) >= 30, f"Expected >= 30 quizzes, got {len(QUIZZES)}"

    # Check unique IDs
    cat_ids = [c["id"] for c in CATEGORIES]
    assert len(cat_ids) == len(set(cat_ids)), "Duplicate category IDs found!"
    topic_ids = [t["id"] for t in all_topics]
    assert len(topic_ids) == len(set(topic_ids)), "Duplicate topic IDs found!"
    quiz_ids = [q["id"] for q in QUIZZES]
    assert len(quiz_ids) == len(set(quiz_ids)), "Duplicate quiz IDs found!"
    
    cat_set = set(cat_ids)
    topic_set = set(topic_ids)

    # 2. Check categories structure
    groups = [c for c in CATEGORIES if c["kind"] == "group"]
    domains = [c for c in CATEGORIES if c["kind"] == "domain"]
    assert len(groups) == 24, f"Expected 24 groups (12 fundamental + 12 ecosystem), got {len(groups)}"
    assert len(domains) == 52, f"Expected 52 ecosystem domains, got {len(domains)}"
    for d in domains:
        assert d["layer"] == "ecosystem", f"Domain {d['id']} layer must be ecosystem"
        assert d["parent_id"] in cat_set, f"Domain {d['id']} parent {d['parent_id']} not found"

    # 3. Check topics integrity
    for t in all_topics:
        assert t["category_id"] in cat_set, f"Topic {t['id']} category {t['category_id']} not found"
        assert t["level"] in ("beginner", "intermediate", "advanced"), f"Topic {t['id']} invalid level"
        assert len(t["summary"].strip()) > 0, f"Topic {t['id']} summary empty"
        assert len(t["explanation_simple"].strip()) > 0, f"Topic {t['id']} explanation_simple empty"
        assert len(t["explanation_technical"].strip()) > 0, f"Topic {t['id']} explanation_technical empty"
        assert len(t["why_vibecoding_matters"].strip()) > 0, f"Topic {t['id']} why_vibecoding_matters empty"
        assert len(t["code_examples"]) >= 1, f"Topic {t['id']} must have >= 1 code example"
        assert len(t["related_topic_ids"]) >= 1, f"Topic {t['id']} must have >= 1 related topic"
        assert t["estimated_minutes"] > 0, f"Topic {t['id']} estimated_minutes must be > 0"
        
        # Check 8 pedagogical dimensions
        assert len(t.get("problem_context", "").strip()) > 0, f"Topic {t['id']} problem_context empty"
        assert len(t.get("when_to_use", "").strip()) > 0, f"Topic {t['id']} when_to_use empty"
        assert len(t.get("misconceptions", [])) >= 2, f"Topic {t['id']} must have >= 2 misconceptions"
        for m in t.get("misconceptions", []):
            assert len(m.get("misconception", "").strip()) > 0, f"Topic {t['id']} misconception text empty"
            assert len(m.get("explanation", "").strip()) > 0, f"Topic {t['id']} misconception explanation empty"
            assert len(m.get("spot_in_code", "").strip()) > 0, f"Topic {t['id']} misconception spot_in_code empty"
        assert len(t.get("reflection_questions", [])) >= 2, f"Topic {t['id']} must have >= 2 reflection questions"
        for q in t.get("reflection_questions", []):
            assert len(q.get("question", "").strip()) > 0, f"Topic {t['id']} reflection question empty"
            assert len(q.get("answer", "").strip()) > 0, f"Topic {t['id']} reflection answer empty"

        # Check prerequisites
        for p in t["prerequisite_ids"]:
            assert p in topic_set, f"Prerequisite {p} for topic {t['id']} not in topics"
            assert p != t["id"], f"Topic {t['id']} cannot be its own prerequisite"
            
        # Check related
        for r in t["related_topic_ids"]:
            assert r in topic_set, f"Related topic {r} for topic {t['id']} not in topics"
            assert r != t["id"], f"Topic {t['id']} cannot be related to itself"

    # 4. Check DAG acyclicity (Kahn's algorithm)
    print("Checking prerequisite graph acyclicity...")
    in_degree = {t["id"]: 0 for t in all_topics}
    adj = {t["id"]: [] for t in all_topics}
    for t in all_topics:
        for p in t["prerequisite_ids"]:
            adj[p].append(t["id"])
            in_degree[t["id"]] += 1
            
    queue = [tid for tid, deg in in_degree.items() if deg == 0]
    visited_count = 0
    while queue:
        curr = queue.pop(0)
        visited_count += 1
        for neighbor in adj[curr]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    assert visited_count == len(all_topics), f"CYCLE DETECTED! Only {visited_count}/{len(all_topics)} topics visited."
    print("DAG is strictly acyclic! [PASS]")

    # 5. Check Comparison groups
    comparison_map = {}
    for t in all_topics:
        for ex in t["code_examples"]:
            key = ex.get("comparison_key")
            if key:
                comparison_map.setdefault(key, set()).add(ex["language"])
                
    print(f"Comparison groups found: {len(comparison_map)}")
    for k, langs in comparison_map.items():
        print(f"  - {k}: {sorted(langs)}")
        assert {"dart", "typescript", "python"} <= langs, f"Group {k} missing required languages, got {langs}"
    assert len(comparison_map) >= 9, f"Expected at least 9 comparison groups, got {len(comparison_map)}"

    # 6. Check Quizzes
    lang_quizzes = [q for q in QUIZZES if q["type"] == "language"]
    concept_quizzes = [q for q in QUIZZES if q["type"] == "concept"]
    print(f"Quizzes: {len(lang_quizzes)} language, {len(concept_quizzes)} concept")
    assert len(lang_quizzes) >= 10, f"Expected >= 10 language quizzes, got {len(lang_quizzes)}"
    assert len(concept_quizzes) >= 20, f"Expected >= 20 concept quizzes, got {len(concept_quizzes)}"
    
    quiz_topics = {q["topic_id"] for q in QUIZZES}
    assert len(quiz_topics) >= 15, f"Expected >= 15 distinct topics in quizzes, got {len(quiz_topics)}"
    
    for q in QUIZZES:
        assert q["topic_id"] in topic_set, f"Quiz {q['id']} topic {q['topic_id']} not found"
        assert len(q["options"]) == 4, f"Quiz {q['id']} must have exactly 4 options"
        opt_ids = [o["id"] for o in q["options"]]
        opt_texts = [o["text"] for o in q["options"]]
        assert len(opt_ids) == len(set(opt_ids)) == 4, f"Quiz {q['id']} option IDs not unique"
        assert len(opt_texts) == len(set(opt_texts)) == 4, f"Quiz {q['id']} option texts not unique"
        assert q["correct_option_id"] in opt_ids, f"Quiz {q['id']} correct_option_id {q['correct_option_id']} not in options"

    # 7. Check Preset Goals
    preset_goals = {
        "general": [
            "f-programming-logic", "f-variables-data-types", "f-operators",
            "f-conditionals", "f-loops", "f-functions", "f-debugging",
            "f-testing", "f-git"
        ],
        "flutter": [
            "f-type-system", "f-oop", "f-modules-packages", "f-dependencies",
            "f-error-handling", "f-async", "f-apis", "f-serialization",
            "f-testing", "e-mobile-overview", "e-frameworks-overview"
        ],
        "web": [
            "f-http-web", "f-apis", "f-serialization", "f-async",
            "f-security", "e-frontend-overview", "e-backend-overview"
        ],
        "backend": [
            "f-apis", "f-databases", "f-sql", "f-data-modeling", "f-auth",
            "f-security", "f-testing", "f-deployment", "e-backend-overview"
        ],
        "data": [
            "f-data-structures", "f-algorithms", "f-databases", "f-sql",
            "f-data-modeling", "e-data-engineering-overview", "e-data-science-overview"
        ]
    }
    for goal, targets in preset_goals.items():
        for tid in targets:
            assert tid in topic_set, f"Preset goal {goal} target {tid} not in topics!"
    print("All preset goals verified! [PASS]")

    # 8. Test SQLite in-memory with real schema
    print("Verifying SQLite insertion & foreign keys in-memory...")
    root = SCRIPT_DIR.parent
    sql = (root / "docs" / "schema.sql").read_text(encoding="utf-8")
    db = sqlite3.connect(":memory:")
    db.executescript(sql)
    db.execute("PRAGMA foreign_keys = ON;")

    def insert(table, record):
        cols = ", ".join(record.keys())
        placeholders = ", ".join("?" for _ in record)
        db.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", tuple(record.values()))

    with db:
        for c in CATEGORIES:
            insert("categories", c)
        for t in all_topics:
            row = dict(t)
            row.pop("prerequisite_ids")
            row.pop("related_topic_ids")
            row["code_examples_json"] = json.dumps(row.pop("code_examples"), ensure_ascii=False)
            row["keywords_json"] = json.dumps(row.pop("keywords"), ensure_ascii=False)
            row["misconceptions_json"] = json.dumps(row.pop("misconceptions", []), ensure_ascii=False)
            row["reflection_questions_json"] = json.dumps(row.pop("reflection_questions", []), ensure_ascii=False)
            row["is_active"] = 1 if row.get("is_active", True) else 0
            insert("topics", row)
        for t in all_topics:
            for p in t["prerequisite_ids"]:
                insert("topic_prerequisites", {"topic_id": t["id"], "prerequisite_id": p})
            for r in t["related_topic_ids"]:
                insert("topic_related", {"topic_id": t["id"], "related_topic_id": r})
        for q in QUIZZES:
            row = dict(q)
            row["options_json"] = json.dumps(row.pop("options"), ensure_ascii=False)
            row["is_active"] = 1 if row.get("is_active", True) else 0
            insert("quizzes", row)
        insert("content_meta", {
            "id": 1,
            "content_version": 4,
            "dataset": "production",
            "locale": "id-ID"
        })

    fk_errors = db.execute("PRAGMA foreign_key_check").fetchall()
    assert len(fk_errors) == 0, f"Foreign key check failed: {fk_errors}"
    integrity = db.execute("PRAGMA integrity_check").fetchone()[0]
    assert integrity == "ok", f"Integrity check failed: {integrity}"
    db.close()
    print("SQLite import & constraints passed! [PASS]")

    # 9. Write final content.json
    production_package = {
        "format_version": 1,
        "content_version": 4,
        "dataset": "production",
        "locale": "id-ID",
        "categories": CATEGORIES,
        "topics": all_topics,
        "quizzes": QUIZZES,
    }

    target_file = root / "codeatlas" / "assets" / "content" / "content.json"
    json_text = json.dumps(production_package, ensure_ascii=False, indent=2)
    target_file.write_text(json_text, encoding="utf-8")
    file_size_kb = target_file.stat().st_size / 1024
    print(f"SUCCESS: Wrote production content.json ({file_size_kb:.1f} KB) to {target_file}")


if __name__ == "__main__":
    validate_and_generate()
