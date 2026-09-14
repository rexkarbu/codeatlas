<p align="center">
  <img src="codeatlas/assets/branding/codeatlas_icon_1024.png" width="128" height="128" alt="CodeAtlas App Icon" />
</p>

<h1 align="center">CodeAtlas</h1>

<p align="center">
  <b>Ensiklopedia Interaktif Fundamental Pemrograman & Peta Ekosistem Rekayasa Perangkat Lunak</b><br>
  <i>Aplikasi Mobile Offline-First (Flutter) Berbahasa Indonesia untuk Pemula dan Vibecoder</i>
</p>

---

## 🎨 Identitas Visual & Ikon Aplikasi

CodeAtlas menggunakan identitas visual berbasis filosofi **Deep Tech Synth**:
- **Sintesis Konsep**: Menggabungkan kisi kartografi / sumbu meridian atlas pengetahuan (*constellation nodes*) dengan kurung siku kode (`< / >`).
- **Palet Warna**: *Deep Space Midnight Indigo* (`#1E1B4B`), *Electric Violet* (`#8B5CF6`), *Luminous Lavender* (`#A78BFA`), dan *Hyper Cyan* (`#06B6D4`).
- **Dukungan Adaptif**: Dilengkapi ikon launcher adaptif Android (foreground terpisah dan background aman), ikon bulat legacy, serta *Monochrome Themed Icon* untuk Android 13+.
- **Aset Vektor & Master**: Berkas master SVG dan PNG resolusi tinggi tersedia di `codeatlas/assets/branding/`.

<p align="center">
  <img src="codeatlas/assets/branding/codeatlas_icon_preview.png" width="850" alt="Matriks Ikon dan Keterbacaan CodeAtlas" />
</p>

---

## 📁 Struktur Repositori

```
ca/
├── codeatlas/                 # Aplikasi mobile Flutter (Dart 3, Material 3, SQLite)
│   ├── assets/content/        # Dataset produksi 99 topik, 76 kategori, 36 kuis (content.json)
│   ├── lib/                   # Arsitektur kode modular (features, data, widgets, state)
│   └── test/                  # Suite 50 pengujian (11 berkas uji komprehensif)
├── docs/                      # Dokumentasi teknis, PRD, dan spesifikasi arsitektur
└── scripts/                   # Generator kurikulum, generator konten, & verifikasi migrasi SQLite
```

---

## ✨ Fitur Utama

1. **Beranda (Home)**
   - Status pembelajaran per lapis (*Fundamental* & *Ekosistem*) secara *real-time*.
   - Pintasan **Mulai dari nol** dan **Pilih tujuan**.
   - Kartu **Lanjutkan Membaca** yang mengarahkan langsung ke topik terakhir yang dibuka.
   - Status pemahaman mandiri: **Belum**, **Sedang**, dan **Paham**.

2. **Jelajah (Explore)**
   - Tampilan dua tab terpisah: **Fundamental Programming** (47 topik dalam 12 kelompok) dan **Dunia & Ekosistem** (52 domain dalam 12 kelompok industri).
   - Mesin pencarian teks cerdas mencakup judul, ringkasan, penjelasan awam/teknis, kata kunci (*keywords*), dan konteks masalah.
   - Filter gabungan (*AND logic*): Lapis, Kategori, dan Tingkat Kesulitan (*Pemula*, *Menengah*, *Lanjutan*).

3. **Detail Topik (Deep Pedagogical Article)**
   - **8 Bagian Terstruktur**:
     1. Analogi Keseharian (pemahaman konkret non-teknis)
     2. Konteks Masalah (latar belakang diciptakannya konsep)
     3. Penjelasan Teknis Akurat (standar industri & runtime behavior)
     4. Miskonsepsi Umum (kesalahan asumsi pemula/AI)
     5. Contoh Kode Nyata (snippet 3–15 baris + output yang diharapkan)
     6. Kapan Menggunakan & Kapan Menghindari (panduan arsitektural)
     7. Kenapa Penting saat Vibecoding (mitigasi risiko kode AI)
     8. Refleksi Pemahaman (pertanyaan interaktif dengan kunci jawaban tersembunyi)
   - **FAB Navigasi Daftar Isi**: Modal *bottom sheet* untuk melompat langsung ke bagian yang diinginkan.
   - **Catatan Pribadi**: Editor catatan dengan batas 20.000 karakter, indikator status simpan otomatis, dan proteksi *in-flight typing*.

4. **Peta Prasyarat Bertingkat (Progressive Roadmap)**
   - **Level 1 (Peta Awal)**: Pemilih lapis responsif (*Wrap*) dan daftar kartu kelompok materi dengan indikator pemahaman.
   - **Level 2 (Alur Topik Kelompok)**: Alur vertikal topik dengan konektor panah prasyarat internal dan chip lompatan lintas kelompok.
   - **Level 3 (Panel Fokus Bawah)**: Panel bawah yang menampilkan detail topik terpilih, prasyarat, topik dependen, dan tombol langsung **Buka Artikel**.
   - **Tampilan Aksesibilitas**: Opsi beralih ke daftar relasi teks bertingkat (*screen reader friendly*).
   - **Bebas Overflow**: Teruji pada lebar 360px & 400px serta skala teks 100% dan 200%.

