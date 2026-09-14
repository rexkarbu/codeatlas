# Prompt implementasi CodeAtlas untuk Antigravity

Anda bertindak sebagai Flutter engineer dan penulis materi pemrograman untuk pemula. Bangun aplikasi mobile **CodeAtlas** berdasarkan PRD, model data, struktur folder, skema SQL, dan contoh JSON dalam dokumen ini. Seluruh dokumen ini adalah satu prompt yang mandiri; tidak membutuhkan percakapan sebelumnya atau lampiran lain.

Kerjakan implementasinya, bukan hanya menjawab dengan rencana. Baca proyek dan instruksi lokal terlebih dahulu, gunakan kode yang sudah ada jika sesuai, lalu lanjutkan sampai fitur dan kriteria penerimaan di bawah terpenuhi. Gunakan keputusan yang ditetapkan di sini sebagai default. Jangan menambahkan backend, layanan AI, atau fitur yang tidak diminta. Jika toolchain tidak tersedia, lanjutkan pekerjaan yang memungkinkan dan laporkan batas verifikasi secara jujur.

## 1. PRD: tujuan dan batas produk

**Masalah:** pengguna sering meminta AI membuat kode, tetapi belum memahami konsep dasar, hubungan antar teknologi, atau konsekuensi perubahan kode tersebut.

**Visi:** ensiklopedia interaktif berbahasa Indonesia yang membantu pengguna membaca kode, mengenali konsep, dan bertanya kepada AI dengan pemahaman yang lebih baik.

**Pengguna utama:** pemula yang belajar dari nol dan pengguna vibecoding yang sudah membuat aplikasi tetapi sering bingung membaca hasil AI. Pengetahuan awal bahasa pemrograman tidak diasumsikan.

**Hasil belajar yang dituju:** pengguna dapat menjelaskan konsep dengan kata sendiri, mengenali contoh kode, membedakan teknologi yang sering tertukar, mengetahui prasyarat, dan mengidentifikasi pertanyaan atau pemeriksaan yang diperlukan saat menerima kode AI.

**Platform dan asumsi v1:** Flutter untuk Android dan iOS, satu pengguna lokal, antarmuka dan materi bahasa Indonesia, istilah teknis asli tetap ditampilkan. Android menjadi target verifikasi pertama; verifikasi build iOS memerlukan macOS/Xcode. Tidak ada login. Semua fungsi inti tersedia sejak pembukaan pertama dalam mode pesawat setelah aplikasi terpasang.

**Koreksi inventaris:** daftar kebutuhan memuat **47 topik fundamental**, walaupun judul awal menyebut 46. Pertahankan semua 47. Lapis 2 memuat **52 kategori ekosistem**. Tiap kategori ekosistem memiliki satu artikel pengantar lengkap pada v1: total **99 artikel**, bukan 99 konsep unik karena beberapa konsep dibahas dari dua sudut pandang. Angka progress dihitung dari data aktual, bukan konstanta 46 atau 99.

**Cakupan rilis awal:** kedua lapis konten dan seluruh delapan fitur yang diminta wajib selesai. Tiga contoh JSON dalam prompt adalah referensi format dan tahap pengembangan pertama, bukan batas konten rilis.

**Di luar cakupan:** code editor, tombol Run, REPL, sandbox eksekusi kode, compiler/interpreter buatan aplikasi, evaluasi kode dinamis, pengiriman snippet ke layanan eksekusi, login, backend, cloud sync, chat AI, pembayaran, iklan, leaderboard, sertifikat, notifikasi, dan CMS. Flutter/Dart toolchain untuk membangun aplikasi tetap digunakan secara normal; larangan eksekusi berlaku pada fitur untuk pengguna dan snippet konten.

**Batas penyimpanan:** v1 menyimpan data pada perangkat ini. Uninstall atau penghapusan data aplikasi dapat menghilangkan progress, catatan, dan jalur belajar. Jelaskan singkat di halaman Tentang. Backup/export dan sinkronisasi menjadi pekerjaan terpisah ketika diminta, bukan implementasi tersembunyi dalam v1.

## 2. Taksonomi lengkap dan identitas konten

Pisahkan **lapis** dari **tingkat kesulitan**. Lapis adalah `fundamentals` atau `ecosystem`; tingkat kesulitan adalah `beginner`, `intermediate`, atau `advanced`, dengan label Pemula, Menengah, Lanjutan. Artikel ekosistem boleh berada pada tingkat Pemula.

Gunakan ID berikut sebagai identitas stabil. Judul dapat diperbaiki tanpa mengganti ID. `sort_order` mengikuti urutan daftar pada kelompoknya dan bukan relasi prasyarat.

### 2.1 Lapis 1: Fundamental Programming

Setiap baris adalah Category bertipe `group`, berlapis `fundamentals`, dengan `parent_id = null`. Semua ID item dalam kolom terakhir adalah ID Topic lengkap.

| Category ID | Kelompok | Jumlah | Topic ID dan judul |
| --- | --- | ---: | --- |
| f-logic | Logika & Sintaks Dasar | 9 | `f-programming-logic`: Programming Logic; `f-variables-data-types`: Variables & Data Types; `f-operators`: Operators; `f-conditionals`: Conditional Statements; `f-loops`: Loops; `f-functions`: Functions; `f-scope`: Scope; `f-type-system`: Type System; `f-recursion`: Recursion |
| f-data-algorithms | Struktur Data & Algoritma | 3 | `f-data-structures`: Data Structures; `f-algorithms`: Algorithms; `f-big-o`: Big-O Notation |
| f-code-quality | Paradigma & Kualitas Kode | 5 | `f-oop`: OOP; `f-functional-programming`: Functional Programming Basics; `f-clean-code`: Clean Code; `f-design-patterns`: Design Patterns Basics; `f-software-architecture`: Software Architecture Basics |
| f-errors | Menangani Kesalahan | 3 | `f-error-handling`: Error Handling; `f-debugging`: Debugging; `f-testing`: Testing |
| f-systems | Sistem, Memori & I/O | 5 | `f-memory`: Memory Basics; `f-references`: Pointers/References; `f-input-output`: Input/Output; `f-file-system`: File System Basics; `f-operating-system`: Operating System Basics |
| f-tooling | Modularitas & Tooling | 6 | `f-modules-packages`: Modules & Packages; `f-dependencies`: Dependency Management; `f-build-compilation`: Build & Compilation Basics; `f-runtime`: Runtime Basics; `f-git`: Version Control/Git; `f-terminal`: Command Line/Terminal |
| f-web | Jaringan & Web | 4 | `f-networking`: Networking Basics; `f-http-web`: HTTP/Web Fundamentals; `f-apis`: API Fundamentals; `f-serialization`: Data Serialization (JSON/XML/YAML) |
| f-data | Data & Database | 3 | `f-databases`: Database Fundamentals; `f-sql`: SQL; `f-data-modeling`: Data Modeling |
| f-security-access | Keamanan & Akses | 2 | `f-auth`: Authentication & Authorization; `f-security`: Security Basics |
| f-concurrency-group | Konkurensi | 2 | `f-concurrency`: Concurrency/Parallelism; `f-async`: Asynchronous Programming |
| f-process | Proses & Kebiasaan Kerja | 4 | `f-deployment`: Deployment Basics; `f-logging-monitoring`: Logging & Monitoring Basics; `f-sdlc-agile`: SDLC & Agile Basics; `f-documentation`: Kebiasaan Dokumentasi |
| f-overview | Payung Besar | 1 | `f-computer-science`: Computer Science Fundamentals |

Jumlah: 12 kategori kelompok dan 47 Topic.

### 2.2 Lapis 2: Dunia & Ekosistem Coding

Kolom pertama berisi Category `group` berlapis `ecosystem`, `parent_id = null`. Setiap item pada kolom terakhir adalah Category `domain` dengan `parent_id` menunjuk kelompoknya. Buat satu Topic pengantar per domain, ber-ID `<domain_id>-overview`, dengan `category_id` domain tersebut. Contoh: domain `e-runtime` memiliki Topic `e-runtime-overview`.

