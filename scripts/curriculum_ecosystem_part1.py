"""Ecosystem Curriculum Part 1: Groups 1 - 6 (Topics 1 - 26).
Includes Benchmark 4 (e-frontend-overview).
"""

ECOSYSTEM_CURRICULUM_PART1 = {
    "e-languages-overview": {
        "summary": "Peta lanskap bahasa pemrograman di industri software dan kriteria pemilihan teknologi.",
        "explanation_simple": (
            "Bayangkan kotak perkakas seorang montir mobil profesional. Di dalamnya terdapat kunci pas, obeng kembang, "
            "tang jepit, dan mesin las listrik. Setiap alat diciptakan untuk pekerjaan khusus: kamu tidak menggunakan mesin las "
            "untuk mengencangkan baut kecil kaca spion, dan tidak memakai obeng plastik untuk menyambung rangka sasis truk baja.\n\n"
            "Bahasa pemrograman adalah perkakas rekayasa perangkat lunak: TypeScript adalah penguasa ekosistem web, "
            "Python adalah standar de facto kecerdasan buatan (AI) dan data science, Dart/Flutter unggul di aplikasi mobile multiplatform, "
            "Go mendominasi cloud microservices berkinerja tinggi, dan Rust menjadi pilihan utama keamanan memori sistem tingkat rendah. "
            "Batas analogi perkakas: perkakas besi bersifat kaku, sedangkan bahasa pemrograman modern terus berevolusi "
            "saling mengadopsi fitur terbaik dari satu sama lain."
        ),
        "problem_context": (
            "Memilih bahasa pemrograman yang salah untuk sebuah produk dapat mematikan kelangsungan startup atau proyek perusahaan. "
            "Jika kamu memilih bahasa berorientasi sistem manual (seperti C) untuk membuat prototipe aplikasi media sosial yang butuh iterasi harian, "
            "kamu akan kehabisan modal sebelum fitur pertama selesai. Sebaliknya, jika kamu memilih bahasa script ber-Garbage Collector lambat "
            "untuk membuat sistem kendali rem mobil otomatis berkecepatan tinggi, jeda waktu GC dapat membahayakan nyawa manusia. "
            "Insinyur software wajib memahami kompromi arsitektur setiap bahasa."
        ),
        "explanation_technical": (
            "Klasifikasi bahasa pemrograman berporos pada tiga dimensi arsitektural: "
            "1. Sistem Pengetikan: Static vs Dynamic Typing, Strong vs Weak Typing. Bahasa bertipe statis (TypeScript, Dart, Go, Rust) "
            "mencegah bug di tahap kompilasi dan memudahkan refactoring skala besar; bahasa bertipe dinamis (Python, Ruby) menawarkan kecepatan prototipe kilat. "
            "2. Model Eksekusi: Kompilasi Mesin Asli AOT (Go, Rust, C++) menghasilkan biner mandiri tanpa overhead; "
            "Bytecode Virtual Machine / JIT (Java JVM, Dart VM, Node.js V8) mengoptimalkan eksekusi saat berjalan; "
            "Interpreted murni memproses kode secara langsung.\n\n"
            "3. Paradigma Dominan: Multi-paradigma modern memadukan Object-Oriented (OOP) dan Functional Programming (FP). "
            "Pertimbangan pemilihan di industri: ketersediaan talenta programmer di pasar (talent pool), kematangan ekosistem library (package ecosystem), "
            "dan rasio antara Developer Velocity (kecepatan rilis) versus Runtime Performance (konsumsi memori dan latensi CPU)."
        ),
        "misconceptions": [
            {
                "misconception": "Ada satu bahasa pemrograman terbaik di dunia yang akan menggantikan semua bahasa lain.",
                "explanation": "Tidak ada satu bahasa yang optimal untuk semua domain; software modern dibangun dengan pendekatan Polyglot (misal backend Go dengan frontend TypeScript dan pipeline AI Python).",
                "spot_in_code": "Memaksakan penulisan skrip otomasi data machine learning menggunakan C++ murni."
            },
            {
                "misconception": "Bahasa yang diketik cepat saat coding (seperti Python) selalu menghasilkan proyek yang lebih cepat selesai.",
                "explanation": "Kecepatan awal mengetik sering terbayar mahal di masa pemeliharaan jika ketiadaan type safety menimbulkan bug runtime yang sulit dilacak pada codebase besar.",
                "spot_in_code": "Membangun sistem monolit 500.000 baris tanpa anotasi tipe statis apapun."
            }
        ],
        "when_to_use": (
            "Gunakan TypeScript untuk aplikasi web frontend dan backend full-stack node. "
            "Gunakan Python untuk eksplorasi data, scripting otomasi, machine learning, dan integrasi API AI. "
            "Gunakan Dart untuk aplikasi mobile lintas platform (iOS & Android) dengan performa grafis 60/120 FPS. "
            "Gunakan Go untuk backend microservices cloud-native berkonkurensi tinggi."
        ),
        "why_vibecoding_matters": (
            "AI mampu menghasilkan kode dalam puluhan bahasa berbeda. Jika kamu tidak membatasi bahasa secara eksplisit, "
            "AI bisa menghasilkan modul utilitas dalam bahasa yang tidak didukung oleh runtime proyekmu. "
            "Saat vibecoding, tetapkan batasan: 'Gunakan ekosistem bahasa resmi proyek ini (misal TypeScript strictly typed), "
            "jangan gunakan sintaks eksperimental yang membutuhkan flag compiler khusus.'"
        ),
        "reflection_questions": [
            {
                "question": "Apa arti dari 'Developer Velocity' vs 'Runtime Efficiency' dalam pertimbangan pemilihan bahasa pemrograman?",
                "answer": "Developer velocity mengukur seberapa cepat tim programmer dapat menulis dan merilis fitur baru, sedangkan runtime efficiency mengukur seberapa hemat konsumsi CPU dan RAM server saat melayani jutaan pengguna."
            },
            {
                "question": "Mengapa bahasa modern seperti Rust dan Go melarang fitur class inheritance tradisional?",
                "answer": "Untuk mencegah arsitektur hierarki class yang kaku dan rapuh, menggantikannya dengan komposisi struct dan interfaces yang jauh lebih fleksibel serta mudah dipelihara."
            }
        ]
    },

    "e-compilers-overview": {
        "summary": "Mesin penerjemah kode sumber manusia menjadi biner eksekusi mesin atau representasi perantara.",
        "explanation_simple": (
            "Bayangkan dua jenis penerjemah bahasa asing di sebuah konferensi internasional. "
            "Penerjemah pertama adalah Penerjemah Buku (Compiler): ia membaca naskah pidato dari awal sampai akhir, mengedit tata bahasa, "
            "memperbaiki kalimat rancu, lalu mencetak seluruh terjemahan menjadi buku rapi sebelum acara dimulai. "
            "Penerjemah kedua adalah Penerjemah Lisan Simultan (Interpreter): ia mendengarkan pembicara berbicara satu kalimat, "
            "lalu langsung membisikkan terjemahan kalimat itu ke telinga pendengar saat itu juga.\n\n"
            "Kompilator (Compiler) dan Interpreter adalah mesin penerjemah kode sumber manusia ke instruksi CPU komputer. "
            "Batas analogi: mesin kompilator komputer modern (seperti LLVM) tidak hanya menerjemahkan bahasa, "
            "tetapi juga mengoptimasi tata letak instruksi mesin agar berjalan dengan kecepatan fisik maksimum pada prosesor target."
        ),
        "problem_context": (
            "Tanpa compiler dan interpreter, manusia harus menulis kode komputer langsung dalam angka heksadesimal atau binary opcodes "
            "(misal B8 2A 00 00 00 untuk memuat angka 42 ke register CPU). "
            "Menulis software sebesar browser web atau sistem operasi dengan cara ini adalah kemustahilan kognitif bagi otak manusia. "
            "Perkembangan teknologi compiler adalah fondasi utama yang memungkinkan lahirnya seluruh industri software modern."
        ),
        "explanation_technical": (
            "Tiga paradigma eksekusi penerjemahan bahasa: "
            "1. Ahead-Of-Time (AOT) Compilers (Rust, Go, C++, Dart Release): Mem-parsing AST, melakukan optimasi IR (Intermediate Representation) tingkat tinggi, "
            "dan menghasilkan biner machine code spesifik untuk arsitektur target (x86, ARM). Waktu startup instan, penggunaan memori ramping, "
            "dan tidak membutuhkan runtime interpreter di perangkat pengguna. "
            "2. Pure Interpreters: Membaca AST dan mengevaluasi node satu per satu secara langsung (sederhana namun lambat secara CPU). "
            "3. Just-In-Time (JIT) Compilers (V8 di Chrome/Node, JVM, PyPy, Dart Debug): Mengompilasi kode ke bytecode portabel terlebih dahulu, "
            "lalu memantau fungsi yang sering dipanggil (Hot Spots) saat program berjalan, dan mengompilasi hot functions tersebut secara dinamis "
            "ke machine code teroptimasi tinggi saat runtime (adaptive profiling)."
        ),
        "misconceptions": [
            {
                "misconception": "Bahasa terkompilasi selalu 100% lebih cepat daripada bahasa dengan JIT compiler di segala situasi.",
                "explanation": "JIT compiler memiliki keunggulan informasi profil runtime aktual (runtime devirtualization) yang tidak dimiliki AOT statis, sehingga untuk tugas komputasi kontinu yang panjang, JIT modern dapat menyamai kecepatan AOT.",
                "spot_in_code": "Mengira eksekusi loop matematika murni di Node.js V8 pasti jauh lebih lambat daripada C++ tanpa benchmark."
            },
            {
                "misconception": "File bytecode (seperti .pyc atau .class) adalah machine code biner prosesor fisik.",
                "explanation": "Bytecode adalah instruksi biner untuk mesin virtual abstrak (Virtual Machine), bukan untuk CPU fisik; ia masih harus dieksekusi atau dikompilasi ulang oleh VM runtime di komputer lokal.",
                "spot_in_code": "Mencoba menjalankan file bytecode Java secara langsung di shell Linux tanpa Java Runtime."
            }
        ],
        "when_to_use": (
            "Pilih AOT Compilation saat membangun aplikasi mobile (Flutter/iOS), command-line tools (Go/Rust), atau sistem embedded yang membutuhkan startup time instan tanpa waktu pemanasan. "
            "Manfaatkan JIT Compilation selama siklus development aktif untuk menikmati produktivitas Hot Reload instan. "
            "Pelajari flag optimasi compiler (-O2 / -O3 pada C/Rust) saat melakukan tuning performa biner."
        ),
        "why_vibecoding_matters": (
            "AI sering kali tidak memahami perbedaan antara target kompilasi: menyarankan opsi kompilasi yang mematikan optimasi "
            "atau menyertakan simbol debug yang memperbesar ukuran file instalasi hingga ratusan megabyte. "
            "Saat membuild artefak bersama AI, instruksikan: 'Gunakan konfigurasi build release AOT dengan strip debug symbols "
            "dan tree shaking maksimal untuk meminimalkan ukuran file biner akhir.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Apple App Store melarang penggunaan JIT Compilation murni pada aplikasi pihak ketiga di iOS?",
                "answer": "Karena JIT membutuhkan izin memori W^X (Write XOR Execute) untuk menulis machine code baru di RAM dan langsung mengeksekusinya, yang berpotensi disalahgunakan untuk mengeksekusi kode berbahaya tanpa lolos audit keamanan Apple."
            },
            {
                "question": "Apa keunggulan LLVM (Low Level Virtual Machine) dalam ekosistem compiler modern seperti Rust, Swift, dan Clang?",
                "answer": "LLVM memisahkan frontend bahasa (parser sintaks) dari backend hardware (generator machine code); setiap bahasa baru hanya perlu membuat frontend ke LLVM IR untuk otomatis mendukung puluhan arsitektur prosesor di dunia."
            }
        ]
    },

    "e-runtime-overview": {
        "summary": "Mesin lingkungan eksekusi modern (Node.js, Deno, Bun, Dart VM) dan perannya dalam ekosistem server serta desktop.",
        "explanation_simple": (
            "Bayangkan mesin mobil listrik bertenaga baterai. Baterai dan motor penggeraknya adalah runtime engine. "
            "Baterai yang sama (mesin V8) awalnya hanya dirancang untuk menggerakkan mobil sedan di jalan raya kota (browser web Google Chrome). "
            "Namun seorang insinyur jenius (Ryan Dahl pada tahun 2009) mengeluarkan mesin mobil tersebut dari rangka sedan, "
            "memasangkannya ke generator pabrik raksasa di darat, dan melengkapinya dengan kabel listrik tegangan tinggi dan pipa pendingin (sistem berkas dan jaringan). "
            "Lahir lah pembangkit listrik mandiri bernama Node.js.\n\n"
            "Runtime Engine Server memungkinkan bahasa yang awalnya hanya hidup di browser web dieksekusi di server cloud backend. "
            "Batas analoginya: mesin pabrik fisik memiliki tombol putar manual, sedangkan runtime engine modern "
            "mengotomatiskan alokasi thread pool I/O dan garbage collection ribuan koneksi konkuren secara non-blocking."
        ),
        "problem_context": (
            "Sebelum era Node.js, server web tradisional (seperti Apache HTTP Server dengan PHP) membuat satu thread sistem operasi baru "
            "untuk setiap satu pengguna yang terhubung. Ketika 10.000 pengguna terhubung bersamaan (masalah C10K problem), "
            "server kehabisan memori RAM hanya untuk mengalokasikan stack thread dan sistem crash. "
            "Runtime berbasis Single-Threaded Event Loop non-blocking diciptakan untuk melayani puluhan ribu koneksi simultan "
            "dengan konsumsi memori yang sangat ramping."
        ),
        "explanation_technical": (
            "Peta persaingan Runtime Engine JavaScript/TypeScript modern: "
            "1. Node.js: Pelopor industri; memadukan V8 engine dengan libuv (C library untuk asynchronous I/O thread pool). "
            "Ekosistem terbesar di dunia (npm), stabil, namun membawa utang teknis warisan (CommonJS vs ESM, ketiadaan TypeScript native). "
            "2. Deno: Dibuat oleh pencipta Node.js untuk memperbaiki kekurangan desain lama; mendukung TypeScript secara native tanpa konfigurasi, "
            "berbasis security sandbox ketat (wajib izin eksplisit --allow-net, --allow-read), dan mematuhi Web Standards API (fetch, WebSockets). "
            "3. Bun: Runtime generasi terbaru yang ditulis dalam bahasa Zig di atas mesin JavaScriptCore (WebKit Safari); "
            "berfokus pada kecepatan startup ultra-kencang, bundler bawaan, test runner terintegrasi, dan kompatibilitas penuh dengan ekosistem npm.\n\n"
            "Dart VM: Runtime multi-mode yang dapat mengeksekusi bytecode JIT (untuk hot reload flutter) atau dikompilasi ke machine code AOT."
        ),
        "misconceptions": [
            {
                "misconception": "Node.js murni berjalan di satu thread dan tidak pernah menggunakan multi-threading sama sekali.",
                "explanation": "Kode JavaScript pengguna memang berjalan di main event loop single-thread, tetapi di balik layar library libuv menjalankan thread pool latar belakang (default 4 thread) untuk operasi disk I/O, DNS lookup, dan kriptografi.",
                "spot_in_code": "Kaget melihat konsumsi thread Node.js di task manager menunjukkan lebih dari 5 threads."
            },
            {
                "misconception": "Deno dan Bun tidak bisa menggunakan paket-paket yang ada di npm registry.",
                "explanation": "Deno dan Bun modern memiliki lapisan kompatibilitas npm yang sangat matang; kamu bisa mengimpor library npm secara langsung menggunakan prefix npm: di Deno atau langsung di package.json Bun.",
                "spot_in_code": "Menolak memakai Deno karena mengira harus menulis ulang seluruh library dari nol."
            }
        ],
        "when_to_use": (
            "Gunakan Node.js (LTS version) untuk proyek backend skala perusahaan yang membutuhkan stabilitas teruji dan kepatuhan pustaka warisan. "
            "Gunakan Bun untuk tooling berkecepatan tinggi, script otomasi CLI, atau aplikasi yang sensitif terhadap cold start di lingkungan serverless. "
            "Gunakan Deno saat keamanan sandbox dan kepatuhan standar web native menjadi prioritas utama arsitekturmu."
        ),
        "why_vibecoding_matters": (
            "AI sering mencampuradukkan sintaks modul antara Node.js lawas (require / module.exports) dengan standar modern ESM (import / export) "
            "di dalam file yang sama, menghasilkan SyntaxError saat aplikasi dijalankan di runtime modern. "
            "Saat vibecoding, instruksikan AI: 'Gunakan standar ES Modules murni (package.json type: module) "
            "yang kompatibel dengan Node.js LTS modern dan TypeScript tanpa sintaks require lama.'"
        ),
        "reflection_questions": [
            {
                "question": "Bagaimana model keamanan Deno membedakannya dari Node.js dalam mengeksekusi library pihak ketiga?",
                "answer": "Secara default Deno mengunci akses ke file sistem, jaringan internet, dan environment variables; library pihak ketiga tidak bisa membaca disk lokal tanpa izin flag eksplisit dari pengguna saat menjalankan aplikasi."
            },
            {
                "question": "Mengapa runtime engine Bun dapat menghasilkan waktu startup yang jauh lebih cepat daripada Node.js?",
                "answer": "Bun ditulis dalam bahasa sistem tingkat rendah Zig dan menggunakan JavaScriptCore (mesin Safari) yang dirancang untuk inisialisasi cepat, serta mengintegrasikan transpiler TypeScript native langsung di dalam core C++ engine-nya."
            }
        ]
    },

    "e-package-managers-overview": {
        "summary": "Perangkat lunak pengelola dependensi eksternal, registri publik, dan resolusi rantai pasok software.",
        "explanation_simple": (
            "Bayangkan toko aplikasi digital (seperti App Store atau Google Play) khusus untuk para programmer. "
            "Ketika kamu ingin menambahkan fitur pemindaian barcode atau grafik animasi ke kodemu, kamu tidak perlu mencari "
            "file zip acak di forum internet yang rawan virus. Kamu membuka terminal dan mengetik satu baris perintah instalasi. "
            "Manajer paket memeriksa apakah library tersebut aman, mengunduh versi yang cocok, dan menyimpannya di folder proyekmu.\n\n"
            "Package Manager adalah sistem logistik otomatis untuk menginstal, memperbarui, dan menghapus pustaka pihak ketiga. "
            "Batas analoginya: App Store mengunduh aplikasi jadi untuk pengguna akhir, sedangkan Package Manager "
            "mengunduh modul-modul komponen pembangun yang dirakit ke dalam kode aplikasi sumbermu."
        ),
        "problem_context": (
            "Di awal tahun 2000-an, menginstal library pihak ketiga membutuhkan proses manual yang melelahkan: "
            "mengunduh file zip, mengekstrak file header, menyalin file .dll atau .so ke direktori sistem, dan mengatur PATH environment. "
            "Jika library tersebut membutuhkan tiga library lain, kamu harus mengulangi proses manual itu berulang-ulang. "
            "Ketiadaan Package Manager resmi membuat kolaborasi proyek open source berskala global menjadi sangat lambat dan rapuh."
        ),
        "explanation_technical": (
            "Package Manager modern beroperasi di atas arsitektur ekosistem: "
            "1. Central Registry: Repositori publik terkelola (npm untuk JS, pub.dev untuk Dart/Flutter, PyPI untuk Python, Crates.io untuk Rust). "
            "2. Manifest File: File deklarasi dependensi tingkat tinggi yang dikelola developer (package.json, pubspec.yaml, requirements.txt). "
            "3. Lockfile: Snapshot deterministik pohon dependensi (pubspec.lock, package-lock.json, poetry.lock, pnpm-lock.yaml) "
            "yang mencatat cryptographic integrity hash (SHA-512) dari setiap paket untuk mencegah manipulasi transmisi.\n\n"
            "Evolusi arsitektur penyimpanan lokal: "
            "- npm tradisional: menduplikasi node_modules di setiap proyek (boros disk gigabyte). "
            "- pnpm: menggunakan Global Content-Addressable Store dan Hard Links / Symlinks, sehingga library yang sama hanya disimpan satu kali di seluruh harddisk komputer. "
            "- pub (Dart): menggunakan sistem cache terpusat di direktori home pengguna dengan referensi symlink otomatis."
        ),
        "misconceptions": [
            {
                "misconception": "Tanda caret (^) dan tilde (~) di file deklarasi dependensi tidak memiliki perbedaan teknis.",
                "explanation": "Caret ^1.2.3 mengizinkan pembaruan minor dan patch (< 2.0.0); tilde ~1.2.3 hanya mengizinkan pembaruan patch bugfix (< 1.3.0); salah memasang tanda bisa meloloskan breaking change secara tak sengaja.",
                "spot_in_code": "Bingung mengapa library terupdate otomatis saat menjalankan npm install ulang."
            },
            {
                "misconception": "Semua paket yang ada di registry resmi (npm/PyPI) sudah diaudit dan dijamin 100% aman oleh pengelola platform.",
                "explanation": "Registry publik terbuka untuk siapa saja; serangan Typosquatting (meniru nama paket populer) dan akun developer yang dibajak sering menyisipkan malware pencuri crypto ke dalam paket publik.",
                "spot_in_code": "Salah ketik nama paket dan menginstal modul berbahaya buatan peretas."
            }
        ],
        "when_to_use": (
            "Gunakan pnpm sebagai alternatif npm untuk menghemat puluhan gigabyte kapasitas SSD dan mempercepat proses instalasi dependensi. "
            "Gunakan flutter pub untuk mengelola plugin mobile native yang membutuhkan integrasi Gradle (Android) dan CocoaPods (iOS). "
            "Jalankan command audit keamanan dependensi secara rutin di CI/CD pipeline."
        ),
        "why_vibecoding_matters": (
            "AI sering mengusulkan nama paket yang salah ketik (hallucinated package name) yang ternyata tidak ada di pub.dev atau npm. "
            "Jika kamu asal instal, kamu berisiko menjadi korban serangan Typosquatting dari paket berbahaya yang sengaja didaftarkan penyerang. "
            "Saat vibecoding, verifikasi nama paket di situs resmi registry terlebih dahulu sebelum menjalankan perintah instalasi."
        ),
        "reflection_questions": [
            {
                "question": "Bagaimana pnpm berhasil menghemat ruang disk dibandingkan npm v6 tradisional?",
                "answer": "pnpm menyimpan semua versi paket di satu lokasi global terpusat di disk dan membuat Hard Link ke folder proyek, sehingga paket yang dipakai di 10 proyek hanya memakan ruang disk satu kali."
            },
            {
                "question": "Apa bahaya dari serangan 'Dependency Confusion' pada perusahaan besar yang menggunakan paket internal pribadi?",
                "answer": "Penyerang mendaftarkan nama paket internal perusahaan yang sama di registry publik dengan nomor versi lebih tinggi, menipu package manager untuk mengunduh paket peretas dari internet alih-alih paket internal perusahaan."
            }
        ]
    },

    "e-build-tools-overview": {
        "summary": "Otomatisasi rantai build, bundling aset, transpiler, minifikasi, dan module bundler modern.",
        "explanation_simple": (
            "Bayangkan dapur restoran koki bintang lima yang sedang bersiap menghadapi jam makan malam. "
            "Asisten koki tidak memotong bawang satu per satu saat pesanan masuk. "
            "Sebelum restoran buka, mesin otomatis mengiris 10 kg bawang, mencampur kaldu dasar, memeras bumbu ke botol saus siap tuang, "
            "dan menyusun semua bahan di meja racik koki dalam urutan yang tepat. "
            "Ketika pesanan masuk, hidangan dapat disajikan dalam waktu 3 menit.\n\n"
            "Build Tools (Alat Pembangun) adalah kru dapur otomatis proyekmu: mereka mengompilasi TypeScript menjadi JavaScript, "
            "mengompresi ukuran gambar, memangkas CSS yang tidak terpakai, dan menggabungkan puluhan file modul menjadi satu bundel web yang ringan dan cepat. "
            "Batas analoginya: bumbu dapur fisik basi jika disimpan lama, sedangkan build tools software "
            "menggunakan sistem Cache pintar yang hanya memproses ulang file yang benar-benar kamu ubah."
        ),
        "problem_context": (
            "Browser web di masa lalu hanya memahami HTML, CSS murni, dan JavaScript ES5 jadul. "
            "Ketika developer ingin menulis kode dengan fitur modern (TypeScript, JSX/React, Sass, ES Modules), "
            "browser tidak dapat membacanya secara langsung. Selain itu, memuat 500 file modul terpisah melalui jaringan HTTP/1.1 "
            "membuat situs web membutuhkan waktu 30 detik untuk terbuka. "
            "Build Tools diciptakan untuk mentranspilasi sintaks modern dan membundel aset agar ramah untuk browser pengguna."
        ),
        "explanation_technical": (
            "Evolusi ekosistem Build Tools & Module Bundlers: "
            "1. Era Task Runners (Gulp, Grunt): Menjalankan tugas otomasi imperatif (salin file, kompres gambar, gabung string). "
            "2. Era Classic Bundlers (Webpack, Rollup): Membangun Dependency Graph menyeluruh dari entry point, "
            "menggunakan Loaders dan Plugins untuk mengubah semua aset (bahkan CSS dan font) menjadi modul JavaScript. Sangat kuat dan fleksibel, tetapi lambat pada proyek raksasa. "
            "3. Era Modern Next-Gen Bundlers (Vite, esbuild, Turbopack, SWC): Ditulis dalam bahasa sistem kencang (Go, Rust). "
            "Vite memanfaatkan Native ES Modules di browser saat mode development (tanpa bundling di awal, startup instan dalam 50 milidetik!) "
            "dan menggunakan Rollup/esbuild saat memproduksi build rilis akhir.\n\n"
            "Teknik optimasi build: Minification (menghapus spasi dan memperpendek nama variabel), Tree Shaking (memangkas dead code), "
            "dan Code Splitting (memecah bundel menjadi potongan chunk dinamis yang hanya diunduh saat halamannya dibuka)."
        ),
        "misconceptions": [
            {
                "misconception": "Semua build tools modern membutuhkan file konfigurasi ratusan baris yang rumit seperti Webpack lama.",
                "explanation": "Alat generasi baru seperti Vite dan Bun menganut filosofi Zero-Configuration by Default; kamu bisa langsung membuild proyek TypeScript/React modern tanpa menulis satu baris pun file konfigurasi khusus.",
                "spot_in_code": "Menolak beralih ke tooling modern karena trauma dengan kerumitan webpack.config.js masa lalu."
            },
            {
                "misconception": "Code Splitting terjadi secara otomatis tanpa perlu dirancang oleh programmer.",
                "explanation": "Code Splitting membutuhkan programmer menggunakan sintaks dynamic import() pada rute halaman (misal React.lazy() atau router dynamic imports) agar bundler tahu di mana batas pemisahan chunk filenya.",
                "spot_in_code": "Mengimpor seluruh halaman admin raksasa secara statis di file navigasi utama aplikasi publik."
            }
        ],
        "when_to_use": (
            "Gunakan Vite sebagai build tool default standar untuk semua proyek web frontend modern (React, Vue, Svelte, Vanilla TS). "
            "Gunakan Rollup saat membangun open-source library yang membutuhkan output multi-format (ESM, CJS, UMD). "
            "Terapkan dynamic imports untuk memecah halaman-halaman berat aplikasi web ke dalam chunk terpisah."
        ),
        "why_vibecoding_matters": (
            "AI sering menyarankan plugin webpack atau loader usang yang sudah ditinggalkan sejak 5 tahun lalu "
            "ketika kamu bertanya cara menangani file CSS atau aset gambar. "
            "Saat vibecoding, arahkan AI ke standar modern: 'Gunakan Vite dengan konfigurasi minimalis berbasis standard ES Modules dan esbuild; "
            "jangan gunakan konfigurasi Webpack usang.'"
        ),
        "reflection_questions": [
            {
                "question": "Bagaimana Vite dapat memulai server development lokal dalam 50 milidetik pada proyek yang memiliki ribuan modul?",
                "answer": "Vite tidak membundel seluruh kode di awal; ia menyerahkan resolusi modul ke fitur Native ESM bawaan browser dan hanya mentranspilasi modul individual secara on-demand saat browser memintanya."
            },
            {
                "question": "Apa yang dimaksud dengan optimasi 'Tree Shaking' dalam proses bundling kode produksi?",
                "answer": "Proses static analysis yang memindai pohon dependensi import/export dan membuang fungsi atau class yang diekspor tetapi tidak pernah dipanggil oleh bagian manapun di aplikasi."
            }
        ]
    },

    "e-frameworks-overview": {
        "summary": "Fondasi struktural perangkat lunak yang menetapkan arsitektur kontrol dan pola desain aplikasi.",
        "explanation_simple": (
            "Bayangkan membeli rumah tipe perumahan klaster siap huni. Rangka tiang beton penopang rumah, denah kamar tidur, "
            "instalasi pipa air bawah tanah, dan jalur kabel listrik sudah dipasang kokoh oleh developer perumahan. "
            "Kamu tidak boleh sembarangan merobohkan tiang beton utama rumah, tetapi kamu bebas mengecat dinding dengan warna kesukaanmu, "
            "memilih sofa ruang tamu, dan memasang gorden jendela sesuai seleramu.\n\n"
            "Framework (Kerangka Kerja) adalah rumah siap huni bagi aplikasimu. "
            "Ia menyediakan arsitektur fondasi yang sudah jadi sehingga kamu tidak perlu merancang sistem navigasi atau penanganan HTTP dari nol. "
            "Batas analoginya: rumah fisik tidak bisa dipindahkan, sedangkan framework software dipilih di awal proyek "
            "dan mengikat pola pikir seluruh tim developer selama siklus hidup aplikasi tersebut."
        ),
        "problem_context": (
            "Ketika 10 orang programmer membangun satu aplikasi besar tanpa framework, setiap programmer akan membuat gaya arsitekturnya sendiri: "
            "developer A membuat sistem routing URL versinya sendiri, developer B membuat sistem koneksi database versinya sendiri. "
            "Kode menjadi sangat berantakan, tidak konsisten, dan jika developer A resign, tidak ada yang bisa membaca kodenya. "
            "Framework diciptakan untuk menegakkan konvensi arsitektur terstandarisasi (Convention over Configuration) "
            "sehingga siapa pun yang menguasai framework tersebut dapat langsung produktif bekerja."
        ),
        "explanation_technical": (
            "Perbedaan mendasar paling esensial antara Framework dan Library terletak pada Inversion of Control (IoC - Hollywood Principle): "
            "- Library: KODEMU yang memanggil KODE LIBRARY. Kamu memegang kendali penuh atas alur eksekusi aplikasi. "
            "- Framework: KODE FRAMEWORK yang memanggil KODEMU. Framework memegang kendali siklus hidup utama (Lifecycle); "
            "kamu hanya menaruh potongan kodemu di dalam slot-slot method callback yang disediakan oleh framework.\n\n"
            "Peta Framework di Industri: "
            "1. Frontend Web & Mobile: Flutter (declarative reactive UI canvas), React (komponen deklaratif), Next.js (full-stack SSR web), Vue / Nuxt, Angular (enterprise monolitik bertipe ketat). "
            "2. Backend Server: Express/NestJS (TypeScript modular terstruktur), Django/FastAPI (Python cepat & kaya fitur), Spring Boot (Java enterprise industri keuangan), Ruby on Rails (pelopor konvensi kilat)."
        ),
        "misconceptions": [
            {
                "misconception": "React adalah sebuah framework web lengkap seperti Angular atau Flutter.",
                "explanation": "Secara teknis resmi, React murni hanyalah sebuah Library antarmuka pengguna (View Library); ia membutuhkan library tambahan untuk routing, state management, dan build tools (atau menggunakan meta-framework seperti Next.js).",
                "spot_in_code": "Bingung mengapa create-react-app kosong tidak menyertakan sistem routing halaman bawaan."
            },
            {
                "misconception": "Menguasai satu framework berarti kamu sudah tidak perlu lagi mempelajari dasar bahasa pemrogramannya.",
                "explanation": "Developer yang hanya tahu framework tanpa paham fondasi bahasa (misal tahu Flutter tanpa paham Dart, atau tahu React tanpa paham JavaScript murni) akan lumpuh total saat menghadapi bug performa atau memory leak internal.",
                "spot_in_code": "Tidak mengerti cara kerja event loop JavaScript saat menghadapi bug async di React."
            }
        ],
        "when_to_use": (
            "Gunakan Framework komprehensif (seperti Flutter atau Next.js) saat membangun produk komersial yang membutuhkan kecepatan peluncuran fitur dan standar tim yang seragam. "
            "Patuhi konvensi dan pola siklus hidup (Lifecycle methods) resmi yang ditetapkan oleh dokumentasi framework. "
            "Hindari melawan pola alami framework (don't fight the framework) dengan membuat trik hacky di luar alur resmi."
        ),
        "why_vibecoding_matters": (
            "AI sering kali mencampuradukkan pola antar-framework (misalnya menyarankan manipulasi DOM document.getElementById() di dalam widget Flutter atau komponen React deklaratif). "
            "Hal ini merusak siklus rendering framework dan memicu bug UI yang tidak sinkron. "
            "Saat vibecoding, tegaskan paradigma: 'Tulis solusi ini sepenuhnya menggunakan pendekatan deklaratif dan idiomatik "
            "sesuai best practice resmi dari framework ini.'"
        ),
        "reflection_questions": [
            {
                "question": "Apa yang dimaksud dengan 'Hollywood Principle' (Don't call us, we'll call you) dalam arsitektur Framework?",
                "answer": "Prinsip Inversion of Control di mana alur kontrol utama dipegang oleh framework: framework yang menentukan kapan memanggil fungsi event, lifecycle, dan render milik developer, bukan sebaliknya."
            },
            {
                "question": "Mengapa pemahaman 'Convention over Configuration' pada framework mempercepat produktivitas tim?",
                "answer": "Karena framework sudah menetapkan keputusan arsitektur standar (lokasi folder, penamaan rute, koneksi database), sehingga developer tidak perlu membuang waktu memperdebatkan dan mengonfigurasi hal-hal mendasar dari nol."
            }
        ]
    },

    "e-libraries-overview": {
        "summary": "Kumpulan fungsi dan modul spesifik yang dapat dipanggil untuk menyelesaikan tugas komputasi terisolasi.",
        "explanation_simple": (
            "Bayangkan kamu sedang memasak di dapur rumahmu sendiri. Dapurmu adalah milikmu sepenuhnya: "
            "kamu yang memutuskan kapan menyalakan kompor dan menu apa yang ingin kamu masak hari ini (kamu memegang kendali). "
            "Ketika kamu membutuhkan bumbu penyedap instan atau saus tomat, kamu mengambil toples saus dari rak bumbu, "
            "menuangkannya dua sendok ke dalam wajanmu, lalu mengembalikan toples ke rak. "
            "Toples bumbu tersebut tidak mengatur caramu memasak; ia hanyalah bahan pembantu yang kamu panggil saat dibutuhkan.\n\n"
            "Library (Pustaka) adalah alat pembantu spesifik dalam kodemu. "
            "Batas analoginya: bumbu dapur habis setelah dipakai, sedangkan fungsi library komputer "
            "dapat dipanggil jutaan kali untuk memproses data tanpa pernah habis."
        ),
        "problem_context": (
            "Menghitung algoritma matematika rumit (seperti kalkulasi jarak dua koordinat GPS di permukaan bumi bundar), "
            "mengompresi data ke format zip, atau memanipulasi format tanggal lintas zona waktu dunia adalah tugas yang sangat rumit dan penuh jebakan edge-case. "
            "Jika setiap programmer harus menulis algoritma enkripsi SHA-256 atau parsing format gambar PNG sendiri, "
            "akan ada jutaan bug keamanan dan pemborosan waktu rekayasa di seluruh dunia. Library diciptakan sebagai unit solusi pakai-ulang terstandarisasi."
        ),
        "explanation_technical": (
            "Library adalah kumpulan kode terkontrol yang menyediakan API spesifik tanpa mengambil alih alur kendali eksekusi program. "
            "Kategori library populer di industri: "
            "1. Utility & Data Manipulation: Lodash (JS), RxDart/RxJS (Reactive Streams), date-fns/intl (internasionalisasi waktu). "
            "2. Networking & HTTP Clients: Dio / http (Dart), Axios (JS), Requests (Python). "
            "3. Visualisasi & UI Components: D3.js / Chart.js (grafik visual), Lucide / FontAwesome (ikonografi), Tailwind utilities. "
            "4. Math & Science: NumPy / SciPy (vektor numerik Python), Decimal/BigInt (presisi finansial bebas floating point rounding error).\n\n"
            "Kriteria evaluasi kualitas library sebelum diadopsi: "
            "- Ukuran bundel (bundle weight): apakah menambah beban megabyte berlebihan? "
            "- Pemeliharaan & Komunitas: kapan commit terakhir dilakukan? Apakah isu keamanan segera diperbaiki? "
            "- Lisensi Open Source: apakah lisensi mengizinkan penggunaan komersial (MIT, Apache 2.0, BSD) atau menuntut keterbukaan kode (GPL)?"
        ),
        "misconceptions": [
            {
                "misconception": "Menggunakan library selalu lebih baik daripada menulis fungsi buatan sendiri 5 baris.",
                "explanation": "Memasang library eksternal untuk tugas sepele menambah dependensi rantai pasok (supply chain risk) dan beban maintenance; jika masalah bisa diselesaikan dengan 3 baris fungsi standar bawaan bahasa, buatlah sendiri.",
                "spot_in_code": "Memasang package npm eksternal hanya untuk mengecek apakah sebuah string kosong."
            },
            {
                "misconception": "Semua lisensi open source mengizinkan kamu menjual software tanpa syarat apapun.",
                "explanation": "Lisensi Copyleft seperti GPL v3 mewajibkan seluruh software turunanmu dibuka kode sumbernya secara gratis ke publik; selalu periksa lisensi (pilih MIT atau Apache 2.0 untuk produk komersial tertutup).",
                "spot_in_code": "Memasukkan library berlisensi AGPL ke dalam backend tertutup perusahaan perbankan."
            }
        ],
        "when_to_use": (
            "Gunakan library untuk masalah teknis yang rumit, membutuhkan akurasi tinggi, dan bukan merupakan keunggulan kompetitif inti bisnismu (misal kriptografi, parsing CSV, validasi kartu kredit). "
            "Periksa lisensi library sebelum memasukkannya ke dalam proyek komersial. "
            "Bungkus pemanggilan library pihak ketiga di balik interface/adapter internal agar mudah diganti jika library tersebut usang di masa depan."
        ),
        "why_vibecoding_matters": (
            "AI gemar menyarankan library-library acak yang populer di masa lalu tetapi sudah tidak dirawat lagi oleh pembuatnya (deprecated). "
            "Saat vibecoding, verifikasi rekomendasi library AI: 'Berapa ukuran library ini, apa lisensi open sourcenya, "
            "dan apakah tugas ini sebenarnya bisa diselesaikan dengan API standar bawaan bahasa tanpa library eksternal?'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa membungkus library pihak ketiga di balik Adapter Pattern internal merupakan praktek arsitektur yang bijak?",
                "answer": "Agar kode inti aplikasimu tidak terikat langsung pada sintaks library pihak ketiga; jika suatu saat library tersebut ditinggalkan atau bermasalah, kamu hanya perlu mengganti kode di dalam adapter tanpa merombak ratusan file aplikasi."
            },
            {
                "question": "Apa perbedaan esensial antara lisensi software MIT dan GPL (General Public License)?",
                "answer": "Lisensi MIT mengizinkan kode digunakan, dimodifikasi, dan dijual kembali secara tertutup (permissive), sedangkan GPL mewajibkan karya turunan tetap berlisensi terbuka dan membagikan kode sumbernya (copyleft)."
            }
        ]
    },

    "e-orm-overview": {
        "summary": "Pemetaan objek relasional (Object-Relational Mapping) dan lapisan abstraksi database query builder.",
        "explanation_simple": (
            "Bayangkan dua orang yang bekerja sama tetapi berbicara dalam bahasa yang sangat berbeda: "
            "satu adalah Insinyur Pemrograman yang hanya berbicara dalam konsep Objek dan Class (bahasa Dart/TypeScript), "
            "dan yang satu lagi adalah Petugas Arsip Baja yang hanya berbicara dalam bahasa Tabel, Baris, dan Kolom SQL. "
            "Daripada sang insinyur harus selalu belajar kosakata SQL kuno setiap kali ingin menyimpan satu data objek User, "
            "mereka mempekerjakan seorang Penerjemah Pribadi bernama ORM.\n\n"
            "ORM (Object-Relational Mapping) menerjemahkan objek di memori kode menjadi baris data di tabel database secara otomatis. "
            "Batas analoginya: penerjemah manusia bisa memahami nuansa kontekstual, sedangkan ORM komputer "
            "dapat menghasilkan query SQL yang sangat boros dan lambat di balik layar jika programmer tidak memahami cara kerjanya."
        ),
        "problem_context": (
            "Menulis query SQL mentah manual di setiap fungsi backend menimbulkan fenomena 'Object-Relational Impedance Mismatch': "
            "kode aplikasi berpikir dalam hierarki objek, relasi pointer, dan polimorfisme; sedangkan database berpikir dalam tabel datar 2 dimensi dan relasi foreign key. "
            "Developer menghabiskan 40% waktunya hanya untuk menulis boilerplate pemetaan: membaca kolom result['user_email'], mengonversi tipe data, "
            "dan menyusun string SQL panjang yang rawan kesalahan pengetikan dan celah SQL Injection. ORM diciptakan untuk mengotomatisasi pemetaan ini."
        ),
        "explanation_technical": (
            "ORM memetakan Class ke Table, Objek Instance ke Row, dan Atribut ke Column. "
            "Dua pola arsitektur ORM utama: "
            "1. Active Record (Django ORM, Prisma, Ruby on Rails): Objek data membawa metode persistensi sendiri (misal: user = new User(); user.save();). Sederhana dan cepat untuk CRUD. "
            "2. Data Mapper (TypeORM, Hibernate, SQLAlchemy): Memisahkan entitas data murni dari logika penyimpanan repository (misal: userRepository.save(user)). "
            "Lebih bersih secara arsitektur dan mematuhi Single Responsibility Principle.\n\n"
            "Anatomi masalah klasik ORM: "
            "- N+1 Query Problem: Mengambil 100 data pesanan memicu 1 query untuk pesanan ditambah 100 query terpisah untuk mengambil nama pelanggan masing-masing! "
            "Mitigasi: Eager Loading (JOIN / include) alih-alih Lazy Loading. "
            "- Migrations: Pelacakan riwayat perubahan skema database secara berurutan dan terotomatisasi (schema migrations)."
        ),
        "misconceptions": [
            {
                "misconception": "Menggunakan ORM berarti developer tidak perlu lagi belajar dan mengerti bahasa SQL.",
                "explanation": "Ini adalah ilusi berbahaya; tanpa pemahaman SQL, developer tidak akan menyadari saat ORM menghasilkan query raksasa yang tidak terindeks atau memicu bencana N+1 query yang melumpuhkan performa server.",
                "spot_in_code": "Melakukan loop for pada list pesanan dan di dalam loop memanggil await order.getCustomer() (memicu N+1 query)."
            },
            {
                "misconception": "ORM selalu lebih lambat daripada query SQL mentah sehingga tidak boleh dipakai di sistem produksi.",
                "explanation": "Untuk 95% operasi CRUD standar, overhead ORM hanya beberapa mikrodetik yang tidak terasa oleh pengguna; kecepatan rilis dan keamanan anti-SQLi yang ditawarkan ORM jauh melampaui kerugian mikrodetik tersebut.",
                "spot_in_code": "Menulis query SQL mentah ratusan baris manual hanya untuk operasi baca profil sederhana demi alasan 'biar cepat'."
            }
        ],
        "when_to_use": (
            "Gunakan ORM atau Type-Safe Query Builder (seperti Prisma, Drift di Flutter/Dart, SQLAlchemy, Drizzle) untuk operasi transaksi bisnis standar dan manajemen migrasi skema otomatis. "
            "Gunakan Eager Loading (JOIN eksplisit) saat membaca data entitas yang memiliki relasi One-to-Many untuk mencegah N+1 query. "
            "Gunakan Raw SQL / Native Query hanya untuk laporan analitik agregasi yang sangat kompleks dan membutuhkan optimasi query planner khusus."
        ),
        "why_vibecoding_matters": (
            "AI gemar menggunakan ORM dengan pola pemanggilan relasi malas (Lazy Loading) di dalam perulangan loop, "
            "menciptakan bug N+1 query yang membuat server mengirimkan 1.000 query terpisah ke database hanya untuk menampilkan satu halaman daftar produk. "
            "Saat mereview kode ORM buatan AI, periksa: 'Apakah query ini sudah menggunakan eager loading (include/join) "
            "untuk mencegah N+1 query problem, dan apakah file migrasi skemanya sudah dibuat dengan benar?'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa 'N+1 Query Problem' menjadi penyebab utama kelambatan backend yang menggunakan ORM?",
                "answer": "Karena bukannya menjalankan satu query JOIN yang efisien, ORM mengeksekusi 1 query awal untuk mengambil daftar data lalu menjalankan N query tambahan terpisah untuk mengambil relasi setiap baris, membebani database dengan network round-trips masif."
            },
            {
                "question": "Apa fungsi dari sistem Database Migration yang disediakan oleh ORM?",
                "answer": "Mengelola versi perubahan skema tabel secara bertahap dan terprogram (seperti git untuk database), memungkinkan tim menyinkronkan struktur database di berbagai laptop developer dan server produksi secara aman tanpa kehilangan data."
            }
        ]
    },

    "e-frontend-overview": {
        "summary": "Arsitektur presentasi visual, interaksi pengguna berbasis antarmuka klien, dan ekosistem rekayasa web modern.",
        "explanation_simple": (
            "Bayangkan etalase toko roti dan meja resepsionis di lobi depan sebuah hotel berbintang. "
            "Tamu hotel (pengguna aplikasi) tidak pernah melihat dapur bawah tanah tempat adonan roti dipanggang atau ruang generator listrik gedung (backend server). "
            "Tamu hanya berinteraksi langsung dengan resepsionis yang tersenyum ramah, kartu kunci kamar digital, lampu lobi yang elegan, "
            "dan tombol lift yang menyala lembut saat disentuh. Resepsionis menerima pesanan tamu, memformat tampilan kamar, "
            "dan memberikan kenyamanan seketika tanpa ada jeda yang membingungkan.\n\n"
            "Frontend adalah wajah dan tubuh interaktif aplikasimu di browser web, layar ponsel, atau monitor desktop. "
            "Batas analoginya: dekorasi lobi fisik hotel bersifat statis, sedangkan frontend modern adalah aplikasi komputasi penuh "
            "yang mengelola state lokal, merender animasi 120 FPS, memvalidasi form masukan secara instan, dan menyinkronkan data jaringan secara reaktif."
        ),
        "problem_context": (
            "Di awal era World Wide Web (dekade 1990-an), setiap kali pengguna mengklik tombol atau tautan di halaman web, "
            "seluruh layar monitor berkedip putih kosong selama 3 detik selagi browser mengunduh dokumen HTML baru utuh dari server (Multi-Page Application / MPA). "
            "Interaksi terasa kaku seperti membaca brosur kertas elektronik. Pengguna modern menuntut pengalaman digital yang mulus, responsif, "
            "dan secepat aplikasi desktop tanpa kedipan layar, melahirkan arsitektur Single Page Application (SPA) dan Component-Driven Development."
        ),
        "explanation_technical": (
            "Arsitektur Frontend Modern berputar di sekitar tiga pilar inti: "
            "1. Component-Based Architecture: Memecah antarmuka visual menjadi komponen-komponen independen terisolasi yang dapat digunakan kembali "
            "(Button, Card, Navbar, Modal). Komponen menerima Props (data masukan dari induk) dan mengelola internal State (data reaktif lokal). "
            "Arsitektur komponen modern menganut prinsip Aliran Data Satu Arah (One-Way Data Flow: props mengalir ke bawah dari induk ke anak, "
            "dan anak mengirimkan event ke atas untuk meminta perubahan state pada induk).\n\n"
            "2. Perbandingan Paradigma Alat Frontend Utama: "
            "- React: Menggunakan Declarative Virtual DOM; runtime membandingkan pohon virtual (Diffing Algorithm / Reconciliation) "
            "dan hanya mengupdate node DOM fisik yang berubah. Ekosistem terbesar di dunia, fleksibilitas tanpa batas, kurva belajar moderat. "
            "- Vue: Pendekatan progresif berbasis template HTML dengan sistem reaktivitas halus (fine-grained reactivity) berbasis JavaScript Proxy untuk pelacakan dependensi otomatis. "
            "Penting dipahami: reaktivitas Proxy adalah mekanisme deteksi perubahan state lokal, BUKAN aliran data dua arah yang liar; "
            "fitur v-model pada Vue hanyalah syntactic sugar untuk pasangan prop :modelValue dan event @update:modelValue yang tetap mematuhi prinsip one-way data flow. "
            "- Svelte: Menghilangkan Virtual DOM sepenuhnya! Bekerja sebagai Compiler saat build-time yang menghasilkan kode manipulasi DOM vanilla murni "
            "berukuran mini tanpa runtime overhead; performa reaktif instan. "
            "- Flutter (Web & Multiplatform): Mengabaikan DOM HTML tradisional sepenuhnya; merender setiap piksel langsung ke kanvas grafis (CanvasKit/Skia/Impeller) "
            "untuk konsistensi visual 100% identik di web, Android, iOS, dan desktop.\n\n"
            "3. Paradigma Rendering Kontemporer: "
            "- CSR (Client-Side Rendering): Browser mengunduh bundel JS kosong lalu merender seluruh UI di perangkat pengguna (rawan SEO dan initial load lambat). "
            "- SSR (Server-Side Rendering via Next.js/Nuxt): Server merender HTML siap saji di setiap request untuk SEO prima dan First Contentful Paint cepat. "
            "- SSG (Static Site Generation): Halaman HTML dikompilasi saat build time untuk kecepatan CDN kilat."
        ),
        "misconceptions": [
            {
                "misconception": "Sistem reaktivitas otomatis (seperti Proxy pada Vue) berarti data mengalir bebas dua arah antara komponen induk dan anak.",
                "explanation": "Reaktivitas Proxy bertugas mendeteksi perubahan state lokal untuk memperbarui DOM fisik; aliran data antar-komponen tetap menganut One-Way Data Flow (props turun dari induk ke anak, event naik dari anak ke induk). Aliran data dua arah tanpa kendali adalah anti-pattern yang dihindari oleh framework modern.",
                "spot_in_code": "Mengira v-model di Vue adalah two-way binding mutlak tanpa event, padahal hanyalah singkatan dari prop :modelValue dan event @update:modelValue."
            },
            {
                "misconception": "State dan Props adalah istilah yang sama untuk data di komponen UI.",
                "explanation": "Props adalah data konfigurasi yang dioper dari komponen induk ke anak dan bersifat read-only (immutable bagi anak); State adalah data internal komponen yang dapat dimutasi dan memicu render ulang saat nilainya berubah.",
                "spot_in_code": "Mencoba memodifikasi props secara langsung di dalam komponen anak (props.count = 5)."
            },
            {
                "misconception": "Virtual DOM selalu lebih cepat daripada manipulasi DOM langsung di semua situasi.",
                "explanation": "Virtual DOM membutuhkan alokasi memori untuk pohon objek virtual dan komputasi diffing; framework berbasis compiler seperti Svelte membuktikan bahwa manipulasi DOM langsung yang terarah tanpa vDOM sering kali lebih hemat memori dan lebih kencang.",
                "spot_in_code": "Mengira React pasti lebih kencang daripada vanilla JS untuk animasi DOM sederhana."
            }
        ],
        "when_to_use": (
            "Gunakan React / Next.js saat membangun aplikasi web skala besar dengan ekosistem library kaya dan kebutuhan SEO tinggi melalui SSR/SSG. "
            "Gunakan Svelte atau Vue untuk dashboard atau aplikasi interaktif yang memprioritaskan kesederhanaan sintaks, ukuran unduhan kecil, dan kecepatan rendering. "
            "Gunakan Flutter saat kamu membutuhkan satu codebase tunggal yang berjalan mulus dengan UI identik di Mobile (iOS/Android), Web, dan Desktop."
        ),
        "why_vibecoding_matters": (
            "AI gemar menulis komponen frontend yang menggabungkan logika pengambilan data API, state management, dan styling visual ke dalam satu file raksasa 500 baris. "
            "Hal ini memicu re-render liar di mana seluruh halaman berkedip dan melambat setiap kali pengguna mengetik satu huruf di form input. "
            "Saat vibecoding, tegaskan arsitektur: 'Pecah halaman ini menjadi komponen-komponen kecil yang reusable, "
            "pisahkan logika bisnis dan pemanggilan API ke custom hooks / state management terpisah, dan optimalkan komponen agar tidak re-render berlebihan!'"
        ),
        "reflection_questions": [
            {
                "question": "Apa perbedaan utama antara Client-Side Rendering (CSR) dan Server-Side Rendering (SSR) dari sudut pandang SEO dan performa awal?",
                "answer": "CSR mengirimkan HTML kosong ke browser sehingga bot mesin pencari lambat mengindeks dan pengguna menunggu bundel JS selesai diunduh, sedangkan SSR mengirimkan HTML lengkap yang sudah terisi konten dari server sehingga langsung terbaca oleh mesin pencari dan pengguna."
            },
            {
                "question": "Mengapa fenomena 'Prop Drilling' dianggap sebagai bau kode (code smell) pada aplikasi frontend skala menengah ke atas?",
                "answer": "Karena meneruskan data props melintasi 5 lapis komponen perantara yang sebenarnya tidak membutuhkan data tersebut membuat struktur komponen terikat kaku dan sangat menyulitkan proses refactoring."
            }
        ]
    },

    "e-backend-overview": {
        "summary": "Arsitektur sisi server, pemrosesan logika bisnis, transaksi database, dan keamanan data terpusat.",
        "explanation_simple": (
            "Bayangkan dapur restoran bintang lima yang berada di balik pintu tertutup lobi depan. "
            "Di dapur inilah kompor gas berkobar, koki memotong daging berkualitas, bumbu rahasia diracik sesuai resep warisan, "
            "dan manajer gudang mengunci lemari bahan baku dingin agar stok makanan tidak dicuri atau terkontaminasi. "
            "Pelayan di depan hanya membawa tiket pesanan ke dapur dan membawa hidangan jadi ke meja tamu.\n\n"
            "Backend adalah dapur komputasi server yang mengolah logika rahasia, memproses transaksi uang, "
            "dan mengamankan database dari jangkauan publik. "
            "Batas analoginya: dapur fisik hanya bisa melayani tamu di ruangan restoran tersebut, sedangkan backend server modern "
            "dapat melayani jutaan aplikasi mobile dan web dari seluruh penjuru bumi secara serentak melalui protokol jaringan cloud."
        ),
        "problem_context": (
            "Jika seluruh logika aplikasi diletakkan di sisi frontend (di browser atau HP pengguna), pengguna nakal dapat membuka "
            "Developer Tools, mengubah harga barang di form dari Rp 500.000 menjadi Rp 1, dan mengirimkan pesanan palsu tersebut. "
            "Perangkat klien tidak pernah bisa dipercaya (Untrusted Environment). "
            "Backend diciptakan sebagai Single Source of Truth (sumber kebenaran tunggal) yang memiliki kendali mutlak atas aturan bisnis, "
            "keamanan transaksi, dan integritas penyimpanan data."
        ),
        "explanation_technical": (
            "Komponen arsitektur backend standar: "
            "1. Web Server & Reverse Proxy (Nginx, Caddy, Envoy): Menangani terminasi SSL/TLS, kompresi gzip/brotli, proteksi DDoS, "
            "dan penyeimbangan beban trafik (Load Balancing) ke beberapa instance aplikasi. "
            "2. Application Server: Menjalankan runtime kode bisnismu (Node.js/Express/Nest, Python/FastAPI, Go/Gin, Java/Spring). "
            "Bertanggung jawab atas routing request, autentikasi JWT/Session, validasi skema payload masukan, eksekusi aturan bisnis, "
            "dan orkestrasi pemanggilan database.\n\n"
            "3. Database & Caching: Relational Database (PostgreSQL) untuk integritas ACID, dipadukan dengan In-Memory Cache (Redis) "
            "untuk mengurangi beban query baca yang berulang. "
            "4. Background Task Workers & Message Queues: Memproses pekerjaan lambat (pengiriman email, pembuatan laporan PDF, kompresi video) "
            "secara asinkron di luar siklus request-response HTTP menggunakan antrean pesan (RabbitMQ, Redis Celery/BullMQ, Kafka)."
        ),
        "misconceptions": [
            {
                "misconception": "Backend yang baik cukup mengandalkan validasi yang sudah dilakukan oleh tim frontend di form input.",
                "explanation": "Validasi frontend hanyalah kenyamanan visual untuk pengguna; penyerang dapat mem-bypass seluruh frontend dengan mengirimkan HTTP request langsung via terminal cURL atau Postman; backend WAJIB memvalidasi ulang setiap byte masukan.",
                "spot_in_code": "Tidak memvalidasi format email dan panjang password di controller backend karena 'sudah divalidasi di React'."
            },
            {
                "misconception": "Pekerjaan lambat seperti mengirim email selamat datang boleh ditunggu langsung di dalam handler HTTP request.",
                "explanation": "Menunggu operasi jaringan pihak ketiga (seperti SMTP email) di dalam handler request membuat waktu tunggu pengguna melonjak dari 50 milidetik menjadi 3 detik dan menghabiskan alokasi thread server; delegasikan ke background worker queue.",
                "spot_in_code": "await kirimEmailSelamatDatang(user.email); sebelum mengembalikan return res.status(201)."
            }
        ],
        "when_to_use": (
            "Gunakan backend server terpusat untuk setiap aplikasi yang melibatkan data pengguna bersama, autentikasi kredensial, "
            "transaksi pembayaran finansial, atau algoritma bisnis yang dirahasiakan dari publik. "
            "Terapkan background queue worker untuk semua tugas yang membutuhkan waktu pemrosesan lebih dari 200 milidetik. "
            "Pasang Reverse Proxy (seperti Nginx) di depan application server untuk menangani SSL dan static caching."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis backend endpoint yang rentan terhadap masalah konkurensi (Race Conditions) saat memproses stok atau saldo "
            "(misal membaca saldo di memori, menguranginya di JavaScript, lalu menyimpannya kembali ke database tanpa locking atau atomic update). "
            "Saat vibecoding, instruksikan AI: 'Pastikan operasi saldo atau stok ini menggunakan Atomic Database Update "
            "(seperti UPDATE accounts SET balance = balance - 100 WHERE balance >= 100) atau transaksi dengan row-level locking!'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa operasi pemotongan saldo atau stok barang tidak boleh dilakukan dengan kalkulasi di memori aplikasi (Read-Modify-Write di kode)?",
                "answer": "Karena jika dua request datang bersamaan pada mikrodetik yang sama, keduanya akan membaca nilai saldo awal yang sama sebelum sempat menyimpan perubahan, mengakibatkan salah satu transaksi menimpa transaksi lain (Lost Update anomaly)."
            },
            {
                "question": "Apa peran Reverse Proxy (seperti Nginx) di depan application server Node.js atau Python?",
                "answer": "Meringankan beban application server dengan menangani enkripsi SSL/TLS, melayani file statis berkecepatan tinggi, melindungi dari serangan DoS, dan membagi beban trafik (load balancing) ke beberapa instance aplikasi."
            }
        ]
    }
}
