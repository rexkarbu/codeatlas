# Rencana Aplikasi: Ensiklopedia Fundamental Coding

> Tujuan: aplikasi personal untuk memahami **fundamental coding** dari nol sampai paham (bukan cuma vibecoding tanpa dasar), sekaligus jadi "peta dunia coding" yang menjelaskan semua istilah dan konsep yang sering muncul.

---

## 1. Ringkasan

Masalah yang mau diselesaikan: sering vibecoding (nulis/nyuruh AI nulis kode) tapi nggak paham fundamentalnya — kenapa sesuatu bekerja, istilah apa itu, dan gimana semua bagian (bahasa, framework, database, server, dll) saling terhubung.

Solusinya: satu aplikasi referensi + pembelajaran, isinya dua lapis:

- **Lapis 1 — Fundamental Programming**: konsep dasar yang wajib dipahami siapa pun yang coding (logika, variabel, fungsi, OOP, Git, HTTP, SQL, dst).
- **Lapis 2 — Dunia & Ekosistem Coding**: peta lengkap semua kategori teknologi yang ada di industri (bahasa, framework, cloud, DevOps, AI, dst), supaya paham istilah dan konteks besarnya.

Semua penjelasan pakai **bahasa orang awam dulu** (analogi sehari-hari), baru istilah teknisnya menyusul.

---

## 2. Rekomendasi Nama Aplikasi

| Nama                           | Alasan                                                                             |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| **CodeAtlas** ⭐ (rekomendasi) | "Atlas" = peta lengkap dunia coding, pas karena aplikasi ini memuat semua kategori |
| **Primer**                     | Simpel, satu kata, artinya "buku pengantar/dasar" — cocok tema fundamental         |
| **DevRoots**                   | "Roots" = akar/fundamental development                                             |
| **CodeCompass**                | Kompas penuntun arah belajar coding                                                |
| **Fondasi.dev**                | Bahasa Indonesia "fondasi" + akhiran .dev, terasa personal                         |

Kalau mau konsisten dengan gaya nama app kamu sebelumnya (huruf kecil semua, singkat, ala "mywatchlist"), bisa pakai versi lowercase: `codeatlas` atau `myprimer`.

---

## 3. Filosofi Konten (aturan wajib untuk semua materi)

1. **Bahasa awam dulu** — tiap topik dibuka dengan analogi sederhana (contoh: "Variable itu kayak kotak/laci yang punya nama, isinya bisa diganti-ganti"), baru definisi teknis.
2. **Berjenjang** — tiap topik punya level: `Fundamental` → `Menengah` → `Lanjutan/Opsional`.
3. **Saling terhubung** — tiap topik mencantumkan **prasyarat** (harus paham apa dulu) dan **topik terkait** (lanjut ke mana).
4. **Contoh konkret** — tiap konsep disertai contoh kode singkat (idealnya multi-bahasa: JS/TS, karena itu yang kamu kuasai).
5. **Kenapa penting** — tiap topik jelasin di mana konsep ini biasanya "nongol" saat vibecoding (misal: "kamu pasti sering lihat `async/await` — ini yang lagi dipelajari").

---

## 4. Struktur Konten — Level 1: Fundamental Programming

List asli kamu (39 topik) dikelompokkan + beberapa **tambahan (ditandai +)** yang menurutku penting biar makin lengkap.

**A. Logika & Sintaks Dasar**
Programming Logic · Variables & Data Types · Operators · Conditional Statements · Loops · Functions · Scope
`+ Type System (Static vs Dynamic Typing)` — kenapa TypeScript "strict" dan JavaScript "bebas"
`+ Recursion` — konsep fungsi yang manggil dirinya sendiri, sering bikin bingung pemula

**B. Struktur Data & Algoritma**
Data Structures · Algorithms
`+ Big-O Notation / Analisis Kompleksitas` — dasar buat ngerti "kenapa kode ini lambat"

**C. Paradigma & Kualitas Kode**
Object-Oriented Programming · Functional Programming Basics · Clean Code / Code Organization · Design Patterns Basics · Software Architecture Basics

**D. Menangani Kesalahan**
Error Handling · Debugging · Testing