| Group ID | Kelompok | Jumlah domain | Domain ID dan judul |
| --- | --- | ---: | --- |
| e-core-tools | Bahasa & Alat Inti | 5 | `e-languages`: Bahasa Pemrograman; `e-compilers`: Compiler/Interpreter; `e-runtime`: Runtime; `e-package-managers`: Package Manager; `e-build-tools`: Build Tools |
| e-frameworks-libraries | Framework & Library | 3 | `e-frameworks`: Framework; `e-libraries`: Library; `e-orm`: ORM/Query Builder |
| e-platforms | Pengembangan per Platform | 7 | `e-frontend`: Frontend; `e-backend`: Backend; `e-mobile`: Mobile; `e-desktop`: Desktop; `e-games`: Game Development; `e-embedded`: Embedded Systems/IoT; `e-graphics`: Graphics Programming |
| e-data-communication | Data & Komunikasi | 4 | `e-databases`: Database; `e-api-communication`: API & Communication; `e-message-brokers`: Message Queue/Broker; `e-caching`: Caching |
| e-computing | Ilmu Komputer | 4 | `e-dsa`: Data Structures & Algorithms; `e-paradigms`: Paradigma Pemrograman; `e-system-programming`: System Programming; `e-computer-science`: Computer Science Fundamentals |
| e-architecture-design | Arsitektur & Desain | 3 | `e-architecture`: Software Architecture; `e-patterns`: Design Pattern; `e-distributed`: Distributed Systems |
| e-infrastructure | Infrastruktur & Jaringan | 7 | `e-networking`: Networking; `e-operating-systems`: Operating System; `e-shells`: Terminal/Shell; `e-web-servers`: Web Server/Reverse Proxy; `e-cloud`: Cloud Computing; `e-iac`: Infrastructure as Code; `e-orchestration`: Container Orchestration |
| e-quality-security | Kualitas & Keamanan | 5 | `e-testing`: Testing; `e-debugging`: Debugging; `e-security`: Security; `e-cybersecurity`: Cybersecurity; `e-accessibility`: Accessibility |
| e-operations | DevOps & Operasional | 4 | `e-devops`: DevOps; `e-observability`: Observability; `e-production`: Deployment & Production; `e-developer-tools`: Developer Tools |
| e-advanced-data | Data Lanjutan & AI | 3 | `e-data-engineering`: Data Engineering; `e-data-science`: Data Science & Analytics; `e-ai-ml`: AI/Machine Learning |
| e-collaboration | Proses & Kolaborasi | 5 | `e-version-control`: Version Control; `e-engineering-process`: Software Engineering Process; `e-ui-ux`: UI/UX untuk Development; `e-technical-docs`: Technical Documentation & API Design; `e-localization`: Localization & Internationalization |
| e-advanced-optional | Opsional/Lanjutan | 2 | `e-blockchain`: Blockchain/Web3; `e-open-source`: Software Licensing & Open Source |

Jumlah: 12 kategori kelompok, 52 kategori domain, dan 52 Topic pengantar. Total seluruh tabel categories v1 adalah **76**: 12 kelompok fundamental + 12 kelompok ekosistem + 52 domain. Jangan menampilkan angka 76 sebagai jumlah kategori ekosistem kepada pengguna.

Lapis 1 menjelaskan konsep dan cara membaca kode. Lapis 2 menjelaskan peran suatu bidang/alat, contoh teknologi, kapan dipakai, dan kaitannya dengan bidang lain. Misalnya `f-runtime` membahas apa yang terjadi saat program berjalan; `e-runtime-overview` memetakan runtime dalam ekosistem. Hubungkan lewat topik terkait; jangan menyalin artikel yang sama. Artikel pengantar Computer Science Fundamentals bukan prasyarat wajib seluruh atlas. Hindari siklus prasyarat karena dua artikel saling mengacu secara konseptual; gunakan relasi terkait untuk itu.

Blockchain/Web3 ditandai advanced dan opsional. Software Licensing & Open Source tetap berada pada kelompok yang diminta tetapi artikel pengantarnya boleh beginner/intermediate. Pengantar lisensi menjelaskan konsep dengan contoh identifier seperti SPDX, tanpa menjanjikan kesimpulan legal universal.

## 3. Aturan penulisan konten

Setiap Topic aktif wajib memiliki:

1. Judul, ringkasan satu kalimat, tingkat kesulitan, estimasi baca, dan kategori.
2. **Penjelasan awam lebih dulu:** analogi keseharian, arti konsep, dan batas analogi bila bisa menyesatkan. Jangan membuka artikel dengan jargon yang belum dijelaskan.
3. **Penjelasan teknis:** definisi akurat, istilah penting, perilaku, dan kesalahan umum. Jelaskan istilah saat pertama muncul.
4. **Contoh kode singkat:** minimal satu snippet sekitar 3–15 baris, bahasa diberi label, penjelasan cara membaca, dan hasil yang diharapkan jika relevan. Pseudocode, SQL, shell, konfigurasi, atau komentar lisensi diperbolehkan bila sesuai topik, dengan label yang jujur. Jangan membuat kode pura-pura untuk topik nonkode.
5. **Prasyarat:** daftar ID topik yang diperlukan; daftar kosong sah untuk titik masuk.
6. **Topik terkait:** daftar ID valid, minimal satu untuk artikel rilis; dapat lintas lapis dan tidak berarti wajib dipelajari dulu.
7. **Kenapa penting saat vibecoding:** satu skenario konkret, risiko salah memahami, dan hal yang perlu diperiksa atau ditanyakan kepada AI.

Materi sekitar 300–600 kata per artikel adalah pedoman, bukan alasan menambah pengisi; prioritaskan kejelasan dan kelengkapan. Semua contoh kode dan output adalah konten statis. UI menamai output **“Hasil yang diharapkan”**, tidak memberi kesan baru menjalankan kode. Jangan mengeksekusi snippet, termasuk ketika import/seed dan kuis. Validasi konten membaca strukturnya, bukan melakukan eval.

Bahasa awal perbandingan: **Dart, TypeScript, Python**. Jelaskan jika semantik tidak persis sama, seperti `const`, `final`, boolean, pembagian, dan typing. Jangan menyatakan sebuah bahasa secara universal “compiled” atau “interpreted” tanpa konteks implementasi. Contoh teknologi pada lapis ekosistem bukan rekomendasi untuk selalu memasangnya. Verifikasi klaim yang berubah terhadap dokumentasi primer ketika menulis materi produksi.

Paket produksi wajib memuat semua 99 artikel lengkap, tanpa TODO, lorem ipsum, atau penjelasan generik yang disalin ke semua topik. Paket tiga artikel di bagian akhir berstatus `reference`. Ganti menjadi `production` hanya setelah memenuhi cakupan dan pemeriksaan konten rilis.

## 4. Alur pengguna dan kebutuhan fungsional

Navigasi bawah: **Beranda, Jelajah, Peta, Latihan, Jalurku**. Detail topik dibuka sebagai halaman tersendiri dari semua titik masuk. Pencarian berada di Jelajah; perbandingan sintaks tersedia di Latihan dan detail topik. Pengaturan tema/Tentang dapat diakses dari Beranda. Gunakan komponen Material 3 dan label teks yang jelas.

Alur pertama: buka aplikasi → seed lokal dengan indikator loading → Beranda menjelaskan dua lapis secara singkat → pilih “Mulai dari nol” atau “Pilih tujuan”. Pengguna juga dapat langsung menjelajah. Jangan mewajibkan onboarding panjang atau pengisian profil.