5. **Latihan (Practice)**
   - **Kuis Tebak Bahasa**: Membaca dan mengenali bahasa pemrograman dari ciri sintaks (label bahasa disembunyikan sebelum menjawab).
   - **Kuis Tebak Konsep**: Menguji pemahaman konsep logika, arsitektur, dan mitigasi bug dari potongan kode.
   - **Perbandingan Sintaks Multi-Bahasa**: Menampilkan konsep identik berdampingan dalam **Dart**, **TypeScript**, dan **Python** dengan pengalih tata letak (swipe horizontal / list vertikal adaptif).

6. **Jalur Belajar (Learning Paths)**
   - 5 Preset jalur belajar siap pakai:
     - *Memahami dasar dari nol* (`general`)
     - *Membaca kode Flutter* (`flutter`)
     - *Memahami web* (`web`)
     - *Memahami backend* (`backend`)
     - *Memahami data* (`data`)
   - Algoritma pelengkap prasyarat transitif (*transitive closure*) dan pengurutan topologis (*Topological Sort*).
   - Editor jalur kustom (*custom path*) dengan validasi ketergantungan.

---

## 📊 Cakupan Konten (Production Dataset)

- **Total Kategori**: **76** (12 Kelompok Fundamental, 12 Kelompok Ekosistem, 52 Domain Ekosistem)
- **Total Artikel Topik**: **99 Artikel Lengkap** (47 Fundamental + 52 Ekosistem)
- **Total Soal Kuis**: **36 Soal** (14 Tebak Bahasa + 22 Tebak Konsep)
- **Kelompok Perbandingan Sintaks**: **10 Kelompok** (masing-masing dalam Dart, TypeScript, dan Python)

---

## 🛠️ Arsitektur & Teknologi

- **Framework**: Flutter 3.47+ (Dart 3.13+)
- **UI System**: Material 3, Dark/Light theme otomatis mengikuti sistem, tata letak adaptif.
- **Penyimpanan Lokal**: SQLite via `sqflite` (skema DDL ketat dengan `PRAGMA foreign_keys = ON`).
- **Migrasi Database**: Skema database v2 mendukung struktur artikel 8 bagian secara atomik dengan proteksi anti-downgrade.
- **Offline-First**: Seluruh konten dibundel di dalam aset `codeatlas/assets/content/content.json` dan di-seed saat pembukaan pertama.
- **Bebas Eksekusi Kode**: Tidak mengeksekusi kode di perangkat pengguna demi keamanan, privasi, dan stabilitas.

---

## 🧪 Jaminan Kualitas & Pengujian (50 Tests)

Seluruh 50 pengujian otomatis lulus 100% dari 11 berkas uji:

| No | Berkas Pengujian | Tes | Area yang Diuji |
|:--:|:---|:--:|:---|
| 1 | `test/bootstrap_and_retry_widget_test.dart` | 3 | Fallback banner saat upgrade gagal, error & retry saat DB kosong, dan update katalog. |
| 2 | `test/comparison_widget_test.dart` | 2 | Auto-switch tata letak vertikal skala 200% tanpa overflow & pengalih mode perbandingan. |
| 3 | `test/content_and_path_test.dart` | 6 | Validasi integritas JSON 76 kategori, 99 topik, DAG asiklik (Kahn), dan 36 kuis. |
| 4 | `test/explore_filter_widget_test.dart` | 2 | Navigasi tab Fundamental/Ekosistem dan kombinasi pencarian + filter (logika AND). |
| 5 | `test/learning_flow_test.dart` | 8 | Model progress, label status bahasa Indonesia, limit catatan 20k karakter, kuis scoring. |
| 6 | `test/learning_path_algorithm_test.dart` | 7 | Transitive closure, deduplikasi, topological sort, penolakan urutan tak valid, 5 preset. |
| 7 | `test/quiz_session_widget_test.dart` | 3 | Penyembunyian label bahasa UI & Semantics sebelum menjawab, opsi acak stabil, cegah resubmit. |
| 8 | `test/roadmap_filter_widget_test.dart` | 2 | Alur bertahap Roadmap (Level 1 -> 2 -> 3) dan lompatan prasyarat lintas kelompok. |
| 9 | `test/topic_detail_widget_test.dart` | 5 | Rendering 8 bagian artikel, modal navigasi Daftar Isi, ekspansi refleksi, uji bebas overflow 200%. |
| 10 | `test/topic_notes_widget_test.dart` | 5 | Rendering catatan, update status tanpa menimpa catatan, indikator teks belum disimpan, in-flight typing. |
| 11 | `test/version_branching_unit_test.dart` | 7 | Percabangan versi DB (initialSeed, skipEqual, upgradeHigher, migrasi v1->v2, penolakan downgrade). |

---

## 🚀 Cara Menjalankan

```bash
# 1. Pindah ke folder aplikasi
cd codeatlas

# 2. Unduh dependensi
flutter pub get

# 3. Jalankan pengujian
flutter test

# 4. Periksa kepatuhan kode
flutter analyze

# 5. Jalankan aplikasi atau kompilasi APK debug
flutter run
# atau: flutter build apk --debug
```
