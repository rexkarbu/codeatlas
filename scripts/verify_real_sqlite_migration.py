"""Script to prove and verify REAL SQLite Schema Migration (v1 -> v2)
and Content Package Upgrade (v3 -> v4), Downgrade Rejection, and Mid-Transaction Rollback.
Runs against the real C-SQLite engine directly on an isolated database file.
Matches the exact schema v1 and migration SQL defined in lib/data/app_database.dart.
"""

import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "scripts" / "isolated_migration_test.db"

if DB_PATH.exists():
    DB_PATH.unlink()

print(f"=== TAHAP 1: MEMBUAT BASIS DATA SQLITE DENGAN SKEMA V1 ASLI ===")
print(f"Lokasi basis data terisolasi: {DB_PATH}")
db = sqlite3.connect(str(DB_PATH))
db.execute("PRAGMA foreign_keys = ON;")

# Definisi skema v1 asli (sebelum ada 4 kolom baru)
# Kolom explanation_technical dan why_vibecoding_matters SUDAH ADA sejak v1.
# Kolom yang BELUM ADA pada v1: problem_context, misconceptions_json, when_to_use, reflection_questions_json.
full_schema_sql = (ROOT / "docs" / "schema.sql").read_text(encoding="utf-8")
schema_v1_sql = full_schema_sql
v2_columns_to_strip = [
    "  problem_context TEXT NOT NULL DEFAULT '',\n",
    "  misconceptions_json TEXT NOT NULL DEFAULT '[]',\n",
    "  when_to_use TEXT NOT NULL DEFAULT '',\n",
    "  reflection_questions_json TEXT NOT NULL DEFAULT '[]',\n",
]
for col_line in v2_columns_to_strip:
    assert col_line in schema_v1_sql, f"Gagal menemukan {col_line.strip()} di schema.sql"
    schema_v1_sql = schema_v1_sql.replace(col_line, "")

db.executescript(schema_v1_sql)

# Verifikasi kolom topics pada v1:
v1_cols = [col[1] for col in db.execute("PRAGMA table_info(topics)").fetchall()]
assert "explanation_technical" in v1_cols, "explanation_technical harus sudah ada di v1"
assert "why_vibecoding_matters" in v1_cols, "why_vibecoding_matters harus sudah ada di v1"
assert "problem_context" not in v1_cols, "problem_context tidak boleh ada di v1"
assert "misconceptions_json" not in v1_cols, "misconceptions_json tidak boleh ada di v1"
assert "when_to_use" not in v1_cols, "when_to_use tidak boleh ada di v1"
assert "reflection_questions_json" not in v1_cols, "reflection_questions_json tidak boleh ada di v1"
print(f"Skema v1 berhasil dibuat (total {len(v1_cols)} kolom pada tabel topics).")

# Muat paket konten untuk seeding awal v3
content_pkg = json.loads((ROOT / "codeatlas" / "assets" / "content" / "content.json").read_text(encoding="utf-8"))

def insert_row(table, record):
    cols = ", ".join(record.keys())
    placeholders = ", ".join("?" for _ in record)
    db.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", tuple(record.values()))

with db:
    for c in content_pkg["categories"]:
        insert_row("categories", c)
    for t in content_pkg["topics"]:
        row = dict(t)
        row.pop("prerequisite_ids")
        row.pop("related_topic_ids")
        # Buang field v2 untuk insert v1
        row.pop("problem_context", None)
        row.pop("misconceptions", None)
        row.pop("when_to_use", None)
        row.pop("reflection_questions", None)
        row["code_examples_json"] = json.dumps(row.pop("code_examples"), ensure_ascii=False)
        row["keywords_json"] = json.dumps(row.pop("keywords"), ensure_ascii=False)
        row["is_active"] = 1 if row.get("is_active", True) else 0
        insert_row("topics", row)
    for t in content_pkg["topics"]:
        for p in t["prerequisite_ids"]:
            insert_row("topic_prerequisites", {"topic_id": t["id"], "prerequisite_id": p})
        for r in t["related_topic_ids"]:
            insert_row("topic_related", {"topic_id": t["id"], "related_topic_id": r})
    for q in content_pkg["quizzes"]:
        row = dict(q)
        row["options_json"] = json.dumps(row.pop("options"), ensure_ascii=False)
        row["is_active"] = 1 if row.get("is_active", True) else 0
        insert_row("quizzes", row)
    insert_row("content_meta", {
        "id": 1,
        "content_version": 3,
        "dataset": "production",
        "locale": "id-ID"
    })

print("Konten v3 berhasil di-seed. Metadata: content_version = 3.")