| ID | Cerita pengguna dan perilaku | Kriteria penerimaan |
| --- | --- | --- |
| F01 | Sebagai pemula, saya ingin menemukan titik mulai dan melanjutkan bacaan. Beranda menampilkan mulai dari nol, topik terakhir dibaca, dan progress per lapis. | Instalasi baru menampilkan angka nol; setelah membuka topik lalu restart, “Lanjutkan membaca” menuju ID yang sama. Membaca saja tidak mengubah status. |
| F02 | Saya ingin menjelajah kedua lapis berdasarkan pengelompokan yang diminta. | Fundamental menampilkan 12 kelompok/47 artikel. Ekosistem menampilkan 12 kelompok/52 domain dengan artikel pengantar. Istilah “Lapis” dan “Tingkat kesulitan” tidak dicampur. |
| F03 | Saya ingin memahami sebuah topik dengan bahasa sehari-hari sebelum membaca definisi. | Urutan detail: judul/ringkasan → analogi awam → teknis → kode → penting saat vibecoding → prasyarat/terkait → catatan. Status dan estimasi baca terlihat. Semua tautan topik membuka detail yang benar. |
| F04 | Saya ingin melihat peta hubungan yang dapat disentuh. | Peta menampilkan node topik dan panah prasyarat → topik tujuan, dengan label status, zoom/pan, tap ke detail, serta fokus lapis/kategori/jalur. Ada legenda dan tampilan daftar relasi yang setara untuk aksesibilitas. |
| F05 | Saya ingin memberi penilaian pemahaman saya sendiri. | Status Belum/Sedang/Paham dapat diubah dua arah kapan pun dan tersimpan setelah restart. Membuka halaman atau benar di kuis tidak menandai Paham otomatis. |
| F06 | Saya ingin menulis catatan pribadi pada topik. | Catatan multiline maksimal 20.000 karakter Unicode; ada tombol Simpan, keadaan belum disimpan/tersimpan/gagal, dan peringatan saat keluar dengan perubahan belum tersimpan. Simpan kosong mengosongkan catatan tanpa mengubah status. Gagal tulis mempertahankan draft di layar dan menawarkan coba lagi. |
| F07 | Saya ingin mengenali bahasa atau konsep dari kode. | Kuis pilihan ganda offline memiliki dua mode, tanpa editor. Jawaban dicek lewat ID opsi, feedback menjelaskan alasannya, dan tersedia tautan ke topik. Satu soal dinilai satu kali dalam satu sesi. |
| F08 | Saya ingin membandingkan konsep yang sama dalam beberapa bahasa. | Pilih konsep dan 2–3 bahasa; tampilkan snippet berdampingan, penjelasan perbedaan, dan hasil statis bila ada. Di ponsel gunakan kartu dalam area horizontal yang dapat digeser; tersedia alternatif daftar vertikal pada teks besar. Jangan mengganti dengan satu bahasa saja. |
| F09 | Saya ingin mencari istilah dan mempersempit hasil. | Pencarian mengabaikan kapitalisasi, mencakup judul, keywords, ringkasan, penjelasan awam/teknis, dan manfaat vibecoding. Filter lapis, kategori, dan level digabung dengan AND. Kueri kosong menampilkan seluruh hasil yang cocok dengan filter. Ada jumlah hasil, kosong/tidak ditemukan, serta reset filter. |
| F10 | Saya ingin jalur belajar sesuai tujuan. | Pilih tujuan, lihat usulan urutan dan alasan singkat, edit nama/topik/urutan yang valid, simpan, buka kembali, lalu lanjutkan topik pertama yang belum Paham. Mendukung lebih dari satu jalur dan jalur dari nol. |

### 4.1 Progress dan catatan

Mapping status: `not_started` = Belum, `in_progress` = Sedang, `understood` = Paham. Tidak ada baris Progress berarti Belum, catatan kosong, belum pernah dibaca. Boleh membuat baris default ketika pertama dibaca untuk menyimpan `last_reviewed_at`; status tetap Belum.

Persentase = jumlah Topic aktif berstatus Paham / jumlah Topic aktif dalam cakupan × 100. Jika penyebut nol, tampilkan 0% dengan pesan belum ada materi. Tampilkan juga jumlah Sedang. Category hanya mengagregasi status topik turunannya; tidak memiliki status independen. Progress jalur menggunakan daftar ID uniknya dan dibagikan dengan progress atlas, bukan disalin per jalur. Label Paham adalah penilaian diri, bukan sertifikasi kompetensi.

Simpan perubahan status hanya ke kolom status/timestamp; simpan catatan hanya ke notes/timestamp. Jangan menimpa catatan dengan draft lama ketika pengguna mengganti status. Tombol Simpan baru menampilkan sukses setelah transaksi selesai. Saat keluar dengan draft: Simpan, Buang perubahan, atau Tetap di halaman; jika penyimpanan gagal, tetap di halaman. Progress tidak dapat hilang karena pembaruan artikel.

### 4.2 Roadmap

Gunakan graph terarah tanpa siklus untuk prasyarat. Edge disimpan sebagai pasangan `(topic_id, prerequisite_id)` tetapi **digambar dari prerequisite ke topic**. Akses artikel selalu terbuka; prasyarat yang belum Paham hanya diberi keterangan “Disarankan pelajari dahulu”.

