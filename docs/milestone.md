# Milestone CodeAtlas

Terakhir diperbarui: 15 September 2026.

Dokumen ini mencatat perkembangan CodeAtlas dan rencana berikutnya. Bagian yang berstatus selesai didasarkan pada laporan implementasi dalam percakapan, kecuali disebut telah direview langsung oleh pengguna. Dokumen ini bukan hasil pengujian ulang kode atau verifikasi rilis secara langsung.

## Status dan aturan penggunaan

- **Selesai — laporan:** implementasi atau pemeriksaan dilaporkan selesai oleh Antigravity.
- **Diterima pengguna:** pengguna telah meninjau dan menerima hasilnya.
- **Perlu verifikasi:** bukti pengujian atau penggunaan nyata masih belum lengkap.
- **Direncanakan:** arah pekerjaan telah dibahas; implementasinya belum dilaporkan selesai.
- **Usulan:** kandidat pengembangan, belum menjadi komitmen implementasi.
- **Opsional:** dikerjakan hanya jika kebutuhan pengguna mendukungnya.

Checklist `[x]` berarti pekerjaan dilaporkan selesai; jenis buktinya tetap mengikuti keterangan milestone. Jangan menandai pekerjaan selesai hanya karena skrip pengujiannya telah dibuat.

## Batas produk yang dipertahankan

- Aplikasi mobile Flutter, offline-first, dengan SQLite lokal dan konten JSON terstruktur.
- Tujuan utama: memahami konsep, membaca kode, dan memeriksa hasil vibecoding.
- Tidak menyediakan editor kode yang menjalankan program, compiler, interpreter, sandbox, atau code runner.
- Materi dimulai dari bahasa awam sebelum istilah teknis.
- Membaca artikel atau menjawab kuis tidak otomatis mengubah status menjadi Paham.
- Catatan disimpan manual; draf dan data pengguna harus terlindungi.
- Materi yang telah diterima tidak ditulis ulang tanpa temuan atau kebutuhan yang jelas.
- Rencana materi terinspirasi dari cakupan Mimo, tetapi penjelasan, contoh, soal, ilustrasi, dan studi kasus CodeAtlas harus dibuat sendiri.
- Backend, akun, sinkronisasi, dan monetisasi bukan syarat untuk menggunakan versi offline.

## Ringkasan milestone

| ID  | Milestone                                 | Status                                               |
| --- | ----------------------------------------- | ---------------------------------------------------- |
| M1  | Fondasi aplikasi dan paket konten         | Selesai — laporan                                    |
| M2  | Fitur pembelajaran inti                   | Selesai — laporan                                    |
| M3  | Pendalaman materi dan keterbacaan         | Materi diterima pengguna; UI selesai menurut laporan |
| M4  | Identitas visual dan distribusi v1.0.2    | Selesai — laporan                                    |
| M5  | Validasi perangkat dan pemeliharaan rilis | Perlu verifikasi                                     |
| M6  | Redesign UI/UX (sebagian)                 | Sebagian diterima pengguna; layar lain ditunda       |
| M7  | Website pengenalan CodeAtlas              | Usulan                                               |
| M8  | Jalur pendalaman dan studi kasus          | Usulan; cakupan diperbarui dari referensi Mimo       |
| M9  | Dukungan desktop                          | Opsional                                             |
| M10 | Validasi pengguna dan pendapatan          | Eksplorasi                                           |

## M1 — Fondasi aplikasi dan paket konten

**Tujuan:** menyediakan ensiklopedia yang dapat digunakan tanpa backend.

- [x] Flutter, Material 3, dan SQLite lokal.
- [x] Paket JSON dengan 47 artikel fundamental dan 52 pengantar ekosistem: 99 artikel total.
- [x] Taksonomi 76 kategori: 12 grup fundamental, 12 grup ekosistem, dan 52 domain.
- [x] Model kategori, topik, contoh kode, progres, kuis, dan jalur belajar.
- [x] Seed tervalidasi, penolakan downgrade konten, skip versi sama, dan upgrade transaksional.
- [x] Fallback ke konten lama yang valid saat pembaruan gagal.
- [x] Pengarsipan topik untuk mempertahankan hubungan dengan data pengguna.

