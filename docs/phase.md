# CodeAtlas — Fase Implementasi

Dokumen ini membagi implementasi CodeAtlas menjadi delapan fase. Antigravity mengerjakan aplikasi; hasil tiap fase direview berdasarkan kode dan hasil pengujian yang benar-benar tersedia.

Tiga artikel pertama digunakan untuk membuktikan alur aplikasi sebelum seluruh konten dilengkapi. Pembagian fase tidak mengurangi cakupan akhir produk.

Jika proyek atau suatu fitur sudah tersedia, periksa dan lanjutkan implementasinya. Jangan membuat ulang proyek atau menimpa pekerjaan yang sudah ada tanpa memahami kondisinya.

## Cakupan akhir

- Flutter mobile untuk Android dan iOS, berbahasa Indonesia.
- Offline-first, SQLite lokal, dan konten dari JSON yang dibundel sebagai asset.
- 47 artikel fundamental dan 52 artikel pengantar ekosistem: total 99 artikel.
- 76 record Category: 12 kelompok fundamental, 12 kelompok ekosistem, dan 52 domain ekosistem.
- Jelajah, pencarian/filter, detail artikel, progress, catatan, kuis, perbandingan sintaks, roadmap, dan learning path custom.
- Tidak membangun code editor, sandbox, compiler/interpreter, atau layanan untuk menjalankan snippet. Snippet selalu diperlakukan sebagai teks statis.
- Tidak memerlukan backend, login, atau layanan AI pada versi awal.

Catatan: daftar fundamental yang diberikan berisi 47 topik, walaupun judul awal menyebut 46. Seluruh topik dipertahankan.

## Fase 1 — Persiapan proyek dan aplikasi dasar

### Pekerjaan

- Periksa Flutter, Dart, Android SDK, kondisi folder, dan instruksi proyek.
- Buat proyek Flutter Android/iOS jika belum tersedia; lanjutkan proyek yang sudah ada.
- Tambahkan dependency wajib `sqflite` dan `path` dengan versi yang kompatibel dengan SDK terpasang.
- Konfigurasikan asset `assets/content/content.json`.
- Siapkan Material 3, tema terang/gelap mengikuti sistem, serta navigasi Beranda, Jelajah, Peta, Latihan, dan Jalurku.

### Hasil yang diharapkan

Aplikasi dasar dapat dibangun dan navigasi antarlayar tersedia dengan dependency minimal.

### Pemeriksaan

- Jalankan `flutter analyze` dan build APK debug.
- Verifikasi navigasi lewat widget test atau perangkat yang tersedia.
- Catat versi toolchain dan hasil perintah sebenarnya. Build APK belum membuktikan aplikasi berjalan pada perangkat.

## Fase 2 — Model data, SQLite, dan seed tiga artikel

### Pekerjaan

- Implementasikan Category, Topic, Progress, Quiz, serta model pendukung learning path dan contoh kode.
- Buat tabel SQLite, foreign key, repository, dan parser JSON.
- Masukkan Programming Logic, Variables & Data Types, dan Operators sebagai tiga artikel referensi awal.
- Validasi field wajib, tipe data, enum, keunikan ID, referensi, opsi kuis, dan siklus prasyarat.
- Pisahkan `format_version` JSON, `content_version`, dan versi skema database.
- Implementasikan seed atomik dan idempotent, serta pembaruan konten yang mempertahankan progress, catatan, dan jalur pengguna.
- Jika pembaruan konten gagal, rollback dan tetap izinkan penggunaan database lama yang valid.

### Hasil yang diharapkan

Katalog dapat dibaca dari SQLite. Seed berulang tidak menggandakan data. Paket rusak ditolak tanpa merusak data lama.

### Pemeriksaan

- Uji parser dan validasi dengan contoh valid, referensi putus, ID ganda, serta siklus prasyarat.
- Uji seed berulang dan kegagalan pembaruan pada SQLite nyata ketika perangkat tersedia.
- Catat pengujian SQLite pada perangkat secara terpisah jika belum dapat dijalankan. Unit test parser tidak membuktikan integrasi penyimpanan mobile.

## Fase 3 — Alur belajar utama

### Pekerjaan

- Bangun Jelajah dan Detail Topik dengan pengelompokan kedua lapis konten.
- Tampilkan penjelasan awam terlebih dahulu, lalu teknis, contoh kode, manfaat saat vibecoding, prasyarat, dan topik terkait.
- Tambahkan pencarian serta filter lapis, kategori, dan tingkat kesulitan yang digabung dengan AND.
- Implementasikan status Belum/Sedang/Paham dan catatan pribadi per topik.
- Sediakan tombol Simpan, indikator belum disimpan/tersimpan/gagal, penanganan gagal simpan, serta dialog ketika keluar dengan perubahan belum tersimpan.
- Lengkapi Beranda dengan progress per lapis dan lanjutkan bacaan terakhir.
- Simpan perubahan status dan catatan melalui pembaruan kolom terpisah agar tidak saling menimpa.