Default peta fokus satu kelompok, dengan opsi melihat satu lapis atau jalur. Posisi node ditentukan dari kedalaman prasyarat menggunakan urutan topologis, kemudian `sort_order` dan ID sebagai pemecah seri. Gunakan `InteractiveViewer`, `Stack` berisi widget node, dan `CustomPainter` untuk garis; tidak perlu library graph/layout fisika. Pan/zoom tersedia dari [InteractiveViewer resmi Flutter](https://api.flutter.dev/flutter/widgets/InteractiveViewer-class.html).

Ketika memilih node, tampilkan prasyarat langsung dan topik yang langsung memerlukannya. Relasi lintas filter ditampilkan sebagai chip berlabel lapis/kategori, dengan aksi pindah fokus; jangan menghapus relasi tersebut dari data. Relasi terkait tidak dipakai untuk menentukan urutan: tampilkan pada panel node/detail, bukan sebagai semua garis tambahan. Node memakai label teks dan Semantics, bukan hanya gambar di canvas. Detail dan daftar relasi tetap menjadi jalan alternatif saat peta padat atau pengguna memakai pembaca layar.

### 4.3 Kuis

Satu record Quiz = satu soal; tidak ada objek sesi bernama Quiz yang membungkus banyak soal. Sesi dibuat dari kumpulan soal aktif yang sesuai mode/lapis/level. Ambil acak tanpa pengulangan sebanyak `min(5, jumlah_soal_tersedia)`. Nol soal menampilkan keadaan kosong; kurang dari lima tetap dapat dimainkan. Acak opsi sambil mempertahankan ID; simpan pilihan/susunan dalam state sesi agar rebuild tidak mengacaknya lagi.

Sebelum pengguna mengirim jawaban, jangan tampilkan metadata bahasa pada kuis tebak bahasa, termasuk judul code block, accessibility label, atau tooltip. Gunakan teks monospace biasa. Setelah dikirim, kunci jawaban soal tersebut, tampilkan benar/salah, jawaban yang benar, dan alasan. Semua pertanyaan harus memiliki satu jawaban yang tidak ambigu di antara opsi; snippet yang valid dalam banyak bahasa harus memakai pilihan yang tidak bertabrakan atau pertanyaan yang lebih spesifik.

Ringkasan sesi: jumlah benar/total dan tautan topik untuk soal salah. Skor tidak mengubah Progress. State sesi cukup di memori: keluar dari sesi yang belum selesai memunculkan konfirmasi; force-close dapat mengakhiri sesi. Histori lintas sesi dan model QuizAttempt belum diperlukan.

Bank soal produksi minimum 30: sedikitnya 10 tebak bahasa dan 20 tebak konsep, mencakup minimal 15 topik berbeda (minimal 10 fundamental dan 5 ekosistem). Jangan memaksakan kuis tebak bahasa untuk konsep yang tidak punya snippet pembeda yang masuk akal. Tiga soal contoh di bawah hanya untuk pengembangan awal.

### 4.4 Perbandingan sintaks

Gunakan `Topic.code_examples`, dikelompokkan dengan `(topic_id, comparison_key)`. Tiap kelompok berisi maksimal satu contoh per bahasa dan menggambarkan tugas yang sama. `comparison_key = null` berarti contoh berdiri sendiri dan tidak masuk daftar perbandingan. Fitur hanya menawarkan kelompok dengan minimal dua bahasa; pilihan yang tidak punya padanan harus dijelaskan, bukan diisi snippet konsep lain.

Produksi memiliki minimal sembilan kelompok perbandingan: variabel/tipe, operator, conditional, loop, function, list, class/object, error handling, async/await. Masing-masing tersedia dalam Dart, TypeScript, dan Python; contoh sequence tambahan dari referensi boleh dipertahankan. Snippet asynchronous memiliki asumsi konteks yang dijelaskan, tanpa menyatakan eksekusi semua bahasa identik.

### 4.5 Learning path custom

Gunakan aturan deterministik lokal, tanpa model AI. Setiap preset adalah daftar target Topic ID dalam kode kecil `path_builder.dart`; bukan sistem rekomendasi baru. Prasyarat aktual berasal dari konten. Tampilkan target yang diminta, topik tambahan dari prasyarat, dan alasan preset cocok dengan tujuan.

| Goal | Nama yang ditampilkan | Target inti sebelum menambahkan prasyarat |
| --- | --- | --- |
| general | Memahami dasar dari nol | `f-programming-logic`, `f-variables-data-types`, `f-operators`, `f-conditionals`, `f-loops`, `f-functions`, `f-debugging`, `f-testing`, `f-git` |
| flutter | Membaca kode Flutter | `f-type-system`, `f-oop`, `f-modules-packages`, `f-dependencies`, `f-error-handling`, `f-async`, `f-apis`, `f-serialization`, `f-testing`, `e-mobile-overview`, `e-frameworks-overview` |
| web | Memahami web | `f-http-web`, `f-apis`, `f-serialization`, `f-async`, `f-security`, `e-frontend-overview`, `e-backend-overview` |
| backend | Memahami backend | `f-apis`, `f-databases`, `f-sql`, `f-data-modeling`, `f-auth`, `f-security`, `f-testing`, `f-deployment`, `e-backend-overview` |
| data | Memahami data | `f-data-structures`, `f-algorithms`, `f-databases`, `f-sql`, `f-data-modeling`, `e-data-engineering-overview`, `e-data-science-overview` |
| custom | Buat sendiri | Target dipilih pengguna dari daftar topik aktif, minimal satu. |

Algoritma: kumpulkan seluruh prasyarat transitif target → hilangkan duplikasi ID → urutkan secara topologis, dengan `(sort_order, id)` sebagai urutan stabil untuk kandidat yang sama-sama siap → simpan daftar Topic ID. Topik yang sudah Paham tetap terlihat sebagai selesai dan tidak disarankan untuk diulang; “Lanjutkan” melewatinya. Jika semua sudah Paham, tampilkan jalur selesai.

Pengguna dapat menambah/menghapus topik, mengganti nama, dan menyeret urutan. Menambah topik juga menambahkan prasyarat transitif yang belum ada. Menyeret tidak boleh menempatkan prasyarat sesudah topik yang membutuhkannya; tolak gerakan dengan penjelasan. Menghapus prasyarat yang masih diperlukan topik lain ditolak dengan daftar dependennya; pengguna bisa menghapus dependen dahulu. Dengan demikian kustomisasi tidak menghasilkan urutan yang bertentangan diam-diam. Jalur tidak boleh kosong ketika disimpan. Jangan mengunci artikel berdasarkan jalur.

Simpan daftar jalur dalam satu transaksi; pengurutan ulang dapat menghapus dan menulis ulang **item jalur itu saja**, tanpa menyentuh Topic atau Progress. Hapus jalur meminta konfirmasi dan hanya menghapus jalur serta itemnya. Jika pembaruan konten mengubah prasyarat, tampilkan pemberitahuan jalur perlu ditinjau dan pratinjau perbaikan; jangan mengubah jalur pengguna diam-diam.

## 5. Kebutuhan nonfungsional, risiko, dan ukuran keberhasilan

| Area | Ketentuan |
| --- | --- |
| Offline | Semua teks, contoh kode, soal, dan metadata ada dalam assets. Tidak memakai font/gambar wajib dari jaringan, HTTP API, telemetry, atau koneksi untuk membuka konten. Perangkat baru dapat seed dalam mode pesawat. |
| Keandalan data | Semua perubahan lokal ditunggu hasilnya; error terlihat dan dapat dicoba ulang. Seed idempotent dan atomik; migrasi tidak mereset data pengguna. Jangan memakai drop database sebagai pemulihan otomatis. |
| Kecepatan | Target, bukan klaim yang sudah diukur: startup sampai Beranda ≤3 detik setelah seed pertama dan pencarian ≤200 ms pada dataset rilis, diuji pada satu perangkat Android kelas menengah yang dicatat. Loading awal tetap ditampilkan bila seed memerlukan waktu lebih lama. |
| Keterbacaan | Light/dark mengikuti sistem, teks dapat diperbesar sampai 200%, tombol sentuh minimal 48×48 logical pixels, contrast teks normal ditargetkan ≥4.5:1. Tidak mengandalkan warna saja untuk status atau jawaban. |
| Aksesibilitas | Label Semantics, urutan fokus masuk akal, keyboard tidak menutup Simpan, code block dapat di-scroll/diseleksi, layar kecil tidak overflow. Roadmap punya alternatif daftar. |
| Privasi dan input | Tidak mengirim catatan atau progress keluar perangkat. Query memakai parameter, bukan interpolasi SQL. Catatan teks biasa, tanpa HTML yang dieksekusi; tidak menulis isi catatan ke log. |
| Konten | Semua ID/rujukan valid, prasyarat acyclic, perbedaan lapis jelas, soal tidak ambigu, dan analogi diperiksa manusia. Validasi struktur tidak boleh diklaim membuktikan akurasi pedagogis. |

Pilihan SQLite dengan `sqflite` sesuai kebutuhan penyimpanan mobile lokal, dan parameter query mengikuti [panduan SQLite resmi Flutter](https://docs.flutter.dev/cookbook/persistence/sqlite). Aplikasi ini tidak membutuhkan mekanisme sinkronisasi karena v1 hanya mempunyai sumber data lokal.

**Ukuran keberhasilan teknis:** 99 artikel lengkap dapat dibuka offline; tidak ada broken link konten; seluruh fitur F01–F10 lulus; progress/catatan/jalur tetap ada setelah restart dan upgrade konten; tidak ada fitur eksekusi snippet.

**Ukuran keberhasilan belajar untuk uji awal:** ajak 3–5 pengguna pemula, masing-masing mencari satu istilah, membaca tiga topik pertama, menjelaskan satu konsep dengan bahasanya sendiri, dan menyelesaikan sesi pengenalan kode. Target awal ≥80% dapat menyelesaikan tugas navigasi tanpa bantuan; evaluasi jawaban dengan penjelasan, bukan menyamakan jumlah artikel Paham dengan kompetensi. Catat hasil uji manual, tanpa SDK analytics.

**Risiko utama dan mitigasi:** cakupan 99 artikel berpotensi dangkal → penulisan per kelompok dengan pemeriksaan editorial; graph terlalu padat → fokus kelompok dan panel relasi; progress memberi rasa mahir yang keliru → label penilaian diri; pembaruan merusak catatan → transaksi dan pemisahan tabel; konsep lintas bahasa disamakan → penjelasan perbedaan semantik per snippet.

## 6. Model data dan kontrak persistensi

JSON dan kolom database memakai `snake_case`; properti Dart memakai `camelCase`. Buat class immutable dengan `final`, enum yang diserialisasi sebagai string, dan parsing manual yang memvalidasi input. Tidak perlu `freezed`, ORM, atau generator JSON untuk skala ini.

### 6.1 Category

| Field JSON/SQL | Tipe Dart | Aturan |
| --- | --- | --- |
| id | String | Primary key stabil, nonkosong. |
| parent_id | String? | Null untuk group; domain menunjuk group ekosistem di lapis yang sama. Maksimum dua tingkat kategori. |
| layer | ContentLayer | `fundamentals` atau `ecosystem`. |
| kind | CategoryKind | `group` atau `domain`. Fundamental hanya group. |
| title | String | Nama kelompok/domain yang ditampilkan. |
| description | String | Ringkasan awam yang tidak kosong. |
| sort_order | int | Urutan tampilan dalam induknya, ≥0. |

### 6.2 Topic

| Field JSON/model | Tipe Dart | Penyimpanan/aturan |
| --- | --- | --- |
| id | String | PK stabil, `f-*` untuk fundamental atau `<domain_id>-overview` untuk pengantar ekosistem. |
| category_id | String | FK Category; Topic fundamental pada group fundamental, Topic ekosistem pada domain. |
| title, summary | String | Judul dan ringkasan nonkosong. |
| level | Difficulty | beginner/intermediate/advanced; tidak sama dengan layer. |
| explanation_simple | String | Analogi dan penjelasan awam; tampil lebih dahulu. |
| explanation_technical | String | Penjelasan teknis nonkosong. |
| code_examples | List<CodeExample> | Minimal satu; disimpan JSON TEXT dalam `code_examples_json`. |
| prerequisite_ids | List<String> | Relasi terarah di tabel `topic_prerequisites`; tanpa duplikasi/self-reference/siklus. |
| related_topic_ids | List<String> | Relasi saran di tabel `topic_related`; tanpa duplikasi/self-reference. Boleh membentuk siklus dan boleh lintas lapis. |
| why_vibecoding_matters | String | Kasus konkret dan hal yang diperiksa. |
| keywords | List<String> | Alias pencarian; JSON TEXT dalam `keywords_json`. |
| estimated_minutes | int | Estimasi baca >0, bukan waktu yang dilacak. |
| sort_order | int | Urutan tampilan dalam kategori. |
| is_active | bool | SQL INTEGER 0/1. Artikel yang dipensiunkan tetap disimpan untuk menjaga referensi pengguna. |

`CodeExample`: `language: String`, `comparison_key: String?`, `label: String`, `code: String`, `explanation: String`, `expected_output: String?`. Label bahasa konsisten, misalnya `dart`, `typescript`, `python`, `sql`, `shell`, `pseudocode`. Pseudocode selalu ditandai sebagai ilustrasi, bukan bahasa executable.

Relasi terkait bersifat editorial per arah: jika A mencantumkan B, B tidak wajib mencantumkan A. UI menggunakan daftar yang ditulis, tidak menambah relasi balik tersimpan secara otomatis. Arah balik prasyarat dihitung dari tabel yang sama untuk “Topik yang membutuhkan ini”.

### 6.3 Progress

| Field | Tipe Dart | Aturan |
| --- | --- | --- |
| topic_id | String | PK sekaligus FK Topic; satu baris per topik, tanpa user_id untuk v1 satu pengguna lokal. |
| status | LearningStatus | not_started/in_progress/understood. |
| notes | String | Default kosong, maksimum 20.000 Unicode code points; validasi Dart dengan `runes.length`. |
| last_reviewed_at | DateTime? | Waktu terakhir artikel dibuka; disimpan UTC epoch milliseconds, null bila belum pernah. |
| updated_at | DateTime | Waktu pembuatan/perubahan status atau catatan; UTC epoch milliseconds. |

### 6.4 Quiz

| Field JSON/model | Tipe Dart | Aturan |
| --- | --- | --- |
| id | String | PK stabil. |
| topic_id | String | FK ke topik utama penjelasan. |
| type | QuizType | language/concept. |
| level | Difficulty | Tingkat kesulitan soal. |
| prompt | String | Pertanyaan spesifik dan tidak kosong. |
| snippet | String | Kode/pseudocode statis untuk dibaca. |
| snippet_language | String | Metadata internal; disembunyikan sebelum menjawab kuis bahasa. |
| options | List<QuizOption> | Tepat empat opsi untuk v1, ID dan teks unik; disimpan sebagai `options_json`. |
| correct_option_id | String | Harus cocok tepat satu ID opsi. Jangan menyimpan jawaban sebagai indeks. |
| explanation | String | Alasan jawaban benar dan pembeda dari pilihan yang mengecoh. |
| is_active | bool | Menentukan apakah dapat masuk sesi. |

`QuizOption`: `id: String`, `text: String`. State sesi (urutan soal, opsi yang diacak, jawaban yang dipilih, skor) cukup di memori dan terpisah dari konten soal. Tidak perlu tabel attempt untuk fitur yang diminta.

### 6.5 Data tambahan yang diperlukan fitur

`LearningPath`: `id: int` PK lokal otomatis, `name: String` 1–100 karakter, `goal: String` sesuai preset/custom, `created_at` dan `updated_at` UTC epoch milliseconds. `LearningPathItem`: `path_id: int`, `topic_id: String`, `position: int`. Satu topik hanya muncul sekali dalam satu jalur; urutan posisi unik dan ditulis berurutan mulai 0.

`content_meta`: satu baris dengan `content_version`, `dataset`, dan `locale`. **Tiga versi berbeda:** `format_version` pada JSON menentukan kontrak parser; `content_version` menentukan revisi materi; versi database pada `openDatabase(version: ...)` menentukan migrasi tabel. Jangan menyamakan ketiganya.

Tidak perlu tabel Notes, Comparison, User, atau Goal terpisah: Notes melekat ke Progress, comparison menggunakan contoh kode Topic, pengguna hanya satu lokal, dan preset tujuan cukup konstanta kecil.

Hubungan ringkas:

```text
Category(group) -> Category(domain)       hanya ekosistem
Category -> Topic                       1 : banyak
Topic -> Progress                       1 : 0..1
Topic -> Quiz                           1 : banyak
Topic -> Topic                          banyak : banyak, prasyarat / terkait
LearningPath -> LearningPathItem -> Topic
```

### 6.6 Skema SQLite yang harus dipakai

DDL di bawah adalah referensi executable. Pada Flutter, jalankan per-statement saat `onCreate`; aktifkan foreign keys di `onConfigure` untuk setiap koneksi sebelum transaksi. Constraint lintas record yang tidak dinyatakan DDL (kategori sejenis, graph acyclic, isi JSON, jawaban soal) divalidasi oleh seed loader. Foreign keys perlu diaktifkan secara eksplisit sebagaimana dijelaskan [dokumentasi SQLite](https://www.sqlite.org/foreignkeys.html).

<!-- BEGIN EMBEDDED SQL -->
```sql
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
```
<!-- END EMBEDDED SQL -->

### 6.7 Seed, validasi, dan upgrade tanpa kehilangan data

1. Bundle satu file `assets/content/content.json` pada `pubspec.yaml`. Decode dengan `dart:convert`. Tolak format_version tidak didukung, tipe data salah, field wajib kosong, enum tidak dikenal, ID ganda, dan referensi putus. Pesan validasi harus mencantumkan ID/field bermasalah.
2. Validasi seluruh graph kategori dan prasyarat sebelum menulis. Domain harus mempunyai group ekosistem yang benar; Topic harus berada pada jenis Category yang sesuai. Tolak self-reference, duplikasi edge, dan siklus prasyarat. Deteksi siklus dengan DFS warna atau Kahn, bukan traversal yang bisa berulang tanpa akhir.
3. Validasi snippet nonkosong, pasangan bahasa/comparison unik, opsi soal/jawaban valid, dan referensi soal ke Topic aktif. Paket `production` diperiksa terhadap seluruh 47 ID fundamental, 52 domain, dan 52 ID artikel pengantar yang tercantum di taksonomi; bukan sekadar menghitung jumlah. Artikel aktif hanya mereferensikan artikel aktif. Semua kelompok perbandingan dan jumlah kuis produksi harus memenuhi PRD.
4. Pada database kosong, insert kategori induk dahulu, domain, seluruh Topic, relasi, lalu Quiz dalam satu transaksi; tulis content_meta paling akhir. **Jangan seed Progress atau jalur pengguna dari JSON konten.**
5. Jika content_version sama, tidak menulis ulang konten. Jika lebih tinggi, validasi dulu, lalu update record yang ada dan insert ID baru dalam satu transaksi. Versi lebih rendah tidak boleh menurunkan konten database secara otomatis; tampilkan pesan versi tidak cocok jika parser aplikasi tidak dapat membacanya.
6. Update Category/Topic/Quiz berdasarkan PK; jangan `INSERT OR REPLACE` untuk record induk. REPLACE dapat menghapus baris lama sebelum insert menurut [dokumentasi SQLite](https://www.sqlite.org/lang_conflict.html). Gunakan UPDATE lalu INSERT jika belum ada, atau UPSERT yang kompatibel dengan target SQLite.
7. Untuk topik yang masih aktif, refresh edge konten dalam transaksi. Jika sebuah ID Topic/Quiz tidak lagi ada dalam paket terbaru, tandai inactive dan pertahankan record lama. Jangan menghapus Category lama atau progress, catatan, dan item jalur. Konten inactive disembunyikan dari penjelajahan baru, tetapi masih dapat dibuka dari catatan/jalur lama dengan label Diarsipkan; Beranda menyediakan akses ke catatan pada topik arsip jika ada.
8. Jangan mengganti ID hanya karena perubahan judul. Jalur lama dipertahankan sebagai urutan tersimpan; perubahan graph ditampilkan sebagai kebutuhan tinjau jalur, bukan mengubah data pengguna diam-diam. Topik arsip tidak masuk penyebut progress aktif; jalur dengan artikel arsip menampilkan hitungan arsip dan saran untuk meninjau.
9. Jika seed/upgrade gagal, rollback semua perubahan konten dan metadata. Pertahankan database lama yang valid dan tampilkan kegagalan pembaruan dengan coba lagi. Pada instalasi baru, tampilkan error pemuatan dengan coba lagi, tanpa dashboard kosong yang seolah sukses. Kegagalan migrasi skema juga tidak boleh memicu reset database.
10. Semua query berparameter. Semua operasi dalam transaksi menggunakan objek transaksi `sqflite` yang sama. Tidak ada write tanpa await atau exception yang ditelan.

## 7. Arsitektur dan struktur folder Flutter

Pilih **SQLite + sqflite**, bukan SQLite dan Hive bersamaan. Dependency runtime tambahan awal cukup `sqflite` dan `path`, seperti pada [resep SQLite Flutter](https://docs.flutter.dev/cookbook/persistence/sqlite). Gunakan versi stable yang kompatibel dengan SDK terpasang ketika implementasi, catat versi sebenarnya di README, dan commit `pubspec.lock`; jangan menyalin nomor versi asumsi dari ingatan.

State sederhana: `ChangeNotifier` + `ListenableBuilder`, dengan objek repository konkret diinjeksi lewat constructor. `ChangeNotifier` merupakan fasilitas Flutter untuk memberitahu perubahan state, sebagaimana [panduan state management Flutter](https://docs.flutter.dev/data-and-backend/state-mgmt/simple). Gunakan `Navigator`/`MaterialPageRoute` dan NavigationBar bawaan. Tidak perlu DI container, BLoC, Riverpod, routing package, atau lapisan use-case untuk tiap operasi CRUD pada v1.

Satu ContentRepository menangani baca konten dan relasi; satu LearningRepository menangani Progress dan LearningPath. AppDatabase mengelola koneksi/skema; SeedLoader mengimpor dan memvalidasi konten. Widget tidak menjalankan SQL. Path builder adalah fungsi domain kecil yang dapat diuji tanpa perangkat. Pertahankan state edit catatan dan sesi kuis pada layar agar tidak memenuhi global AppState.

```text
codeatlas/
  pubspec.yaml
  pubspec.lock
  README.md
  analysis_options.yaml
  assets/
    content/
      content.json                 # seluruh 99 artikel + kategori + kuis
  lib/
    main.dart                      # bootstrap database, seed, dan error awal
    app.dart                       # MaterialApp, tema sistem, navigasi utama
    data/
      models.dart                  # empat model inti + value object/jalur
      app_database.dart            # open, onConfigure, schema, migrations
      seed_loader.dart             # validasi paket dan seed atomik
      content_repository.dart      # katalog, detail, search, relasi, kuis
      learning_repository.dart     # progress, catatan, jalur belajar
    state/
      app_state.dart               # state bersama yang benar-benar dipakai
    features/
      home/
        home_screen.dart
      explore/
        explore_screen.dart        # kategori, search, filter
      topic/
        topic_screen.dart          # detail, status, catatan
      roadmap/
        roadmap_screen.dart        # graph + alternatif daftar
      practice/
        practice_screen.dart       # pilihan kuis / perbandingan
        quiz_screen.dart
        comparison_screen.dart
      learning_paths/
        paths_screen.dart          # daftar dan detail jalur
        path_editor_screen.dart
        path_builder.dart          # preset + closure + urutan prasyarat
    widgets/
      code_snippet.dart            # teks monospace read-only yang dipakai ulang
      topic_tile.dart              # judul, lapis, level, status
  test/
    content_and_path_test.dart     # validasi referensi, cycle, closure/urutan
    learning_flow_test.dart        # widget progress/catatan/kuis
  integration_test/
    offline_persistence_test.dart  # SQLite nyata: seed/restart/upgrade
  android/                         # hasil flutter create
  ios/                             # hasil flutter create
  docs/
    PRD.md                         # salinan kontrak produk dari prompt
```

Struktur di atas direkomendasikan, bukan alasan membuat file kosong. Bila dua layar pendek lebih jelas dalam satu file, boleh digabung. Pecah `models.dart` hanya setelah ukurannya mengganggu pembacaan. Jangan membuat interface dengan satu implementasi, generic base repository, event bus, service locator, atau sistem plugin konten.

Search dapat memfilter katalog yang sudah dibaca di memori: lowercase + split whitespace, semua token harus muncul pada gabungan field yang ditentukan. Urutkan judul exact match, prefix judul, lalu urutan kategori/topik yang stabil. Seluruh filter tetap berlaku pada semua hasil. Untuk sekitar 99 artikel ini cukup; beri komentar `ponytail: linear scan untuk katalog kecil; gunakan FTS ketika pengukuran pencarian tidak memenuhi target.` Tidak perlu mesin pencari eksternal atau fuzzy matching v1.

Snippet ditampilkan melalui `SelectableText` monospace dan scroll horizontal; tidak perlu editor/highlighter dependency untuk memenuhi pengenalan kode. Semua styling bersumber dari tema; jangan menambahkan WebView untuk merender kode. Pengaturan mengikuti tema sistem tanpa tabel preferensi tambahan.

## 8. Contoh JSON lengkap untuk tiga topik pertama

JSON ini valid dan mandiri: satu kategori fundamental, tiga Topic berurutan, sembilan contoh kode untuk perbandingan, dan tiga soal. Seluruh ID relasi merujuk record yang tersedia di contoh. Daftar prasyarat kosong pada Programming Logic memang disengaja. Array terkait boleh mencakup topik yang lebih awal maupun lebih lanjut.

Gunakan contoh ini untuk memverifikasi flow pertama; kemudian perluas file yang sama mengikuti taksonomi lengkap. Tidak perlu menambahkan placeholder untuk membuat jumlah artikel terlihat lengkap. Bahasa perbandingan dan angka kuis pada paket `reference` tidak harus memenuhi jumlah produksi, tetapi semua pemeriksaan integritas berlaku.

<!-- BEGIN EMBEDDED JSON -->
```json
{
  "format_version": 1,
  "content_version": 1,
  "dataset": "reference",
  "locale": "id-ID",
  "categories": [
    {
      "id": "f-logic",
      "parent_id": null,
      "layer": "fundamentals",
      "kind": "group",
      "title": "Logika & Sintaks Dasar",
      "description": "Belajar memberi instruksi yang jelas, menyimpan informasi, dan mengolahnya.",
      "sort_order": 1
    }
  ],
  "topics": [
    {
      "id": "f-programming-logic",
      "category_id": "f-logic",
      "title": "Programming Logic",
      "level": "beginner",
      "summary": "Menyusun langkah yang jelas agar komputer melakukan hal yang kita maksud.",
      "explanation_simple": "Bayangkan kamu meminta seseorang menyiapkan segelas air. Instruksi 'ambil gelas, tuang air, lalu minum' masuk akal karena urutannya jelas. Jika 'minum' diletakkan sebelum air dituangkan, hasilnya tidak sesuai harapan. Komputer juga membutuhkan instruksi yang jelas. Analogi ini punya batas: manusia bisa menebak maksud kita, sedangkan program mengikuti aturan yang ditulis dan tidak otomatis memahami niat pembuatnya.",
      "explanation_technical": "Programming logic adalah cara menyusun langkah dan aturan untuk mengubah masukan menjadi hasil yang diinginkan. Tiga pola dasarnya adalah urutan instruksi (sequence), pemilihan berdasarkan kondisi (selection), dan pengulangan (iteration). Topik ini mengenalkan urutan terlebih dahulu; percabangan dan pengulangan dibahas di topik berikutnya. Algoritma adalah rangkaian langkah penyelesaian masalah, sedangkan sintaks adalah aturan penulisan dalam bahasa tertentu. Kode dapat benar secara sintaks tetapi salah secara logika jika urutannya tidak sesuai tujuan.",
      "code_examples": [
        {
          "language": "typescript",
          "comparison_key": "sequence",
          "label": "Menampilkan tiga instruksi secara berurutan",
          "code": "console.log(\"Ambil gelas\");\nconsole.log(\"Tuang air\");\nconsole.log(\"Minum air\");",
          "explanation": "Baca dari atas ke bawah. Setiap console.log menampilkan satu baris teks. Program ini hanya menampilkan instruksi; program tidak mengambil gelas atau menuangkan air secara fisik.",
          "expected_output": "Ambil gelas\nTuang air\nMinum air"
        },
        {
          "language": "python",
          "comparison_key": "sequence",
          "label": "Urutan yang sama dalam Python",
          "code": "print(\"Ambil gelas\")\nprint(\"Tuang air\")\nprint(\"Minum air\")",
          "explanation": "print menampilkan teks. Nama perintahnya berbeda dari TypeScript, tetapi urutan instruksi dan hasil bacaan sama.",
          "expected_output": "Ambil gelas\nTuang air\nMinum air"
        },
        {
          "language": "dart",
          "comparison_key": "sequence",
          "label": "Urutan yang sama dalam Dart",
          "code": "void main() {\n  print(\"Ambil gelas\");\n  print(\"Tuang air\");\n  print(\"Minum air\");\n}",
          "explanation": "main adalah titik awal program Dart. Baca tiga print di dalam kurung kurawal dari atas ke bawah. Bentuk fungsi main akan dijelaskan lebih lengkap pada topik Functions.",
          "expected_output": "Ambil gelas\nTuang air\nMinum air"
        }
      ],
      "prerequisite_ids": [],
      "related_topic_ids": ["f-variables-data-types", "f-operators"],
      "why_vibecoding_matters": "Saat AI membuat alur checkout, kode bisa terlihat rapi tetapi mengosongkan keranjang sebelum pesanan berhasil disimpan. Memahami urutan membuatmu bisa meminta AI menjelaskan kapan data dibaca, disimpan, dan dihapus, lalu memeriksa apakah urutannya sesuai kebutuhan.",
      "keywords": ["logika", "urutan", "sequence", "alur program"],
      "estimated_minutes": 5,
      "sort_order": 1,
      "is_active": true
    },
    {
      "id": "f-variables-data-types",
      "category_id": "f-logic",
      "title": "Variables & Data Types",
      "level": "beginner",
      "summary": "Memberi nama pada informasi dan mengenali jenis nilainya.",
      "explanation_simple": "Bayangkan rak dengan label 'nama barang', 'jumlah', dan 'tersedia'. Label membantu kamu menemukan informasi yang tepat. Isi 'jumlah' cocok berupa angka, sedangkan 'tersedia' cukup ya atau tidak. Variabel mirip label untuk mengakses nilai. Analogi rak tidak selalu harfiah: beberapa nama dapat merujuk ke objek yang sama, dan beberapa nama memang tidak boleh diberi nilai baru.",
      "explanation_technical": "Variabel menghubungkan nama dengan nilai atau lokasi penyimpanan, tergantung model bahasanya. Jenis data menentukan nilai dan operasi yang masuk akal, misalnya string untuk teks, angka untuk perhitungan, dan boolean untuk true/false. TypeScript dan Dart memeriksa banyak aturan tipe sebelum program dijalankan; Python memeriksa operasi tipe saat program berjalan. Python tetap mempunyai tipe data walaupun contoh ini tidak menuliskan anotasi tipe. Di TypeScript, let mengizinkan pemberian nilai baru dan const melarang penggantian binding; const tidak otomatis membekukan isi sebuah objek. Di Dart, final melarang pemberian nilai baru pada variabel. Perbedaan sistem tipe dibahas lebih jauh di Type System.",
      "code_examples": [
        {
          "language": "typescript",
          "comparison_key": "variables",
          "label": "Nama, jumlah, dan ketersediaan sebuah barang",
          "code": "const nama: string = \"Buku\";\nlet jumlah: number = 2;\nconst tersedia: boolean = true;\njumlah = 3;\nconsole.log(nama, jumlah, tersedia);",
          "explanation": "nama berisi teks, jumlah berisi angka, dan tersedia berisi boolean. Tanda = memberikan nilai. Nilai jumlah berubah dari 2 menjadi 3 sebelum ditampilkan. Anotasi setelah titik dua adalah petunjuk tipe TypeScript.",
          "expected_output": "Buku 3 true"
        },
        {
          "language": "python",
          "comparison_key": "variables",
          "label": "Data yang sama dalam Python",
          "code": "nama = \"Buku\"\njumlah = 2\ntersedia = True\njumlah = 3\nprint(nama, jumlah, tersedia)",
          "explanation": "Anotasi tipe tidak diperlukan pada contoh Python ini. True ditulis dengan huruf T besar. Nilai akhir sama, tetapi pembatasan pemberian nilai baru berbeda: ketiga nama di sini dapat diberi nilai baru.",
          "expected_output": "Buku 3 True"
        },
        {
          "language": "dart",
          "comparison_key": "variables",
          "label": "Data yang sama dalam Dart",
          "code": "void main() {\n  final String nama = \"Buku\";\n  int jumlah = 2;\n  final bool tersedia = true;\n  jumlah = 3;\n  print(\"$nama $jumlah $tersedia\");\n}",
          "explanation": "String, int, dan bool menyatakan jenis data. jumlah dapat diberi nilai baru; nama dan tersedia menggunakan final. Bentuk $nama di dalam teks menyisipkan nilai variabel ke teks hasil.",
          "expected_output": "Buku 3 true"
        }
      ],
      "prerequisite_ids": ["f-programming-logic"],
      "related_topic_ids": ["f-programming-logic", "f-operators"],
      "why_vibecoding_matters": "AI kadang memperlakukan harga dari formulir sebagai angka padahal nilainya masih berupa teks. Akibatnya, operasi yang terlihat seperti penjumlahan bisa menghasilkan gabungan teks. Kamu perlu mengenali jenis nilai dan meminta konversi serta validasi pada batas masukan, bukan sekadar meminta AI menghilangkan pesan error tipe.",
      "keywords": ["variabel", "tipe data", "string", "number", "boolean", "let", "const", "final"],
      "estimated_minutes": 7,
      "sort_order": 2,
      "is_active": true
    },
    {
      "id": "f-operators",
      "category_id": "f-logic",
      "title": "Operators",
      "level": "beginner",
      "summary": "Mengenali simbol untuk menghitung, membandingkan, dan menggabungkan syarat.",
      "explanation_simple": "Saat membeli tiga buku seharga lima ribu rupiah, kamu mengalikan harga dengan jumlah. Setelah itu kamu membandingkan totalnya dengan uang yang dibawa. Kamu juga perlu memastikan toko buka. Simbol operator mirip tombol kalkulator dan kata penghubung pada keputusan sehari-hari: cukup uang DAN toko buka. Analogi kalkulator terbatas karena operator program juga dapat bekerja pada teks dan nilai benar/salah.",
      "explanation_technical": "Operator melakukan operasi pada satu atau lebih operand, yaitu nilai yang diolah. Operator aritmetika seperti * menghitung nilai; operator perbandingan seperti >= menghasilkan boolean; operator logika menggabungkan atau membalik kondisi. Dalam TypeScript dan Dart, && adalah AND logis; padanan pada contoh Python adalah and. Pada contoh ini kedua operand AND berupa boolean. Jangan menyamakan = untuk assignment dengan pemeriksaan kesamaan: TypeScript lazim menggunakan === untuk kesamaan ketat, sedangkan Python dan Dart menggunakan ==. Prioritas operator memengaruhi urutan evaluasi; gunakan kurung jika maksud ekspresi sulit dibaca. TypeScript dan Python memiliki detail perilaku operand non-boolean yang dibahas pada materi lanjutan.",
      "code_examples": [
        {
          "language": "typescript",
          "comparison_key": "operators",
          "label": "Uang cukup tetapi toko tutup",
          "code": "const total = 5000 * 3;\nconst cukup = 20000 >= total;\nconst tokoBuka = false;\nconsole.log(total);\nconsole.log(cukup && tokoBuka);",
          "explanation": "* menghasilkan 15000. Perbandingan 20000 >= 15000 bernilai true. AND memerlukan kedua kondisi bernilai true; karena tokoBuka false, hasil akhirnya false.",
          "expected_output": "15000\nfalse"
        },
        {
          "language": "python",
          "comparison_key": "operators",
          "label": "Perhitungan dan kondisi yang sama dalam Python",
          "code": "total = 5000 * 3\ncukup = 20000 >= total\ntoko_buka = False\nprint(total)\nprint(cukup and toko_buka)",
          "explanation": "Python menggunakan kata and. Untuk dua operand boolean pada contoh ini, maknanya sama dengan && pada TypeScript dan Dart. False memakai huruf F besar.",
          "expected_output": "15000\nFalse"
        },
        {
          "language": "dart",
          "comparison_key": "operators",
          "label": "Perhitungan dan kondisi yang sama dalam Dart",
          "code": "void main() {\n  final total = 5000 * 3;\n  final cukup = 20000 >= total;\n  final tokoBuka = false;\n  print(total);\n  print(cukup && tokoBuka);\n}",
          "explanation": "Dart menyimpulkan tipe dari nilai awal pada contoh ini. && menggabungkan dua kondisi boolean. Hasil tetap false karena toko tutup walaupun uang cukup.",
          "expected_output": "15000\nfalse"
        }
      ],
      "prerequisite_ids": ["f-variables-data-types"],
      "related_topic_ids": ["f-programming-logic", "f-variables-data-types"],
      "why_vibecoding_matters": "Pada kode hasil AI, satu simbol dapat mengubah aturan bisnis: > tidak mencakup batas yang sama dengan >=, dan AND berbeda dari OR. Saat membaca syarat diskon atau akses, periksa kasus tepat di batas dan syarat yang bernilai false. Memahami operator membantu kamu menemukan perubahan perilaku meskipun aplikasinya tetap bisa dibuka.",
      "keywords": ["operator", "aritmetika", "perbandingan", "logika", "AND", "assignment"],
      "estimated_minutes": 7,
      "sort_order": 3,
      "is_active": true
    }
  ],
  "quizzes": [
    {
      "id": "q-logic-sequence-01",
      "topic_id": "f-programming-logic",
      "type": "concept",
      "level": "beginner",
      "prompt": "Pola alur apa yang paling jelas ditunjukkan oleh tiga langkah ini?",
      "snippet": "AMBIL gelas\nTUANG air_ke_gelas\nMINUM air",
      "snippet_language": "pseudocode",
      "options": [
        {"id": "sequence", "text": "Urutan langkah (sequence)"},
        {"id": "condition", "text": "Memilih berdasarkan syarat (conditional)"},
        {"id": "loop", "text": "Mengulang langkah (loop)"},
        {"id": "recursion", "text": "Fungsi memanggil dirinya sendiri (recursion)"}
      ],
      "correct_option_id": "sequence",
      "explanation": "Langkah dikerjakan satu per satu dari atas ke bawah. Tidak ada syarat untuk memilih cabang, perintah mengulang, atau fungsi yang memanggil dirinya sendiri. Ini pseudocode: cara menulis alur untuk manusia, bukan sintaks bahasa yang harus dijalankan.",
      "is_active": true
    },
    {
      "id": "q-variables-language-01",
      "topic_id": "f-variables-data-types",
      "type": "language",
      "level": "beginner",
      "prompt": "Dari empat pilihan ini, bahasa mana yang memakai anotasi number seperti pada potongan ini?",
      "snippet": "let jumlah: number = 2;\njumlah = 3;",
      "snippet_language": "typescript",
      "options": [
        {"id": "typescript", "text": "TypeScript"},
        {"id": "javascript", "text": "JavaScript biasa"},
        {"id": "python", "text": "Python"},
        {"id": "dart", "text": "Dart"}
      ],
      "correct_option_id": "typescript",
      "explanation": "Anotasi : number setelah nama variabel dengan let menunjukkan TypeScript di antara pilihan ini. JavaScript biasa tidak memakai anotasi tipe tersebut. Python dan Dart memiliki bentuk deklarasi yang berbeda. let mengizinkan jumlah diberi nilai baru.",
      "is_active": true
    },
    {
      "id": "q-operators-and-01",
      "topic_id": "f-operators",
      "type": "concept",
      "level": "beginner",
      "prompt": "Apa fungsi operator && pada baris kedua?",
      "snippet": "const total = 15000;\nconst diskon = total >= 10000 && true;",
      "snippet_language": "typescript",
      "options": [
        {"id": "and", "text": "Mengharuskan kedua kondisi bernilai true"},
        {"id": "or", "text": "Mengharuskan setidaknya satu kondisi bernilai true"},
        {"id": "multiply", "text": "Mengalikan dua angka"},
        {"id": "assign", "text": "Memberi nilai baru ke total"}
      ],
      "correct_option_id": "and",
      "explanation": "Untuk operand boolean di sini, && adalah AND: kedua kondisi harus true. OR memerlukan setidaknya satu kondisi true, perkalian menggunakan *, dan assignment menggunakan =. Pada contoh, 15000 >= 10000 dan operand kanan sama-sama true, sehingga diskon bernilai true.",
      "is_active": true
    }
  ]
}
```
<!-- END EMBEDDED JSON -->

## 9. Urutan implementasi dan Definition of Done

Kerjakan dalam tahap yang masing-masing dapat diverifikasi. Tahapan tidak mengurangi cakupan rilis awal.

1. **Fondasi yang berjalan:** cek Flutter SDK/proyek, buat target Android/iOS bila belum ada, tambah hanya dependency wajib, implementasikan database/model/parser, seed tiga topik contoh, dan tampilkan Jelajah → Detail. Hasil tahap ini masih paket reference.
2. **Belajar lokal:** tambahkan progress, catatan, Beranda lanjut baca, search/filter, dan penyimpanan yang aman. Verifikasi tutup-buka aplikasi dan kegagalan simpan. Status/notes harus dibaca ulang dari SQLite, bukan data mock yang selalu kembali ke default.
3. **Hubungan dan latihan:** implementasikan peta beserta panah/aksesibilitas, kedua mode kuis, perbandingan sintaks, dan jalur custom berbasis prasyarat. Uji kasus graph/cycle, soal kurang dari lima, opsi teracak, serta jalur kosong/duplikat/reorder tidak valid.
4. **Lengkapi konten:** tulis seluruh 47 fundamental dan 52 pengantar ekosistem per kelompok, hubungkan relasi lintas lapis dengan benar, lengkapi bank soal dan perbandingan. Lakukan pemeriksaan editorial, lalu jadikan paket production. Jangan berhenti setelah tiga artikel pertama atau mengklaim app lengkap ketika artikel lain placeholder.
5. **Verifikasi rilis:** jalankan formatting, analyze, unit/widget test, dan integration test pada perangkat yang tersedia. Bangun APK debug untuk pengujian; jangan mempublikasikan ke store atau menandatangani rilis produksi tanpa permintaan tersendiri.

Pemeriksaan wajib yang proporsional:

- `dart format --output=none --set-exit-if-changed lib test integration_test` setelah formatter dijalankan untuk memperbaiki format.
- `flutter analyze` dan `flutter test` harus lulus.
- Jalankan `flutter test integration_test/offline_persistence_test.dart -d <device_id>` dengan SQLite nyata, dan `flutter build apk --debug` jika toolchain Android tersedia.
- Satu test paket konten memeriksa semua ID, enum, field wajib, jenis kategori, validitas opsi, serta graph tanpa siklus. Fixture negatif kecil harus membuktikan siklus dan referensi putus ditolak.
- Test path: shared prerequisite tidak terduplikasi, prasyarat selalu mendahului dependen, target Paham dilewati saat lanjutkan, serta edit yang melanggar urutan ditolak.
- Test kuis: opsi diacak tetapi correct_option_id tetap dinilai benar; submit berulang tidak menambah skor; hasil tidak mengubah status topik.
- Test simpan: ubah status lalu catatan atau sebaliknya tidak saling menimpa. Tulis gagal tidak menampilkan sukses atau membuang draft.
- Test persistensi/upgrade: seed dua kali tidak menggandakan data; setelah data pengguna dibuat, naikkan content_version dengan revisi artikel dan pastikan catatan/status/jalur utuh; paket rusak tidak mengubah data atau content_meta; artikel yang hilang dari paket diarsipkan dan catatannya tetap dapat diakses.
- Uji manual mode pesawat sejak first launch, restart aplikasi, seluruh titik masuk detail, peta lintas kategori, dua bahasa berdampingan pada ponsel kecil, keyboard catatan, dark mode, skala teks 200%, dan pembaca layar untuk status/jawaban/relasi.
- Inspeksi dependency dan UI: tidak ada code runner, eval, layanan eksekusi remote, atau tombol Run. Kode konten selalu diperlakukan sebagai string.

Gunakan `flutter_test` dan `integration_test` dari SDK; tidak perlu menambah framework pengujian. Jangan menulis test trivial per getter. Tes persistence mobile harus benar-benar dijalankan pada emulator/perangkat; SQLite Python atau mock repository saja tidak membuktikan integrasi sqflite. Jika lingkungan Windows tidak dapat membangun iOS, tandai iOS belum diverifikasi dan tulis cara menjalankannya pada macOS, tanpa mengklaim lulus.

**Selesai berarti:** seluruh F01–F10 bekerja offline, paket production berisi 99 artikel lengkap dengan taksonomi yang benar, data pengguna bertahan saat restart/upgrade, quality checks yang tersedia lulus, dan README menjelaskan setup, cara menambah konten, aturan ID/versioning, perintah verifikasi, serta batas yang memang belum diuji. Laporkan berkas utama yang dibuat, hasil checks yang benar-benar dijalankan, dan hal yang masih terblokir oleh lingkungan. Jangan menandai tahap atau fitur selesai berdasarkan UI dummy.