**Bukti:** laporan implementasi dan pengujian otomatis. Verifikasi runtime Android dicatat terpisah pada M5.

## M2 — Fitur pembelajaran inti

- [x] Beranda, Jelajah, Peta, Latihan, dan Jalurku.
- [x] Search serta filter lapis, kategori, dan tingkat kesulitan.
- [x] Progres Belum / Sedang / Paham dan catatan pribadi per topik.
- [x] Perlindungan pengetikan selama proses simpan dan kegagalan penyimpanan catatan.
- [x] Peta bertahap: kelompok → topik → panel fokus, termasuk lompatan lintas kelompok.
- [x] Relasi prasyarat tanpa siklus dan relasi topik terkait.
- [x] 36 kuis: 14 tebak bahasa dan 22 tebak konsep.
- [x] 10 kelompok perbandingan sintaks Dart, TypeScript, dan Python.
- [x] Jalur kustom dan lima preset: Dasar, Flutter, Web, Backend, dan Data.

**Batas penyelesaian:** ketersediaan preset tidak berarti sudah ada kursus mendalam dan studi kasus lengkap untuk setiap tujuan. Pendalaman dicatat pada M8.

## M3 — Pendalaman materi dan keterbacaan

- [x] Delapan bagian pedagogis: analogi, konteks masalah, mekanisme, contoh dan penelusuran, miskonsepsi, penggunaan, relevansi vibecoding, serta refleksi.
- [x] Konten versi 5 dan skema database versi 2, berdasarkan laporan terakhir.
- [x] Penyederhanaan artikel Programming Logic dan ringkasan topik.
- [x] Akses tunggal Daftar Isi melalui AppBar; FAB yang menutupi artikel dihapus.
- [x] Perbandingan sintaks memakai pemilih konsep tunggal, label Indonesia, dan kartu vertikal.
- [x] Pengguna menyatakan seluruh penjelasan telah diperiksa dan lengkap.

**Bukti:** penerimaan materi oleh pengguna dan laporan implementasi UI. Tidak perlu mengulang audit seluruh materi tanpa temuan baru.

## M4 — Identitas visual dan distribusi

- [x] Eksplorasi identitas melalui MCP Stitch, menurut laporan Antigravity.
- [x] Logo, ikon launcher adaptive, serta varian monochrome.
- [x] Penyederhanaan logo untuk ukuran kecil dan penggunaan `Image.asset`.
- [x] GitHub Actions untuk pemeriksaan, build APK release, dan publikasi.
- [x] Signing persisten dan pemeriksaan fingerprint sebelum publikasi.
- [x] Pengujian pemulihan backup keystore dilaporkan berhasil.
- [x] Rilis v1.0.2, versionCode 3, dengan applicationId `com.codeatlas.app`.

**Riwayat penting:** v1.0.0 dan v1.0.1 menggunakan `com.codeatlas.codeatlas` dengan sertifikat berbeda. v1.0.2 memakai paket terpisah agar dapat dipasang berdampingan. Catatan dan progres lama tidak otomatis dipindahkan. Jangan menghapus aplikasi lama sebelum pengguna mengamankan data yang dibutuhkan.

**Tautan bukti yang dilaporkan:**