**E. Sistem, Memori & I/O**
Memory Basics · Pointers / References · Input / Output · File System Basics · Operating System Basics

**F. Modularitas & Tooling**
Modules & Packages · Dependency Management · Build & Compilation Basics · Runtime Basics · Version Control / Git · Command Line / Terminal

**G. Jaringan & Web**
Networking Basics · HTTP / Web Fundamentals · API Fundamentals
`+ Data Serialization (JSON/XML/YAML)` — format tukar data antar sistem

**H. Data & Database**
Database Fundamentals · SQL · Data Modeling

**I. Keamanan & Akses**
Authentication & Authorization · Security Basics

**J. Konkurensi**
Concurrency / Parallelism
`+ Asynchronous Programming (Promise/Async-Await)` — ini yang paling sering dipakai tapi jarang dipahami akarnya

**K. Proses & Kebiasaan Kerja**
Deployment Basics · Logging & Monitoring Basics
`+ Software Development Life Cycle (SDLC) & Agile Basics` — alur kerja proyek software
`+ Kebiasaan Dokumentasi (Comments & README)` — skill kecil tapi krusial

**L. Payung Besar**
Computer Science Fundamentals

**Total: 39 asli + 7 tambahan = 46 topik fundamental**

---

## 5. Struktur Konten — Level 2: Dunia & Ekosistem Coding

List asli kamu (45 kategori) dikelompokkan + **tambahan (+)**.

**A. Bahasa & Alat Inti**
Bahasa Pemrograman · Compiler / Interpreter · Runtime · Package Manager · Build Tools

**B. Framework & Library**
Framework · Library · ORM / Query Builder

**C. Pengembangan per Platform**
Frontend Development · Backend Development · Mobile Development · Desktop Development · Game Development · Embedded Systems / IoT · Graphics Programming

**D. Data & Komunikasi**
Database · API & Communication · Message Queue / Broker · Caching

**E. Ilmu Komputer**
Data Structures & Algorithms · Paradigma Pemrograman · System Programming · Computer Science Fundamentals

**F. Arsitektur & Desain**
Software Architecture · Design Pattern
`+ Distributed Systems` — dasar sistem yang jalan di banyak server sekaligus

**G. Infrastruktur & Jaringan**
Networking · Operating System · Terminal / Shell · Web Server / Reverse Proxy · Cloud Computing · Infrastructure as Code · Container Orchestration

**H. Kualitas & Keamanan**
Testing · Debugging · Security · Cybersecurity
`+ Accessibility (a11y)` — bikin aplikasi bisa dipakai semua orang, sering terlewat

**I. DevOps & Operasional**
DevOps · Observability · Deployment & Production · Developer Tools

**J. Data Lanjutan & AI**
Data Engineering · AI / Machine Learning
`+ Data Science & Analytics` — beda dari Data Engineering (fokus analisis/insight, bukan infrastruktur data)

**K. Proses & Kolaborasi**
Version Control · Software Engineering Process · UI/UX untuk Development
`+ Technical Documentation & API Design (OpenAPI/Swagger)`
`+ Localization & Internationalization (i18n/l10n)`

**L. Opsional / Lanjutan**
`+ Blockchain / Web3` (opsional, tandai sebagai advanced)
`+ Software Licensing & Open Source` — jenis lisensi (MIT, GPL, dll), penting kalau pakai/kontribusi ke open source

**Total: 45 asli + 7 tambahan = 52 kategori dunia coding**

---

## 6. Fitur Aplikasi