### Hasil yang diharapkan

Pengguna dapat mencari artikel, membacanya, mengganti status, menulis catatan, dan melanjutkan bacaan.

### Pemeriksaan

- Mengubah status tidak menimpa catatan, dan menyimpan catatan tidak mengubah status.
- Membuka artikel tidak otomatis mengubah status.
- Pencarian mengikuti seluruh filter dan memiliki kondisi kosong yang jelas.
- Gagal simpan tidak menampilkan sukses atau membuang draft.
- Data terbaca kembali setelah aplikasi dibuka ulang ketika pengujian perangkat tersedia.

## Fase 4 — Kuis dan perbandingan sintaks

### Pekerjaan

- Implementasikan mode tebak bahasa dan tebak konsep.
- Pilih maksimal lima soal per sesi tanpa pengulangan; jika soal kurang dari lima, gunakan yang tersedia.
- Acak opsi dengan mempertahankan ID jawaban yang stabil.
- Sembunyikan metadata bahasa sebelum menjawab kuis bahasa, termasuk pada accessibility label.
- Tambahkan feedback, penjelasan jawaban, ringkasan sesi, dan tautan ke materi.
- Implementasikan perbandingan menggunakan pasangan `(topic_id, comparison_key)`.
- Sediakan pilihan 2–3 bahasa, tampilan berdampingan yang dapat digeser, dan alternatif vertikal untuk teks besar.
- Jelaskan perbedaan semantik antarbahasa; hasil contoh ditampilkan sebagai “Hasil yang diharapkan”.

### Hasil yang diharapkan

Contoh tiga artikel dapat digunakan untuk latihan dan perbandingan Dart, TypeScript, dan Python.

### Pemeriksaan

- Pengacakan opsi tidak merusak penilaian jawaban.
- Submit berulang tidak menambah skor.
- Hasil kuis tidak mengubah status topik menjadi Paham.
- Kondisi nol soal dan kurang dari lima soal ditangani.
- Kelompok perbandingan menggambarkan tugas yang sama dan tidak mencampur topik berbeda.
- Seluruh snippet tetap teks statis tanpa fitur eksekusi.

## Fase 5 — Peta hubungan dan roadmap

### Pekerjaan

- Bangun peta memakai `InteractiveViewer`, widget node, dan garis melalui `CustomPainter`.
- Tampilkan panah dari prasyarat menuju topik yang membutuhkan.
- Tambahkan status topik, legenda, dan filter lapis/kategori.
- Saat node dipilih, tampilkan prasyarat langsung dan topik yang langsung membutuhkannya.
- Sediakan perpindahan fokus untuk hubungan lintas kategori.
- Tambahkan alternatif daftar relasi yang dapat digunakan pembaca layar.
- Gunakan prasyarat untuk urutan topologis; relasi terkait tetap menjadi saran editorial.

### Hasil yang diharapkan

Pengguna dapat memahami hubungan topik, menggeser atau memperbesar peta, dan membuka artikel dari node.

### Pemeriksaan

- Arah panah benar dan posisi node mengikuti hubungan prasyarat.
- Relasi terkait tidak diperlakukan sebagai prasyarat.
- Node memiliki label yang dapat diakses; status tidak dibedakan melalui warna saja.
- Hubungan lintas kategori tetap dapat ditemukan.
- Artikel boleh dibuka meskipun prasyarat belum Paham.

## Fase 6 — Learning path berdasarkan tujuan

### Pekerjaan

- Tambahkan preset dasar umum, Flutter, web, backend, dan data, serta jalur custom.
- Implementasikan penambahan prasyarat transitif, penghapusan duplikasi, dan pengurutan topologis yang stabil.
- Izinkan pengguna memberi nama, menambah atau menghapus topik, dan mengubah urutan selama tidak melanggar prasyarat.
- Simpan beberapa jalur secara lokal dan tampilkan progress dari status topik yang sama dengan atlas.
- Tombol Lanjutkan menuju topik pertama yang belum Paham; tampilkan selesai jika seluruh topik aktif dalam jalur sudah Paham.
- Tambahkan pilihan melihat jalur pada roadmap.
- Jika pembaruan konten mengubah prasyarat, tampilkan kebutuhan meninjau jalur tanpa mengubah jalur tersimpan secara diam-diam.

### Hasil yang diharapkan