- [Release v1.0.2](https://github.com/rexkarbu/codeatlas/releases/tag/v1.0.2)
- [Workflow rilis v1.0.2](https://github.com/rexkarbu/codeatlas/actions/runs/34862429628)

Pembaruan berikutnya mempertahankan applicationId dan signing key serta menaikkan versionCode. Jangan menyimpan kredensial atau isi keystore dalam dokumen ini.

## M5 — Validasi perangkat dan pemeliharaan rilis

- [x] Laporan terakhir menyebut 55 tes otomatis lulus dan analisis statis bersih.
- [x] Instalasi APK v1.0.2 dari GitHub pada perangkat pengguna dan pemeriksaan kedua aplikasi berdampingan.
- [x] Verifikasi catatan/progres setelah aplikasi ditutup dan dibuka kembali.
- [x] Verifikasi membaca, pencarian, kuis, dan jalur belajar dalam mode pesawat.
- [x] Verifikasi keyboard, tombol simpan, navigasi kembali, screen reader, dan skala teks 200% pada perangkat.
- [x] Jalankan integration test SQLite pada Android; pisahkan dari unit/widget test dan pengujian SQLite desktop.
- [x] Uji pembaruan dari v1.0.2 ke rilis berikutnya tanpa uninstall ketika kandidat rilis tersedia.
- [x] Simpan backup signing terenkripsi beserta akses pemulihannya di lokasi terpisah dari komputer utama.

**Kriteria selesai:** hasil aktual perangkat dicatat dengan versi APK, perangkat, skenario, dan hasilnya. Tidak menyimpulkan keberhasilan persistensi hanya dari screenshot atau build yang sukses.

Fungsi ekspor/impor data telah dilaporkan ditambahkan pada repository, tetapi antarmuka pengguna belum tersedia. Jangan mengiklankannya sebagai fitur pengguna atau solusi otomatis untuk APK lama.

## M6 — Redesign UI/UX (sebagian)

**Tujuan:** memberi karakter visual dan alur belajar yang lebih menarik tanpa mengurangi keterbacaan.

**Status:** sebagian diterima pengguna; perluasan redesign layar lainnya ditunda.

**Hasil yang telah diterima pengguna:**
- [x] Tema aplikasi (`AtlasTheme`) terpadu untuk mode terang dan gelap (palet warna, tipografi, bentuk kartu/dialog, bottom sheet, dan snackbar).
- [x] Redesign Beranda: kartu preset alur belajar (`Umum / Dasar dari Nol`, `Flutter & Mobile`, `Web Frontend`, `Backend & Server`, `Data & Algoritma`), ringkasan statistik, maskot Koda, dan navigasi langsung ke Detail Jalur.
- [x] Layar Detail Jalur (`PathDetailScreen`): daftar materi bertahap, resolusi prasyarat dinamis, waktu baca konsisten, membaca materi langsung di memori sebelum pembuatan jalur, pencegahan ketukan ganda, serta mempertahankan urutan kustom pengguna.
- [x] Redesign Artikel Topik (`TopicScreen`): banner jalur pembelajaran, navigasi materi bertahap via `pushReplacement`, dialog perlindungan draf catatan (`_onWillPop`), selektor bahasa kode terpadu, dan status pemahaman di bilah bawah yang aman dari overflow (skala teks 200% dan layar sempit 360dp).
- [x] Alur Beranda → Detail Jalur → Artikel telah diuji secara manual pada perangkat dan dilaporkan aman oleh pengguna.

**Cakupan yang ditunda:**
- Redesign layar lainnya (Jelajah, Peta, Latihan, Kuis, Perbandingan, dan editor Jalurku) ditunda atas keputusan pengguna agar stabilitas fitur saat ini terjaga.
- Seluruh milestone M5 dan M6 tidak ditandai selesai penuh; pengujian yang belum dilakukan tidak diklaim selesai.

**Kriteria selesai:** desain diterima pengguna, semua navigasi utama berfungsi, kontrol tidak menutupi konten, dan perilaku penyimpanan tetap terlindungi.

## M7 — Website pengenalan CodeAtlas

**Status:** usulan. Folder `website/` dalam repo yang sama menjadi opsi awal; tidak perlu repo atau backend baru untuk landing page.

- [ ] Hero dengan manfaat utama, screenshot, fitur, contoh pelajaran, dan tautan unduh/GitHub.
- [ ] Tampilan responsif serta aset orisinal yang konsisten dengan aplikasi.
- [ ] Informasi offline, versi rilis, dan transisi paket yang jelas.

**Kriteria selesai:** website dapat diakses, nyaman di ponsel, dan tautan unduh mengarah ke APK rilis yang benar.

## M8 — Jalur pendalaman dan studi kasus

**Tujuan:** menghubungkan ensiklopedia yang sudah tersedia menjadi pembelajaran berbasis tujuan. Materi Mimo menjadi referensi cakupan; bukan sumber yang disalin dan bukan janji kesetaraan seluruh kurikulum.

### Prioritas A — Penguatan kebutuhan utama CodeAtlas

| Kandidat                      | Cakupan tambahan                                                                       | Bentuk hasil                                                                    |
| ----------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Membaca dan memeriksa kode AI | Asumsi, input/output, perubahan kode, efek samping, dan pertanyaan verifikasi untuk AI | Studi kasus membaca kode dan pembahasan perubahan                               |
| Debugging & Testing           | Pesan error, penelusuran nilai, penyebab masalah, batas pembuktian sebuah tes          | Tebak hasil, temukan masalah, dan penjelasan pengujian                          |
| Perjalanan satu fitur         | UI → request → validasi → penyimpanan → respons → tampilan                             | Penelusuran fitur pencarian, login, atau catatan; bertahap dari kasus sederhana |

### Prioritas B — Materi dan jalur yang relevan dari Mimo

Semua baris berikut **usulan**, belum diimplementasikan sebagai kursus pendalaman CodeAtlas. Topik pengantar yang sudah ada tetap digunakan sebagai prasyarat.

| Materi / jalur         | Cakupan yang dapat ditambahkan                                                   | Penyesuaian untuk CodeAtlas                                                              |
| ---------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| HTML                   | Struktur dokumen, elemen, tautan, form, semantic HTML, dan aksesibilitas         | Mengenali hubungan markup dengan tampilan dan fungsi elemen                              |
| CSS                    | Selector, cascade, box model, layout responsif, Flexbox, dan Grid                | Membaca aturan styling dan membandingkan cuplikan dengan ilustrasi hasil statis          |
| JavaScript             | Nilai, percabangan, loop, array, fungsi, objek, ES6, DOM/event, class, dan async | Penelusuran nilai dan interaksi; gunakan ulang fundamental yang sudah tersedia           |
| TypeScript             | Anotasi tipe, union, narrowing, interface/type, dan hubungan dengan JavaScript   | Membaca kontrak data dan memahami pesan kesalahan tipe                                   |
| React                  | Komponen, JSX, props, state, event, rendering list, dan pengambilan data         | Menelusuri bagaimana perubahan data memengaruhi UI melalui contoh terpandu               |
| Node.js & Express      | Peran runtime server, route, request/response, middleware, validasi, dan error   | Menelusuri endpoint API tanpa menyediakan server/code runner dalam aplikasi              |
| SQL & database praktis | SELECT, filter, agregasi, JOIN, perubahan data, relasi, dan integrasi dengan API | Tabel contoh, query statis, hasil yang diharapkan, dan alasan hasil tersebut             |
| Python                 | Dasar bahasa, flow control, list, fungsi, dictionary/tuple/set, OOP, dan API     | Membaca skrip, menelusuri data, serta studi kasus otomatisasi sederhana                  |
| Frontend               | HTML → CSS → JavaScript → TypeScript sesuai kebutuhan → React                    | Jalur penghubung dan satu studi kasus UI web; bukan duplikasi semua artikel              |
| Backend                | JavaScript → Node.js → Express → SQL → integrasi API                             | Studi kasus API beserta validasi, akses data, dan penanganan error                       |
| Fullstack              | Menghubungkan frontend, API backend, dan database                                | Satu aplikasi contoh yang sama dari antarmuka sampai penyimpanan dan kembali ke pengguna |
| Python Developer       | Menggabungkan modul Python menjadi jalur tujuan                                  | Studi kasus pengolahan data/file dan konsumsi API yang dijelaskan bertahap               |

Detail cakupan adalah rancangan adaptasi CodeAtlas; tidak menyatakan setiap butir identik dengan silabus Mimo.

### Prioritas C — Pendalaman lanjutan dan opsi ekosistem

| Kandidat                        | Cakupan                                                                               | Status                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Swift                           | Sintaks dasar, optional, koleksi, fungsi, struct/class, dan pengantar ekosistem Apple | Opsional; Swift tercantum di katalog Mimo, tetapi bukan prioritas sebelum jalur utama matang |
| Flutter dari konsep ke aplikasi | Widget, state, navigasi, API, penyimpanan lokal                                       | Pengembangan khas CodeAtlas; bukan materi Mimo yang telah dikonfirmasi                       |
| Keamanan aplikasi               | Pemeriksaan input, hak akses, secret, dan penyimpanan data                            | Usulan, gunakan ulang materi keamanan yang tersedia                                          |
| Deployment & DevOps             | Build, environment, CI/CD, signing, rilis, dan rollback                               | Usulan, terhubung dengan contoh kasus aplikasi                                               |
| Data & AI                       | Alur pengolahan data dan integrasi layanan/model AI                                   | Opsional; jangan mengklaim pembahasan mendalam ML hanya dari pengantar Python                |
| Desktop & CLI                   | Struktur aplikasi komputer dan skrip terminal                                         | Opsional, sesuai kebutuhan pengguna                                                          |

Katalog Mimo yang diperiksa menandai **AI-driven Development** sebagai **Coming soon**. Ini tidak dicatat sebagai kursus Mimo yang sudah tersedia penuh. Jalur Membaca Kode AI adalah kebutuhan CodeAtlas yang dapat dikembangkan sendiri.

### Format belajar yang sesuai

- Prediksi hasil kode, lalu buka penelusuran langkah.
- Kenali masalah pada cuplikan kode beserta penjelasannya.
- Bandingkan kode sebelum/sesudah perubahan dan alasan perubahan.
- Ikuti satu fitur lintas beberapa berkas/lapisan aplikasi.
- Buka definisi istilah tanpa kehilangan konteks artikel, jika kebutuhan ini dikonfirmasi.
- Pertahankan contoh dan hasil sebagai konten statis; tidak menambahkan eksekusi kode.

### Urutan pengerjaan dan kriteria selesai

- [ ] Inventarisasi materi yang sudah tersedia; pisahkan pengantar, pendalaman yang kurang, dan studi kasus baru.
- [ ] Pilih satu modul pilot sesuai kebutuhan pengguna; prioritas awal Membaca Kode AI atau Debugging.
- [ ] Susun tujuan, prasyarat, dan contoh orisinal; jangan menambah seluruh kandidat sekaligus.
- [ ] Review pilot dengan pengguna sebelum memperluas format ke modul lain.
- [ ] Kembangkan fondasi web, lalu jalur Frontend/Backend; satukan melalui studi kasus Fullstack.
- [ ] Kembangkan jalur Python dan SQL menurut permintaan pengguna.
- [ ] Pastikan contoh, hasil, refleksi, relasi, dan istilah konsisten; verifikasi klaim teknis dengan sumber resmi.
- [ ] Naikkan content_version dari nilai aktual ketika paket konten berubah, dengan ID lama tetap stabil.
- [ ] Uji pembaruan tanpa kehilangan catatan, progres, atau jalur pengguna.

**Kriteria selesai per modul:** tujuan dapat dijelaskan pengguna melalui contoh yang disediakan, seluruh bagian dapat dibaca offline, dan materi telah direview. Jumlah topik baru ditetapkan setelah inventarisasi; tidak memaksakan target jumlah artikel.

**Referensi cakupan, diperiksa 15 September 2026:**

- [Katalog kursus Mimo](https://mimo.org/courses): HTML, CSS, JavaScript, Python, SQL, Swift, TypeScript, React; empat career path; status AI-driven Development.
- [Daftar bahasa dan jalur Mimo](https://support.mimo.org/hc/en-us/articles/4407444187794-Which-programming-languages-can-I-learn-with-Mimo): juga mencantumkan Node.js dan Express.js.
- [Kurikulum Fullstack Mimo](https://mimo.org/courses/full-stack-development): struktur web, layout, JavaScript, React, SQL, dan Express.
- [Jalur Python Mimo](https://mimo.org/courses/python-development).

## M9 — Ekspansi desktop

- [ ] Validasi kebutuhan Linux, Windows, atau macOS sebelum memilih platform pertama.
- [ ] Periksa dukungan SQLite desktop, layout layar besar, mouse, keyboard, dan distribusi.
- [ ] Uji build serta penyimpanan pada OS target.

**Batas:** data tetap lokal per perangkat. Desktop tidak otomatis menambahkan sinkronisasi atau backend.

## M10 — Validasi pengguna dan pendapatan

- [ ] Uji awal dengan 15–30 pengguna sasaran selama sekitar dua minggu; angka ini rancangan eksperimen, bukan syarat produk.
- [ ] Catat pemahaman, kebiasaan kembali belajar, hambatan, dan permintaan materi.
- [ ] Uji minat pada satu paket pendalaman atau workshop sebelum membangun pembayaran.
- [ ] Pilih model pendapatan jika ada bukti permintaan: paket sekali beli, sponsor, donasi, atau layanan terkait.
- [ ] Periksa kebijakan distribusi/pembayaran yang berlaku saat implementasi.

**Belum diputuskan:** harga, paywall, langganan, iklan, akun, dan backend. Aplikasi gratis tanpa sumber pendapatan tidak otomatis dibayar berdasarkan unduhan.

## Utang teknis opsional dari audit Ponytail

Audit ini terkait kompleksitas, bukan kekurangan materi dan bukan syarat wajib rilis. Status berikut belum dilaporkan selesai:

- [ ] Hilangkan duplikasi field kurikulum pada Python perantara; gabungkan di memori saat menghasilkan JSON dengan seluruh data unik tetap utuh.
- [ ] Hapus skrip pembaruan ringkasan sekali pakai jika tidak diperlukan lagi.
- [ ] Satukan isi kartu perbandingan vertikal/horizontal dalam fungsi lokal yang sama.
- [ ] Ganti konfigurasi global codec model dengan `dart:convert` langsung.
- [ ] Hapus `cupertino_icons` jika tetap tidak dipakai.

Penyederhanaan CustomPainter logo menjadi `Image.asset` sudah dilaporkan selesai pada M4. Estimasi pengurangan baris dari audit tidak dianggap hasil aktual sebelum perubahan diukur.

## Prioritas berikutnya

1. Lengkapi bukti penggunaan APK release di perangkat dan backup signing di luar komputer utama.
2. Uji pengalaman belajar dengan pengguna; gunakan hasilnya untuk memilih satu modul pendalaman.
3. Bangun website pengenalan bila diperlukan untuk distribusi.
4. Kembangkan jalur pada M8 bertahap; perluasan redesign UI layar lain, desktop, dan monetisasi mengikuti kebutuhan yang terbukti.

## Riwayat dokumen

- **15 September 2026 (Pembaruan UI/UX):** Beranda, Artikel, tema aplikasi, serta alur Beranda → Detail Jalur → Artikel diterima pengguna setelah pengujian manual pada perangkat dilaporkan aman. Redesign layar lainnya ditunda atas keputusan pengguna. M5 dan M6 tetap berstatus sebagian / perlu verifikasi lanjutan.
- **15 September 2026:** dokumen awal dibuat dari milestone yang telah direncanakan; menambahkan cakupan adaptasi Mimo, status rilis v1.0.2, penerimaan materi pengguna, serta pemisahan pekerjaan selesai, belum terverifikasi, dan usulan masa depan.