- **Peta topik (roadmap/graph view)** — visualisasi hubungan antar topik, prasyarat → lanjutan
- **Halaman tiap topik**: analogi awam → penjelasan teknis → contoh kode → kapan dipakai → topik terkait
- **Progress tracker**: status tiap topik (Belum / Sedang / Paham), dengan checklist
- **Catatan pribadi** per topik (tempat nulis pemahaman sendiri)
- **Kuis "Tebak Bahasa/Konsep dari Potongan Kode"** — user disodori snippet kode, lalu tebak bahasa apa itu / konsep apa yang dipakai. Sifatnya baca & kenali, **bukan** menulis/menjalankan kode — pas untuk tujuan "paham bahasa yang belum pernah tahu" tanpa perlu bangun sandbox/compiler
- **Perbandingan Sintaks Antar Bahasa**: satu konsep (loop, function, class, dll) ditampilkan berdampingan di beberapa bahasa, biar begitu AI kasih kode dalam bahasa asing, langsung bisa "dibaca"
- **Search & filter** by kategori/level
- **Learning path custom**: misal "saya vibecoding Flutter, tunjukkan fundamental yang wajib saya kuasai duluan"
- **Mode "Kenapa Ini Penting"**: kaitkan tiap konsep dengan skenario vibecoding nyata

> Catatan desain: aplikasi ini **sengaja tidak** pakai code editor/sandbox yang bisa run kode beneran. Fokusnya pengenalan & pemahaman (karena kamu tetap akan lebih banyak vibecoding), bukan latihan menulis kode dari nol — jadi nggak perlu bangun compiler/interpreter di app, cukup konten statis + kuis.

---

## 7. Struktur Data (Model Konten)

```
Category
  - id, name, level (fundamental/dunia-coding), order, description

Topic
  - id, category_id
  - name
  - level (fundamental / menengah / lanjutan)
  - explanation_simple (bahasa awam)
  - explanation_technical
  - code_examples[] (bahasa: js/ts/dart/dll)
  - prerequisites[] (topic_id)
  - related_topics[] (topic_id)
  - why_it_matters (kaitan ke vibecoding)
  - resources[] (link belajar lanjutan, opsional)

Progress
  - topic_id, status, notes, last_reviewed_at

Quiz
  - topic_id, questions[] (pertanyaan, pilihan, jawaban benar, penjelasan)
```

---

## 8. Rekomendasi Tech Stack

Karena kamu sudah terbiasa dengan **Flutter** untuk proyek-proyek sebelumnya, disarankan lanjut Flutter juga di sini biar alur vibecoding-nya konsisten:

- **Frontend/App**: Flutter (mobile, offline-first)
- **Penyimpanan konten**: SQLite atau Hive lokal — konten (topik, kategori) di-seed dari file JSON terstruktur, jadi gampang di-generate/diedit
- **Progress & catatan user**: disimpan lokal juga (SQLite/Hive), tidak perlu backend di awal
- **Opsional nanti**: kalau mau sync progress lintas device, baru tambah backend sederhana (pola sama seperti proyek watchlist kamu: Go + SQLite)

Alternatif: kalau kontennya berat teks (ensiklopedia panjang) dan kamu ingin gampang diakses dari device apa saja, web app (Next.js) juga valid — tapi Flutter tetap konsisten dengan workflow kamu sekarang.

---

## 9. Prompt Siap Kirim ke Codex CLI

Salin blok di bawah ini untuk diberikan ke Codex CLI, minta dibuatkan dokumentasi lengkap (PRD, struktur folder, skema data, dan prompt final untuk vibecoding di Antigravity):

