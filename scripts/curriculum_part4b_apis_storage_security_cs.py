"""Enrichment Part 4B: APIs, Serialization, Databases, Security, DevOps, and CS Foundations (12 Topics).
Completes all 47 Fundamental Topics!
"""

CURRICULUM_PART4B = {
    "f-apis": {
        "summary": "Antarmuka kontrak komunikasi terstandarisasi yang menghubungkan sistem perangkat lunak independen.",
        "explanation_simple": (
            "Bayangkan colokan listrik dinding di rumahmu. Perusahaan listrik PLN tidak mengizinkanmu menyambungkan kabel tembaga telanjang "
            "langsung ke gardu trafo tegangan tinggi. Sebagai gantinya, mereka menyediakan stopkontak dua lubang berstandar 220 Volt di dinding kamar. "
            "Pabrikan pembuat kulkas, TV, dan charger laptop cukup membuat steker dua kaki yang cocok dengan stopkontak tersebut. "
            "Kulkasmu tidak perlu tahu apakah listrik PLN dibangkitkan dari tenaga surya, air, atau batubara; ia hanya butuh stopkontak yang bekerja.\n\n"
            "API (Application Programming Interface) adalah stopkontak resmi perangkat lunak. "
            "Batas analoginya: stopkontak listrik mengalirkan arus satu arah ke alatmu, sedangkan API modern "
            "adalah percakapan cerdas dua arah yang memvalidasi otorisasi, memfilter data, dan membatasi kuota panggilan (Rate Limiting)."
        ),
        "problem_context": (
            "Di masa lalu, jika aplikasi mobile ingin memesan ojek atau memproses pembayaran kartu kredit, "
            "perusahaan ojek harus memberikan akses langsung ke kode sumber internal database mereka kepada pihak luar. "
            "Hal ini menimbulkan bencana keamanan, risiko kebocoran data pengguna, dan merusak stabilitas server pusat. "
            "API diciptakan sebagai gerbang perantara resmi yang mengekspos fungsi yang diizinkan saja dengan kontrak data yang ketat."
        ),
        "explanation_technical": (
            "API mendefinisikan kontrak formal (Interface Contract) antara penyedia layanan (Provider) dan konsumen (Consumer). "
            "Paradigma arsitektur API modern mencakup: "
            "1. REST (Representational State Transfer): Berbasis resource URI (/users, /orders), menggunakan HTTP verbs semantik (GET, POST, PUT, DELETE), "
            "stateless, dan merespons dalam format JSON standar. "
            "2. GraphQL: Klien dapat menentukan dengan presisi field data apa saja yang dibutuhkan dalam satu query, mengeliminasi masalah over-fetching dan under-fetching. "
            "3. gRPC: Berbasis Remote Procedure Call (RPC) di atas HTTP/2 menggunakan biner Protocol Buffers (Protobuf) untuk komunikasi server-to-server berlatensi ultra-rendah.\n\n"
            "Mekanisme pelindung API meliputi: "
            "- Rate Limiting / Throttling (algoritma Token Bucket / Leaky Bucket) untuk mencegah serangan DoS. "
            "- API Versioning (URI /v1/ atau HTTP Header) untuk menjamin pembaruan backend tidak merusak aplikasi mobile klien versi lama."
        ),
        "misconceptions": [
            {
                "misconception": "API selalu berarti web service yang diakses melalui internet menggunakan HTTP.",
                "explanation": "Web API hanyalah salah satu bentuk API; library fungsi lokal (seperti Java SDK API, Win32 API, atau interface class internal) juga merupakan API karena menyediakan antarmuka kontrak pemanggilan.",
                "spot_in_code": "Mengira memanggil Math.sqrt() bukan interaksi dengan API."
            },
            {
                "misconception": "REST API mewajibkan respons selalu berbentuk JSON dan tidak boleh format lain.",
                "explanation": "Prinsip arsitektur REST bersifat bebas format (content negotiation); REST API sah mengembalikan XML, file PDF, gambar biner, atau teks polos via header Content-Type.",
                "spot_in_code": "Menganggap endpoint yang mengembalikan stream byte gambar bukan bagian dari RESTful API."
            }
        ],
        "when_to_use": (
            "Gunakan REST API untuk antarmuka publik atau integrasi pihak ketiga yang membutuhkan kesederhanaan dan kemudahan konsumsi oleh berbagai platform. "
            "Gunakan GraphQL jika aplikasi mobile frontend memiliki banyak layar dengan kebutuhan variasi data yang dinamis dan kompleks. "
            "Gunakan gRPC untuk komunikasi antarlayanan microservices internal yang membutuhkan performa dan efisiensi biner maksimum."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis kode konsumsi API yang mengabaikan kemungkinan respons error status (seperti 429 Too Many Requests atau 503 Maintenance). "
            "Akibatnya, saat kuota API gratisanmu habis di tengah jalan, aplikasi langsung crash tanpa pesan yang jelas. "
            "Saat vibecoding, beri prompt: 'Buatlah API Client yang tangguh: tangani status code 429 dengan exponential backoff retry, "
            "lakukan validasi skema data respons, dan tangani skenario koneksi timeout.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa API Versioning (seperti /api/v1/ vs /api/v2/) sangat penting bagi aplikasi mobile di Google Play / App Store?",
                "answer": "Karena pengguna tidak selalu langsung mengupdate aplikasi di ponsel mereka; versioning memastikan server dapat melayani aplikasi versi lama yang masih beredar tanpa merusak fitur."
            },
            {
                "question": "Apa masalah 'Over-fetching' pada REST API yang berhasil dipecahkan oleh GraphQL?",
                "answer": "Over-fetching terjadi saat endpoint REST mengembalikan seluruh data profil 50 field, padahal aplikasi mobile hanya membutuhkan nama dan foto avatar; GraphQL mengizinkan klien meminta 2 field itu saja."
            }
        ]
    },

    "f-serialization": {
        "summary": "Proses konversi struktur data objek di memori menjadi format byte atau teks linear untuk transmisi dan penyimpanan permanen.",
        "explanation_simple": (
            "Bayangkan kamu membeli lemari pakaian kayu besar dari toko furnitur online. "
            "Pihak toko tidak bisa mengirimkan lemari yang sudah terpasang utuh begitu saja ke dalam mobil kurir kecil karena ukurannya memakan tempat. "
            "Sebagai gantinya, toko membongkar lemari tersebut menjadi papan-papan kayu pipih berlabel rapi, "
            "memasukkannya ke dalam satu kardus datar (Serialisasi), lalu mengirimkannya melalui kurir. "
            "Begitu kardus tiba di kamar rumahmu, kamu membaca buku petunjuk dan merakit kembali papan-papan tersebut "
            "menjadi lemari pakaian utuh yang siap dipakai (Deserialisasi).\n\n"
            "Serialisasi mengubah objek memori kompleks menjadi aliran teks (JSON, YAML) atau biner (Protobuf) agar bisa dikirim melintasi kabel jaringan atau disimpan ke disk. "
            "Batas analoginya: papan kayu furnitur tidak bisa disusupi virus, sedangkan deserialisasi data teks asing dari internet "
            "bisa disusupi kode berbahaya (Deserialization Injection Attacks) jika tidak divalidasi dengan ketat."
        ),
        "problem_context": (
            "Sebuah objek User di dalam memori komputer berupa pohon pointer pointer heksadesimal yang tersebar di blok heap memory RAM. "
            "Alamat memori 0x7FFF tersebut hanya bermakna di dalam laptop pengembang pada detik itu. "
            "Jika kamu mencoba mengirimkan byte pointer mentah tersebut ke laptop temanmu atau ke server Linux di cloud, "
            "komputer penerima tidak akan mengerti apa-apa dan mengalami crash seketika. "
            "Serialisasi diciptakan untuk menerjemahkan data memori ke dalam format teks/biner universal yang dapat dipahami oleh mesin apapun di dunia."
        ),
        "explanation_technical": (
            "Serialisasi (Marshaling / Encoding) mengubah graph objek runtime menjadi deretan byte berurutan (linear stream). "
            "Deserialisasi (Unmarshaling / Decoding) membangun kembali instance objek runtime yang setara dari deretan byte tersebut.\n\n"
            "Format serialisasi populer terbagi menjadi: "
            "1. Human-Readable Text: "
            "- JSON (JavaScript Object Notation): standar emas API web; ringan, berbasis teks, tipe data sederhana (string, number, boolean, array, object, null). "
            "- YAML: ramah konfigurasi manusia (indentasi). "
            "2. Binary Formats (Mesin): Protocol Buffers (Protobuf), MessagePack, FlatBuffers. Menggunakan integer varint dan field tags biner "
            "untuk menghasilkan ukuran payload hingga 70% lebih kecil dan waktu parsing 10x lebih cepat daripada JSON.\n\n"
            "Keamanan deserialisasi adalah isu kritis: Deserialisasi objek secara polimorfik tanpa validasi skema ketat (seperti pickle di Python atau Java ObjectInputStream) "
            "memungkinkan penyerang menyisipkan muatan Remote Code Execution (RCE) yang mengeksekusi perintah shell berbahaya di server."
        ),
        "misconceptions": [
            {
                "misconception": "JSON secara native mendukung serialisasi tipe tanggal (Date), fungsi, dan set nilai unik (Set).",
                "explanation": "Spesifikasi JSON murni hanya mendukung string, number, boolean, array, object, dan null; Date harus diubah menjadi string format ISO-8601 atau timestamp integer.",
                "spot_in_code": "Kaget mendapati objek Date berubah menjadi string '2026-09-14T...' setelah JSON.stringify()."
            },
            {
                "misconception": "Modul pickle di Python aman digunakan untuk menerima data cache dari pengguna publik.",
                "explanation": "pickle dapat menjalankan instruksi Python arbitrer saat deserialisasi; jangan pernah melakukan pickle.loads() pada data yang berasal dari jaringan luar tanpa autentikasi kriptografi HMAC.",
                "spot_in_code": "Menerima payload HTTP lalu langsung memanggil pickle.loads(request.body)."
            }
        ],
        "when_to_use": (
            "Gunakan JSON untuk komunikasi API publik web dan antarmuka aplikasi mobile karena kemudahan inspeksi dan debugging. "
            "Gunakan Protocol Buffers (Protobuf) untuk sistem antarlayanan internal berkapasitas tinggi (microservices) atau game multiplayer yang sensitif kuota bandwidth. "
            "Selalu gunakan pustaka pemodelan yang menghasilkan serialisasi type-safe (seperti json_serializable di Dart atau Zod di TypeScript)."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis parsing JSON manual yang mengasumsikan semua field selalu ada (misal data['user']['profile']['avatar']), "
            "sehingga saat server mengembalikan null atau format field sedikit berbeda, seluruh halaman aplikasi meledak dengan TypeError / Null Check Operator error. "
            "Saat vibecoding, instruksikan AI: 'Gunakan model serialisasi type-safe yang memetakan JSON ke Data Class konkret "
            "dengan nilai default yang aman dan validasi skema untuk setiap field nullable.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa format biner seperti Protobuf jauh lebih efisien dalam ukuran data dibandingkan JSON?",
                "answer": "Protobuf tidak menyertakan nama string atribut berulang kali pada setiap record data (hanya menggunakan field tag integer 1-2 byte) dan mengompresi angka menggunakan encoding varint biner."
            },
            {
                "question": "Apa perbedaan utama antara serialization dan encryption?",
                "answer": "Serialisasi bertujuan mengubah bentuk data agar dapat ditransmisikan dan dipahami oleh sistem lain (tidak rahasia), sedangkan enkripsi bertujuan mengacak data agar tidak dapat dibaca oleh pihak yang tidak memiliki kunci rahasia."
            }
        ]
    },

    "f-databases": {
        "summary": "Sistem penyimpanan terkelola untuk persistensi, integritas, dan pengambilan data terstruktur dalam skala besar.",
        "explanation_simple": (
            "Bayangkan buku besar pencatatan kas di bank desa. Jika pencatatan uang nasabah hanya ditulis di secarik kertas catatan tempel, "
            "kertas tersebut bisa terbang tertiup angin, basah terkena kopi, atau salah dijumlahkan saat pembukuan akhir tahun. "
            "Oleh karena itu, bank menggunakan brankas pembukuan baja: setiap transaksi setoran dan penarikan dicatat permanen dengan tinta emas, "
            "memiliki nomor halaman urut, dan ditandatangani oleh dua teller resmi.\n\n"
            "Basis Data (Database) adalah brankas penyimpanan permanen aplikasi komputermu. "
            "Ia memastikan bahwa data pengguna (akun, pesanan, saldo) tetap tersimpan aman meskipun server mati listrik mendadak. "
            "Batas analogi buku kas: buku fisik hanya bisa dibaca satu orang dalam satu waktu, sedangkan sistem basis data modern "
            "dapat melayani puluhan ribu transaksi baca dan tulis secara bersamaan dalam hitungan milidetik."
        ),
        "problem_context": (
            "Menyimpan data aplikasi hanya dengan menulis file teks JSON atau CSV biasa di disk menimbulkan tiga bencana besar: "
            "1. Ketiadaan Transaksi: jika server mati di tengah proses transfer uang (uang pengirim sudah dipotong tetapi uang penerima belum ditambah), saldo hilang selamanya. "
            "2. Concurrency Conflict: jika dua pengguna membeli barang terakhir di toko secara bersamaan, kedua transaksi berhasil dan stok menjadi minus. "
            "3. Kecepatan: mencari satu pengguna di antara 10 juta baris file teks CSV memakan waktu berjam-jam. "
            "Database Management System (DBMS) diciptakan untuk menjamin integritas transaksi dan pencarian instan."
        ),
        "explanation_technical": (
            "Sistem basis data terbagi menjadi dua paradigma utama: "
            "1. Relational Databases (RDBMS: PostgreSQL, MySQL, SQLite): data disimpan dalam tabel bertaut dengan skema kaku, "
            "menjamin integritas referensial (Foreign Keys), dan menjunjung tinggi standar transaksi ACID: "
            "- Atomicity: seluruh langkah transaksi berhasil semua, atau dibatalkan total jika satu langkah gagal (Rollback). "
            "- Consistency: data selalu mematuhi semua aturan validasi dan relasi skema. "
            "- Isolation: transaksi konkuren yang berjalan paralel tidak saling mengintip data setengah jadi (Isolation Levels: Read Committed, Serializable). "
            "- Durability: data yang sudah di-commit dijamin selamat di disk permanen (via Write-Ahead Logging / WAL).\n\n"
            "2. NoSQL Databases (MongoDB, Redis, Cassandra): mengorbankan sebagian garansi ACID demi fleksibilitas skema horizontal "
            "(Document-store, Key-Value, Columnar, Graph), berfokus pada skalabilitas terdistribusi (Teorema CAP: Consistency vs Availability)."
        ),
        "misconceptions": [
            {
                "misconception": "NoSQL selalu lebih modern dan lebih cepat daripada Relational Database (SQL).",
                "explanation": "RDBMS modern seperti PostgreSQL sangat cepat, kaya fitur (mendukung JSONB terindeks), dan menjamin ACID; memilih NoSQL untuk data yang sarat relasi bisnis justru memaksa programmer menulis logika validasi manual yang rawan bug di aplikasi.",
                "spot_in_code": "Menggunakan MongoDB untuk aplikasi perbankan akuntansi yang sarat transaksi debit-kredit terikat."
            },
            {
                "misconception": "Database otomatis mengindeks semua kolom sehingga setiap query SELECT pasti berjalan cepat.",
                "explanation": "Database hanya mengindeks Primary Key secara default; kolom lain yang sering dicari (seperti email atau created_at) wajib dibuatkan Index secara eksplisit (B-Tree Index) agar tidak terjadi Full Table Scan.",
                "spot_in_code": "Query SELECT * FROM users WHERE email = ? yang memindai jutaan baris karena tidak ada index di kolom email."
            }
        ],
        "when_to_use": (
            "Gunakan Relational Database (PostgreSQL / SQLite) sebagai pilihan utama default untuk mayoritas produk bisnis yang membutuhkan integritas relasi dan konsistensi transaksi uang/data. "
            "Gunakan Key-Value Store (seperti Redis) untuk caching in-memory berkecepatan tinggi atau sesi login sementara. "
            "Gunakan SQLite untuk penyimpanan lokal di aplikasi mobile (Android/iOS) dan desktop."
        ),
        "why_vibecoding_matters": (
            "AI sering menyarankan pembaruan data tanpa transaksi (tanpa blok BEGIN TRANSACTION ... COMMIT), "
            "sehingga jika operasi kedua gagal, operasi pertama tetap tersimpan dan meninggalkan data 'yatim piatu' (corrupt state). "
            "Saat vibecoding modul database, perintahkan AI: 'Bungkus operasi multi-tabel ini dalam transaksi ACID: "
            "pastikan terjadi rollback otomatis jika ada operasi yang melempar exception, dan buat indeks pada kolom foreign key.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa prinsip 'Atomicity' pada transaksi ACID sangat vital dalam sistem transfer perbankan?",
                "answer": "Karena atomisitas menjamin operasi pemotongan saldo pengirim dan penambahan saldo penerima dieksekusi sebagai satu kesatuan tunggal: jika salah satu gagal, seluruh transaksi dibatalkan sehingga uang tidak hilang di udara."
            },
            {
                "question": "Bagaimana Write-Ahead Logging (WAL) menjamin prinsip 'Durability' pada SQLite atau PostgreSQL?",
                "answer": "Setiap perubahan ditulis terlebih dahulu ke file log sekuensial (WAL) sebelum diaplikasikan ke halaman database utama, sehingga jika listrik padam mendadak, transaksi yang telah di-commit dapat dipulihkan kembali saat startup."
            }
        ]
    },

    "f-sql": {
        "summary": "Bahasa deklaratif terstandarisasi untuk mendefinisikan, memanipulasi, dan meminta data dari basis data relasional.",
        "explanation_simple": (
            "Bayangkan kamu memesan hidangan prasmanan ke penyedia katering pesta. "
            "Kamu tidak perlu memberi tahu juru masak: 'Ambil pisau, iris bawang, nyalakan kompor gas suhu 150 derajat selama 12 menit'. "
            "Kamu cukup menyatakan apa yang kamu inginkan secara jelas: 'Tolong siapkan 100 porsi Rendang Sapi yang tidak pedus, "
            "urutkan pengantarannya mulai dari meja tamu VVIP'. Koki katering yang ahli akan memikirkan sendiri rute memasak dan bahan baku yang paling efisien.\n\n"
            "SQL (Structured Query Language) adalah bahasa deklaratif untuk berbicara dengan basis data. "
            "Kamu menyatakan DATA APA yang kamu inginkan, bukan BAGAIMANA LANGKAH MENCARINYA. "
            "Batas analoginya: katering pesta hanya memasak makanan, sedangkan mesin database modern "
            "memiliki Query Optimizer canggih yang menganalisis statistik tabel untuk memilih rute pencarian data tercepat."
        ),
        "problem_context": (
            "Sebelum ada SQL, programmer harus menulis kode imperatif yang rumit dengan membuka file pointer biner disk, "
            "melakukan perulangan loop baris per baris, dan memfilter data secara manual. "
            "Jika ada perubahan struktur kolom file, ribuan baris kode pencarian harus ditulis ulang. "
            "E.F. Codd memperkenalkan model relasional dan bahasa SQL pada tahun 1970-an untuk memisahkan logika query data manusia "
            "dari detail fisik penyimpanan perangkat keras komputer."
        ),
        "explanation_technical": (
            "Instruksi SQL dikategorikan menjadi sub-bahasa formal: "
            "1. DDL (Data Definition Language): mendefinisikan struktur skema (CREATE TABLE, ALTER TABLE, DROP, TRUNCATE). "
            "2. DML (Data Manipulation Language): memanipulasi data baris (INSERT, UPDATE, DELETE). "
            "3. DQL (Data Query Language): meminta data (SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT).\n\n"
            "Operasi relasi paling mendasar adalah JOIN untuk menggabungkan dua tabel berbasis kunci kecocokan: "
            "- INNER JOIN: mengembalikan baris yang memiliki kecocokan di kedua tabel. "
            "- LEFT JOIN: mengembalikan semua baris dari tabel kiri ditambah baris yang cocok dari tabel kanan (atau NULL jika tidak ada). "
            "- FULL OUTER JOIN: mengembalikan semua baris dari kedua belah pihak.\n\n"
            "Di balik layar, Database Query Planner mengubah teks query SQL menjadi pohon eksekusi relasional aljabar, "
            "memilih algoritma join optimal (Nested Loop, Hash Join, Merge Join) berdasarkan ketersediaan Indeks B-Tree."
        ),
        "misconceptions": [
            {
                "misconception": "Menggunakan string concatenation biasa (SELECT * FROM users WHERE name = '\" + input + \"') adalah cara normal membuat query dinamis.",
                "explanation": "Ini adalah celah keamanan nomor 1 di dunia web: SQL Injection; penyerang dapat menyisipkan string ' OR '1'='1 yang membobol seluruh database. Selalu gunakan Parameterized Queries / Prepared Statements.",
                "spot_in_code": "db.rawQuery(\"SELECT * FROM items WHERE id = \" + idInput);."
            },
            {
                "misconception": "Klausa WHERE dan HAVING adalah hal yang sama dan dapat saling bertukar posisi.",
                "explanation": "WHERE memfilter baris individual sebelum agregasi GROUP BY dihitung; HAVING memfilter hasil grup agregasi setelah GROUP BY dieksekusi.",
                "spot_in_code": "Menaruh kondisi agregat WHERE COUNT(id) > 5 alih-alih di dalam klausa HAVING."
            }
        ],
        "when_to_use": (
            "Gunakan Parameterized Queries / Prepared Statements secara mutlak tanpa pengecualian untuk setiap parameter input dari luar. "
            "Gunakan klausa EXPLAIN QUERY PLAN untuk memeriksa apakah query-mu memanfaatkan index atau melakukan Full Table Scan lambat. "
            "Hindari SELECT * pada query produksi; sebutkan hanya nama kolom yang benar-benar dibutuhkan untuk menghemat bandwidth I/O."
        ),
        "why_vibecoding_matters": (
            "AI yang diprompt cepat sering kali menyusun query mentah dengan penggabungan string (string interpolation) "
            "yang membuka celah SQL Injection fatal pada aplikasimu. "
            "Saat vibecoding, tegaskan standar keamanan: 'Gunakan parameter binding / prepared statements untuk query ini; "
            "jangan ada penggabungan string langsung ke sintaks SQL!'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Parameterized Query / Prepared Statement 100% kebal terhadap serangan SQL Injection?",
                "answer": "Karena database mengompilasi struktur sintaks query SQL terlebih dahulu sebelum menyisipkan parameter nilai pengguna murni sebagai data literal yang tidak akan pernah dieksekusi sebagai instruksi kode."
            },
            {
                "question": "Apa perbedaan hasil antara INNER JOIN dan LEFT JOIN ketika baris di tabel kanan tidak memiliki data yang cocok?",
                "answer": "INNER JOIN membuang baris tersebut dari hasil akhir, sedangkan LEFT JOIN tetap menampilkan baris tabel kiri dengan kolom tabel kanan diisi nilai NULL."
            }
        ]
    },

    "f-data-modeling": {
        "summary": "Perancangan skema relasi entitas, penegakan integritas data, dan normalisasi struktur basis data.",
        "explanation_simple": (
            "Bayangkan kamu sedang merancang denah arsitektur rumah bertingkat sebelum tukang bangunan meletakkan batu bata pertama. "
            "Kamu memutuskan kamar tidur berada di lantai dua, dapur di lantai satu dekat saluran pipa air, dan pintu garasi memiliki akses langsung ke jalan raya. "
            "Jika kamu salah merancang denah dan menaruh kamar mandi di tengah ruang tamu tanpa saluran pembuangan, "
            "membongkar dinding beton yang sudah kering setelah rumah jadi akan menelan biaya renovasi yang luar biasa mahal.\n\n"
            "Pemodelan Data (Data Modeling) adalah denah cetak biru struktur informasi bisnismu di dalam database. "
            "Batas analoginya: denah rumah menampung benda fisik, sedangkan pemodelan data mendefinisikan entitas abstrak "
            "(Pengguna, Pesanan, Produk, Pembayaran) dan aturan relasi keterikatan di antara mereka."
        ),
        "problem_context": (
            "Jika developer menyimpan data transaksi toko online dengan menggabungkan nama pelanggan, alamat rumah, nama produk, "
            "dan harga dalam satu tabel raksasa yang datar, timbul tiga anomali database yang mematikan: "
            "1. Insertion Anomaly: tidak bisa menambahkan produk baru sebelum ada pelanggan yang membelinya. "
            "2. Update Anomaly: jika pelanggan pindah alamat rumah, programmer harus memperbarui 100 baris riwayat pesanan lama; satu terlewat, data menjadi inkonsisten. "
            "3. Deletion Anomaly: menghapus riwayat pesanan terakhir seorang pelanggan ikut menghapus data master pelanggan tersebut dari sistem selamanya."
        ),
        "explanation_technical": (
            "Pemodelan data relasional menggunakan diagram Entity-Relationship (ERD) dan aturan Normalisasi (Normal Forms): "
            "- 1NF (First Normal Form): setiap kolom hanya berisi nilai tunggal atomik (tidak ada array bersarang atau koma ganda dalam satu sel). "
            "- 2NF: memenuhi 1NF dan seluruh atribut non-kunci bergantung penuh pada seluruh Primary Key (menghilangkan partial dependency). "
            "- 3NF: memenuhi 2NF dan tidak ada dependensi transitif (kolom non-kunci tidak boleh bergantung pada kolom non-kunci lainnya).\n\n"
            "Relasi entitas terbagi menjadi: "
            "1. One-to-One (1:1): satu pengguna memiliki satu kartu identitas KTP. "
            "2. One-to-Many (1:N): satu pengguna memiliki banyak pesanan belanjaan (Foreign Key diletakkan di sisi tabel pesanan). "
            "3. Many-to-Many (M:N): satu mahasiswa mengambil banyak mata kuliah, dan satu mata kuliah diikuti banyak mahasiswa "
            "(diwajibkan menggunakan Junction/Junction Table perantara dengan foreign keys komposit).\n\n"
            "Dalam arsitektur data warehouse analitik, teknik Denormalisasi (seperti Star Schema) sengaja diterapkan demi kecepatan baca aggregasi query analitik."
        ),
        "misconceptions": [
            {
                "misconception": "Relasi Many-to-Many bisa langsung dibuat dengan menyimpan daftar ID koma ('1,2,5') di dalam satu kolom teks biasa.",
                "explanation": "Menyimpan daftar ID terpisah koma melanggar 1NF, merusak Foreign Key constraint, membuat query pencarian lambat (tidak bisa menggunakan index B-Tree), dan sangat sulit diupdate.",
                "spot_in_code": "Kolom categories_ids VARCHAR(255) yang berisi string '1,4,9' di tabel produk."
            },
            {
                "misconception": "Normalisasi tingkat tertinggi (seperti 3NF) wajib diterapkan pada setiap tabel di semua jenis aplikasi.",
                "explanation": "Pada sistem analitik read-heavy (OLAP / Big Data), normalisasi berlebihan memaksa 10 join tabel yang sangat lambat; denormalisasi terkontrol sering kali sengaja dipilih untuk performa baca.",
                "spot_in_code": "Membuat tabel terpisah hanya untuk menyimpan kode pos dua digit di database laporan bulanan."
            }
        ],
        "when_to_use": (
            "Terapkan pemodelan relasional 3NF untuk sistem transaksional operasional (OLTP) agar integritas data terjamin dan bebas anomali update. "
            "Gunakan Junction Table untuk setiap hubungan Many-to-Many dengan foreign key cascade delete yang terdefinisi jelas. "
            "Lakukan denormalisasi hanya jika terbukti ada bottleneck performa nyata pada query baca tertentu setelah dilakukan indexing."
        ),
        "why_vibecoding_matters": (
            "AI sering kali merancang skema database yang malas dengan menumpuk atribut relasional ke dalam satu kolom teks JSON atau string koma, "
            "yang membuat pembuatan fitur laporan atau filter data di masa depan menjadi mimpi buruk. "
            "Saat merancang database bersama AI, berikan prompt tegas: 'Rancang skema relasional yang ternormalisasi (3NF): "
            "buatkan tabel entitas terpisah, tentukan primary key dan foreign key yang eksplisit, dan gunakan junction table untuk relasi many-to-many.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa relasi Many-to-Many (M:N) membutuhkan Junction Table (tabel perantara)?",
                "answer": "Karena dalam basis data relasional, sebuah sel kolom tidak boleh menampung multi-nilai; junction table memecah relasi M:N menjadi dua relasi One-to-Many (1:N) yang bersih dan mematuhi 1NF."
            },
            {
                "question": "Apa fungsi dari constraint 'ON DELETE CASCADE' pada Foreign Key relasi basis data?",
                "answer": "Secara otomatis menghapus baris-baris anak di tabel terkait ketika baris induknya dihapus (misal menghapus akun pengguna otomatis menghapus semua item profil miliknya), mencegah adanya orphaned records."
            }
        ]
    },

    "f-auth": {
        "summary": "Protokol verifikasi identitas pengguna (Autentikasi) dan pembatasan hak akses sumber daya (Otorisasi).",
        "explanation_simple": (
            "Bayangkan pergi menonton festival konser musik internasional. Di pintu gerbang terluar, petugas keamanan memeriksa KTP "
            "dan wajahmu untuk memastikan kamu adalah orang yang sesungguhnya (Autentikasi / Authentication: Siapa Kamu?). "
            "Setelah terbukti asli, kamu diberi gelang tiket khusus bertuliskan 'Akses Reguler'. "
            "Ketika kamu mencoba berjalan masuk ke panggung VIP di belakang layar, petugas panggung memeriksa gelangmu "
            "dan melarangmu masuk karena tiketmu tidak memiliki izin akses panggung (Otorisasi / Authorization: Apa yang Boleh Kamu Lakukan?).\n\n"
            "Autentikasi membuktikan identitasmu, sedangkan Otorisasi menentukan batas kekuasaanmu. "
            "Batas analogi konser: gelang konser bisa dipotong atau dipinjamkan ke teman, sedangkan dalam keamanan digital, "
            "kredensial token dilengkapi tanda tangan digital kriptografi yang tidak bisa dipalsukan."
        ),
        "problem_context": (
            "Pada awal internet sebelum ada protokol otentikasi standar, situs web menyimpan kata sandi pengguna dalam bentuk teks polos (plaintext). "
            "Ketika database dicuri peretas, jutaan kata sandi bocor seketika. "
            "Selain itu, server web harus mengingat sesi login pengguna di tengah protokol HTTP yang stateless. "
            "Standar autentikasi modern diciptakan untuk mengamankan kredensial pengguna menggunakan hashing satu arah "
            "dan mengelola sesi login tanpa kebocoran data."
        ),
        "explanation_technical": (
            "Perbedaan esensial: "
            "- Authentication (AuthN): Memvalidasi identitas (Username/Password, MFA/2FA, OAuth2, Biometrik). "
            "- Authorization (AuthZ): Memvalidasi hak akses setelah terotentikasi (Role-Based Access Control - RBAC, Attribute-Based Access Control - ABAC).\n\n"
            "Keamanan Kata Sandi: "
            "Kata sandi DILARANG KERAS disimpan dalam teks polos atau hash cepat biasa (MD5/SHA-256). "
            "Wajib menggunakan Adaptive Slow Hashing Functions yang dilengkapi Salt acak: bcrypt, Argon2, atau scrypt. "
            "Algoritma ini sengaja dirancang lambat secara CPU dan memori untuk menggagalkan serangan Brute-Force dan Rainbow Table.\n\n"
            "Manajemen Sesi Digital: "
            "1. Session-Based: Server menyimpan session ID di memori/Redis dan mengirimkannya ke klien via HTTP-Only Secure Cookie. Stateful. "
            "2. Token-Based (JWT - JSON Web Token): Klien menyimpan token yang ditandatangani secara kriptografi (HMAC-SHA256 atau RSA). "
            "Stateless, tetapi sulit di-revoke sebelum masa expired habis kecuali menggunakan blacklist/refresh token pattern."
        ),
        "misconceptions": [
            {
                "misconception": "JWT (JSON Web Token) mengenkripsi payload data sehingga aman untuk menyimpan rahasia seperti nomor kartu kredit di dalamnya.",
                "explanation": "JWT payload secara default hanya di-encode dalam format Base64Url yang dapat dibaca dan didekodekan oleh siapa saja dalam 1 detik; JWT hanya ditandatangani (signed) untuk integritas, bukan dienkripsi (encrypted) kecuali menggunakan spesifikasi JWE.",
                "spot_in_code": "Menyimpan PIN ATM atau password pengguna di dalam payload claims JWT."
            },
            {
                "misconception": "Menggunakan enkripsi hashing SHA-256 buatan sendiri sudah cukup aman untuk menyimpan password di database.",
                "explanation": "SHA-256 adalah fast cryptographic hash yang dirancang super cepat; kartu grafis (GPU) peretas modern mampu menghitung miliaran tebakan SHA-256 per detik untuk membobol password; gunakan bcrypt atau Argon2.",
                "spot_in_code": "const hash = crypto.createHash('sha256').update(password).digest('hex')."
            }
        ],
        "when_to_use": (
            "Gunakan bcrypt atau Argon2id dengan work factor terkalibrasi untuk setiap penyimpanan password akun. "
            "Gunakan HTTP-Only, Secure, SameSite cookies untuk menyimpan token sesi di web browser guna menangkal serangan pencurian token via XSS. "
            "Terapkan prinsip Role-Based Access Control (RBAC) pada setiap endpoint API sensitif."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis sistem login yang membandingkan password dengan string biasa atau menggunakan algoritma hash usang (MD5/SHA1), "
            "serta lupa memeriksa otorisasi kepemilikan data pada endpoint API (misalnya user A bisa mengedit data user B hanya dengan mengganti parameter URL id). "
            "Saat vibecoding modul auth, perintahkan AI: 'Gunakan bcrypt untuk hashing password, terapkan JWT dengan access token dan refresh token pattern, "
            "dan pastikan setiap endpoint memeriksa apakah resource yang diakses benar-benar milik pengguna yang sedang login!'"
        ),
        "reflection_questions": [
            {
                "question": "Apa tujuan penambahan 'Salt' acak pada proses hashing kata sandi pengguna?",
                "answer": "Salt mencegah serangan Rainbow Table (tabel hash siap pakai) dan memastikan bahwa dua pengguna yang memiliki password yang sama persis akan menghasilkan nilai hash yang sama sekali berbeda di database."
            },
            {
                "question": "Mengapa menyimpan token autentikasi di Browser LocalStorage lebih berisiko daripada di HTTP-Only Cookie?",
                "answer": "Karena LocalStorage dapat dibaca oleh script JavaScript apapun di halaman, sehingga sangat rentan dicuri jika aplikasi memiliki celah Cross-Site Scripting (XSS), sedangkan HTTP-Only Cookie tidak bisa diakses oleh JavaScript."
            }
        ]
    },

    "f-security": {
        "summary": "Prinsip perlindungan sistem terhadap ancaman siber, pencegahan celah kerentanan perangkat lunak, dan pertahanan berlapis.",
        "explanation_simple": (
            "Bayangkan brankas penyimpanan uang emas di bank sentral. Bank tidak hanya mengandalkan satu pintu pagar depan yang tipis. "
            "Mereka menerapkan pertahanan berlapis (Defense in Depth): ada pos penjaga bersenjata di gerbang luar, kamera pengawas sensor gerak, "
            "pintu baja brankas dengan kunci kombinasi ganda yang membutuhkan dua staf berbeda, dan sensor panas di dalam ruangan brankas. "
            "Jika seorang penyusup berhasil melewati pos gerbang luar, mereka tetap akan tertahan oleh pintu baja berikutnya.\n\n"
            "Keamanan Perangkat Lunak (Software Security) adalah penerapan pertahanan berlapis pada setiap baris kode aplikasimu. "
            "Batas analoginya: perampok bank fisik terlihat oleh mata manusia, sedangkan penyerang siber di internet "
            "dapat berupa bot otomatis yang memindai jutaan celah kode di seluruh dunia 24 jam sehari tanpa suara."
        ),
        "problem_context": (
            "Satu celah keamanan kecil pada kode aplikasi dapat meruntuhkan reputasi perusahaan dan menimbulkan denda hukum ratusan miliar rupiah. "
            "Setiap tahun, ribuan institusi mengalami peretasan karena kerentanan klasik seperti SQL Injection, pencurian sesi (Session Hijacking), "
            "dan pembobolan akses server. Asumsi keliru bahwa 'aplikasi saya kecil dan tidak ada yang mau meretas' adalah pintu masuk utama "
            "bagi bot otomatis malware global yang tidak pandang bulu dalam mengeksploitasi kelemahan software."
        ),
        "explanation_technical": (
            "Standar keamanan industri software dipandu oleh OWASP Top 10 (Open Worldwide Application Security Project). "
            "Tiga pilar keamanan CIA Triad: "
            "- Confidentiality: data hanya boleh dibaca oleh pihak berwenang (Enkripsi at-rest dan in-transit via TLS/HTTPS). "
            "- Integrity: data dijamin tidak dimanipulasi di tengah jalan (Digital Signatures & HMAC). "
            "- Availability: sistem tetap dapat melayani pengguna saat diserang (DDoS protection & Rate limiting).\n\n"
            "Kerentanan kode paling berbahaya dan mitigasinya: "
            "1. Injection (SQLi, Command Injection): Penyerang menyelipkan instruksi kode ke dalam input teks. Mitigasi: Input Sanitization & Parameterized Queries. "
            "2. Cross-Site Scripting (XSS): Penyerang menyisipkan script jahat ke dalam tampilan pengguna lain. Mitigasi: Output Encoding, HTML Escaping, dan Content Security Policy (CSP). "
            "3. Cross-Site Request Forgery (CSRF): Memaksa browser korban mengeksekusi aksi tak diinginkan pada web yang sedang login. Mitigasi: Anti-CSRF Tokens dan SameSite Cookies.\n\n"
            "Prinsip fundamental: 'Never Trust User Input' (Anggap semua data masukan dari internet bermusuhan)."
        ),
        "misconceptions": [
            {
                "misconception": "Keamanan melalui kerahasiaan (Security through Obscurity) — seperti menyembunyikan nama URL admin rahasia — sudah cukup aman.",
                "explanation": "Menyembunyikan letak pintu tanpa memasang gembok kuat adalah ilusi; bot peretas memindai seluruh endpoint secara brutal dan cepat atau lambat pasti menemukan URL tersembunyi tersebut.",
                "spot_in_code": "Membuat halaman admin di URL /rahasia-jangan-dibuka tanpa memasang middleware autentikasi dan otorisasi."
            },
            {
                "misconception": "Validasi input di antarmuka frontend (JavaScript di browser) sudah cukup untuk mencegah data berbahaya masuk ke database.",
                "explanation": "Validasi frontend sangat mudah dilewati dalam 5 detik menggunakan curl, Postman, atau inspect element; validasi wajib diulang dan ditegakkan secara mutlak di sisi backend server.",
                "spot_in_code": "Hanya memasang atribut required di form HTML tanpa memvalidasi ulang request body di server controller."
            }
        ],
        "when_to_use": (
            "Terapkan Principle of Least Privilege: berikan hak akses seminimal mungkin bagi setiap akun database, API keys, dan proses sistem operasi. "
            "Sanitasi dan validasi setiap input pengguna pada batas terluar server controller. "
            "Gunakan library keamanan resmi dan audit dependensi secara berkala (Dependency Vulnerability Scanning)."
        ),
        "why_vibecoding_matters": (
            "Kode yang dihasilkan AI sering kali rentan terhadap kerentanan OWASP karena AI memprioritaskan kode yang 'berhasil jalan' dengan cepat. "
            "AI sering menulis query mentah, mengeksekusi shell command menggunakan exec(), atau me-render HTML mentah tanpa escaping (dangerouslySetInnerHTML). "
            "Saat vibecoding, jalankan pemeriksaan keamanan ketat: 'Audit kode ini terhadap OWASP Top 10: "
            "apakah ada celah SQL Injection, XSS, insecure direct object references (IDOR), atau penanganan rahasia kredensial yang bocor?'"
        ),
        "reflection_questions": [
            {
                "question": "Apa bahaya dari kerentanan Insecure Direct Object References (IDOR) pada API endpoint?",
                "answer": "IDOR terjadi ketika API mengizinkan pengguna mengakses data pengguna lain hanya dengan menebak atau mengganti nomor ID di URL (misal: /api/orders/101 diganti menjadi /api/orders/102) tanpa memvalidasi hak kepemilikan."
            },
            {
                "question": "Mengapa prinsip 'Defense in Depth' (pertahanan berlapis) selalu diwajibkan dalam arsitektur keamanan?",
                "answer": "Karena tidak ada satu lapisan keamanan pun yang sempurna 100%; jika satu lapisan pertahanan (misal firewall) berhasil ditembus penyerang, lapisan pertahanan berikutnya (enkripsi data dan RBAC) tetap melindungi aset berharga."
            }
        ]
    },

    "f-deployment": {
        "summary": "Proses otomatisasi perilisan, pengemasan lingkungan, dan pengoperasian perangkat lunak di server produksi.",
        "explanation_simple": (
            "Bayangkan merakit pesawat terbang komersial. Kamu dan tim teknisi merakit dan menguji mesin pesawat di hanggar tertutup pabrik (Lingkungan Development). "
            "Setelah pesawat siap, kamu membawanya ke landasan uji coba khusus yang meniru kondisi cuaca asli untuk uji terbang simulasi pilot (Lingkungan Staging). "
            "Baru setelah seluruh izin penerbangan dan inspeksi lulus 100%, pesawat tersebut diisi oleh ratusan penumpang nyata "
            "untuk terbang di rute penerbangan komersial internasional (Lingkungan Produksi).\n\n"
            "Deployment adalah perjalanan membawa aplikasi dari laptop pengembang ke tangan pengguna nyata di seluruh dunia. "
            "Batas analoginya: pesawat fisik diterbangkan satu per satu, sedangkan deployment perangkat lunak modern "
            "dilakukan secara otomatis melalui pipeline CI/CD tanpa ada jeda mati (Zero-Downtime Deployment)."
        ),
        "problem_context": (
            "Di masa lalu, deployment dilakukan secara manual dan menegangkan pada tengah malam: developer menyalin file kode via FTP "
            "ke server produksi hidup, mengubah konfigurasi database manual, dan berdoa agar aplikasi tidak rusak. "
            "Sering kali terjadi masalah klasik 'di laptop saya jalan normal, tetapi di server meledak error' "
            "karena versi sistem operasi dan library server berbeda dengan laptop developer. "
            "Containerization (Docker) dan CI/CD diciptakan untuk membuat proses rilis menjadi otomatis, deterministik, dan dapat diulang tanpa kepanikan."
        ),
        "explanation_technical": (
            "Pipeline Deployment modern bertumpu pada konsep CI/CD (Continuous Integration / Continuous Deployment): "
            "- CI (Continuous Integration): setiap kode baru yang di-push otomatis menjalankan linter, static analysis, dan seluruh automated tests di lingkungan virtual bersih. "
            "- CD (Continuous Delivery/Deployment): jika seluruh tes lulus, artefak otomatis dikemas dan dirilis ke server target.\n\n"
            "Containerization dengan Docker mengemas kode aplikasi beserta runtime, konfigurasi OS, dan pustaka dependensinya "
            "ke dalam satu Image terisolasi yang dijamin berperilaku 100% identik di lingkungan mana pun.\n\n"
            "Strategi Zero-Downtime Deployment: "
            "1. Blue-Green Deployment: memiliki dua lingkungan identik (Blue yang aktif melayani pengguna, Green yang dipasangi versi baru). "
            "Setelah Green teruji sehat, router traffic dialihkan seketika dari Blue ke Green. "
            "2. Canary Deployment: mengalirkan versi baru hanya ke 5% pengguna terlebih dahulu; jika metrik error normal, perlahan dinaikkan ke 100%."
        ),
        "misconceptions": [
            {
                "misconception": "Menyimpan kredensial database password langsung di dalam file konfigurasi kode adalah hal praktis yang aman.",
                "explanation": "Kredensial rahasia dilarang keras di-hardcode di kode; wajib dikelola melalui Environment Variables atau secret manager sistem cloud (Twelve-Factor App methodology).",
                "spot_in_code": "const DB_PASS = 'rahasia123'; tertulis di dalam file server.ts yang dicommit ke git."
            },
            {
                "misconception": "Deployment selesai begitu file berhasil disalin ke server produksi.",
                "explanation": "Deployment baru dianggap tuntas setelah sistem melewati proses health check, metrik monitoring stabil, dan tidak ada lonjakan grafik error rate pada dashboard observabilitas pasca-rilis.",
                "spot_in_code": "Langsung mematikan laptop dan tidur 1 menit setelah perintah deployment selesai dieksekusi."
            }
        ],
        "when_to_use": (
            "Gunakan Docker Container untuk mengemas backend services agar terhindar dari ketidakcocokan lingkungan host OS. "
            "Otomatisasikan build dan testing menggunakan CI/CD (GitHub Actions, GitLab CI) pada setiap Pull Request. "
            "Gunakan Blue-Green atau Rolling updates untuk aplikasi produksi yang tidak boleh mengalami masa henti layanan (zero downtime)."
        ),
        "why_vibecoding_matters": (
            "AI sering menyarankan cara cepat menjalankan aplikasi di server dengan mengetik node server.js atau python app.py di terminal SSH, "
            "yang akan langsung mati seketika begitu jendela terminal ditutup atau server kehabisan memori. "
            "Saat vibecoding untuk deployment, mintalah arsitektur produksi: 'Buatlah konfigurasi Dockerfile multi-stage build yang aman dan minimalis, "
            "serta siapkan file workflow CI/CD GitHub Actions untuk menjalankan automated test dan deployment otomatis.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa prinsip Twelve-Factor App mewajibkan pemisahan tegas antara konfigurasi rahasia dengan kode sumber?",
                "answer": "Agar kode sumber aplikasi dapat dibuka atau dipindahkan ke repositori publik tanpa risiko membocorkan kredensial database dan API keys rahasia yang spesifik untuk lingkungan produksi."
            },
            {
                "question": "Apa keunggulan strategi Blue-Green Deployment saat terjadi kegagalan fatal pada versi baru?",
                "answer": "Rollback dapat dilakukan seketika dalam waktu satu detik cukup dengan membalikkan kembali router traffic ke lingkungan lama (Blue) yang masih hidup dan sehat."
            }
        ]
    },

    "f-logging-monitoring": {
        "summary": "Perekaman peristiwa sistem, pemantauan metrik kesehatan performa, dan instrumentasi observabilitas produksi.",
        "explanation_simple": (
            "Bayangkan ruang kokpit pesawat terbang modern. Di hadapan pilot terdapat ratusan instrumen dasbor: "
            "indikator ketinggian altimeter, kompas navigasi, sisa bahan bakar avtur, dan lampu peringatan tekanan kabin. "
            "Di bagian belakang pesawat terpasang kotak hitam (Black Box) yang merekam setiap percakapan radio dan parameter mesin secara terus-menerus. "
            "Pilot tidak menerbangkan pesawat hanya dengan melihat jendela luar; mereka mengandalkan instrumen dasbor tersebut untuk mengantisipasi badai "
            "dan mendiagnosis anomali mesin sebelum terjadi malapetaka.\n\n"
            "Logging & Monitoring adalah kokpit dan kotak hitam aplikasi komputermu di lingkungan produksi. "
            "Batas analoginya: kotak hitam pesawat baru dibuka setelah terjadi kecelakaan, sedangkan sistem observabilitas software modern "
            "memberikan peringatan alarm otomatis (Alerting) ke ponsel tim insinyur di detik pertama saat grafik error mulai melonjak."
        ),
        "problem_context": (
            "Ketika pengguna di belahan dunia lain mengeluhkan aplikasi sering macet atau transaksi gagal, "
            "developer yang tidak memiliki sistem logging terstruktur hanya bisa kebingungan dan menebak-nebak di ruang gelap. "
            "Tanpa catatan log, kamu tidak tahu parameter apa yang dikirim pengguna, query database mana yang lambat, "
            "atau server mana yang sedang kehabisan RAM. Logging dan monitoring diciptakan untuk memberikan pandangan tembus pandang "
            "(Observability) ke dalam jeroan sistem produksi."
        ),
        "explanation_technical": (
            "Tiga pilar utama Observabilitas Sistem (The Three Pillars of Observability): "
            "1. Logs: Catatan diskrit peristiwa berstempel waktu (Timestamped Events). "
            "Wajib menggunakan format Structured Logging (JSON) dengan level terstandarisasi: "
            "- DEBUG: informasi diagnostik detail saat development. "
            "- INFO: konfirmasi alur normal (misal: 'User ID 42 berhasil checkout'). "
            "- WARN: anomali yang tidak mematikan sistem (misal: 'Koneksi lambat, retry ke-2'). "
            "- ERROR: kegagalan operasi yang harus ditangani (misal: 'Gagal menghubungi payment gateway'). "
            "- FATAL: sistem tidak dapat melanjutkan eksekusi.\n\n"
            "2. Metrics: Data agregasi numerik yang dapat dihitung dari waktu ke waktu (Time-Series: CPU usage, Memory heap, Request Per Second, P99 Latency). "
            "3. Distributed Tracing: Melacak perjalanan sebuah permintaan pengguna melintasi puluhan microservices independen menggunakan Correlation ID (Trace ID)."
        ),
        "misconceptions": [
            {
                "misconception": "Logging sebanyak-banyaknya di level INFO untuk setiap baris kode adalah hal yang bagus.",
                "explanation": "Logging berlebihan (Log Spam) memakan kapasitas disk server hingga penuh, memicu biaya tagihan cloud logging yang membengkak, dan menenggelamkan pesan error penting di lautan log sampah.",
                "spot_in_code": "Mencetak isi payload body utuh di setiap request API di lingkungan produksi."
            },
            {
                "misconception": "Log boleh mencantumkan seluruh data masukan pengguna apa adanya.",
                "explanation": "Mencatat data pribadi sensitif (Personally Identifiable Information - PII) seperti password, nomor KTP, atau kartu kredit ke dalam file log adalah pelanggaran regulasi privasi berat (GDPR / UU PDP) dan celah kebocoran keamanan data.",
                "spot_in_code": "logger.info('User login: ' + JSON.stringify(request.body));."
            }
        ],
        "when_to_use": (
            "Gunakan Structured Logging (JSON format) agar log dapat diindeks dan dicari secara instan oleh agregator log (seperti Datadog, ELK Stack, Grafana Loki). "
            "Semprotkan Correlation ID / Trace ID di header setiap permintaan HTTP antarlayanan untuk memudahkan penelusuran error lintas server. "
            "Pasang alert alarm otomatis jika metrik error rate 5xx melampaui ambang batas 1%."
        ),
        "why_vibecoding_matters": (
            "Kode yang dihasilkan AI sering kali hanya berisi console.log teks mentah yang tidak terstruktur dan tidak memiliki tingkatan level log, "
            "sehingga mustahil difilter saat aplikasi berjalan di server cloud. "
            "Saat vibecoding, instruksikan AI: 'Gunakan structured logging library: "
            "format log dalam JSON, gunakan level log yang tepat (INFO/ERROR), sertakan konteks userId dan requestId, "
            "dan pastikan data sensitif seperti password disanitasi/masking dari output log!'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa metrik 'P99 Latency' (persentil 99) jauh lebih bermakna daripada 'Average Latency' (rata-rata) dalam mengukur performa sistem?",
                "answer": "Karena nilai rata-rata menyamarkan lonjakan masalah; P99 latency menunjukkan waktu tunggu paling lambat yang dialami oleh 1% pengguna paling tidak beruntung, mengungkap bottleneck ekstrem yang tersembunyi."
            },
            {
                "question": "Bagaimana Correlation ID membantu proses debugging pada arsitektur Microservices terdistribusi?",
                "answer": "Correlation ID disematkan di header dan diteruskan ke seluruh rantai layanan, memungkinkan insinyur memfilter seluruh log dari 10 microservices berbeda yang memproses transaksi yang sama hanya dengan satu kata kunci ID."
            }
        ]
    },

    "f-sdlc-agile": {
        "summary": "Metodologi siklus hidup rekayasa perangkat lunak, kolaborasi iteratif tangkas, dan pengiriman nilai berkelanjutan.",
        "explanation_simple": (
            "Bayangkan memesan lukisan potret keluarga ke seorang pelukis kanvas. "
            "Metode lama (Waterfall) bekerja seperti pelukis yang mengunci diri di kamar selama 6 bulan tanpa komunikasi, "
            "lalu keluar membawa lukisan utuh yang ternyata salah warna baju dan pose wajahnya tidak disukai keluargamu. "
            "Sebaliknya, metode tangkas (Agile) bekerja seperti pelukis yang menunjukkan sketsa pensil kasar di minggu pertama untuk meminta masukan, "
            "lalu mewarnai latar belakang di minggu kedua, dan menyempurnakan detail wajah di minggu ketiga bersama keluargamu.\n\n"
            "SDLC (Software Development Life Cycle) dan Agile adalah cara tim mengatur alur kerja dari ide hingga rilis. "
            "Batas analoginya: lukisan kanvas tidak bisa diubah begitu cat minyak kering, sedangkan perangkat lunak modern "
            "adalah artefak digital fleksibel yang dapat terus disempurnakan setiap dua minggu berdasarkan umpan balik pengguna nyata."
        ),
        "problem_context": (
            "Pada dekade 1980-an dan 1990-an, industri software didominasi oleh metode Waterfall yang kaku: "
            "analisis kebutuhan berbulan-bulan, perancangan dokumen tebal, penulisan kode setahun, dan pengujian di akhir. "
            "Hasil riset membuktikan lebih dari 60% proyek software gagal total: ketika proyek selesai dua tahun kemudian, "
            "kebutuhan pasar sudah berubah total dan software yang dibangun tidak lagi dibutuhkan. "
            "Manifesto Agile dideklarasikan pada tahun 2001 untuk menggantikan birokrasi dokumen kaku dengan adaptabilitas dan iterasi cepat."
        ),
        "explanation_technical": (
            "Fase standar dalam SDLC (Software Development Life Cycle): "
            "1. Requirements & Discovery -> 2. Design & Architecture -> 3. Implementation (Coding) -> 4. Verification (Testing) -> 5. Deployment -> 6. Maintenance & Feedback.\n\n"
            "Prinsip Inti Agile (Agile Manifesto): "
            "- Individu dan interaksi lebih penting daripada proses dan alat bantu. "
            "- Software yang berfungsi lebih penting daripada dokumentasi yang komprehensif. "
            "- Kolaborasi dengan pelanggan lebih penting daripada negosiasi kontrak. "
            "- Tanggap terhadap perubahan lebih penting daripada mengikuti rencana kaku.\n\n"
            "Framework Agile populer: "
            "- Scrum: Membagi pekerjaan ke dalam siklus waktu tetap bernama Sprints (biasanya 2 minggu), "
            "dengan peran Product Owner, Scrum Master, Developers, dan ritual Sprint Planning, Daily Standup, Sprint Review, dan Retrospective. "
            "- Kanban: Memvisualisasikan alur kerja di papan kartu (To Do, In Progress, Done) dengan pembatasan Work In Progress (WIP Limits) untuk mencegah bottleneck tim."
        ),
        "misconceptions": [
            {
                "misconception": "Agile berarti bekerja tanpa perencanaan dan tanpa dokumentasi sama sekali.",
                "explanation": "Agile tetap merencanakan dan mendokumentasikan, namun perencanaan dilakukan secara adaptif per iterasi dan dokumentasi difokuskan pada hal yang benar-benar bernilai bagi pemeliharaan sistem.",
                "spot_in_code": "Menolak menulis dokumentasi arsitektur dengan alasan 'kami kan tim Agile'."
            },
            {
                "misconception": "Sprint 2 mingguan adalah cara memeras developer agar bekerja lembur terus-menerus tanpa henti.",
                "explanation": "Prinsip Agile menekankan Sustainable Pace (kecepatan kerja yang berkelanjutan) agar tim tidak mengalami burnout dan dapat menjaga konsistensi kualitas kode dalam jangka panjang.",
                "spot_in_code": "Memaksakan 80 story points ke dalam satu sprint yang kapasitas normal timnya hanya 40 points."
            }
        ],
        "when_to_use": (
            "Gunakan Scrum atau Kanban saat membangun produk digital baru yang kebutuhan fiturnya masih berkembang dan butuh validasi pasar yang cepat. "
            "Pecah tugas besar menjadi User Stories kecil yang dapat diselesaikan dalam hitungan hari. "
            "Manfaatkan Sprint Retrospective untuk terus memperbaiki proses kerja dan komunikasi tim."
        ),
        "why_vibecoding_matters": (
            "Dengan adanya AI, kecepatan menulis kode meningkat 10x lipat, namun risiko membangun 'fitur yang salah' juga meningkat 10x lipat. "
            "Tanpa pemahaman siklus iterasi Agile, kamu bisa menghasilkan ribuan baris kode AI yang sia-sia karena tidak pernah memvalidasinya ke pengguna nyata. "
            "Terapkan mindset Agile dalam vibecoding: 'Rancang potongan fitur terkecil yang fungsional (MVP), "
            "uji bersama pengguna atau penguji internal, kumpulkan umpan balik, lalu lakukan iterasi berikutnya bersama AI.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa pembatasan 'Work In Progress' (WIP Limits) pada papan Kanban sangat efektif meningkatkan produktivitas tim?",
                "answer": "Karena membatasi jumlah tugas yang dikerjakan bersamaan meminimalisasi multitasking dan context switching, memaksa tim fokus menyelesaikan tugas yang ada (Stop Starting, Start Finishing)."
            },
            {
                "question": "Apa tujuan utama dari ritual Sprint Retrospective dalam metodologi Scrum?",
                "answer": "Untuk mengevaluasi proses kerja tim (bukan hasil fitur): apa yang berjalan baik, apa kendala komunikasi yang terjadi, dan merumuskan rencana aksi perbaikan konkret untuk sprint berikutnya."
            }
        ]
    },

    "f-documentation": {
        "summary": "Penyusunan catatan arsitektur, panduan antarmuka pemrograman (API specs), dan pemeliharaan pengetahuan teknis.",
        "explanation_simple": (
            "Bayangkan membeli lemari kabinet modern dari toko furnitur yang dikirim dalam bentuk 50 kepingan kayu dan 100 baut kecil, "
            "tetapi di dalam kardus tidak disertakan selembar pun buku petunjuk perakitan bergambar. "
            "Meskipun bahan kayu dan bautnya berkualitas super, kamu akan menghabiskan waktu berhari-hari dalam frustrasi "
            "mencoba menebak baut mana yang masuk ke lubang mana, dan lemari yang kamu pasang mungkin miring atau roboh saat diisi pakaian.\n\n"
            "Dokumentasi Teknis (Technical Documentation) adalah buku manual perakitan dan peta penunjuk jalan bagi kodemu. "
            "Batas analoginya: buku manual furnitur tidak pernah berubah setelah dicetak, sedangkan dokumentasi software "
            "adalah artefak hidup yang wajib diperbarui seirama dengan setiap perubahan kode sumber aplikasi."
        ),
        "problem_context": (
            "Ketika developer utama pembuat sistem mengundurkan diri (resign) dari perusahaan tanpa meninggalkan dokumentasi, "
            "tim yang ditinggalkan mengalami krisis fatal (Bus Factor problem). Tidak ada yang berani menyentuh modul pembayaran "
            "karena tidak ada yang tahu mengapa kode tertentu ditulis seperti itu. "
            "Fitur onboarding developer baru memakan waktu 4 bulan hanya untuk menyiapkan lingkungan laptop. "
            "Dokumentasi teknis diciptakan untuk melembagakan pengetahuan agar sistem tidak bergantung pada ingatan rapuh satu individu."
        ),
        "explanation_technical": (
            "Kategori dokumentasi teknis dalam rekayasa perangkat lunak: "
            "1. In-Code Documentation: Docstrings terstandarisasi (Dartdoc ///, JSDoc /** */, Python Docstrings \"\"\") "
            "yang menjelaskan parameter fungsi, tipe kembalian, dan kemungkinan exceptions. Tooling IDE menampilkan docstring ini saat developer mengarahkan kursor (hover). "
            "2. Project Onboarding (README.md): Instruksi prasyarat sistem, langkah instalasi dependensi, cara menjalankan aplikasi lokal, dan cara mengeksekusi tes. "
            "3. API Specifications (OpenAPI / Swagger): Spesifikasi formal mesin-terbaca yang mendokumentasikan endpoint, skema request/response, dan status code secara interaktif. "
            "4. Architecture Decision Records (ADR): Dokumen ringkas satu halaman yang mencatat konteks 'MENGAPA' sebuah keputusan arsitektural besar diambil "
            "(misal: 'ADR-005: Memilih PostgreSQL daripada MongoDB untuk ledger transaksi')."
        ),
        "misconceptions": [
            {
                "misconception": "Kode yang bersih (Clean Code) tidak membutuhkan dokumentasi sama sekali.",
                "explanation": "Clean code menjelaskan APA yang dilakukan kode dan BAGAIMANA ia bekerja; tetapi kode tidak pernah bisa menjelaskan MENGAPA keputusan bisnis tertentu diambil atau alternatif teknologi apa yang ditolak saat itu.",
                "spot_in_code": "Tidak mendokumentasikan alasan memilih workaround aneh untuk bug platform tertentu."
            },
            {
                "misconception": "Menulis dokumentasi hanya dilakukan sekali di akhir proyek setelah seluruh aplikasi selesai dirilis.",
                "explanation": "Dokumentasi yang ditulis di akhir hampir selalu tidak pernah terwujud karena tim sudah pindah ke proyek baru; dokumentasi terbaik ditulis bersamaan dengan penulisan kode (Documentation-Driven Development).",
                "spot_in_code": "Menunda pembuatan README hingga berbulan-bulan setelah rilis produksi."
            }
        ],
        "when_to_use": (
            "Tulis file README.md yang jelas pada setiap repositori proyek sejak hari pertama. "
            "Gunakan Docstrings (/// di Dart) untuk mendokumentasikan semua class dan fungsi publik pada modul bersama (Shared Libraries). "
            "Tulis ADR (Architecture Decision Record) setiap kali tim memutuskan adopsi teknologi baru atau perubahan arsitektur besar."
        ),
        "why_vibecoding_matters": (
            "AI asisten sangat terbantu oleh dokumentasi yang jelas: jika repositorimu memiliki README dan docstrings yang rapi, "
            "AI dapat memahami konteks kancah aplikasimu dengan presisi tinggi dan menghasilkan kode yang konsisten dengan arsitekturmu. "
            "Gunakan kapabilitas AI untuk mendokumentasikan sistemmu: 'Tuliskan dokumentasi OpenAPI (Swagger) untuk endpoint ini, "
            "dan buatkan Architecture Decision Record (ADR) ringkas yang merangkum alasan pemilihan arsitektur modular yang baru kita buat.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa Architecture Decision Records (ADR) sangat berharga bagi developer yang baru bergabung ke tim 2 tahun kemudian?",
                "answer": "ADR memberikan konteks historis mengenai kendala, pertimbangan, dan alternatif yang dibahas di masa lalu, mencegah developer baru mengulangi eksperimen gagal yang sudah pernah dibantah sebelumnya."
            },
            {
                "question": "Apa peran spesifikasi OpenAPI (Swagger) dalam kolaborasi antara tim backend dan tim frontend?",
                "answer": "OpenAPI bertindak sebagai kontrak independen mesin yang memungkinkan tim frontend menghasilkan mock server dan API client otomatis sebelum implementasi backend sesungguhnya selesai dibuat."
            }
        ]
    },

    "f-computer-science": {
        "summary": "Landasan teoretis komputasi, sains informasi, batas kemampuan mesin Turing, dan abstraksi sistem komputasional.",
        "explanation_simple": (
            "Bayangkan ilmu arsitektur sipil yang mempelajari kekuatan beton dan gravitasi bumi, dibandingkan dengan tukang bangunan "
            "yang memegang sendok semen dan batu bata. Tukang bangunan tahu cara menyusun batu bata agar lurus, "
            "tetapi insinyur sipil memahami hukum mekanika fisika mengapa sebuah jembatan gantung tidak akan ambruk saat diterpa badai angin topan.\n\n"
            "Ilmu Komputer (Computer Science) adalah hukum fisika dan sains di balik setiap ketukan jarimu di keyboard. "
            "Ia mempelajari apa yang secara matematis BISA dihitung oleh mesin dan apa yang TIDAK PERNAH BISA diselesaikan oleh komputer tercepat sekalipun. "
            "Batas analoginya: gravitasi bumi adalah hukum alam mutlak, sedangkan fondasi ilmu komputer berakar pada traktat matematika murni "
            "(logika formal, otomata, dan teori komputabilitas) yang melampaui keterbatasan teknologi silikon fisik."
        ),
        "problem_context": (
            "Banyak orang mengira komputer super canggih dapat memecahkan masalah apapun di dunia jika diberi waktu dan memori yang cukup. "
            "Pada tahun 1936, sebelum komputer elektronik pertama selesai dirakit, Alan Turing secara brilian membuktikan bahwa "
            "ada masalah matematika yang mustahil dipecahkan oleh program komputer apapun (The Halting Problem). "
            "Memahami batas fundamental komputasi mencegah insinyur membuang miliaran rupiah mencoba menyelesaikan masalah "
            "yang secara matematis terbukti mustahil diselesaikan (NP-Complete / Undecidable problems)."
        ),
        "explanation_technical": (
            "Disiplin Ilmu Komputer berakar pada pilar-pilar teoretis fundamental: "
            "1. Teori Komputabilitas & Automata (Turing Machine, Chomsky Hierarchy): Mesin Turing adalah model komputasi matematis abstrak "
            "yang memanipulasi simbol pada pita pita tak terbatas sesuai tabel aturan; mendefinisikan batas kemampuan komputasi modern (Turing Completeness). "
            "2. Teori Kompleksitas Komputasi (P vs NP Problem): Mengklasifikasikan masalah berdasarkan sumber daya yang dibutuhkan untuk menyelesaikannya. "
            "- Kelas P: masalah yang dapat diselesaikan dalam waktu polinomial O(n^k). "
            "- Kelas NP: masalah yang solusinya sulit dicari tetapi dapat diverifikasi kebenarannya dalam waktu polinomial. "
            "3. Teori Informasi (Claude Shannon): Mengukur kuantitas informasi, redundansi, kompresi data (entropi Shannon), dan batas transmisi sinyal data pada saluran derau berisik."
        ),
        "misconceptions": [
            {
                "misconception": "Ilmu komputer adalah ilmu tentang cara merakit komputer atau cara menggunakan aplikasi perangkat lunak.",
                "explanation": "Seperti kata Edsger Dijkstra: 'Ilmu komputer tidak lebih tentang komputer daripada astronomi tentang teleskop'; ilmu komputer adalah sains matematika tentang komputasi, algoritma, dan informasi.",
                "spot_in_code": "Menganggap belajar bahasa pemrograman baru sama artinya dengan menguasai ilmu komputer."
            },
            {
                "misconception": "Komputer kuantum di masa depan akan mampu memecahkan masalah The Halting Problem.",
                "explanation": "Halting Problem terbukti secara logika matematika tak terputuskan (undecidable) pada sistem komputasi formal manapun, termasuk komputer kuantum.",
                "spot_in_code": "Mencoba membuat program yang dapat menganalisis program lain untuk menjamin 100% apakah program tersebut akan berhenti atau infinite loop."
            }
        ],
        "when_to_use": (
            "Manfaatkan teori State Machine (Finite State Automata - FSA) saat merancang alur status transaksi kompleks (misal: Cart -> Checkout -> Paid -> Shipped) untuk mencegah invalid transitions. "
            "Pahami klasifikasi masalah NP-Hard (seperti Travelling Salesperson atau Knapsack problem) agar kamu tidak membuang waktu mencari solusi eksak brute force; gunakan algoritma Heuristik atau Aproksimasi. "
            "Terapkan prinsip Information Theory saat merancang skema kompresi dan encoding data."
        ),
        "why_vibecoding_matters": (
            "Saat vibecoding dengan AI, kamu mungkin meminta AI menyelesaikan masalah optimasi kombinatorial yang sebenarnya tergolong NP-Hard. "
            "Jika kamu tidak memahami batas komputasi, AI akan menghasilkan kode pencarian eksak yang membeku selamanya saat dijalankan pada data nyata. "
            "Pemahaman ilmu komputer membantumu mengarahkan AI: 'Masalah ini tergolong NP-Hard; "
            "jangan cari solusi eksak brute-force, gunakan pendekatan algoritma heuristik greedy atau aproksimasi genetik!'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa The Halting Problem membuktikan bahwa mustahil membuat program antivirus sempurna yang dapat mendeteksi semua potensi bug infinite loop?",
                "answer": "Karena Alan Turing membuktikan lewat kontradiksi matematis bahwa tidak ada algoritma umum yang dapat menentukan dengan pasti untuk semua pasangan program-input apakah program tersebut akan berhenti atau berjalan selamanya."
            },
            {
                "question": "Apa makna dari pertanyaan terbesar sains komputer modern 'Apakah P = NP'?",
                "answer": "Apakah setiap masalah yang solusinya dapat diverifikasi dengan cepat (dalam waktu polinomial) juga dapat ditemukan solusinya dengan cepat, ataukah pencarian solusi pada dasarnya jauh lebih sulit daripada verifikasi."
            }
        ]
    }
}
