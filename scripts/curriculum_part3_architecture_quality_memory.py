"""Enrichment Part 3: Architecture, Quality, Memory, and Async (Topics 20 - 29).
Includes Benchmark 3 (f-async).
"""

CURRICULUM_PART3 = {
    "f-design-patterns": {
        "summary": "Pola solusi arsitektural teruji untuk memecahkan persoalan desain perangkat lunak yang berulang.",
        "explanation_simple": (
            "Bayangkan seorang arsitek yang merancang gedung perkantoran modern. Arsitek tersebut tidak perlu menemukan kembali cara membuat "
            "tangga darurat, pintu geser otomatis, atau instalasi pipa air dari nol. Mereka menggunakan standar desain arsitektur yang sudah "
            "terbukti kokoh, aman, dan efisien selama puluhan tahun di ribuan bangunan lain.\n\n"
            "Design Patterns (Pola Desain) adalah cetak biru solusi tingkat konseptual untuk masalah struktur kode yang sering dihadapi insinyur software. "
            "Batas analoginya: kamu tidak bisa sekadar menyalin fisik tangga darurat dan menempelkannya sembarangan di ruang tamu kecil rumah tinggal. "
            "Design pattern adalah pola pikir (mindset) dan strategi relasi antarkelas, bukan potongan kode kaku yang bisa di-copy-paste tanpa penyesuaian konteks."
        ),
        "problem_context": (
            "Ketika sistem software berkembang besar, kode yang awalnya sederhana mulai membelit: pembuatan objek baru tersebar di 50 file berbeda, "
            "satu perubahan format data mengharuskan pengubahan puluhan class, dan modul notifikasi terikat mati dengan modul transaksi. "
            "Sistem menjadi rapuh dan kaku terhadap perubahan. Pada tahun 1994, empat insinyur software (Gang of Four / GoF) mengkatalogkan "
            "23 pola desain teruji untuk membebaskan software dari belitan kopling ketat ini."
        ),
        "explanation_technical": (
            "Design Patterns GoF dikelompokkan ke dalam tiga rumpun besar: "
            "1. Creational Patterns (Penciptaan): mengisolasi mekanisme instansiasi objek agar sistem independen dari cara objek dibuat, dikomposisi, dan direpresentasikan. "
            "Contoh: Singleton (menjamin satu instance global), Factory Method (mendelegasikan instansiasi ke subclass), Builder (merakit objek kompleks bertahap). "
            "2. Structural Patterns (Struktur): menyusun class dan objek menjadi struktur yang lebih besar namun tetap fleksibel. "
            "Contoh: Adapter (menjembatani antarmuka tak kompatibel), Decorator (menambah tanggung jawab dinamis tanpa inheritance), Facade (menyediakan antarmuka ringkas ke subsistem kompleks). "
            "3. Behavioral Patterns (Perilaku): mengatur komunikasi, algoritma, dan pembagian tanggung jawab antar-objek. "
            "Contoh: Observer (mekanisme pub/sub event), Strategy (menukar algoritma runtime), Command (mengenkapsulasi permintaan aksi).\n\n"
            "Pola modern menekankan Inversion of Control (IoC) dan Dependency Injection (DI) untuk memutus ketergantungan langsung antar-kelas layanan."
        ),
        "misconceptions": [
            {
                "misconception": "Semakin banyak design pattern yang dimasukkan ke dalam proyek, semakin hebat arsitektur kodenya.",
                "explanation": "Penyalahgunaan pattern (Patternitis / Over-engineering) menciptakan lapisan abstraksi berlebihan yang membuat kode sederhana menjadi berbelit-belit dan sulit didebug; gunakan pattern hanya saat ada masalah konkret.",
                "spot_in_code": "Menerapkan AbstractFactoryProviderStrategy hanya untuk mengonversi format teks huruf besar/kecil."
            },
            {
                "misconception": "Singleton Pattern adalah solusi terbaik untuk menyimpan state bersama di seluruh aplikasi.",
                "explanation": "Singleton sering kali menjadi anti-pattern terselubung (global variable berkedok class) yang mempersulit unit testing karena state globalnya tidak bisa diisolasi atau di-mock dengan mudah.",
                "spot_in_code": "Membuat SessionManager.getInstance() yang diakses langsung di dalam 30 widget UI."
            }
        ],
        "when_to_use": (
            "Gunakan Observer Pattern saat kamu merancang sistem reaktif (seperti event bus atau state management UI). "
            "Gunakan Strategy Pattern jika kamu memiliki beberapa variasi algoritma yang harus bisa ditukar saat runtime (misal berbagai opsi kalkulasi ongkos kirim). "
            "Gunakan Adapter saat menghubungkan library pihak ketiga ke domain kode internal aplikasimu."
        ),
        "why_vibecoding_matters": (
            "AI sering kali memaksakan penerapan Singleton atau Factory yang berlebihan pada modul-modul kecil karena pola tersebut dominan dalam data latihannya. "
            "Saat vibecoding, kritik arsitektur AI: 'Apakah penggunaan Factory Pattern di sini benar-benar diperlukan, ataukah cukup dengan fungsi biasa? "
            "Sederhanakan kode jika pola ini menambah lapisan boilerplate yang tidak memberikan fleksibilitas nyata.'"
        ),
        "reflection_questions": [
            {
                "question": "Bagaimana Adapter Pattern membantu mengisolasi sistem kita dari perubahan API library pihak ketiga?",
                "answer": "Adapter bertindak sebagai perantara yang menerjemahkan antarmuka library luar ke antarmuka internal kita; jika library luar diganti atau diupdate, kita hanya perlu memodifikasi adapter tanpa menyentuh kode bisnis utama."
            },
            {
                "question": "Kapan Strategy Pattern lebih disukai daripada percabangan switch-case yang panjang?",
                "answer": "Ketika variasi algoritma sering bertambah atau berubah; Strategy mematuhi Open/Closed Principle dengan membiarkan kita menambah strategi baru tanpa harus memodifikasi dan menguji ulang class konteks yang sudah ada."
            }
        ]
    },

    "f-software-architecture": {
        "summary": "Struktur fundamental tingkat tinggi perangkat lunak yang menetapkan batas modul dan aturan interaksi subsistem.",
        "explanation_simple": (
            "Bayangkan tata ruang kota metropolitan modern. Perencana kota memisahkan dengan tegas antara zona perumahan warga, "
            "zona industri pabrik pengolahan limbah, dan zona pusat perkantoran komersial. Pipa air bersih dan kabel listrik bawah tanah "
            "dihubungkan melalui koridor utilitas terstandarisasi. Pemisahan zonasi ini mencegah limbah pabrik mencemari air minum perumahan "
            "dan memastikan kota dapat berkembang tanpa kekacauan.\n\n"
            "Arsitektur Perangkat Lunak (Software Architecture) adalah penataan zonasi modul kode dalam skala besar. "
            "Batas analoginya: bangunan gedung di kota terikat tanah fisik permanen, sedangkan arsitektur software dapat dimigrasikan "
            "dari monolit ke microservices atau dari arsitektur berlapis ke event-driven seiring pertumbuhan skala organisasi dan bisnis."
        ),
        "problem_context": (
            "Tanpa batasan arsitektur yang jelas, seiring bertambahnya programmer dan fitur baru, proyek akan terjerumus ke dalam arsitektur "
            "'Big Ball of Mud'. Kode antarmuka visual (UI) langsung memanggil query SQL mentah ke database, perhitungan diskon bisnis "
            "tertanam di tombol klik frontend, dan modul pembayaran bergantung langsung pada format tampilan layar. "
            "Ketika tampilan aplikasi ingin diperbarui ke platform mobile, seluruh sistem runtuh karena logika bisnis tidak dapat dipisahkan dari tampilan."
        ),
        "explanation_technical": (
            "Arsitektur perangkat lunak memandu pembagian tanggung jawab subsistem (Separation of Concerns). Pola-pola arsitektur kanonikal meliputi: "
            "1. Layered Architecture (N-Tier): membagi sistem menjadi Presentation Layer, Business Logic Layer, Data Access Layer, dan Database. "
            "Aturan ketatnya: layer atas boleh memanggil layer di bawahnya, tetapi layer bawah dilarang mengetahui layer di atasnya. "
            "2. Clean Architecture / Hexagonal Architecture (Ports & Adapters): menempatkan Domain Entities dan Use Cases murni di pusat terdalam, "
            "sedangkan UI, Database, dan Framework eksternal diletakkan di lingkaran terluar. Aturan ketergantungan (Dependency Rule) mengharuskan panah "
            "dependensi kode hanya boleh mengarah ke dalam (ke arah domain murni yang bebas dari framework eksternal).\n\n"
            "3. Microservices vs Monolith: Monolith menyatukan seluruh subsistem dalam satu deployment unit tunggal (sederhana untuk tim kecil), "
            "sedangkan Microservices memecah domain bisnis menjadi layanan-layanan independen yang berkomunikasi melalui jaringan (REST/gRPC/Kafka) "
            "untuk mendukung skalabilitas tim besar dengan biaya kompleksitas operasional terdistribusi."
        ),
        "misconceptions": [
            {
                "misconception": "Microservices selalu lebih unggul daripada arsitektur Monolith untuk setiap startup atau proyek baru.",
                "explanation": "Microservices memperkenalkan latensi jaringan, konsistensi data terdistribusi (CAP Theorem), dan overhead DevOps yang masif; bagi produk baru dengan batas domain yang masih berubah-ubah, Modular Monolith jauh lebih efektif.",
                "spot_in_code": "Membagi sistem yang hanya memiliki 2 developer menjadi 8 repo microservices terpisah."
            },
            {
                "misconception": "Clean Architecture berarti membuat 5 file berbeda (Entity, DTO, RepositoryInterface, RepositoryImpl, UseCase) untuk setiap form input sederhana.",
                "explanation": "Terapkan Clean Architecture secara pragmatis sesuai kompleksitas domain; memaksakan semua boilerplate untuk operasi CRUD sepele menimbulkan kelelahan arsitektur tanpa nilai bisnis nyata.",
                "spot_in_code": "Membuat 6 layer mapper untuk membaca satu tabel konfigurasi statis."
            }
        ],
        "when_to_use": (
            "Gunakan Clean Architecture pada sistem inti bisnis (Core Domain) yang diperkirakan akan beroperasi jangka panjang dan butuh pengujian unit test tanpa database. "
            "Gunakan Layered Architecture konvensional untuk aplikasi berbasis CRUD yang alurnya lurus. "
            "Tegakkan pemisahan layer melalui pembagian direktori dan aturan linting arsitektur modul."
        ),
        "why_vibecoding_matters": (
            "AI yang diminta membuat fitur baru cenderung meletakkan panggilan jaringan HTTP atau query database langsung di dalam komponen UI atau controller. "
            "Hal ini melanggar pemisahan lapisan dan membuat kode tidak bisa diuji secara terisolasi. "
            "Saat vibecoding, instruksikan AI: 'Patuhi arsitektur berlapis: pisahkan Presentation (UI), Domain (Use Cases/Logika Bisnis), "
            "dan Data (Repository/API Client) ke modul terpisah dengan antarmuka yang bersih.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa dalam Clean Architecture ketergantungan kode hanya boleh mengarah ke dalam (menuju Core Domain)?",
                "answer": "Agar aturan bisnis inti tetap independen dari perubahan teknologi luar (seperti penggantian database, framework UI, atau library jaringan), sehingga domain dapat bertahan puluhan tahun tanpa terpengaruh vendor luar."
            },
            {
                "question": "Apa kompromi (trade-off) terbesar saat memutuskan memigrasikan sistem Monolith ke Microservices?",
                "answer": "Mendapatkan kemandirian deployment dan skalabilitas tim, namun harus membayar dengan kompleksitas jaringan terdistribusi, tantangan konsistensi transaksi (eventual consistency), dan beban pemantauan (observability) yang jauh lebih rumit."
            }
        ]
    },

    "f-error-handling": {
        "summary": "Strategi antisipasi, penangkapan, dan pemulihan kondisi abnormal selama eksekusi program.",
        "explanation_simple": (
            "Bayangkan pertunjukan akrobatik sirkus di udara. Meskipun para pemain akrobat sudah berlatih ribuan kali, "
            "pengelola sirkus selalu memasang jaring pengaman lentur di bawah ayunan tali. Jika seorang pemain terpeleset dari tali, "
            "mereka tidak jatuh menghantam lantai semen yang fatal, melainkan mendarat empuk di jaring, berdiri kembali, "
            "dan pertunjukan sirkus dapat dilanjutkan dengan aman.\n\n"
            "Penanganan Kesalahan (Error Handling) adalah jaring pengaman aplikasi komputermu. Ia mengantisipasi bahwa kegagalan "
            "(seperti koneksi internet putus, file tidak ditemukan, atau format kartu kredit salah) pasti akan terjadi di dunia nyata. "
            "Batas analogi jaring sirkus: jaring fisik hanya menangkap jatuhnya tubuh, sedangkan error handling dalam kode dapat "
            "menganalisis penyebab kecelakaan, mencatat diagnosis di buku log, dan mencoba kembali operasi yang gagal secara otomatis."
        ),
        "problem_context": (
            "Pada bahasa C lama sebelum mekanisme Exception diperkenalkan, fungsi mengindikasikan kegagalan dengan mengembalikan nilai integer khusus "
            "(misalnya mengembalikan -1 atau NULL). Masalah fatalnya: programmer sering malas atau lupa memeriksa nilai kembalian tersebut "
            "(misalnya tidak mengecek if (file == NULL)). Program melanjutkan eksekusi dengan pointer kosong, memicu crash mendadak (Segmentation Fault) "
            "atau merusak data pengguna secara diam-diam (silent corruption) tanpa ada peringatan."
        ),
        "explanation_technical": (
            "Strategi penanganan error modern terbagi menjadi dua paradigma dominan: "
            "1. Exception Mechanism (try-catch-finally): Ketika kondisi abnormal terjadi di titik manapun, instruksi throw membuat objek Exception "
            "dan meluncurkan proses Stack Unwinding: runtime menelusuri Call Stack ke atas untuk mencari blok catch yang cocok. "
            "Blok finally dijamin selalu dieksekusi untuk menutup sumber daya fisik (seperti menutup koneksi database atau file handle).\n\n"
            "2. Result Type / Railway Oriented Programming (Rust, Go, Kotlin, fp-dart): Menghindari exception untuk kesalahan yang dapat diantisipasi "
            "dengan mengembalikan tipe data serikat Result<Success, Failure> atau Either. Pendekatan ini memaksa programmer menangani kasus gagal "
            "secara eksplisit melalui pattern matching sebelum nilai sukses dapat diakses.\n\n"
            "Penting membedakan antara: "
            "- Recoverable Errors (misal: koneksi timeout, validasi form): harus ditangkap dan diberi umpan balik ramah ke pengguna. "
            "- Programmer Errors / Fatal Bugs (misal: out of bounds, null assertion failed): harus di-crash dini (Fail-Fast) agar bug segera diperbaiki."
        ),
        "misconceptions": [
            {
                "misconception": "Menelan error dengan blok catch kosong (catch (e) {}) adalah cara efektif agar aplikasi tidak pernah crash.",
                "explanation": "Blok catch kosong adalah dosa terbesar dalam error handling (Pokemon Exception Handling): ia menyembunyikan akar masalah, membuat data rusak secara diam-diam, dan membuat bug mustahil dilacak di lingkungan produksi.",
                "spot_in_code": "try { simpanDatabase(); } catch (e) { /* biarkan saja */ }."
            },
            {
                "misconception": "Gunakan Exception untuk mengendalikan alur logika percabangan normal program.",
                "explanation": "Membuat dan melempar Exception membutuhkan pembuatan stack trace yang sangat mahal secara CPU; jangan gunakan exception untuk alur reguler (misal gunakan periksa kondisi if userExists alih-alih melempar UserNotFoundException).",
                "spot_in_code": "Menggunakan try-catch untuk memeriksa apakah sebuah key ada di dalam map."
            }
        ],
        "when_to_use": (
            "Gunakan try-catch di sekitar operasi I/O eksternal (panggilan API jaringan, pembacaan file disk, parsing JSON). "
            "Gunakan Result/Either type pada lapisan logika bisnis inti untuk mendokumentasikan kegagalan bisnis secara eksplisit di tanda tangan fungsi. "
            "Selalu bersihkan sumber daya (resource cleanup) di blok finally atau gunakan sintaks otomatis (using di C#, with di Python)."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis blok catch yang hanya mencetak print(e) ke konsol tanpa memberikan penanganan state pemulihan ke pengguna, "
            "membuat layar aplikasi macet di indikator 'loading...' selamanya saat API offline. "
            "Saat vibecoding, perintahkan AI: 'Tambahkan penanganan error yang komprehensif: tangkap exception jaringan secara spesifik, "
            "tampilkan pesan error yang ramah kepada pengguna, sediakan tombol coba lagi (retry), dan log detail teknisnya ke error tracker.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa blok finally dijamin akan selalu dieksekusi meskipun di dalam blok try terjadi instruksi return?",
                "answer": "Karena runtime memprogram eksekusi finally sebagai instruksi pembersihan wajib sebelum stack frame pemanggilan fungsi benar-benar dilepas dari Call Stack."
            },
            {
                "question": "Apa keuntungan menggunakan tipe kembalian Result<Data, Error> dibandingkan melempar unchecked exceptions?",
                "answer": "Compiler dapat memaksa developer menangani kemungkinan gagal secara eksplisit pada saat kompilasi, menghilangkan risiko unhandled exception yang terlewat di runtime."
            }
        ]
    },

    "f-debugging": {
        "summary": "Metodologi ilmiah dan teknik forensik untuk mengidentifikasi, mereproduksi, dan memperbaiki cacat logika pada perangkat lunak.",
        "explanation_simple": (
            "Bayangkan seorang detektif forensik yang sedang menyelidiki tempat kejadian perkara. "
            "Detektif yang berpengalaman tidak menebak-nebak secara acak atau menuduh sembarang orang berdasarkan firasat semata. "
            "Mereka mengumpulkan bukti fisik sidik jari, memeriksa rekaman kamera CCTV detik demi detik, merekonstruksi urutan peristiwa "
            "secara kronologis, dan menguji hipotesis mereka sampai pelakunya terbukti secara meyakinkan.\n\n"
            "Debugging adalah proses investigasi ilmiah untuk menemukan 'siapa pelaku' yang menyebabkan program komputer bertingkah aneh. "
            "Batas analogi detektif: tempat kejadian perkara di dunia nyata tidak bisa diulang persis sama, sedangkan dalam software, "
            "kamu dapat menciptakan kembali kondisi bug secara berulang-ulang melalui tes reproduksi deterministik."
        ),
        "problem_context": (
            "Ketika bug terjadi di sistem produksi perbankan atau rumah sakit, programmer pemula sering panik dan mengubah-ubah baris kode "
            "secara serampangan dengan harapan bug hilang secara ajaib (Shotgun Debugging). "
            "Tindakan tanpa metode ilmiah ini hampir selalu melahirkan tiga bug baru yang lebih parah dan merusak integritas sistem. "
            "Disiplin debugging formal diciptakan untuk menyediakan metode sistematis dalam melacak bug ke akar penyebabnya (Root Cause)."
        ),
        "explanation_technical": (
            "Metodologi debugging ilmiah mengikuti siklus empat tahap: "
            "1. Reproduce: membuat langkah reproduksi minimal (Minimal Reproducible Example) yang konsisten memicu bug. "
            "2. Isolate: mempersempit ruang pencarian menggunakan teknik Binary Search debugging (misalnya git bisect) atau inspeksi Call Stack. "
            "3. Hypothesize & Verify: merumuskan hipotesis ilmiah ('Mengapa nilai variabel X menjadi null di baris 45?') dan membuktikannya menggunakan alat debugger. "
            "4. Fix & Test Regress: memperbaiki akar masalah dan menulis Automated Regression Test agar bug yang sama tidak pernah kambuh lagi.\n\n"
            "Alat debugging modern meliputi: "
            "- Breakpoints: menghentikan eksekusi program di baris tertentu untuk memeriksa status variabel memori secara interaktif. "
            "- Step Over, Step Into, Step Out: menavigasi instruksi eksekusi baris per baris. "
            "- Conditional Breakpoints: hanya menghentikan eksekusi jika kondisi tertentu terpenuhi (misal userId === '999'). "
            "- Memory Heap Profiler: melacak memory leak dan objek yang tidak dibersihkan oleh Garbage Collector."
        ),
        "misconceptions": [
            {
                "misconception": "Menambahkan console.log / print di 20 baris kode adalah cara debugging paling cepat dan canggih.",
                "explanation": "Print debugging lambat, mengotori codebase dengan log sampah, tidak bisa menginspeksi memori secara real-time, dan sering kali mengubah timing eksekusi program konkuren (Heisenbug).",
                "spot_in_code": "Memenuhi fungsi dengan print('masuk sini 1'); print('masuk sini 2');."
            },
            {
                "misconception": "Begitu bug berhenti muncul di layar pengujian, investigasi debugging selesai.",
                "explanation": "Sering kali bug 'hilang' hanya karena gejala luarnya tertutupi (masking), sementara korupsi data internal tetap terjadi; kamu wajib memahami mengapa kode perbaikan bekerja sebelum menutup tiket bug.",
                "spot_in_code": "Menambahkan pengecekan if (x != null) membungkus kode rusak tanpa mencari tahu mengapa x bisa bernilai null."
            }
        ],
        "when_to_use": (
            "Gunakan debugger IDE (VS Code / Android Studio) dengan breakpoints interaktif untuk menyelidiki alur logika yang kompleks atau rekursif. "
            "Gunakan logging terstruktur dengan level log (DEBUG, INFO, WARN, ERROR) untuk sistem backend yang berjalan di server remote. "
            "Selalu buat tes regresi otomatis (regression test) sebelum menandai perbaikan bug selesai."
        ),
        "why_vibecoding_matters": (
            "Saat terjadi bug, developer sering mem-paste pesan error ke AI dan langsung menerima solusi tambal sulam yang diberikan AI. "
            "AI sering kali hanya menambahkan blok try-catch kosong atau pengecekan null defensif yang menyamarkan bug asli. "
            "Saat vibecoding, instruksikan AI secara kritis: 'Analisis stack trace ini: apa akar penyebab (root cause) dari error ini? "
            "Tunjukkan di mana data pertama kali menjadi tidak valid sebelum baris yang meledak ini dieksekusi.'"
        ),
        "reflection_questions": [
            {
                "question": "Apa yang dimaksud dengan 'Heisenbug' dalam dunia debugging perangkat lunak?",
                "answer": "Bug yang menghilang atau berubah perilakunya ketika kamu mencoba memeriksanya (misalnya menambahkan perintah print memperlambat eksekusi sehingga race condition multithreading tidak lagi terpicu)."
            },
            {
                "question": "Mengapa membuat Minimal Reproducible Example (MRE) sangat krusial dalam proses perbaikan bug?",
                "answer": "Karena MRE menyingkirkan variabel pengganggu dari modul lain, membuktikan akar masalah dengan pasti, dan mempercepat waktu pengujian perbaikan hingga hitungan detik."
            }
        ]
    },

    "f-testing": {
        "summary": "Verifikasi otomatis kebenaran fungsional dan ketahanan kode melalui hierarki pengujian bertingkat.",
        "explanation_simple": (
            "Bayangkan pabrik perakitan mobil uji tabrak. Sebelum mobil diizinkan meluncur di jalan raya bersama pengemudi nyata, "
            "setiap komponen diuji bertahap: bilah rem diuji tekanannya di mesin lab mekanik (Unit Test), "
            "lalu rem dipasang bersama pedal dan roda untuk menguji apakah hidrolik bekerja terintegrasi (Integration Test), "
            "dan terakhir mobil utuh dinaiki boneka uji coba untuk menabrak dinding beton dalam simulasi kecelakaan nyata (End-to-End Test).\n\n"
            "Pengujian Otomatis (Testing) adalah jaminan keselamatan softwaremu. Ia memastikan bahwa fitur yang kamu buat hari ini "
            "tidak merusak sepuluh fitur lama yang kamu buat tiga bulan lalu (mencegah regresi). "
            "Batas analoginya: uji tabrak mobil menghancurkan mobil fisik yang mahal, sedangkan pengujian otomatis software "
            "dapat dijalankan ribuan kali dalam hitungan detik tanpa biaya fisik tambahan."
        ),
        "problem_context": (
            "Di tim software yang tidak memiliki tes otomatis, setiap kali ada perubahan kode sekecil apapun, "
            "para developer atau tim QA harus mengklik manual ratusan tombol di layar aplikasi untuk memastikan tidak ada fitur yang rusak. "
            "Pengujian manual ini sangat lambat, membosankan, rawan kelalaian manusia, dan membuat rilis software tertunda berminggu-minggu. "
            "Satu fitur checkout toko online rusak saat promo Midnight Sale dapat membakar jutaan transaksi dalam satu malam."
        ),
        "explanation_technical": (
            "Piramida Pengujian (Test Pyramid - Mike Cohn) membagi strategi pengujian menjadi tiga tingkatan: "
            "1. Unit Tests (Dasar piramida, porsi terbesar ~70%): Menguji fungsi atau class terkecil secara terisolasi tanpa database atau jaringan nyata. "
            "Eksekusi dalam hitungan milidetik, deterministik, dan murah. Menggunakan Test Doubles (Mocks, Stubs, Fakes) untuk mengisolasi dependensi eksternal. "
            "2. Integration Tests (Tengah piramida ~20%): Memverifikasi interaksi antarmodul atau integrasi kode dengan komponen nyata (seperti SQLite DB, file system, atau HTTP endpoints). "
            "3. End-to-End (E2E) / UI Tests (Puncak piramida ~10%): Menguji alur pengguna nyata dari sudut pandang browser/layar HP (misal: registrasi -> checkout -> terima email). "
            "Paling lambat, mahal, dan rawan flakiness (kegagalan semu).\n\n"
            "Pola penulisan tes terstandarisasi menggunakan pola AAA: "
            "- Arrange: menyiapkan data masukan dan mock. "
            "- Act: memanggil fungsi atau mengeksekusi operasi target. "
            "- Assert: memvalidasi bahwa hasil keluaran sesuai dengan ekspektasi matematis."
        ),
        "misconceptions": [
            {
                "misconception": "Code Coverage 100% menjamin aplikasi bebas dari segala jenis bug.",
                "explanation": "Coverage hanya mengukur baris kode mana yang tersentuh eksekusi saat tes berjalan; tes dengan coverage 100% tetap bisa tidak memiliki assertion yang memeriksa kasus batas (edge cases) yang sesungguhnya.",
                "spot_in_code": "Tes yang mengeksekusi fungsi tetapi tidak menuliskan assert(hasil == ekspektasi)."
            },
            {
                "misconception": "Menulis tes otomatis membuang-buang waktu dan memperlambat peluncuran produk startup.",
                "explanation": "Awalnya menulis tes butuh investasi waktu, namun tes otomatis memangkas 90% waktu debugging manual dan memberikan rasa percaya diri tinggi untuk melakukan refactoring dan penambahan fitur dengan cepat tanpa rasa takut.",
                "spot_in_code": "Menolak menulis unit test demi mengejar deadline, lalu menghabiskan dua minggu berikutnya memperbaiki bug regresi di produksi."
            }
        ],
        "when_to_use": (
            "Terapkan Test-Driven Development (TDD) atau tulis unit test bersamaan dengan implementasi logika bisnis inti (kalkulasi uang, autentikasi, algoritma). "
            "Jalankan seluruh rangkaian unit test secara otomatis di CI/CD pipeline pada setiap Pull Request. "
            "Gunakan E2E test hanya untuk alur transaksi paling kritis (smoke test login dan pembayaran utama)."
        ),
        "why_vibecoding_matters": (
            "Kelemahan terbesar vibecoding adalah kamu tidak membaca setiap baris kode yang dihasilkan AI. "
            "Satu-satunya cara aman untuk memastikan kode AI bekerja benar adalah dengan mewajibkan AI menuliskan Unit Test yang komprehensif. "
            "Saat vibecoding, beri prompt tegas: 'Tulis unit test yang mencakup: skenario sukses standar, kasus masukan kosong/null, "
            "kasus nilai batas ekstrem, dan kasus kegagalan jaringan. Jalankan tes tersebut dan pastikan semua lulus!'"
        ),
        "reflection_questions": [
            {
                "question": "Apa perbedaan peran antara Mock dan Stub dalam pembuatan unit test?",
                "answer": "Stub hanya menyediakan data jawaban palsu siap pakai untuk merespons panggilan selama tes, sedangkan Mock juga memverifikasi interaksi perilaku (apakah method tertentu benar-benar dipanggil dengan parameter yang tepat)."
            },
            {
                "question": "Mengapa tes E2E (End-to-End) sebaiknya memiliki porsi paling sedikit dalam piramida pengujian?",
                "answer": "Karena tes E2E sangat lambat dieksekusi, membutuhkan infrastruktur yang rumit, dan rentan terhadap flaky failures (gagal karena gangguan jaringan sesaat atau timing animasi UI alih-alih bug kode nyata)."
            }
        ]
    },

    "f-memory": {
        "summary": "Model pengorganisasian memori virtual, siklus hidup alokasi stack dan heap, serta manajemen sampah memori.",
        "explanation_simple": (
            "Bayangkan sebuah meja kerja di bengkel kayu. Di atas meja kerja yang dekat dengan tanganmu (Call Stack), "
            "kamu meletakkan alat-alat kecil yang sedang kamu pakai sekarang (obeng, penggaris). Begitu pekerjaan selesai, "
            "meja langsung dibersihkan dalam sekejap. Namun, balok-balok kayu besar dan lemari setengah jadi disimpan di gudang luas "
            "di belakang bengkel (Heap Memory). Barang di gudang bisa bertahan berhari-hari dan diakses kapan saja, "
            "tetapi kamu membutuhkan petugas kebersihan berkala (Garbage Collector) untuk menyapu potongan kayu sisa agar gudang tidak penuh sesak.\n\n"
            "Manajemen memori mengatur bagaimana program meminjam RAM dari sistem operasi dan mengembalikannya setelah selesai. "
            "Batas analogi bengkel: ruang RAM komputer menggunakan alamat virtual matematis yang dipetakan oleh kernel sistem operasi, "
            "sehingga program tidak pernah menyentuh keping RAM fisik secara sembarangan."
        ),
        "problem_context": (
            "Pada bahasa pemrograman manual seperti C dan C++, programmer wajib memesan memori dengan malloc() dan membebaskannya dengan free(). "
            "Jika programmer lupa memanggil free(), memori RAM akan terus terpakai hingga server kehabisan RAM dan crash (Memory Leak). "
            "Sebaliknya, jika programmer membebaskan memori terlalu cepat tetapi masih mencoba mengaksesnya, terjadi celah keamanan fatal "
            "(Dangling Pointer / Use-After-Free) yang menjadi sumber dari 70% kerentanan keamanan perangkat lunak di dunia."
        ),
        "explanation_technical": (
            "Sistem operasi modern menyediakan Virtual Address Space untuk setiap proses terisolasi. Arsitektur memori program terbagi menjadi: "
            "1. Text/Code Segment: instruksi biner mesin yang read-only. "
            "2. Data & BSS Segment: variabel global dan statis. "
            "3. Call Stack: struktur LIFO super cepat untuk alokasi stack frames fungsi, variabel lokal primitif, dan return addresses. "
            "Alokasi dan dealokasi stack hanya menggeser Stack Pointer register CPU (SP).\n\n"
            "4. Heap Memory: area memori dinamis untuk objek berukuran fleksibel yang dialokasikan runtime. "
            "Bahasa modern (Dart, JavaScript, Python, Go, Java) menggunakan Automatic Garbage Collection (GC). "
            "Algoritma GC umum adalah Tracing GC (Mark-and-Sweep dan Generational GC): GC menelusuri objek yang masih dapat dijangkau "
            "dari GC Roots (stack variables, global references). Objek yang tidak lagi memiliki rantai referensi dari roots ditandai sebagai sampah dan dibebaskan. "
            "Generational GC membagi heap menjadi Young Generation (objek baru yang sering mati muda) dan Old Generation untuk meminimalkan durasi jeda GC (stop-the-world pause)."
        ),
        "misconceptions": [
            {
                "misconception": "Bahasa dengan Garbage Collection (seperti Dart, Python, JavaScript) mustahil mengalami Memory Leak.",
                "explanation": "Memory leak tetap sering terjadi jika objek yang sudah tidak terpakai masih tersangkut pada referensi yang hidup (misalnya disimpan di dalam List statis global atau listener yang lupa di-unsubscribe).",
                "spot_in_code": "Menambahkan callback ke event listener global tanpa pernah menghapusnya saat widget/halaman dihancurkan."
            },
            {
                "misconception": "Variabel pointer memegang alamat fisik RAM perangkat keras secara langsung.",
                "explanation": "Pointer pada sistem operasi modern memegang alamat memori virtual program yang dipetakan oleh Memory Management Unit (MMU) prosesor ke halaman RAM fisik; program pengguna diisolasi dari akses hardware langsung demi keamanan.",
                "spot_in_code": "Mengira mencetak alamat pointer 0x7ffd... berarti melihat lokasi keping silikon RAM fisik."
            }
        ],
        "when_to_use": (
            "Pahami siklus hidup alokasi memori saat merancang aplikasi mobile atau game yang membutuhkan FPS 60/120 yang mulus tanpa stutter. "
            "Hindari alokasi objek sementara di dalam loop render berkecepatan tinggi agar tidak memicu GC thrashing (GC bekerja terlalu sering). "
            "Selalu bersihkan listener, stream subscriptions, dan controllers di method dispose() komponen."
        ),
        "why_vibecoding_matters": (
            "AI gemar membuat stream subscription atau timer berkala tanpa melengkapinya dengan method pembatalan (cancellation/dispose). "
            "Aplikasi yang dibuat dengan vibecoding mungkin tampak lancar di awal, tetapi setelah berpindah halaman 10 kali, "
            "HP pengguna mulai terasa panas dan baterai cepat habis karena puluhan objek tertinggal di memori. "
            "Saat vibecoding, selalu tanyakan: 'Di mana kode pembersihan (dispose/cleanup) untuk controller, timer, atau listener ini agar tidak terjadi memory leak?'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Generational Garbage Collection memisahkan memori heap menjadi Young Generation dan Old Generation?",
                "answer": "Berdasarkan Hipotesis Lemah Generasional: mayoritas objek baru mati sesaat setelah dibuat; memeriksa dan membersihkan area Young Generation yang kecil jauh lebih cepat daripada memindai seluruh heap memori."
            },
            {
                "question": "Apa perbedaan mendasar antara alokasi memori di Stack vs Heap dari sudut pandang performa CPU?",
                "answer": "Stack hanya membutuhkan satu instruksi penggeseran pointer register CPU (sangat instan), sedangkan Heap membutuhkan algoritma pencarian blok memori kosong, sinkronisasi thread, dan pembersihan Garbage Collection berkala."
            }
        ]
    },

    "f-concurrency": {
        "summary": "Menjalankan beberapa jalur eksekusi tugas yang tumpang tindih dalam satuan waktu melalui threads, processes, atau coroutines.",
        "explanation_simple": (
            "Bayangkan dapur restoran yang sibuk. Jika hanya ada satu koki dan dapur hanya bisa mengerjakan satu hal sekali waktu, "
            "koki harus berdiri diam selama 20 menit menatap oven roti yang sedang memanggang sebelum boleh mulai memotong sayuran sup. "
            "Namun koki yang cerdas menerapkan konkurensi: ia memasukkan roti ke oven, menyetel alarm timer, lalu sambil menunggu oven berbunyi, "
            "ia memotong wortel. Jika restoran sangat kaya, mereka mempekerjakan empat koki sekaligus yang masing-masing memegang pisaunya sendiri di meja terpisah (Paralelisme murni).\n\n"
            "Konkurensi adalah tentang menstrukturkan program agar banyak hal dapat ditangani secara tumpang tindih. "
            "Batas analogi dapur: jika dua koki mencoba memotong wortel di talenan yang sama menggunakan pisau yang sama pada detik yang sama tanpa koordinasi, "
            "jari mereka akan terluka (Race Condition)."
        ),
        "problem_context": (
            "Ketika komputer berevolusi dari satu core prosesor menjadi multi-core (seperti prosesor HP modern yang memiliki 8 core), "
            "program yang hanya berjalan di satu thread tunggal hanya bisa memanfaatkan 12.5% dari total tenaga prosesor. "
            "Lebih parah lagi, ketika aplikasi melakukan operasi lambat (seperti mengunduh file besar dari internet), "
            "seluruh antarmuka layar membeku (ANR - Application Not Responding) jika operasi tersebut memblokir thread utama antarmuka pengguna."
        ),
        "explanation_technical": (
            "Perbedaan krusial yang wajib dipahami insinyur software: "
            "- Concurrency: berurusan dengan struktur (dealing with a lot of things at once) — mengelola banyak tugas yang bersaing dalam interval waktu yang sama. "
            "- Parallelism: berurusan dengan eksekusi fisik (doing a lot of things at once) — menjalankan tugas secara bersamaan pada core CPU perangkat keras yang berbeda.\n\n"
            "Model konkurensi meliputi: "
            "1. Multi-threading dengan Shared Memory: beberapa thread OS berbagi ruang memori heap yang sama. Rentan terhadap Race Conditions dan Deadlock. "
            "Membutuhkan primitif sinkronisasi seperti Mutex (Mutual Exclusion Locks), Semaphores, atau Atomic Operations. "
            "2. Message Passing / Actor Model (Erlang, Go Channels, Dart Isolates): setiap thread/worker memiliki memorinya sendiri yang terisolasi sepenuhnya. "
            "Komunikasi dilakukan murni melalui pengiriman pesan (Share memory by communicating, not communicate by sharing memory), mengeliminasi race condition memori."
        ),
        "misconceptions": [
            {
                "misconception": "Menambah jumlah thread sebanyak-banyaknya (misal 100 thread pada CPU 4 core) pasti membuat program makin cepat.",
                "explanation": "Terlalu banyak thread justru memperlambat sistem karena CPU menghabiskan sebagian besar waktunya melakukan Context Switching (menyimpan dan memuat register antar-thread) alih-alih melakukan komputasi nyata.",
                "spot_in_code": "Membuat thread OS baru di setiap iterasi loop pemrosesan data."
            },
            {
                "misconception": "Konkurensi dan Paralelisme adalah istilah yang identik.",
                "explanation": "Konkurensi dapat berjalan di CPU single-core melalui time-slicing (interleaving); sedangkan paralelisme menuntut keberadaan beberapa core CPU fisik yang mengeksekusi instruksi pada siklus clock yang sama.",
                "spot_in_code": "Mengira kode asinkron di JavaScript/Node.js otomatis berjalan paralel di multi-core CPU."
            }
        ],
        "when_to_use": (
            "Gunakan background worker thread (seperti Dart Isolates, Web Workers, atau thread pool) untuk komputasi CPU-heavy yang berat (seperti kompresi video, enkripsi file besar, atau parsing JSON raksasa) agar UI tetap responsif 60 FPS. "
            "Gunakan model pesan terisolasi (Isolates/Workers) daripada shared-memory lock jika bahasamu mendukungnya untuk menghindari bug deadlock."
        ),
        "why_vibecoding_matters": (
            "Kode konkurensi yang dibuat AI sering kali mengandung bug race condition tersembunyi yang lolos pengujian developer "
            "karena bug tersebut hanya muncul sesekali di perangkat pengguna dengan timing tak terduga. "
            "Saat meminta AI membuat fitur konkurensi, tanyakan: 'Apakah ada data yang diakses atau dimodifikasi oleh beberapa thread secara bersamaan? "
            "Bagaimana cara kode ini menjamin thread-safety tanpa memicu risiko deadlock?'"
        ),
        "reflection_questions": [
            {
                "question": "Apa kondisi yang memicu terjadinya Deadlock pada pemrograman konkuren berbasis thread?",
                "answer": "Deadlock terjadi ketika Thread A memegang Lock 1 dan menunggu Lock 2, sementara pada saat yang sama Thread B memegang Lock 2 dan menunggu Lock 1, sehingga kedua thread terkunci selamanya saling menunggu."
            },
            {
                "question": "Mengapa Dart dan JavaScript memilih model Single-Threaded Event Loop untuk lingkungan antarmuka pengguna?",
                "answer": "Untuk mengeliminasi kompleksitas penguncian memori (locks/mutex) pada komponen UI, sehingga rendering dan manipulasi state antarmuka dapat berjalan deterministik tanpa risiko race condition."
            }
        ]
    },

    "f-async": {
        "summary": "Mengelola tugas tertunda seperti operasi I/O dan koordinasi asinkron tanpa memblokir thread eksekusi utama.",
        "explanation_simple": (
            "Bayangkan memesan makanan cepat saji di kasir restoran modern. Setelah kamu memesan dan membayar burger, "
            "kasir tidak menyuruhmu berdiri diam mematung di depan meja kasir selama 15 menit menunggu burger dimasak. "
            "Kasir memberikanmu sebuah alat pager nirkabel kecil (buzzer) yang bisa kamu bawa ke meja makan. "
            "Kamu bebas duduk santai, membuka media sosial, atau mengobrol. Ketika burger selesai dimasak oleh tim dapur, "
            "pager bergetar dan berbunyi, menandakan kamu bisa berjalan mengambil nampan makananmu.\n\n"
            "Pemrograman Asinkron (Asynchronous Programming) bekerja seperti pager restoran tersebut. "
            "Alat pager adalah representasi dari objek Promise atau Future: janji bahwa hasil data akan tiba di masa depan. "
            "Batas analogi pager kafe: pager hanyalah pengingat pesanan fisik; dalam komputer, mekanisme asinkron dikoordinasikan "
            "oleh mesin bernama Event Loop yang memutar antrean pesan tugas saat thread utama sedang menganggur."
        ),
        "problem_context": (
            "Mengambil data dari server internet membutuhkan waktu 200 hingga 1.000 milidetik, waktu yang sangat lama bagi CPU modern "
            "yang dapat mengeksekusi 3 miliar siklus instruksi per detik. Jika fungsi pembacaan data jaringan bersifat Sinkron (Blocking), "
            "seluruh aplikasi akan macet total: animasi terhenti, sentuhan layar ponsel tidak direspon, dan sistem operasi menganggap aplikasi rusak (hang). "
            "Asynchronous programming diciptakan agar CPU dapat terus melayani animasi antarmuka dan interaksi pengguna selagi menunggu data jaringan tiba."
        ),
        "explanation_technical": (
            "Pemrograman asinkron pada runtime modern (seperti Dart Event Loop, Node.js libuv, Python asyncio) bertumpu pada arsitektur Event Loop non-blocking. "
            "Event Loop memantau dua antrean utama: Event Queue / Task Queue (berisi event I/O, timer, klik pengguna) dan Microtask Queue (tugas prioritas tinggi). "
            "Thread utama mengeksekusi kode sinkron di Call Stack hingga kosong, lalu Event Loop mengambil task berikutnya dari antrean untuk dieksekusi.\n\n"
            "Evolusi sintaks asinkron bergerak dari Callback (rawan Callback Hell / Piramida Kematian), ke objek Promise/Future "
            "(yang merepresentasikan tiga status: pending, fulfilled/resolved, rejected), hingga ke sintaksis modern async/await. "
            "Kata kunci await menangguhkan (suspend) eksekusi fungsi lokal saat itu dan mengembalikan kontrol ke Event Loop, lalu melanjutkan sisa fungsi tersebut "
            "setelah Future/Promise selesai.\n\n"
            "KOREKSI PENTING: Perintah koordinasi seperti Future.wait di Dart, Promise.all di JavaScript, atau asyncio.gather di Python "
            "berfungsi untuk mengoordinasikan beberapa pekerjaan asinkron agar dapat ditunggu secara serempak. "
            "Mekanisme ini TIDAK dengan sendirinya membuat pekerjaan komputasi CPU berjalan secara paralel di multi-core; "
            "operasi CPU-bound tetap membutuhkan thread/isolate terpisah untuk dapat dieksekusi secara paralel murni."
        ),
        "misconceptions": [
            {
                "misconception": "Menggunakan async/await otomatis membuat fungsi berjalan di background thread terpisah secara paralel.",
                "explanation": "async/await tidak membuat thread baru; ia hanya memanfaatkan penjadwalan non-blocking pada Event Loop di thread yang sama. Komputasi berat yang ditulis di dalam fungsi async tetap akan memblokir UI jika dijalankan di thread utama.",
                "spot_in_code": "Menaruh loop perhitungan matematika berat di dalam fungsi async void main() dan heran mengapa UI tetap macet."
            },
            {
                "misconception": "Future.wait atau Promise.all membagi komputasi ke core CPU yang berbeda.",
                "explanation": "Future.wait dan Promise.all hanya mengoordinasikan beberapa tugas I/O atau penantian asinkron secara konkurensi pada event loop tunggal; mereka tidak mendistribusikan beban kalkulasi ke multi-core CPU secara paralel.",
                "spot_in_code": "Memanggil Future.wait([hitungHash1(), hitungHash2()]) dengan harapan durasi CPU berkurang setengah di thread tunggal."
            },
            {
                "misconception": "Lupa menuliskan kata kunci await pada fungsi asinkron tidak berdampak apa-apa.",
                "explanation": "Lupa menuliskan await (Unawaited Future) membuat kode baris berikutnya dieksekusi sebelum data selesai dimuat, mengakibatkan variabel masih bernilai null atau race condition data yang sukar dilacak.",
                "spot_in_code": "user = fetchUser(); print(user.name); yang meledak karena user masih berupa objek Future."
            }
        ],
        "when_to_use": (
            "Gunakan async/await untuk setiap operasi yang melibatkan komunikasi jaringan (HTTP, WebSocket), pembacaan/penulisan basis data, file system, atau penundaan waktu (timer). "
            "Gunakan Future.wait / Promise.all untuk menjalankan beberapa permintaan I/O jaringan independen secara bersamaan (misal mengambil data profil dan data notifikasi secara paralel I/O). "
            "Jika kamu memiliki pekerjaan CPU-heavy (enkripsi, image processing), delegasikan ke Worker Thread atau Dart Isolate, jangan hanya dibungkus fungsi async biasa."
        ),
        "why_vibecoding_matters": (
            "AI sering lupa menyematkan kata kunci await di depan pemanggilan fungsi asinkron atau tidak menangani blok try-catch pada fungsi async, "
            "sehingga kegagalan jaringan menjadi Unhandled Promise Rejection yang mematikan proses server backend. "
            "Saat vibecoding, teliti setiap fungsi asinkron dan tanyakan ke AI: 'Pastikan semua pemanggilan Future/Promise menggunakan await yang tepat, "
            "apakah Future.wait menangani kegagalan salah satu request secara elegan, dan apakah komputasi berat di sini membutuhkan Isolate/Worker terpisah?'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Promise.all / Future.wait tidak otomatis membuat komputasi CPU berjalan paralel di multi-core hardware?",
                "answer": "Karena Promise.all dan Future.wait hanya mengoordinasikan penantian event I/O pada single-threaded event loop; untuk eksekusi paralel komputasi CPU murni, tugas harus dialokasikan ke thread/isolate sistem operasi yang berbeda."
            },
            {
                "question": "Apa yang terjadi di Call Stack dan Event Loop ketika eksekusi kode mencapai baris 'await fetchUserData()'?",
                "answer": "Fungsi saat itu ditangguhkan (paused), stack framenya disimpan, kontrol thread dikembalikan ke Event Loop untuk melayani tugas lain di antrean, dan sisa fungsi akan dijadwalkan kembali ke Call Stack setelah data jaringan tiba."
            }
        ]
    }
}
