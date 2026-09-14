"""Enrichment Part 4A: I/O, Systems, Modules, Tools, and Networking (11 Topics).
"""

CURRICULUM_PART4A = {
    "f-input-output": {
        "summary": "Mekanisme transfer aliran data antara program komputer dengan perangkat eksternal dunia luar.",
        "explanation_simple": (
            "Bayangkan pintu gerbang dermaga pelabuhan peti kemas. Kapal kargo dari samudera lepas (input) membongkar muatan "
            "kontainer barang ke area dermaga. Pekerja dermaga menyortir dan mencatat barang tersebut di gudang (pemrosesan program), "
            "lalu memuat barang-barang yang sudah dipaketkan ke dalam truk pengantar untuk dikirim ke konsumen di darat (output).\n\n"
            "Input/Output (I/O) adalah jembatan komunikasi program dengan dunia nyata: membaca ketikan keyboard, menampilkan piksel di layar, "
            "atau bertukar data melalui kabel serat optik internet. "
            "Batas analogi dermaga: kapal fisik membutuhkan waktu berhari-hari untuk bersandar, sedangkan I/O komputer modern "
            "menggunakan ruang penyangga memori (Buffer) berkecepatan tinggi agar CPU tidak perlu menunggu setiap tetes bit data satu per satu."
        ),
        "problem_context": (
            "Prosesor komputer mampu beroperasi dalam hitungan nanodetik, sedangkan perangkat I/O fisik (seperti harddisk mekanik atau kartu jaringan) "
            "bekerja dalam hitungan milidetik — satu juta kali lebih lambat dari CPU! "
            "Jika setiap kali program membaca 1 byte dari keyboard CPU harus berhenti total menunggu jari manusia menekan tuts, "
            "seluruh daya komputasi komputer modern akan terbuang sia-sia dalam keadaan menganggur (idle). "
            "Arsitektur I/O modern (Interrupts, DMA, Buffering, Streams) diciptakan untuk membebaskan CPU dari belenggu kelambatan fisik ini."
        ),
        "explanation_technical": (
            "Operasi I/O dikelola melalui abstraksi File Descriptors di tingkat kernel sistem operasi (standar POSIX: 0 untuk stdin, 1 untuk stdout, 2 untuk stderr). "
            "Dua model eksekusi I/O: "
            "1. Synchronous / Blocking I/O: Thread pemanggil ditangguhkan oleh kernel hingga operasi transfer byte tuntas. "
            "2. Asynchronous / Non-blocking I/O: Panggilan I/O langsung kembali seketika dengan status EWOULDBLOCK/EAGAIN; "
            "sistem operasi memberitahukan penyelesaian data melalui mekanisme multiplexing I/O tingkat tinggi seperti epoll (Linux), kqueue (macOS/BSD), atau IOCP (Windows).\n\n"
            "Konsep Stream dan Buffer sangat penting: Stream mengalirkan data berukuran besar secara bertahap (chunk by chunk) "
            "tanpa perlu memuat seluruh file gigabyte ke dalam RAM sekaligus, memanfaatkan prinsip Backpressure untuk mengendalikan "
            "kecepatan aliran data agar penerima tidak tenggelam kehabisan memori."
        ),
        "misconceptions": [
            {
                "misconception": "Membaca file 1 GB dengan fs.readFileSync() di Node.js atau File.readAsStringSync() di Dart tidak masalah jika RAM komputer besar.",
                "explanation": "Membaca file besar secara sinkron membekukan total event loop aplikasi dan memakan kuota heap memory secara masif; gunakan file stream (readStream) agar diproses per chunk kecil.",
                "spot_in_code": "const data = fs.readFileSync('video_besar.mp4') di dalam server web produksi."
            },
            {
                "misconception": "Operasi print() atau console.log() tidak membebani performa aplikasi.",
                "explanation": "Pencetakan ke terminal melibatkan operasi I/O write ke stdout yang sering kali bersifat blocking atau memicu overhead pemformatan string yang berat jika dipanggil ribuan kali di dalam loop ketat.",
                "spot_in_code": "Memanggil print() di setiap frame loop animasi 120 FPS."
            }
        ],
        "when_to_use": (
            "Gunakan I/O Streams saat mengunggah, mengunduh, atau memproses file berukuran besar (gambar, video, dataset CSV). "
            "Gunakan buffered I/O untuk mengurangi jumlah system calls ke kernel. "
            "Selalu gunakan non-blocking async I/O pada aplikasi server web berkonkurensi tinggi."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis fungsi pembacaan file dengan memuat seluruh isi file sekaligus ke satu variabel string (readAll). "
            "Kode ini langsung mengalami Out of Memory crash saat pengguna mengunggah file sungguhan di lingkungan produksi. "
            "Saat vibecoding, mintalah AI: 'Gunakan stream chunking dengan backpressure untuk membaca dan memproses data I/O ini "
            "agar konsumsi RAM stabil dan tidak membeku saat menangani file besar.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa konsep Backpressure sangat penting dalam pemrosesan data I/O Stream?",
                "answer": "Backpressure memberi tahu pengirim stream untuk melambatkan aliran data ketika buffer penerima penuh, mencegah memori penerima meledak kehabisan RAM."
            },
            {
                "question": "Apa peran sistem operasi DMA (Direct Memory Access) dalam transfer I/O modern?",
                "answer": "DMA memungkinkan perangkat keras I/O (seperti kartu jaringan atau disk SSD) mentransfer data langsung ke memori RAM utama tanpa melibatkan intervensi langsung dari instruksi CPU."
            }
        ]
    },

    "f-file-system": {
        "summary": "Struktur penyimpanan permanen, hierarki direktori, metadata, dan izin akses file pada disk.",
        "explanation_simple": (
            "Bayangkan lemari arsip baja di kantor kearsipan nasional. Setiap laci memiliki map berkas gantung, "
            "dan di dalam map terdapat formulir dokumen resmi. Di bagian depan setiap dokumen terdapat stiker label: "
            "nama dokumen, ukuran ketebalan lembar, tanggal pembuatan, serta stempel izin rahasia 'Hanya Boleh Dibaca Pimpinan'.\n\n"
            "Sistem Berkas (File System) adalah cara sistem operasi menata dan melacak data yang disimpan di media permanen (SSD atau Flash Drive) "
            "agar data tidak hilang saat komputer dimatikan. "
            "Batas analogi lemari arsip: lemari fisik hanya bisa dibuka satu orang pada satu laci, sedangkan sistem berkas komputer "
            "mendukung akses ratusan proses secara konkuren dengan sistem penguncian file (file locking) dan jurnal pemulihan otomatis (Journaling)."
        ),
        "problem_context": (
            "Media penyimpanan fisik (seperti chip flash NAND pada SSD) hanya memahami blok byte mentah bernomor sektor 0, 1, 2... "
            "Jika programmer harus mengingat di sektor byte nomor berapa file 'laporan.pdf' disimpan, "
            "dan bagaimana menyatukan kembali file tersebut jika pecahannya tersebar di 5 sektor terpisah karena fragmentasi, "
            "pembuatan software akan menjadi mimpi buruk. File System diciptakan untuk menyediakan abstraksi direktori hierarki "
            "yang manusiawi dan menjamin keutuhan data terhadap pemadaman listrik mendadak."
        ),
        "explanation_technical": (
            "Sistem berkas modern (EXT4 di Linux, NTFS di Windows, APFS di macOS) mengelola dua lapisan utama: "
            "1. Metadata Layer (Inode pada sistem UNIX-like): menyimpan informasi izin akses (permissions rwxrwxrwx), "
            "kepemilikan (UID/GID), ukuran file, timestamp (ctime, atime, mtime), dan daftar pointer ke blok data disk. "
            "Nama file dan struktur pohon direktori disimpan terpisah sebagai direktori entri (dentry) yang memetakan string nama ke nomor Inode.\n\n"
            "2. Data Block Layer: blok fisik tempat konten byte sebenarnya disimpan. "
            "Fitur vital lainnya adalah Journaling: mencatat perubahan yang akan dilakukan ke dalam log jurnal sebelum ditulis ke blok utama disk. "
            "Jika listrik padam di tengah penulisan file, sistem berkas dapat memulihkan diri (replay log) dalam hitungan detik tanpa merusak konsistensi disk."
        ),
        "misconceptions": [
            {
                "misconception": "File yang dihapus dari Recycle Bin atau perintah rm langsung lenyap secara fisik dari piringan disk.",
                "explanation": "Perintah hapus biasanya hanya memutuskan pointer dentry dan menandai nomor Inode/blok sebagai 'bebas digunakan kembali'; byte data fisik tetap ada di disk sampai tertimpa data baru (dasar pemulihan data forensik).",
                "spot_in_code": "Mengira memanggil file.delete() sudah cukup aman untuk memusnahkan data rahasia tanpa teknik secure shredding / wiping."
            },
            {
                "misconception": "Pemisah path direktori selalu garis miring terbalik (\\) di semua sistem komputer.",
                "explanation": "Windows secara historis menggunakan backslash (\\), sedangkan Linux, macOS, dan Web menggunakan slash (/); menggabungkan path dengan string concatenation biasa memicu bug lintas platform.",
                "spot_in_code": "Menulis path = folder + '\\' + namaFile alih-alih menggunakan path.join()."
            }
        ],
        "when_to_use": (
            "Gunakan library path utility terstandarisasi (seperti path.join di Node.js atau package:path di Dart) untuk memastikan kompatibilitas lintas OS (Windows vs Linux/Mac). "
            "Gunakan Atomic File Writes (menulis ke file sementara lalu melakukan rename instan) untuk mencegah file korup jika aplikasi crash di tengah penulisan. "
            "Selalu sanitasi nama file masukan dari pengguna untuk mencegah serangan Path Traversal (../../etc/passwd)."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis kode penulisan file dengan menggabungkan path string manual (misalnya folder + '/' + filename) "
            "tanpa memvalidasi apakah filename mengandung karakter berbahaya '../' yang bisa menimpa file sistem operasi penting. "
            "Saat vibecoding, instruksikan AI: 'Gunakan path library resmi lintas platform, "
            "terapkan validasi pencegahan path traversal, dan gunakan teknik atomic write untuk penulisan file kritis.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa operasi penggantian nama file (rename/move) dalam partisi disk yang sama berlangsung instan tanpa peduli ukuran filenya?",
                "answer": "Karena rename dalam partisi yang sama hanya mengubah entri nama string di tabel direktori (dentry) tanpa perlu memindahkan atau menyalin blok data byte fisik di disk."
            },
            {
                "question": "Bagaimana celah keamanan Path Traversal dapat dieksploitasi oleh penyerang jika nama file tidak divalidasi?",
                "answer": "Penyerang dapat mengirimkan nama file seperti '../../../../secret.txt' yang membuat aplikasi melompat keluar dari direktori publik dan membaca atau menimpa file rahasia sistem operasi."
            }
        ]
    },

    "f-operating-system": {
        "summary": "Perangkat lunak pengelola sumber daya perangkat keras dan penyedia lingkungan eksekusi aplikasi yang aman.",
        "explanation_simple": (
            "Bayangkan manajer gedung pencakar langit yang sangat disiplin. Gedung tersebut memiliki fasilitas bersama: "
            "generator listrik, saluran pendingin udara AC, dan lift penumpang. Para penyewa kantor di lantai 5 tidak boleh "
            "begitu saja membongkar kabel listrik gedung atau memonopoli seluruh lift untuk diri mereka sendiri. "
            "Penyewa harus mengajukan izin ke manajer gedung, dan sang manajer membagi aliran listrik serta giliran lift secara adil dan aman.\n\n"
            "Sistem Operasi (Operating System - OS) adalah manajer gedung komputermu. "
            "Ia mengelola CPU, memori RAM, dan kartu grafis agar ratusan aplikasi yang berjalan tidak saling bertabrakan atau mencuri data satu sama lain. "
            "Batas analogi gedung: jika manajer gedung manusia bisa tertipu atau terlambat, kernel OS modern mengeksekusi aturan proteksi "
            "perangkat keras melalui sirkuit prosesor (Ring 0 vs Ring 3) dalam hitungan nanodetik."
        ),
        "problem_context": (
            "Pada komputer generasi pertama, hanya ada satu program yang boleh berjalan dalam satu waktu. "
            "Jika program tersebut mengalami error crash atau memasuki loop abadi, seluruh komputer membeku dan tombol reset daya harus ditekan. "
            "Aplikasi juga bebas mengakses perangkat keras printer atau memori aplikasi lain secara telanjang tanpa proteksi keamanan apapun. "
            "Sistem Operasi diciptakan untuk menyediakan isolasi proses yang kokoh, penjadwalan CPU yang adil, dan keamanan memori berlapis."
        ),
        "explanation_technical": (
            "Arsitektur OS modern berpusat pada Kernel yang berjalan di tingkat hak istimewa tertinggi CPU (Kernel Mode / Ring 0), "
            "sedangkan aplikasi pengguna berjalan di User Mode (Ring 3) yang dibatasi. "
            "Aplikasi meminta layanan perangkat keras melalui System Calls (syscalls: seperti read, write, fork, socket) "
            "yang memicu peralihan konteks perangkat keras (software interrupt / trap).\n\n"
            "Tanggung jawab inti OS meliputi: "
            "1. Process & Thread Management: Proses adalah unit isolasi memori mandiri dengan ruang alamat virtual sendiri; "
            "Thread adalah unit eksekusi terkecil di dalam proses. OS Scheduler (seperti CFS di Linux) mengatur pembagian jatah waktu CPU (time-slicing). "
            "2. Virtual Memory Management: Paging dan TLB memetakan memori virtual ke frame RAM fisik, melindungi proses dari saling mengintip memori. "
            "3. Device Drivers & Hardware Abstraction: menyederhanakan komunikasi beragam kartu grafis, mouse, dan disk ke antarmuka standar."
        ),
        "misconceptions": [
            {
                "misconception": "Proses dan Thread adalah dua kata untuk konsep yang persis sama.",
                "explanation": "Proses memiliki ruang alamat memori virtual dan file descriptor terisolasi sendiri (biaya pembuatan mahal); thread berada di dalam proses dan berbagi ruang heap memori yang sama dengan thread saudara (biaya pembuatan murah namun rawan race conditions).",
                "spot_in_code": "Bingung memilih antara multiprocessing.Process dan threading.Thread di Python."
            },
            {
                "misconception": "Aplikasi pengguna dapat langsung mengirim sinyal listrik ke pin port USB atau kartu grafis secara bebas.",
                "explanation": "Instruksi CPU I/O tingkat rendah dikunci hanya untuk Kernel Mode; setiap akses perangkat keras wajib melewati driver kernel yang terverifikasi melalui gerbang System Call.",
                "spot_in_code": "Mencoba menulis instruksi assembly in/out langsung di aplikasi desktop biasa tanpa driver kernel."
            }
        ],
        "when_to_use": (
            "Pahami konsep proses dan sinyal OS (seperti SIGINT, SIGTERM, SIGKILL) saat merancang aplikasi backend atau microservices "
            "agar server dapat melakukan Graceful Shutdown (menyelesaikan transaksi yang sedang berjalan sebelum dimatikan oleh orkestrator seperti Kubernetes). "
            "Gunakan multi-processing saat membutuhkan isolasi kegagalan total (crash di satu worker tidak mematikan worker lain)."
        ),
        "why_vibecoding_matters": (
            "AI sering membuat aplikasi backend yang langsung mati mendadak saat menerima sinyal shutdown dari sistem operasi, "
            "mengakibatkan data transaksi yang sedang disimpan menjadi terpotong dan korup di database. "
            "Saat vibecoding, beri instruksi ke AI: 'Tambahkan penanganan sinyal SIGTERM dan SIGINT untuk mengimplementasikan graceful shutdown: "
            "hentikan penerimaan request baru, tunggu koneksi yang aktif selesai, dan tutup koneksi database dengan rapi.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa arsitektur prosesor memisahkan eksekusi menjadi User Mode (Ring 3) dan Kernel Mode (Ring 0)?",
                "answer": "Untuk mencegah aplikasi pengguna melakukan operasi berbahaya (seperti mematikan interupsi CPU atau mengakses memori aplikasi lain) yang dapat meruntuhkan seluruh kestabilan sistem operasi."
            },
            {
                "question": "Apa perbedaan perilaku antara sinyal OS SIGTERM dan SIGKILL?",
                "answer": "SIGTERM adalah permintaan penutupan sopan yang dapat ditangkap oleh program untuk membersihkan data (graceful shutdown), sedangkan SIGKILL adalah pembunuhan paksa seketika oleh kernel yang tidak dapat dicegah atau ditangkap oleh aplikasi."
            }
        ]
    },

    "f-modules-packages": {
        "summary": "Organisasi kode modular, enkapsulasi namespace, dan mekanisme ekspor-impor komponen mandiri.",
        "explanation_simple": (
            "Bayangkan bermain dengan satu set balok mainan Lego bertema kastil. "
            "Di dalam kotak, kepingan balok tidak dicampur aduk berantakan dalam satu kantong plastik besar. "
            "Balok dinding dikemas dalam kantong nomor 1, kepingan gerbang hidrolik di kantong nomor 2, dan ksatria di kantong nomor 3. "
            "Setiap kantong memiliki buku instruksi mandiri yang jelas, dan kamu bisa merakit gerbang kastil tanpa harus membuka kantong ksatria.\n\n"
            "Modul dan Paket adalah kantong-kantong pengorganisasian kode perangkat lunak. "
            "Batas analogi Lego: balok Lego fisik hanya bisa dihubungkan jika geriginya pas secara mekanis, sedangkan modul perangkat lunak "
            "mengekspos antarmuka publik (public API) resmi dan menyembunyikan fungsi internal rahasia di balik dinding namespace."
        ),
        "problem_context": (
            "Ketika sebuah aplikasi web bertambah besar hingga mencapai 100.000 baris kode, menyatukan seluruh kode dalam satu file "
            "atau memuat 200 file JavaScript melalui tag <script> di HTML memicu tabrakan nama variabel global (Global Namespace Pollution). "
            "Jika file A memiliki fungsi formatTanggal() dan file B juga memiliki formatTanggal() dengan implementasi berbeda, "
            "file yang dimuat terakhir akan menimpa fungsi pertama secara diam-diam. Sistem modul diciptakan untuk menciptakan dinding pemisah yang aman."
        ),
        "explanation_technical": (
            "Sistem modularitas modern (ES Modules di JavaScript, package system di Dart, modul di Python/Rust/Go) "
            "memberikan batas leksikal terisolasi untuk setiap file kode. Variabel yang dideklarasikan di dalam modul bersifat privat "
            "secara default, kecuali jika diekspor secara eksplisit menggunakan kata kunci export (atau penamaan tanpa underscore di Dart).\n\n"
            "Standar modularitas meliputi: "
            "1. ES Modules (ESM): standar resmi web modern menggunakan sintaks import dan export statis yang dapat dianalisis pada compile-time "
            "untuk optimasi Tree Shaking (memangkas fungsi yang tidak pernah dipanggil dari biner akhir). "
            "2. CommonJS (CJS): standar historis Node.js menggunakan require() dan module.exports yang bersifat dinamis saat runtime.\n\n"
            "Paket (Package) adalah kumpulan satu atau lebih modul terorganisir yang dilengkapi file manifest metadata "
            "(seperti pubspec.yaml di Dart/Flutter, package.json di Node.js, pyproject.toml di Python) yang mendefinisikan versi, entry point, dan dependensi."
        ),
        "misconceptions": [
            {
                "misconception": "Mengimpor seluruh modul dengan import * as Utils dari 'utils' memuat seluruh isi library dan memperlambat performa secara drastis.",
                "explanation": "Pada bundler modern yang mendukung ES Modules murni, bundler menggunakan static analysis Tree Shaking untuk hanya menyertakan method yang benar-benar kamu gunakan dalam biner produksi akhir.",
                "spot_in_code": "Takut menggunakan import nama fungsi spesifik karena mengira seluruh file ribuan baris akan digandakan."
            },
            {
                "misconception": "Circular Dependency (Modul A mengimpor B, dan Modul B mengimpor A) adalah hal wajar yang tidak berdampak buruk.",
                "explanation": "Dependensi sirkular adalah tanda buruk dari arsitektur yang kusut; ia sering memicu nilai variabel undefined saat inisialisasi modul atau kegagalan kompilasi.",
                "spot_in_code": "File user.dart mengimpor order.dart dan order.dart mengimpor user.dart secara langsung."
            }
        ],
        "when_to_use": (
            "Pecah modul saat satu file kode mulai melampaui 300-400 baris atau memiliki lebih dari satu tanggung jawab domain. "
            "Gunakan ES Modules (import/export) sebagai standar penulisan kode modern daripada CommonJS (require). "
            "Gunakan Barrel Files (index.dart / index.ts) untuk mengekspor antarmuka publik fitur secara terpusat dan rapi."
        ),
        "why_vibecoding_matters": (
            "AI sering kali menghasilkan dependensi sirkular (circular imports) saat kamu meminta penambahan relasi antarmodul secara terburu-buru. "
            "Kode akan menampilkan error aneh seperti 'Cannot access variable before initialization' saat dijalankan. "
            "Saat vibecoding, instruksikan AI: 'Pastikan tidak ada ketergantungan sirkular antarmodul; "
            "jika Modul A dan Modul B membutuhkan tipe data yang sama, ekstrak tipe data tersebut ke modul Model bersama terpisah.'"
        ),
        "reflection_questions": [
            {
                "question": "Bagaimana teknik Tree Shaking bekerja pada bundler modern berbasis ES Modules?",
                "answer": "Karena sintaks import dan export ESM bersifat statis, bundler dapat membangun Abstract Syntax Tree sebelum kode dijalankan dan membuang kode mati (dead code) yang tidak pernah diimpor oleh modul mana pun."
            },
            {
                "question": "Mengapa dependensi sirkular (circular dependency) berbahaya bagi proses inisialisasi aplikasi?",
                "answer": "Karena runtime tidak dapat menentukan modul mana yang harus dieksekusi lebih dulu, mengakibatkan salah satu modul menerima objek kosong atau variabel yang belum selesai diinisialisasi."
            }
        ]
    },

    "f-dependencies": {
        "summary": "Manajemen pustaka pihak ketiga, resolusi versi semantik, dan pengendalian rantai pasokan kode eksternal.",
        "explanation_simple": (
            "Bayangkan kamu membuka restoran pizza Italia. Kamu adalah koki ahli yang membuat adonan pizza lezat dengan resep rahasia sendiri. "
            "Namun, kamu tidak perlu beternak sapi sendiri untuk memerah keju mozzarella, dan tidak perlu menanam ladang gandum sendiri untuk menggiling terigu. "
            "Kamu memesan keju dan terigu dari pemasok logistik terpercaya di pasar. "
            "Jika pemasok mengirim keju kadaluarsa atau tiba-tiba menghentikan pengiriman, operasional tokomu bisa lumpuh seketika.\n\n"
            "Dependensi (Dependencies) adalah pustaka (libraries) buatan developer lain yang kamu pasang di aplikasimu untuk mempercepat development. "
            "Batas analogi pemasok: bahan makanan fisik habis saat dipakai, sedangkan library kode perangkat lunak dapat diunduh gratis dari repositori publik "
            "(seperti pub.dev, npm, PyPI) dan digunakan jutaan kali tanpa pernah aus."
        ),
        "problem_context": (
            "Pada awal industri software, developer menyalin file kode orang lain secara manual ke folder proyek. "
            "Ketika library tersebut merilis perbaikan celah keamanan kritis, tidak ada cara otomatis untuk memperbaruinya. "
            "Lebih buruk lagi, terjadi 'Dependency Hell': Library A membutuhkan Library C versi 1.0, sedangkan Library B membutuhkan Library C versi 2.0 yang bertentangan. "
            "Package Manager modern (seperti pub, npm, pip, cargo) diciptakan untuk mengotomatisasi pengunduhan, verifikasi integritas, dan resolusi konflik versi."
        ),
        "explanation_technical": (
            "Manajemen dependensi modern berlandaskan pada konvensi Semantic Versioning (SemVer: MAJOR.MINOR.PATCH): "
            "- PATCH (misal 1.0.1): perbaikan bug kompatibel mundur (backward compatible). "
            "- MINOR (misal 1.1.0): penambahan fitur baru yang tetap kompatibel mundur. "
            "- MAJOR (misal 2.0.0): perubahan yang merusak kompatibilitas (breaking changes).\n\n"
            "Resolusi dependensi menggunakan algoritma pemuas batasan (Constraint Satisfaction / PubGrub algorithm pada Dart) "
            "untuk menemukan kombinasi versi yang cocok bagi seluruh pohon ketergantungan. "
            "Komponen paling krusial adalah Lockfile (seperti pubspec.lock, package-lock.json): mencatat versi eksak hingga checksum hash biner "
            "dari setiap library yang diinstal. Lockfile WAJIB dimasukkan ke dalam Git repository agar setiap developer di tim "
            "dan server CI/CD menggunakan kepingan kode yang 100% identik tanpa perbedaan tak terduga."
        ),
        "misconceptions": [
            {
                "misconception": "File lockfile (pubspec.lock / package-lock.json) adalah file sementara yang tidak perlu dicommit ke Git.",
                "explanation": "Lockfile menjamin build yang deterministik; mengabaikan lockfile membuat server produksi mengunduh versi library yang berbeda dari laptop pengembang, menjadi sumber utama bug 'di laptop saya jalan normal'.",
                "spot_in_code": "Memasukkan package-lock.json atau pubspec.lock ke dalam file .gitignore."
            },
            {
                "misconception": "Semakin banyak memasang library open-source dari internet, semakin hebat dan cepat aplikasi kita.",
                "explanation": "Setiap library luar membawa risiko rantai pasokan (Supply Chain Attacks), memperbesar ukuran biner aplikasi, dan menambah beban pemeliharaan saat dependensi tersebut ditinggalkan pembuatnya.",
                "spot_in_code": "Memasang library npm 50 baris hanya untuk mengecek apakah sebuah angka ganjil (is-odd)."
            }
        ],
        "when_to_use": (
            "Gunakan library pihak ketiga yang teruji dan memiliki komunitas aktif untuk masalah non-bisnis yang rumit (seperti enkripsi cryptography, parsing tanggal lintas zona waktu, koneksi HTTP/WebSockets). "
            "Jalankan audit keamanan berkala (misal flutter pub audit atau npm audit) untuk mendeteksi kerentanan CVE pada library usang. "
            "Selalu commit lockfile ke dalam version control repository."
        ),
        "why_vibecoding_matters": (
            "AI asisten sering menyarankan penginstalan paket baru untuk setiap masalah sepele, bahkan paket yang sudah usang atau paket halusinasi yang tidak pernah ada di registry publik (Hallucinated Package Attack). "
            "Saat vibecoding, jangan sembarangan menjalankan npm install atau flutter pub add yang disarankan AI. "
            "Periksa terlebih dahulu: 'Apakah masalah ini bisa diselesaikan dengan library standar bawaan bahasa? "
            "Berapa reputasi dan status pemeliharaan library ini di pub.dev/npm?'"
        ),
        "reflection_questions": [
            {
                "question": "Apa perbedaan antara direct dependencies dan transitive dependencies?",
                "answer": "Direct dependencies adalah library yang kamu pasang secara eksplisit di manifest proyekmu, sedangkan transitive dependencies adalah library yang dibutuhkan oleh library yang kamu pasang tersebut (dependensi dari dependensi)."
            },
            {
                "question": "Mengapa kenaikan versi MAJOR pada Semantic Versioning mewajibkan kehati-hatian ekstra bagi pengembang?",
                "answer": "Karena rilis versi MAJOR menandakan adanya Breaking Changes pada API publik yang dapat merusak kode aplikasi yang memanggilnya jika tidak dilakukan penyesuaian sintaks."
            }
        ]
    },

    "f-build-compilation": {
        "summary": "Transformasi kode sumber manusia menjadi artefak biner yang dapat dieksekusi oleh mesin target.",
        "explanation_simple": (
            "Bayangkan menulis naskah film berbahasa Indonesia lalu ingin memutarnya di bioskop Jepang. "
            "Proses produksi tidak hanya menerjemahkan teks dialog ke huruf Kanji, tetapi juga merekam dubbing suara pengisi suara Jepang, "
            "menyesuaikan resolusi video ke standar proyektor bioskop, memotong adegan yang tidak lolos sensor, "
            "dan menggabungkan seluruh rol film serta audio menjadi satu kaset DCP digital yang siap diputar di proyektor bioskop manapun.\n\n"
            "Build & Compilation adalah pabrik perakitan yang mengubah teks kode sumber yang kamu ketik "
            "menjadi artefak akhir (file biner .exe, file .apk untuk Android, atau bundel .js untuk web). "
            "Batas analogi film: rol film hanya diputar lurus, sedangkan artefak biner komputer berisi jutaan instruksi logika "
            "yang berinteraksi secara dinamis dengan prosesor dan memori perangkat keras."
        ),
        "problem_context": (
            "Prosesor komputer tidak mengerti kata kunci 'if', 'class', atau 'function'; prosesor hanya memahami voltase bit biner 0 dan 1 "
            "instruksi arsitektur spesifik (seperti x86_64, ARM64, RISC-V). "
            "Jika developer harus menulis biner mesin manual untuk setiap tipe HP Android dan laptop yang berbeda di pasaran, "
            "pembuatan software global tidak akan pernah terwujud. Compiler diciptakan untuk menjembatani bahasa tingkat tinggi manusia "
            "ke efisiensi biner mesin tanpa developer perlu memahami sirkuit silikon mikroprosesor secara mendalam."
        ),
        "explanation_technical": (
            "Pipeline kompilasi klasik (Compiler Pipeline) melewati beberapa fase formal: "
            "1. Lexical Analysis (Scanning): memecah teks kode menjadi aliran token (keywords, identifiers, literals). "
            "2. Syntax Analysis (Parsing): menyusun token menjadi pohon sintaksis pohon abstrak (Abstract Syntax Tree - AST) sesuai tata bahasa formal. "
            "3. Semantic Analysis: memeriksa kepatuhan tipe data, scope variabel, dan deklarasi identifikasi. "
            "4. Intermediate Representation (IR) Optimization: mesin kompilator modern (seperti LLVM) menyederhanakan IR untuk membuang kode mati, "
            "melakukan loop unrolling, dan inlining function tanpa terikat arsitektur hardware tertentu. "
            "5. Code Generation & Linking: menghasilkan kode mesin biner target (Assembler) dan Linker menggabungkan modul biner mandiri "
            "dengan library eksternal menjadi satu file eksekusi (executable).\n\n"
            "Dua model kompilasi utama: "
            "- Ahead-Of-Time (AOT): kompilasi selesai sebelum program dirilis; eksekusi awal super cepat (Dart release mode, Rust, Go, C++). "
            "- Just-In-Time (JIT): kompilasi dilakukan saat program berjalan; mendukung Hot Reload dinamis namun membutuhkan waktu pemanasan awal (Dart debug mode, Java JVM, browser V8)."
        ),
        "misconceptions": [
            {
                "misconception": "Bahasa pemrograman seperti Python dan JavaScript adalah bahasa yang sama sekali tidak mengalami proses kompilasi.",
                "explanation": "Python mengompilasi kode sumber ke biner bytecode (.pyc) sebelum dieksekusi oleh Python Virtual Machine; mesin JS V8 mengompilasi JavaScript ke bytecode dan machine code menggunakan JIT compiler canggih (Ignition & TurboFan).",
                "spot_in_code": "Mengira interpreter mengeksekusi huruf teks string secara harfiah baris demi baris di CPU."
            },
            {
                "misconception": "Build APK debug di Flutter menghasilkan performa kecepatan yang sama dengan APK release produksi.",
                "explanation": "Build debug menggunakan mode JIT dengan overhead tracing assertion dan debugger yang berat; build release menggunakan AOT machine code murni yang hingga 10x lipat lebih kencang.",
                "spot_in_code": "Menguji performa FPS atau benchmark kecepatan animasi pada mode build debug."
            }
        ],
        "when_to_use": (
            "Gunakan mode JIT selama siklus pengembangan aktif untuk menikmati fitur Hot Reload / Hot Module Replacement yang instan. "
            "Selalu gunakan mode AOT / Production Build saat melakukan benchmarking performa, profiling konsumsi baterai, atau rilis ke pengguna akhir. "
            "Aktifkan Minification dan Tree Shaking pada web build untuk memangkas ukuran download aset."
        ),
        "why_vibecoding_matters": (
            "Developer sering mengeluh aplikasi yang dibuat dengan vibecoding terasa lambat atau berukuran raksasa saat dicoba di HP, "
            "hanya karena mereka menguji build debug yang menyertakan seluruh tool developer dan server JIT internal. "
            "Saat vibecoding, pastikan kamu menguji build produksi yang sesungguhnya: "
            "'Jalankan command flutter build apk --release atau npm run build, dan verifikasi performa serta ukuran file pada bundel rilis final.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa fitur 'Hot Reload' pada Flutter hanya dapat berjalan di mode JIT dan tidak di mode AOT?",
                "answer": "Karena JIT mempertahankan kompilator di dalam memori perangkat yang mampu menukar potongan bytecode fungsi baru ke VM yang sedang berjalan tanpa perlu merestart seluruh aplikasi dan status memori."
            },
            {
                "question": "Apa peran Linker dalam tahapan akhir proses kompilasi kode?",
                "answer": "Linker menyambungkan referensi simbol fungsi atau variabel antarmodul objek biner yang terpisah dan mengikat library eksternal menjadi satu file executable yang kohesif."
            }
        ]
    },

    "f-runtime": {
        "summary": "Lingkungan eksekusi perangkat lunak yang mengelola siklus hidup proses, mesin virtual, dan alokasi sumber daya.",
        "explanation_simple": (
            "Bayangkan panggung pertunjukan teater musikal. Naskah drama dan partitur musik yang ditulis sutradara adalah kode program. "
            "Namun agar pertunjukan dapat dinikmati penonton, dibutuhkan panggung megah yang dilengkapi lampu sorot, pengeras suara mikrofon, "
            "lantai hidrolik, dan kru panggung yang sigap mengganti dekorasi di balik layar. "
            "Tanpa fasilitas panggung dan kru tersebut, naskah drama hanyalah tumpukan kertas mati yang tidak bisa ditonton siapa pun.\n\n"
            "Runtime Engine adalah panggung pertunjukan tempat kodemu dieksekusi secara nyata. "
            "Batas analogi panggung: panggung fisik teater bersifat tetap, sedangkan runtime modern (seperti Node.js, browser V8, Dart VM) "
            "mengoptimalkan kinerjanya secara adaptif selagi kode berjalan menggunakan teknik profiling dinamis."
        ),
        "problem_context": (
            "Setiap sistem operasi dan arsitektur hardware memiliki antarmuka yang sangat berbeda: panggilan sistem Linux tidak sama dengan Windows, "
            "dan prosesor Intel tidak memahami perintah prosesor Apple M-series. "
            "Jika bahasa pemrograman tidak memiliki runtime terstandarisasi, programmer harus menulis kode manajemen memori dan interaksi hardware "
            "yang berbeda untuk setiap platform. Lingkungan runtime diciptakan untuk menyediakan sandbox eksekusi terstandarisasi "
            "yang konsisten di berbagai platform fisik (Write Once, Run Anywhere)."
        ),
        "explanation_technical": (
            "Runtime Environment mencakup sekumpulan komponen esensial yang aktif mendampingi program selama berjalan: "
            "1. Virtual Machine / Execution Engine (misalnya V8 di Chrome/Node.js, Dart VM, JVM di Java): menerjemahkan bytecode atau mengeksekusi instruksi AOT. "
            "2. Memory Manager: mengelola Garbage Collection, alokasi heap, dan batas call stack. "
            "3. Concurrency / Event Scheduler: mengelola thread pool sistem operasi dan memutar Event Loop untuk penjadwalan callback asinkron. "
            "4. Standard Built-in APIs: menyediakan akses ke antarmuka I/O dasar, waktu sistem (timers), kriptografi, dan manipulasi teks.\n\n"
            "Perbedaan lingkungan runtime sangat mempengaruhi kapabilitas kode: "
            "- Runtime Browser (V8/JavaScriptCore): diisolasi ketat dalam security sandbox (tidak memiliki akses langsung ke sistem berkas disk lokal atau socket TCP mentah). "
            "- Runtime Server (Node.js/Bun/Deno): memiliki akses penuh ke sistem berkas disk, jaringan server port binding, dan proses sistem operasi."
        ),
        "misconceptions": [
            {
                "misconception": "JavaScript adalah bahasa yang sama persis di mana pun dijalankan, sehingga kode browser pasti bisa berjalan di Node.js.",
                "explanation": "Bahasa sintaksnya sama, tetapi Runtime Environment-nya sangat berbeda: browser menyediakan objek window dan document (DOM) tanpa modul 'fs', sedangkan Node.js menyediakan modul 'fs' dan 'process' tanpa ada window atau document.",
                "spot_in_code": "Mencoba mengakses document.getElementById() di dalam script server backend Node.js."
            },
            {
                "misconception": "Runtime engine hanya ada pada bahasa yang diinterpretasikan seperti Python atau JavaScript.",
                "explanation": "Bahasa terkompilasi seperti Go, Rust, dan Swift tetap memiliki runtime minimal (Go runtime mengelola goroutines dan GC; C runtime crt0 mengelola startup sebelum fungsi main() dipanggil).",
                "spot_in_code": "Mengira biner Go tidak memiliki kode runtime internal."
            }
        ],
        "when_to_use": (
            "Pahami batasan runtime tempat kodemu akan dieksekusi: gunakan Browser Runtime untuk antarmuka pengguna visual interaktif, "
            "dan gunakan Server Runtime (Node.js/Go/Dart) saat membutuhkan akses database atau file system lokal. "
            "Manfaatkan fitur runtime modern seperti WebAssembly (Wasm) jika kamu butuh mengeksekusi komputasi bahasa biner di dalam browser."
        ),
        "why_vibecoding_matters": (
            "AI sering mencampuradukkan API runtime yang tidak kompatibel: menyarankan pemanggilan modul Node.js (seperti 'fs' atau 'crypto' native) "
            "di dalam komponen frontend React browser, yang langsung memicu build error 'Module not found: Can't resolve fs'. "
            "Saat vibecoding, tegaskan konteks runtime ke AI: 'Kode ini akan dijalankan di runtime browser klien, "
            "jangan gunakan API internal server Node.js atau modul native platform.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa kode JavaScript yang menggunakan API 'localStorage' meledak saat dijalankan di Next.js Server-Side Rendering (SSR)?",
                "answer": "Karena saat proses SSR, kode dieksekusi di Server Runtime Node.js yang tidak memiliki objek browser 'window' ataupun 'localStorage'."
            },
            {
                "question": "Apa fungsi utama dari Go Runtime di dalam biner terkompilasi bahasa Go?",
                "answer": "Mengelola alokasi memori, pembersihan Garbage Collection, dan penjadwalan ribuan Goroutines secara efisien di atas thread sistem operasi fisik."
            }
        ]
    },

    "f-git": {
        "summary": "Sistem kendali versi terdistribusi untuk melacak riwayat perubahan, kolaborasi percabangan, dan integritas kode sumber.",
        "explanation_simple": (
            "Bayangkan sebuah mesin waktu untuk naskah buku yang sedang kamu tulis bersama sepuluh penulis lain. "
            "Setiap kali kamu mencapai kemajuan penting (misalnya menyelesaikan Bab 1), kamu menekan tombol simpan khusus "
            "yang mengambil foto rontgen instan (Snapshot / Commit) dari seluruh naskah lengkap dengan catatan tanggal dan namamu. "
            "Jika di Bab 3 alur cerita menjadi buntu, kamu bisa memutar balik waktu ke kondisi Bab 1 dengan satu sentuhan. "
            "Lebih hebat lagi, rekanmu bisa membuat cabang cerita alternatif (Branch) tanpa mengganggu naskah utamamu, "
            "lalu menggabungkannya kembali (Merge) saat alur alternatif tersebut terbukti bagus.\n\n"
            "Git adalah sistem kendali versi paling dominan di dunia rekayasa perangkat lunak. "
            "Batas analogi mesin waktu: mesin waktu fiksi bisa membingungkan paradoks sejarah, sedangkan Git menggunakan "
            "matematika kriptografi graf (DAG berbasis SHA-1/SHA-256) yang menjamin riwayat perubahan tidak bisa dipalsukan atau dirusak secara diam-diam."
        ),
        "problem_context": (
            "Sebelum adanya version control modern, programmer mencadangkan folder proyek dengan cara manual yang kacau: "
            "skripsi_final.zip, skripsi_final_beneran.zip, skripsi_final_revisi_dosen_OK_banget.zip. "
            "Ketika dua programmer mengedit file yang sama di server kantor pada hari yang sama, pekerjaan salah satu programmer "
            "pasti tertimpa dan hilang permanen tanpa jejak. Git diciptakan oleh Linus Torvalds pada tahun 2005 untuk memfasilitasi kolaborasi ribuan pengembang kernel Linux "
            "di seluruh dunia secara terdistribusi tanpa bergantung pada satu server pusat yang rapuh."
        ),
        "explanation_technical": (
            "Arsitektur internal Git berbasis pada Content-Addressable Storage yang memetakan konten data ke hash kriptografi (kunci 40 karakter). "
            "Empat objek inti Git: "
            "1. Blob: menyimpan konten mentah file. "
            "2. Tree: merepresentasikan struktur direktori dan nama file. "
            "3. Commit: menyimpan pointer ke root tree, metadata pembuat (author/committer), timestamp, pesan log, dan pointer ke commit induk (parent commit). "
            "4. Tag/Branch: penunjuk simbolik (pointer referensi ringan) ke hash commit tertentu.\n\n"
            "Tiga area kerja Git di komputer lokal: "
            "- Working Directory: file nyata yang sedang kamu edit. "
            "- Staging Area (Index): berkas yang sudah kamu tandai (git add) untuk dimasukkan ke foto komit berikutnya. "
            "- Repository (.git folder): database objek riwayat permanen (git commit).\n\n"
            "Operasi Merge menyatukan dua cabang independen (Fast-Forward jika lurus, atau 3-Way Merge yang melahirkan merge commit). "
            "Jika baris kode yang sama diubah berbeda di kedua cabang, Git menghentikan proses dan meminta manusia menyelesaikan Merge Conflict."
        ),
        "misconceptions": [
            {
                "misconception": "Git dan GitHub adalah hal yang persis sama.",
                "explanation": "Git adalah alat software version control lokal yang berjalan di komputermu tanpa butuh internet; GitHub adalah layanan hosting web komersial berbasis cloud untuk menyimpan repository Git secara daring.",
                "spot_in_code": "Mengira tidak bisa memakai perintah git commit jika laptop sedang offline tanpa koneksi internet."
            },
            {
                "misconception": "Perintah git push --force adalah cara normal untuk menyelesaikan masalah penolakan push dari server.",
                "explanation": "Force push menimpa dan menghapus riwayat commit rekan setim di server repositori secara brutal; gunakan git pull --rebase atau selesaikan merge conflict secara teratur.",
                "spot_in_code": "Menjalankan git push -f origin main saat ada rekan kerja yang sudah mem-push commit baru."
            }
        ],
        "when_to_use": (
            "Lakukan commit secara teratur dengan cakupan perubahan kecil yang atomik (Atomic Commits) dan pesan deskriptif. "
            "Gunakan cabang fitur (Feature Branches: misal feature/login-page) untuk setiap tugas baru agar cabang utama (main) selalu stabil dan siap rilis. "
            "Gunakan .gitignore untuk mengabaikan file build binary, dependency cache (node_modules), dan file kredensial rahasia (.env)."
        ),
        "why_vibecoding_matters": (
            "Saat vibecoding, AI dapat dengan cepat mengubah ratusan baris kode sekaligus dalam hitungan detik. "
            "Jika kamu tidak melakukan commit sebelum meminta AI melakukan refactoring besar, dan ternyata kode yang dihasilkan AI rusak total, "
            "kamu akan kehilangan seluruh pekerjaanmu sebelumnya tanpa jalan mundur. "
            "Jadikan aturan besi vibecoding: 'Selalu lakukan git commit kondisi kerja yang stabil sebelum memberikan prompt perubahan besar kepada AI!'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Git disebut sistem kendali versi 'terdistribusi' (distributed VCS) berbeda dengan Subversion (SVN)?",
                "answer": "Karena setiap developer memiliki salinan utuh seluruh database riwayat commit di laptop lokalnya masing-masing, sehingga semua operasi (commit, log, branch) dapat berjalan tanpa koneksi ke server pusat."
            },
            {
                "question": "Apa bahaya dari melakukan commit file kredensial rahasia (.env atau API keys) ke dalam repositori Git publik?",
                "answer": "Bot peretas memindai GitHub 24 jam sehari untuk mencuri API keys dalam hitungan detik; menghapus file di commit berikutnya tidak membersihkan riwayat lama, kecuali seluruh history dibersihkan menggunakan filter-repo."
            }
        ]
    },

    "f-terminal": {
        "summary": "Antarmuka baris perintah (CLI) untuk pengendalian sistem operasi, otomatisasi proses, dan manipulasi data langsung.",
        "explanation_simple": (
            "Bayangkan memesan makanan di restoran mewah melalui pelayan yang membawa buku menu bergambar (Antarmuka Grafis / GUI): "
            "kamu menunjuk foto makanan, memilih dari opsi yang sudah disediakan, dan prosesnya terasa santai serta visual. "
            "Sekarang bayangkan kamu berbicara langsung ke kepala koki di dapur melalui walkie-talkie instruksi singkat (Terminal / CLI): "
            "'Panggang daging tingkat medium-well 200 gram, tanpa garam, tambahkan lada hitam giling kasar'. "
            "Instruksi radio baris perintah membutuhkan kamu tahu istilah tepatnya, tetapi ia memberikan kebebasan mutlak, presisi tinggi, dan kecepatan tanpa batas.\n\n"
            "Terminal adalah pintu gerbang komunikasi paling murni antara manusia dan sistem operasi komputer. "
            "Batas analoginya: walkie-talkie fisik memiliki jangkauan suara terbatas, sedangkan terminal komputer modern "
            "dapat mengendalikan ribuan server di benua lain melalui protokol terenkripsi SSH."
        ),
        "problem_context": (
            "Antarmuka visual grafis (GUI) seperti jendela tombol dan klik mouse sangat ramah untuk pengguna biasa, "
            "tetapi sangat buruk untuk otomatisasi pekerjaan massal. "
            "Jika kamu diminta mengubah nama 10.000 file foto dari 'IMG_001.jpg' menjadi 'Liburan_001.jpg', "
            "melakukannya dengan klik mouse akan memakan waktu tiga minggu penuh. "
            "Di terminal CLI, satu baris perintah loop atau pipe dapat menyelesaikan tugas tersebut dalam waktu 2 detik."
        ),
        "explanation_technical": (
            "Terminal bekerja melalui arsitektur Shell (seperti Bash, Zsh di Linux/macOS, PowerShell di Windows). "
            "Shell beroperasi dalam siklus REPL (Read-Eval-Print Loop): membaca baris perintah teks, mem-parsing token, mengevaluasi argumen dan variabel environment, "
            "menjalankan proses biner yang diminta, dan menampilkan output teks ke konsol.\n\n"
            "Prinsip fundamental filosofi UNIX dalam CLI: "
            "1. Standard Streams: setiap program CLI memiliki tiga saluran aliran byte: Standard Input (stdin / 0), Standard Output (stdout / 1), dan Standard Error (stderr / 2). "
            "2. Redirection: mengarahkan output ke file menggunakan operator > (timpa) atau >> (tambah ke akhir file). "
            "3. Pipes (|): menghubungkan stdout dari Program A langsung menjadi stdin bagi Program B tanpa file perantara (misal: cat log.txt | grep 'ERROR' | wc -l). "
            "Komposisi perintah-perintah kecil yang fokus (do one thing well) melahirkan kapabilitas otomatisasi yang tak terbatas."
        ),
        "misconceptions": [
            {
                "misconception": "Perintah terminal adalah mantra sihir yang harus dihapal mati tanpa pola logika.",
                "explanation": "Sebagian besar perintah CLI mengikuti tata bahasa terstruktur yang konsisten: [perintah] [opsi/flags -a/--all] [argumen/target].",
                "spot_in_code": "Panik melihat perintah curl -X POST -H 'Content-Type: application/json' -d '{}' padahal itu hanya struktur flag dan nilai standar."
            },
            {
                "misconception": "Terminal hanya digunakan oleh sysadmin server jadul dan tidak dibutuhkan oleh developer aplikasi modern.",
                "explanation": "Seluruh toolchain pengembangan modern (Git, Flutter CLI, npm, Docker, CI/CD runners) dioperasikan dan diotomatisasi melalui baris perintah terminal.",
                "spot_in_code": "Menolak belajar terminal dan bergantung sepenuhnya pada tombol GUI yang terbatas fiturnya."
            }
        ],
        "when_to_use": (
            "Gunakan terminal untuk menjalankan build tools, package managers, generator kode, dan otomasi skrip deployment. "
            "Gunakan piping (|) dan utilitas text-processing (grep, awk, sed, jq) untuk menganalisis log sistem berukuran ratusan megabyte secara instan di server. "
            "Kuasai navigasi dasar: cd, ls/dir, pwd, rm, mkdir, cat/type, dan curl."
        ),
        "why_vibecoding_matters": (
            "AI sering menyarankan perintah terminal untuk dieksekusi pengguna (misalnya perintah rm -rf, konfigurasi environment variables, atau instalasi global). "
            "Jika kamu mengeksekusi perintah terminal AI secara buta tanpa memahaminya, perintah yang keliru bisa menghapus seluruh file harddisk komputermu secara permanen. "
            "Saat vibecoding, teliti setiap perintah shell: 'Jelaskan apa yang dilakukan oleh setiap flag pada perintah terminal ini sebelum saya menjalankannya!'"
        ),
        "reflection_questions": [
            {
                "question": "Bagaimana operator Pipe (|) menghubungkan dua program yang tidak saling mengenal satu sama lain?",
                "answer": "Sistem operasi menghubungkan saluran Standard Output (stdout) dari program di sebelah kiri pipa langsung ke saluran Standard Input (stdin) program di sebelah kanan pipa melalui buffer kernel in-memory."
            },
            {
                "question": "Mengapa aliran error (stderr) dipisahkan dari aliran output normal (stdout)?",
                "answer": "Agar pesan error diagnostik tetap terlihat di layar terminal pemantau dan tidak mengotori aliran data bersih yang sedang dialihkan (redirected) ke file atau ke pipa program lain."
            }
        ]
    },

    "f-networking": {
        "summary": "Prinsip transmisi paket data melalui jaringan komputer, model hierarki OSI, dan protokol transport TCP/UDP.",
        "explanation_simple": (
            "Bayangkan mengirim surat pos dari Jakarta ke sahabatmu di pedalaman London. Kamu memasukkan surat ke dalam amplop, "
            "menuliskan nama penerima, alamat jalan, kode pos kota, dan negara tujuan. "
            "Petugas kantor pos Jakarta tidak langsung terbang mengantar suratmu ke London; surat dibawa ke kantor pos kecamatan, "
            "lalu ke bandara kargo udara, dipindahkan ke pesawat transit di Dubai, tiba di bandara Heathrow London, "
            "disortir oleh van pos regional, dan akhirnya dimasukkan kurir ke kotak pos rumah sahabatmu.\n\n"
            "Jaringan Komputer (Networking) adalah sistem pengiriman paket data digital melintasi kabel tembaga, serat optik bawah laut, dan gelombang radio Wi-Fi. "
            "Batas analogi pos: surat pos fisik bisa basah atau hilang di jalan, sedangkan jaringan komputer modern "
            "memiliki protokol cerdas (seperti TCP) yang memotong pesan menjadi ribuan paket kecil bernomor urut, "
            "dan meminta pengiriman ulang otomatis jika ada satu paket yang hilang di tengah jalan."
        ),
        "problem_context": (
            "Ketika dua komputer terhubung kabel secara fisik, voltase listrik yang melintasi kabel mudah mengalami interferensi derau (noise), "
            "tabrakan paket (packet collisions), dan keterbatasan jarak sinyal. "
            "Lebih rumit lagi ketika miliaran komputer di seluruh dunia dengan sistem operasi dan kecepatan jaringan yang berbeda ingin saling mengobrol. "
            "Standarisasi protokol jaringan berlapis diciptakan agar setiap lapisan teknologi (dari kabel fisik hingga aplikasi web) "
            "dapat berevolusi secara independen tanpa merusak komunikasi global."
        ),
        "explanation_technical": (
            "Komunikasi jaringan diabstraksikan melalui Model 7 Lapisan OSI (Open Systems Interconnection) "
            "dan arsitektur praktis Internet Protocol Suite (TCP/IP 4 Lapisan): "
            "1. Physical Layer: sinyal listrik bit biner pada kabel fisik, serat optik, atau radio Wi-Fi. "
            "2. Data Link Layer (Ethernet, Wi-Fi MAC Address): transmisi frame data antar-perangkat di jaringan lokal yang sama (LAN). "
            "3. Network Layer (IP - Internet Protocol): perutean paket (routing) melintasi berbagai jaringan menggunakan IP Address (IPv4 32-bit / IPv6 128-bit). "
            "4. Transport Layer: komunikasi antar-proses aplikasi menggunakan port (Port 0-65535).\n\n"
            "Dua protokol Transport paling esensial: "
            "- TCP (Transmission Control Protocol): Connection-oriented, Three-Way Handshake (SYN -> SYN-ACK -> ACK), "
            "menjamin urutan paket, retransmisi paket hilang, dan pengendalian kemacetan (Congestion Control). Digunakan oleh HTTP, Web, Email, SSH. "
            "- UDP (User Datagram Protocol): Connectionless, tanpa handshake, tanpa jaminan urutan atau pengiriman ulang, overhead minimal dan latensi sangat rendah. "
            "Digunakan oleh Voice VoIP, Live Video Streaming, DNS query, dan Game Online real-time."
        ),
        "misconceptions": [
            {
                "misconception": "TCP selalu lebih baik daripada UDP karena TCP menjamin semua data pasti sampai tanpa hilang.",
                "explanation": "Pada game online tembak-menembak atau video call streaming, menunggu pengiriman ulang paket yang hilang (Head-of-Line Blocking pada TCP) justru merusak pengalaman real-time; paket koordinat usang lebih baik dibuang daripada ditunggu.",
                "spot_in_code": "Memilih protokol TCP mentah untuk fitur voice chat real-time berlatensi ultra-rendah."
            },
            {
                "misconception": "IP Address adalah alamat fisik permanen yang menempel mati pada mesin laptop selamanya.",
                "explanation": "IP Address adalah alamat logis sementara yang dialokasikan oleh router (via DHCP); alamat perangkat keras fisik yang permanen adalah MAC Address pada kartu jaringan.",
                "spot_in_code": "Menyimpan IP address pengguna sebagai identitas permanen unik akun di database."
            }
        ],
        "when_to_use": (
            "Gunakan TCP (melalui HTTP/HTTPS/WebSockets) untuk transfer dokumen, transaksi keuangan, autentikasi, dan API di mana integritas data 100% mutlak. "
            "Gunakan UDP (atau WebRTC data channels) untuk streaming audio/video langsung, telemetry sensor IoT berkecepatan tinggi, dan transmisi posisi game real-time. "
            "Pahami batasan MTU (Maximum Transmission Unit, biasanya 1.500 byte) saat merancang paket jaringan mentah."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis kode jaringan tanpa memperhitungkan latensi dunia nyata (Network Latency) dan paket yang putus sesaat (packet drop), "
            "menganggap komunikasi jaringan selalu secepat membaca memori RAM lokal. "
            "Saat vibecoding, ingatkan AI: 'Jaringan internet bersifat tidak stabil (unreliable network): "
            "tambahkan konfigurasi timeout yang masuk akal, mekanisme exponential backoff retry, dan penanganan status offline pada aplikasi ini.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Three-Way Handshake pada TCP diperlukan sebelum transfer data aplikasi dimulai?",
                "answer": "Untuk menyinkronkan nomor urut awal (Initial Sequence Numbers - ISN) antara klien dan server, serta memverifikasi bahwa kedua belah pihak siap mengirim dan menerima paket secara dua arah."
            },
            {
                "question": "Apa fungsi dari Port Number (misalnya Port 80 untuk HTTP atau Port 443 untuk HTTPS) dalam sebuah paket IP?",
                "answer": "IP Address mengidentifikasi mesin komputer di jaringan, sedangkan Port Number mengidentifikasi proses atau aplikasi spesifik di dalam komputer tersebut yang menjadi tujuan akhir data."
            }
        ]
    },

    "f-http-web": {
        "summary": "Protokol komunikasi lapisan aplikasi yang menjadi fondasi pertukaran informasi World Wide Web.",
        "explanation_simple": (
            "Bayangkan memesan hidangan di restoran mewah melalui pelayan. Kamu sebagai tamu (Client / Browser) membaca daftar menu "
            "lalu menyampaikan pesanan ke pelayan: 'Tolong ambilkan Nasi Goreng Spesial' (HTTP Request). "
            "Pelayan membawa pesanan ke dapur koki (Server), menunggu hidangan dimasak, lalu kembali ke mejamu sambil membawa piring "
            "dan berkata: 'Ini Nasi Gorengnya, status 200 Sukses' (HTTP Response). Jika stok ayam habis, pelayan kembali dan berkata: "
            "'Maaf, menu tidak tersedia, status 404 Not Found'.\n\n"
            "HTTP (Hypertext Transfer Protocol) adalah tata krama percakapan resmi antara browser web atau aplikasi HP dengan server di internet. "
            "Batas analogi restoran: pelayan restoran biasanya mengingat wajahmu di meja nomor 4, sedangkan protokol HTTP secara default "
            "bersifat Stateless (lupa ingatan): setiap kali kamu memesan piring kedua, server menganggapmu sebagai orang asing yang baru datang, "
            "sehingga aplikasi membutuhkan Cookie atau Token untuk membuktikan identitasmu."
        ),
        "problem_context": (
            "Ketika Tim Berners-Lee merancang World Wide Web pada tahun 1989, para ilmuwan membutuhkan cara sederhana dan terbuka "
            "untuk bertukar dokumen teks hiperteks antar-komputer universitas di seluruh dunia tanpa mempedulikan jenis sistem operasinya. "
            "Diperlukan sebuah protokol berbasis teks yang universal, fleksibel, dan tidak memerlukan sambungan kabel eksklusif yang terus terbuka. "
            "HTTP diciptakan sebagai protokol Request-Response sederhana yang kini menjadi fondasi seluruh ekonomi digital internet modern."
        ),
        "explanation_technical": (
            "HTTP adalah protokol Application Layer (di atas TCP/IP) berbasis siklus Request-Response: "
            "1. HTTP Request terdiri dari: "
            "- Method / Verb: niat aksi (GET: membaca, POST: membuat baru, PUT: mengganti total, PATCH: mengubah sebagian, DELETE: menghapus). "
            "- URL / Path: alamat sumber daya target (misal: /api/v1/users/42). "
            "- Headers: metadata kontekstual (User-Agent, Content-Type, Authorization, Accept). "
            "- Body: muatan payload data (biasanya berformat JSON pada REST API).\n\n"
            "2. HTTP Response terdiri dari: "
            "- Status Code: kode numerik 3 digit indikator hasil (1xx: Informasi, 2xx: Sukses [200 OK, 201 Created], 3xx: Pengalihan [301, 302], "
            "4xx: Kesalahan Klien [400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found], 5xx: Kesalahan Server [500 Internal Error, 502 Bad Gateway]). "
            "- Response Headers: metadata server (Content-Type, Set-Cookie, Cache-Control). "
            "- Response Body: payload data hasil (HTML, JSON, file biner).\n\n"
            "Evolusi protokol: HTTP/1.1 (koneksi teks, rawan Head-of-Line blocking), HTTP/2 (biner, multiplexing beberapa request dalam satu koneksi TCP), "
            "dan HTTP/3 (berbasis protokol QUIC di atas UDP untuk mengatasi packet loss dan koneksi instan 0-RTT)."
        ),
        "misconceptions": [
            {
                "misconception": "Perbedaan status kode 401 Unauthorized dan 403 Forbidden adalah sepele dan bisa dipakai sembarangan.",
                "explanation": "401 artinya Unauthenticated (server tidak tahu siapa kamu; kamu belum login); 403 artinya Forbidden (server tahu siapa kamu, tetapi kamu tidak memiliki hak akses izin untuk sumber daya ini).",
                "spot_in_code": "Mengembalikan status 401 saat user biasa mencoba mengakses halaman dashboard admin."
            },
            {
                "misconception": "Permintaan HTTP GET aman digunakan untuk mengirimkan data perubahan sensitif seperti password.",
                "explanation": "GET tidak boleh mengubah state server (harus safe & idempotent); parameter query GET tercatat secara telanjang di log history browser, server proxy, dan log ISP, menjadikannya celah kebocoran keamanan parah.",
                "spot_in_code": "Membuat endpoint GET /api/login?user=admin&pass=12345."
            }
        ],
        "when_to_use": (
            "Gunakan GET untuk membaca data, POST untuk pembuatan entitas baru, PUT/PATCH untuk pembaruan, dan DELETE untuk penghapusan sesuai kaidah arsitektur REST. "
            "Selalu gunakan HTTPS (HTTP over TLS/SSL port 443) untuk mengenkripsi lalu lintas data dari serangan penyadapan Man-in-the-Middle. "
            "Manfaatkan header Cache-Control untuk menghemat kuota server dan mempercepat loading aplikasi klien."
        ),
        "why_vibecoding_matters": (
            "AI sering kali menghasilkan endpoint API yang mencampuradukkan HTTP methods (misalnya menggunakan POST untuk mengambil data detail, atau GET untuk menghapus akun). "
            "Selain melanggar konvensi web, hal ini merusak mekanisme caching browser dan membuka celah keamanan CSRF. "
            "Saat vibecoding, instruksikan AI: 'Patuhi standar semantik HTTP: gunakan HTTP verbs yang sesuai, "
            "kembalikan status code yang presisi (200, 201, 400, 401, 404, 500), dan gunakan HTTPS dengan header keamanan standar.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa protokol HTTP disebut protokol yang 'Stateless' (tanpa status memori)?",
                "answer": "Karena server memperlakukan setiap permintaan HTTP sebagai transaksi independen yang berdiri sendiri tanpa menyimpan memori konteks dari permintaan-permintaan sebelumnya."
            },
            {
                "question": "Apa arti dari sifat 'Idempotent' pada HTTP methods seperti GET, PUT, dan DELETE?",
                "answer": "Idempotent berarti mengeksekusi permintaan yang sama sebanyak satu kali atau sepuluh kali berturut-turut akan menghasilkan status akhir yang persis sama pada data server."
            }
        ]
    }
}