Pengguna dapat membuat, mengedit, menyimpan, dan melanjutkan jalur belajar sesuai tujuan.

### Pemeriksaan

- Prasyarat yang dipakai bersama tidak muncul berulang.
- Prasyarat berada sebelum topik yang membutuhkannya.
- Tambah/hapus/reorder yang tidak valid ditolak dengan penjelasan.
- Jalur kosong tidak dapat disimpan.
- Menghapus jalur tidak menghapus progress atau catatan.
- Jalur tersimpan tetap tersedia setelah restart ketika pengujian perangkat tersedia.

## Fase 7 — Konten lengkap dan pemeriksaan editorial

### Pekerjaan

- Lengkapi seluruh 47 artikel fundamental dan 52 artikel pengantar ekosistem.
- Lengkapi 76 record Category sesuai model pengelompokan.
- Pastikan setiap artikel memiliki analogi awam, penjelasan teknis, contoh kode, prasyarat, topik terkait, dan manfaat konkret saat vibecoding.
- Bedakan sudut pandang fundamental dan ekosistem pada artikel yang namanya mirip.
- Lengkapi minimal 30 kuis: 10 tebak bahasa dan 20 tebak konsep, mencakup sedikitnya 10 topik fundamental dan 5 topik ekosistem.
- Lengkapi minimal sembilan kelompok perbandingan: variabel/tipe, operator, conditional, loop, function, list, class/object, error handling, dan async/await. Masing-masing tersedia dalam Dart, TypeScript, dan Python.
- Periksa kualitas materi sebelum menetapkan dataset sebagai `production`.

### Hasil yang diharapkan

Paket produksi berisi seluruh materi lengkap tanpa placeholder, TODO, atau penjelasan generik yang disalin ke semua topik.

### Pemeriksaan

- Validasi identitas seluruh artikel, bukan jumlahnya saja.
- Periksa kelengkapan field, kategori, referensi, dan graph prasyarat.
- Review akurasi analogi, penjelasan teknis, snippet, hasil yang diharapkan, dan jawaban kuis.
- Pastikan contoh perbandingan setara pada tugas yang dibahas dan menjelaskan perbedaan semantik.
- Periksa keterbacaan roadmap dan kecepatan pencarian pada dataset penuh.
- Jangan menganggap validasi JSON sebagai bukti kualitas pedagogis.

## Fase 8 — Verifikasi menyeluruh dan APK pengujian

### Pekerjaan

- Jalankan formatter, `flutter analyze`, unit/widget test, dan build APK.
- Uji seluruh alur pengguna beserta kondisi kosong, error, dan gagal simpan.
- Jalankan pengujian persistensi: seed berulang, restart, upgrade konten, penolakan paket rusak, dan akses catatan pada artikel yang diarsipkan.
- Pada perangkat, periksa mode pesawat sejak pembukaan pertama, layar kecil, keyboard catatan, dark mode, pembesaran teks 200%, dan pembaca layar.
- Gunakan widget test untuk tema, pembesaran teks, dan bagian semantics yang dapat diperiksa tanpa perangkat.
- Siapkan laporan hasil dan lokasi APK yang benar-benar berhasil dibangun.

### Perintah verifikasi

```sh
dart format lib test integration_test
dart format --output=none --set-exit-if-changed lib test integration_test
flutter analyze
flutter test
flutter test integration_test/offline_persistence_test.dart -d <device_id>
flutter build apk --debug
```

Ganti `<device_id>` dengan ID perangkat/emulator yang tersedia. Jangan mengklaim integration test telah dijalankan jika perangkat tidak tersedia.

### Hasil yang diharapkan

APK untuk pengujian dan laporan yang menyebut pemeriksaan lulus, gagal, serta belum dijalankan.

### Pemeriksaan akhir

- Seluruh fitur bekerja dengan data nyata, bukan UI dummy.
- Kedua lapis konten lengkap dan dapat dibuka offline.
- Progress, catatan, dan jalur tidak hilang saat restart atau upgrade konten.
- Tidak ada fitur menjalankan snippet atau mengirimnya ke layanan eksekusi.
- Jika perangkat atau lingkungan iOS belum tersedia, pemeriksaan tersebut tetap ditandai **belum terverifikasi**.

## Format laporan setiap fase

```text
Fase:
Yang sudah diimplementasikan:
File utama yang berubah:
Pengujian yang dijalankan dan hasilnya:
Bagian yang belum terverifikasi:
Masalah yang masih terbuka:
```

Laporkan implementasi dan verifikasi secara terpisah. Keterbatasan perangkat tidak menghalangi pekerjaan lain yang dapat dilanjutkan, tetapi pemeriksaan yang belum dijalankan tetap harus disebutkan.