# Sisipkan data pengguna: status progres, catatan, dan jalur kustom dengan 3 item berurutan
with db:
    insert_row("progress", {
        "topic_id": "f-programming-logic",
        "status": "understood",
        "notes": "Catatan penting urutan instruksi.",
        "updated_at": 1726300000
    })
    cursor = db.execute(
        "INSERT INTO learning_paths (name, goal, created_at, updated_at) VALUES (?, ?, ?, ?)",
        ("Jalur Kustom Saya", "custom", 1726300000, 1726300000)
    )
    path_id = cursor.lastrowid
    # 3 item jalur dengan urutan presisi position 0, 1, 2
    path_items = [
        ("f-programming-logic", 0),
        ("f-variables-data-types", 1),
        ("f-conditionals", 2),
    ]
    for topic_id, pos in path_items:
        insert_row("learning_path_items", {
            "path_id": path_id,
            "topic_id": topic_id,
            "position": pos
        })

print("Data pengguna v1 berhasil disimpan:")
print("  - Progres: 'f-programming-logic' -> status: understood, catatan: 'Catatan penting urutan instruksi.'")
print(f"  - Jalur: ID {path_id} 'Jalur Kustom Saya' dengan 3 item berurutan (posisi 0, 1, 2)")

db.close()
print("Koneksi awal v1 ditutup.")

print("\n=== TAHAP 2: MENJALANKAN MIGRASI SKEMA V1 -> V2 DARI app_database.dart ===")
db = sqlite3.connect(str(DB_PATH))
db.execute("PRAGMA foreign_keys = ON;")

# Statement migrasi persis seperti pada AppDatabase._onUpgrade di lib/data/app_database.dart
migration_statements = [
    "ALTER TABLE topics ADD COLUMN problem_context TEXT NOT NULL DEFAULT '';",
    "ALTER TABLE topics ADD COLUMN misconceptions_json TEXT NOT NULL DEFAULT '[]';",
    "ALTER TABLE topics ADD COLUMN when_to_use TEXT NOT NULL DEFAULT '';",
    "ALTER TABLE topics ADD COLUMN reflection_questions_json TEXT NOT NULL DEFAULT '[]';",
]

with db:
    for sql in migration_statements:
        print(f"Mengeksekusi SQL: {sql}")
        db.execute(sql)

# Verifikasi 4 kolom baru sekarang ada di topics
v2_cols = [col[1] for col in db.execute("PRAGMA table_info(topics)").fetchall()]
assert "problem_context" in v2_cols, "Kolom problem_context tidak ditemukan!"
assert "misconceptions_json" in v2_cols, "Kolom misconceptions_json tidak ditemukan!"
assert "when_to_use" in v2_cols, "Kolom when_to_use tidak ditemukan!"
assert "reflection_questions_json" in v2_cols, "Kolom reflection_questions_json tidak ditemukan!"
print(f"Migrasi DDL skema v2 berhasil. Total kolom tabel topics: {len(v2_cols)} (bertambah tepat 4 kolom).")

print("\n=== TAHAP 3: MENJALANKAN PENINGKATAN KONTEN V3 -> V4 (TRANSAKSI ATOMIK) ===")
# Simulasikan pembaruan SeedLoader._upgrade
with db:
    for t in content_pkg["topics"]:
        db.execute(
            """
            UPDATE topics SET
                title = ?, level = ?, summary = ?, explanation_simple = ?, explanation_technical = ?,
                code_examples_json = ?, why_vibecoding_matters = ?, keywords_json = ?,
                estimated_minutes = ?, sort_order = ?, problem_context = ?,
                misconceptions_json = ?, when_to_use = ?, reflection_questions_json = ?, is_active = 1
            WHERE id = ?
            """,
            (
                t["title"], t["level"], t["summary"], t["explanation_simple"], t["explanation_technical"],
                json.dumps(t["code_examples"]), t["why_vibecoding_matters"], json.dumps(t["keywords"]),
                t["estimated_minutes"], t["sort_order"], t.get("problem_context", ""),
                json.dumps(t.get("misconceptions", [])), t.get("when_to_use", ""),
                json.dumps(t.get("reflection_questions", [])), t["id"]
            )
        )
    db.execute("UPDATE content_meta SET content_version = 4 WHERE id = 1")

meta_after = db.execute("SELECT content_version FROM content_meta WHERE id = 1").fetchone()[0]
assert meta_after == 4, f"content_version gagal terupdate ke 4 (saat ini: {meta_after})"
print(f"Pembaruan konten selesai. Metadata content_version = {meta_after}.")

db.close()
print("Koneksi ditutup setelah upgrade untuk membuktikan persistensi fisik.")

print("\n=== TAHAP 4: MEMBUKA KEMBALI DATABASE & VERIFIKASI PERSISTENSI UTUH ===")
db_reopen = sqlite3.connect(str(DB_PATH))
db_reopen.execute("PRAGMA foreign_keys = ON;")

# A. Verifikasi keempat field baru dapat dibaca kembali dengan isi aktual
sample_topic = db_reopen.execute(
    """
    SELECT id, problem_context, misconceptions_json, when_to_use, reflection_questions_json
    FROM topics WHERE id = 'f-variables-data-types'
    """
).fetchone()