```
Saya ingin membuat aplikasi mobile (Flutter) bernama "CodeAtlas" — sebuah
ensiklopedia interaktif untuk belajar fundamental programming dari nol,
karena saya sering vibecoding tanpa memahami dasar-dasarnya.

Aplikasi ini punya dua lapis konten:

LAPIS 1 - FUNDAMENTAL PROGRAMMING (46 topik), dikelompokkan:
- Logika & Sintaks Dasar: Programming Logic, Variables & Data Types,
  Operators, Conditional Statements, Loops, Functions, Scope,
  Type System, Recursion
- Struktur Data & Algoritma: Data Structures, Algorithms, Big-O Notation
- Paradigma & Kualitas Kode: OOP, Functional Programming Basics,
  Clean Code, Design Patterns Basics, Software Architecture Basics
- Menangani Kesalahan: Error Handling, Debugging, Testing
- Sistem, Memori & I/O: Memory Basics, Pointers/References,
  Input/Output, File System Basics, Operating System Basics
- Modularitas & Tooling: Modules & Packages, Dependency Management,
  Build & Compilation Basics, Runtime Basics, Version Control/Git,
  Command Line/Terminal
- Jaringan & Web: Networking Basics, HTTP/Web Fundamentals,
  API Fundamentals, Data Serialization (JSON/XML/YAML)
- Data & Database: Database Fundamentals, SQL, Data Modeling
- Keamanan & Akses: Authentication & Authorization, Security Basics
- Konkurensi: Concurrency/Parallelism, Asynchronous Programming
- Proses & Kebiasaan Kerja: Deployment Basics, Logging & Monitoring
  Basics, SDLC & Agile Basics, Kebiasaan Dokumentasi
- Payung Besar: Computer Science Fundamentals

LAPIS 2 - DUNIA & EKOSISTEM CODING (52 kategori), dikelompokkan:
- Bahasa & Alat Inti: Bahasa Pemrograman, Compiler/Interpreter, Runtime,
  Package Manager, Build Tools
- Framework & Library: Framework, Library, ORM/Query Builder
- Pengembangan per Platform: Frontend, Backend, Mobile, Desktop, Game
  Development, Embedded Systems/IoT, Graphics Programming
- Data & Komunikasi: Database, API & Communication, Message Queue/
  Broker, Caching
- Ilmu Komputer: Data Structures & Algorithms, Paradigma Pemrograman,
  System Programming, Computer Science Fundamentals
- Arsitektur & Desain: Software Architecture, Design Pattern,
  Distributed Systems
- Infrastruktur & Jaringan: Networking, Operating System, Terminal/
  Shell, Web Server/Reverse Proxy, Cloud Computing, Infrastructure as
  Code, Container Orchestration
- Kualitas & Keamanan: Testing, Debugging, Security, Cybersecurity,
  Accessibility
- DevOps & Operasional: DevOps, Observability, Deployment & Production,
  Developer Tools
- Data Lanjutan & AI: Data Engineering, Data Science & Analytics,
  AI/Machine Learning
- Proses & Kolaborasi: Version Control, Software Engineering Process,
  UI/UX untuk Development, Technical Documentation & API Design,
  Localization & Internationalization
- Opsional/Lanjutan: Blockchain/Web3, Software Licensing & Open Source

ATURAN KONTEN:
- Setiap topik WAJIB dijelaskan pakai bahasa orang awam dulu (analogi
  sehari-hari) sebelum istilah teknis.
- Setiap topik punya: penjelasan awam, penjelasan teknis, contoh kode
  singkat, daftar prasyarat, daftar topik terkait, dan "kenapa ini
  penting saat vibecoding".

FITUR APLIKASI:
- Peta/roadmap visual hubungan antar topik
- Halaman detail per topik sesuai aturan konten di atas
- Progress tracker (Belum/Sedang/Paham) per topik
- Catatan pribadi per topik
- Kuis "Tebak Bahasa/Konsep dari Potongan Kode" (baca & kenali, bukan
  menulis/menjalankan kode)
- Perbandingan Sintaks Antar Bahasa (satu konsep ditampilkan
  berdampingan di beberapa bahasa)
- Search & filter berdasarkan kategori/level
- Learning path custom berdasarkan tujuan user

CATATAN PENTING: aplikasi ini SENGAJA TIDAK memakai code editor/sandbox
yang bisa menjalankan kode. Tujuannya user paham & bisa mengenali kode
(karena user tetap akan lebih banyak vibecoding), bukan latihan menulis
kode dari nol. Jangan bangun compiler/interpreter/code runner apa pun.

TECH STACK: Flutter, penyimpanan lokal (SQLite/Hive), konten di-seed
dari JSON terstruktur, offline-first (tanpa backend di versi awal).

TUGAS ANDA:
1. Buat PRD (Product Requirements Document) lengkap.
2. Buat skema data/model (Category, Topic, Progress, Quiz).
3. Buat struktur folder proyek Flutter yang direkomendasikan.
4. Buat contoh isi JSON untuk 3 topik pertama sebagai referensi format
   konten.
5. Susun semua ini menjadi satu prompt final yang siap saya masukkan ke
   Antigravity untuk proses vibecoding.
```

---