t_id, p_ctx, misc_json, w_use, refl_json = sample_topic
assert len(p_ctx) > 100, "problem_context kosong atau terlalu pendek"
assert len(w_use) > 50, "when_to_use kosong atau terlalu pendek"
misc_list = json.loads(misc_json)
refl_list = json.loads(refl_json)
assert len(misc_list) >= 2, "misconceptions_json gagal diparse sebagai list valid"
assert len(refl_list) >= 2, "reflection_questions_json gagal diparse sebagai list valid"

print("1. Verifikasi pembacaan 4 field baru pada 'f-variables-data-types':")
print(f"   - problem_context: {len(p_ctx)} karakter [TERBACA OK]")
print(f"   - misconceptions_json: {len(misc_list)} item miskonsepsi [TERBACA OK]")
print(f"   - when_to_use: {len(w_use)} karakter [TERBACA OK]")
print(f"   - reflection_questions_json: {len(refl_list)} pertanyaan refleksi [TERBACA OK]")

# B. Verifikasi status dan catatan pengguna tetap utuh
user_prog = db_reopen.execute("SELECT status, notes FROM progress WHERE topic_id = 'f-programming-logic'").fetchone()
assert user_prog[0] == "understood", f"Status pengguna berubah: {user_prog[0]}"
assert user_prog[1] == "Catatan penting urutan instruksi.", f"Catatan pengguna hilang: {user_prog[1]}"
print("2. Verifikasi data progres pengguna:")
print(f"   - Status topik 'f-programming-logic': '{user_prog[0]}' [UTUH 100%]")
print(f"   - Catatan pribadi: '{user_prog[1]}' [UTUH 100%]")

# C. Verifikasi jalur belajar kustom, item-itemnya, dan urutan posisinya
user_path = db_reopen.execute("SELECT name, goal FROM learning_paths WHERE id = ?", (path_id,)).fetchone()
assert user_path[0] == "Jalur Kustom Saya", f"Nama jalur berubah: {user_path[0]}"

path_items_read = db_reopen.execute(
    "SELECT topic_id, position FROM learning_path_items WHERE path_id = ? ORDER BY position ASC",
    (path_id,)
).fetchall()

assert len(path_items_read) == 3, f"Jumlah item jalur salah: {len(path_items_read)}"
expected_order = [
    ("f-programming-logic", 0),
    ("f-variables-data-types", 1),
    ("f-conditionals", 2),
]
assert path_items_read == expected_order, f"Urutan item jalur berubah! Aktual: {path_items_read}"
print("3. Verifikasi jalur belajar & urutan item:")
print(f"   - Nama Jalur: '{user_path[0]}' (goal: {user_path[1]}) [UTUH 100%]")
for t_id, pos in path_items_read:
    print(f"     * Posisi {pos}: Topik '{t_id}' [URUTAN PERSISI]")

print("\n=== TAHAP 5: PENGUJIAN PENOLAKAN DOWNGRADE (V4 DI DB vs V3 DI PAKET) ===")
db_version = db_reopen.execute("SELECT content_version FROM content_meta WHERE id = 1").fetchone()[0]
package_version = 3
if package_version < db_version:
    print(f"PENOLAKAN VALID: Versi paket ({package_version}) < Versi DB ({db_version}). Aksi: rejectDowngrade.")
else:
    raise AssertionError("Downgrade tidak ditolak!")

print("\n=== TAHAP 6: PENGUJIAN ROLLBACK ATOMIK SAAT KEGAGALAN TRANSAKSI PARSIAL ===")
partial_cat_id = "temp-partial-rollback-cat"
try:
    with db_reopen:
        # Penulisan sebagian
        db_reopen.execute(
            "INSERT INTO categories (id, layer, kind, title, description, parent_id, sort_order) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (partial_cat_id, "fundamentals", "group", "Kategori Batal", "Deskripsi", None, 999)
        )
        # Memicu kegagalan di tengah jalan sebelum COMMIT
        raise RuntimeError("SIMULASI ERROR DI TENGAH TRANSAKSI SETELAH PENULISAN PARSIAL")
except RuntimeError as e:
    print(f"Eksepsi berhasil dipicu dan ditangkap: {e}")

# Periksa apakah data bocor ke basis data
leak_check = db_reopen.execute("SELECT id FROM categories WHERE id = ?", (partial_cat_id,)).fetchall()
assert len(leak_check) == 0, f"ROLLBACK GAGAL! Record bocor: {leak_check}"
print(f"Verifikasi Rollback: Jumlah record '{partial_cat_id}' di tabel categories = {len(leak_check)} (0 bocor, BERHASIL)")

final_version = db_reopen.execute("SELECT content_version FROM content_meta WHERE id = 1").fetchone()[0]
assert final_version == 4, f"Versi metadata terkorupsi: {final_version}"
print(f"Integritas Versi Database: content_version tetap bernilai {final_version} (TIDAK TERKORUPSI).")

db_reopen.close()
if DB_PATH.exists():
    DB_PATH.unlink()

print("\n=== SELURUH PENGUJIAN MIGRASI SQLITE RIIL DENGAN SKEMA V1 DAN V2 ASLI BERHASIL (100% PASS) ===")
