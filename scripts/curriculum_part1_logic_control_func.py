"""Enrichment Part 1: Logic, Control Flow, and Functions (Topics 1 - 9)
Includes Benchmark 1 (f-variables-data-types) and Benchmark 2 (f-functions).
"""

CURRICULUM_PART1 = {
    "f-programming-logic": {
        "summary": "Menyusun instruksi dengan urutan yang masuk akal.",
        "explanation_simple": (
            "Bayangkan kamu meminta seseorang yang baru pertama kali ke dapur untuk membuat mie instan. "
            "Jika kamu memberi instruksi: 'Rebus mie 3 menit, tuang mie ke mangkuk, buka bungkus mie', "
            "ia akan bingung atau bahkan merebus mie beserta plastik pembungkusnya. "
            "Urutan yang benar dan masuk akal adalah: buka bungkus mie, rebus mie dalam air mendidih, lalu tuang ke mangkuk bersama bumbu.\n\n"
            "Komputer bekerja persis seperti asisten dapur tersebut: sangat patuh, bekerja secepat kilat, tetapi tidak punya inisiatif "
            "atau akal sehat untuk menebak apa maksud kita. Komputer hanya menjalankan setiap instruksi secara harfiah, baris demi baris, "
            "sesuai urutan yang kita tuliskan. Jika urutannya terbalik, komputer tidak akan membetulkannya sendiri. "
            "Logika pemrograman adalah cara kita menyusun urutan langkah yang masuk akal agar komputer menyelesaikan tugas persis seperti yang kita harapkan."
        ),
        "problem_context": (
            "Masalah terbesar bagi pemula dan orang yang sering meminta AI membuatkan kode (vibecoding) adalah berasumsi bahwa "
            "komputer paham tujuan akhir aplikasi secara ajaib. Padahal, komputer hanya membaca kode dari atas ke bawah.\n\n"
            "Sebagai contoh, bayangkan alur pembayaran di toko online:\n"
            "- Urutan yang salah: Program menghitung potongan harga sebelum pembeli memasukkan kode promo. "
            "Karena kode promo belum dibaca, potongan harga tetap nol dan pembeli membayar harga penuh.\n"
            "- Urutan yang benar: Program menerima kode promo terlebih dahulu, memeriksa apakah promo valid, menghitung potongan harga, "
            "lalu menampilkan total akhir yang harus dibayar.\n\n"
            "Di kedua skenario di atas, komputer tidak menampilkan pesan kesalahan apa pun karena instruksinya sah. "
            "Namun di skenario pertama, hasil bisnisnya salah total. Logika pemrograman memastikan setiap bahan atau data "
            "sudah siap sebelum digunakan oleh langkah berikutnya."
        ),
        "explanation_technical": (
            "Untuk membangun alur program yang benar, ada tiga fondasi logika utama yang selalu digunakan di semua bahasa pemrograman:\n\n"
            "1. Sekuensial (Sequence / Berurutan):\n"
            "Instruksi dijalankan baris demi baris dari atas ke bawah. Langkah kedua baru berjalan setelah langkah pertama tuntas. "
            "Misalnya: mengambil data pengguna, baru kemudian menyapa namanya.\n\n"
            "2. Percabangan (Selection / Branching):\n"
            "Program mengambil keputusan untuk memilih jalur instruksi yang berbeda berdasarkan kondisi benar (true) atau salah (false). "
            "Misalnya: jika saldo mencukupi, potong saldo dan kirim barang; jika saldo tidak cukup, tampilkan peringatan 'Saldo Kurang'.\n\n"
            "3. Perulangan (Iteration / Looping):\n"
            "Program mengulang sekumpulan instruksi berkali-kali selama kondisi tertentu masih terpenuhi. "
            "Misalnya: mengirim notifikasi ke 100 pengguna satu per satu sampai daftar penerima habis.\n\n"
            "Teknik Menelusuri Kode (Step Tracing):\n"
            "Tracing adalah kebiasaan membaca kode baris demi baris seperti komputer, sambil mencatat nilai variabel pada secarik kertas "
            "atau di kepala kita pada setiap langkah. Tracing melatih kita melihat apa yang sebenarnya terjadi di setiap baris, bukan apa yang kita bayangkan terjadi.\n\n"
            "Membedakan Dua Jenis Kesalahan:\n"
            "- Syntax Error (Kesalahan Tata Bahasa): Terjadi saat aturan penulisan bahasa dilanggar (misalnya lupa tanda kurung atau salah ketik kata kunci). "
            "Komputer langsung menolak menjalankan program dan memberi tahu letak baris yang rusak. Ini mudah ditemukan.\n"
            "- Logical Error (Kesalahan Logika): Program ditulis rapi, tidak ada salah ketik, dan berjalan lancar tanpa pesan error, "
            "tetapi hasilnya salah (misalnya rumus diskon yang terbalik atau salah langkah). Kesalahan logika lebih menantang "
            "karena hanya bisa ditemukan dengan menelusuri alur berpikir dalam kode."
        ),
        "misconceptions": [
            {
                "misconception": "Jika program berjalan lancar tanpa pesan error, berarti kode sudah pasti benar.",
                "explanation": "Komputer hanya memeriksa apakah tata bahasa (sintaks) kode sah. Komputer tidak tahu apakah hasil perhitungan atau urutan instruksi sudah sesuai dengan kebutuhan logika yang kamu inginkan.",
                "spot_in_code": "Rumus total = harga * diskon bukannya total = harga - (harga * diskon). Kode berjalan tanpa crash, tetapi nominal belanja menjadi salah total."
            },
            {
                "misconception": "Komputer bisa menebak niat kita dan otomatis melompati langkah yang terlewat.",
                "explanation": "Komputer mengeksekusi instruksi secara kaku dan harfiah. Komputer tidak memiliki intuisi atau akal sehat untuk membetulkan urutan yang keliru.",
                "spot_in_code": "Mencetak isi variabel keranjang belanja sebelum data barang selesai diambil dari server."
            }
        ],
        "when_to_use": (
            "Gunakan pemikiran logika terstruktur setiap kali merancang alur fitur baru sebelum mulai menulis kode. "
            "Uraikan masalah besar menjadi urutan langkah kecil: apa yang harus terjadi pertama kali, kondisi apa yang perlu dicek, "
            "dan bagian mana yang perlu diulang. Terapkan teknik tracing langkah demi langkah setiap kali menemukan bug di mana program berjalan "
            "tanpa pesan error tetapi hasilnya meleset dari harapan."
        ),
        "why_vibecoding_matters": (
            "Saat vibecoding dengan asisten AI, model bahasa sering menghasilkan baris kode yang tampak rapi, canggih, dan bebas syntax error. "
            "Namun, AI kerap melakukan kesalahan urutan secara halus—misalnya memperbarui tampilan sebelum data siap, atau menutup koneksi sebelum proses simpan selesai. "
            "Jika kamu paham logika pemrograman, kamu tidak akan menelan mentah-mentah kode dari AI. Kamu bisa menelusuri urutan instruksi dan bertanya pada AI: "
            "'Jelaskan urutan jalannya kode ini langkah demi langkah, dan tunjukkan nilai data di setiap langkah untuk memastikan alurnya sudah masuk akal.'"
        ),
        "reflection_questions": [
            {
                "question": "Apa perbedaan mendasar antara syntax error dan logical error?",
                "answer": "Syntax error adalah pelanggaran tata bahasa penulisan yang langsung ditolak oleh komputer sebelum berjalan, sedangkan logical error adalah kesalahan urutan atau rumus yang tetap berjalan mulus namun menghasilkan keluaran yang keliru."
            },
            {
                "question": "Mengapa teknik tracing (membaca kode baris demi baris) sangat penting saat memeriksa kode hasil buatan AI?",
                "answer": "Karena AI sering menghasilkan kode yang tampak rapi dan bebas syntax error, namun urutan logikanya bisa saja terbalik atau melewati langkah prasyarat penting."
            }
        ]
    },

    "f-variables-data-types": {
        "summary": "Menyimpan data dengan nama dan wadah yang sesuai jenisnya.",
        "explanation_simple": (
            "Bayangkan deretan toples kaca berlabel di dapur rumahmu. Toples berlabel 'Gula Pasir' dirancang untuk menampung butiran padat, "
            "botol berlabel 'Kecap Asin' untuk cairan, dan saklar lampu di dinding hanya memiliki dua posisi: menyala atau mati. "
            "Label pada toples adalah nama variabel, isi di dalamnya adalah nilainya, dan bentuk wadahnya adalah tipe data. "
            "Jika kamu mencoba menuangkan kecap cair ke dalam kotak kardus tisu, wadah tersebut akan rusak dan dapur menjadi berantakan.\n\n"
            "Variabel memungkinkan programmer memberi nama yang mudah dipahami pada lokasi penyimpanan memori komputer tanpa perlu mengingat "
            "deretan angka biner atau heksadesimal. Namun analogi toples memiliki batasan penting yang bergantung pada bahasa:\n"
            "1. Di bahasa bertipe statis (seperti Dart atau C++), 'wadahnya' memiliki tipe tetap yang dikunci sejak awal deklarasi (`int x = 10;`). "
            "Sebaliknya, di bahasa bertipe dinamis (seperti Python atau JavaScript), variabel hanyalah label penunjuk yang bebas dipindahkan: "
            "pada satu baris label 'x' dapat menunjuk ke angka, lalu di baris berikutnya dipindahkan menunjuk ke teks string (`x = 10; x = 'halo'`).\n"
            "2. Variabel tipe referensi bukanlah toples fisik yang berat, melainkan kartu alamat penunjuk (pointer/reference); "
            "dua label nama berbeda bisa saja sama-sama memegang alamat yang menunjuk ke satu objek fisik yang sama di ruang memori."
        ),
        "problem_context": (
            "Pada tingkat perangkat keras murni, memori komputer (RAM) hanyalah deretan panjang sel biner bernilai 0 dan 1 tanpa label arti apa pun. "
            "Pola bit biner `01000001` dapat bermakna angka desimal 65, karakter huruf `'A'`, atau penggalan instruksi biner CPU. "
            "Tanpa sistem tipe data, prosesor dan compiler tidak memiliki cara untuk mengetahui berapa byte yang harus dibaca, "
            "bagaimana cara menafsirkannya, atau operasi apa yang sah dilakukan (misalnya, mengalikan dua huruf teks tentu tidak masuk akal). "
            "Variabel dan tipe data diciptakan sebagai kontrak keamanan dan makna semantik agar pemrosesan data di memori tetap teratur dan bebas salah tafsir."
        ),
        "explanation_technical": (
            "Secara arsitektural, variabel adalah binding simbolik antara sebuah identifier nama dengan nilai atau alamat di memori virtual. "
            "Sistem tipe data mengatur bagaimana bit ditafsirkan (misal two's complement untuk signed integer, IEEE-754 untuk floating point, UTF-8 untuk teks string) "
            "serta himpunan operasi yang diizinkan.\n\n"
            "Perbedaan krusial dalam sistem tipe dan alokasi memori:\n"
            "1. Bahasa Bertipe Statis vs Dinamis: Pada bahasa statis (Dart, TypeScript/C++), validasi kesesuaian tipe dilakukan oleh kompilator sebelum program berjalan. "
            "Pada bahasa dinamis (Python, JavaScript), tipe data terikat pada nilai/objek di runtime, bukan pada nama variabelnya.\n"
            "2. Alokasi Memori (Stack vs Heap) — Bukan Aturan Universal:\n"
            "- Pada bahasa tingkat rendah seperti C/C++, variabel primitif lokal dialokasikan di Call Stack dengan akses cepat, sedangkan objek dinamis dialokasikan di Heap. "
            "- Namun aturan ini BUKAN hukum mutlak di seluruh bahasa! Di Python, seluruh nilai adalah objek di Heap (bahkan angka kecil seperti `42` adalah alokasi `PyObject` di heap). "
            "- Di Dart dan Java, variabel primitif yang menjadi atribut (field) di dalam sebuah instance class atau tertangkap di dalam closure fungsi akan disimpan di Heap bersama objek pemiliknya. "
            "Mesin virtual modern juga menerapkan escape analysis untuk mengoptimasi alokasi objek ke stack atau register jika objek tidak lolos keluar dari fungsi lokal.\n"
            "3. Perbandingan Nilai vs Identitas Objek (`==`):\n"
            "Perilaku operator perbandingan sangat bervariasi antarbaha:\n"
            "- JavaScript/TypeScript: Operator `==` melakukan konversi tipe otomatis (type coercion: `'5' == 5` adalah true), sedangkan `===` memeriksa kesamaan nilai tanpa konversi. Namun untuk objek, `===` hanya memeriksa identitas referensi memori (`{a: 1} === {a: 1}` bernilai false).\n"
            "- Python: Operator `==` memanggil metode `__eq__()` untuk memeriksa kesamaan nilai konten (`[1, 2] == [1, 2]` bernilai True), sedangkan operator `is` memeriksa identitas referensi memori fisik (`id(a) == id(b)`).\n"
            "- Dart: Operator `==` memanggil method yang dapat di-override untuk memeriksa kesamaan nilai struktural, sedangkan fungsi bawaan `identical(a, b)` digunakan khusus untuk memeriksa apakah dua variabel menunjuk ke instans memori yang sama."
        ),
        "misconceptions": [
            {
                "misconception": "Operator == selalu membandingkan isi nilai secara sama di semua bahasa pemrograman.",
                "explanation": "Di JavaScript == melakukan pemaksaan konversi tipe implisit yang berbahaya; di Python == membandingkan nilai konten dan operator 'is' memeriksa identitas memori; di Dart == adalah method yang default-nya identitas referensi namun dapat di-override untuk kesamaan nilai.",
                "spot_in_code": "Mengira {a: 1} == {a: 1} bernilai true di JavaScript/TypeScript (padahal bernilai false karena alamat referensi memori berbeda)."
            },
            {
                "misconception": "Semua tipe primitif pasti disimpan di Stack dan semua objek pasti disimpan di Heap pada setiap bahasa.",
                "explanation": "Itu generalisasi dari C/C++; di Python setiap data (termasuk integer) adalah objek di heap; di Java dan Dart primitif yang menjadi field kelas tersimpan di heap bersama objek pembungkusnya.",
                "spot_in_code": "Mengasumsikan mendeklarasikan variabel angka di Python tidak memakan alokasi heap memori."
            },
            {
                "misconception": "Variabel selalu memiliki tipe data yang kaku dan tidak bisa berubah.",
                "explanation": "Pada bahasa dinamis seperti Python atau JavaScript, tipe data terikat pada nilai objek di memori, bukan pada variabelnya; variabel bebas diarahkan ke tipe data lain sewaktu-waktu.",
                "spot_in_code": "Menyangka kode Python x = 10; x = 'teks' akan memicu error kompilasi."
            }
        ],
        "when_to_use": (
            "Gunakan deklarasi tipe statis eksplisit pada aplikasi berskala besar untuk mendeteksi inkonsistensi tipe sejak fase kompilasi. "
            "Gunakan operator identitas ketat (=== di JavaScript, is di Python, atau identical() di Dart) saat ingin memverifikasi kesamaan instans memori murni. "
            "Gunakan variabel immutable (final/const) secara default untuk mencegah mutasi nilai yang tidak disengaja."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis kode perbandingan objek menggunakan == di JavaScript yang gagal saat memeriksa kesamaan konten, "
            "atau memicu bug type coercion yang fatal (seperti menganggap input form '50' sebagai angka padahal teks string, sehingga '50' + 10 menghasilkan '5010'). "
            "Saat vibecoding, teliti deklarasi variabel dan instruksikan AI sesuai konteks bahasa: "
            "'Gunakan perbandingan nilai yang tepat (gunakan deep equality untuk objek di JS/TS, atau override operator == di Dart), "
            "dan pastikan konversi tipe data masukan form dilakukan secara eksplisit sebelum operasi matematika!'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa perbandingan [1, 2] == [1, 2] bernilai True di Python namun [1, 2] === [1, 2] bernilai false di JavaScript?",
                "answer": "Karena di Python operator == memanggil metode __eq__ yang membandingkan isi elemen list secara struktural, sedangkan di JavaScript operator === pada tipe array/objek hanya membandingkan apakah kedua referensi menunjuk ke alamat memori fisik yang sama."
            },
            {
                "question": "Mengapa generalisasi bahwa 'primitif selalu di stack' tidak berlaku untuk bahasa seperti Python atau Dart?",
                "answer": "Karena di Python seluruh nilai adalah objek PyObject yang dialokasikan di heap, dan di Dart atau Java variabel primitif yang menjadi field dari suatu class akan tersimpan di heap bersama objek pemiliknya."
            }
        ]
    },

    "f-operators": {
        "summary": "Simbol untuk menghitung, membandingkan, dan mengolah nilai.",
        "explanation_simple": (
            "Bayangkan tanda timbangan neraca dan kalkulator saku di meja kasir. Operator aritmatika seperti tambah (+) dan kali (*) "
            "menghitung total tagihan belanjaanmu. Operator perbandingan seperti lebih besar (>) memastikan apakah uang pembayaranmu cukup. "
            "Operator logika seperti DAN (AND) memeriksa apakah toko sedang buka DAN stok barang masih tersedia.\n\n"
            "Operator adalah kata kerja dalam bahasa pemrograman yang memanipulasi operand (kata benda/nilai). "
            "Batas analoginya: kalkulator biasa menghitung secara langsung dari kiri ke kanan sesuai tombol yang kamu tekan, "
            "sedangkan bahasa pemrograman memiliki aturan presedensi (hirarki prioritas operasi) yang ketat, serta mekanisme efisiensi "
            "seperti short-circuit evaluation yang bisa membatalkan evaluasi sebelah kanan jika hasil sebelah kiri sudah menentukan."
        ),
        "problem_context": (
            "Sebelum adanya operator terstandarisasi dalam bahasa tingkat tinggi, programmer harus memprogram rangkaian gerbang logika "
            "(AND, OR, NOT, XOR) dan instruksi aritmatika ALU (Arithmetic Logic Unit) seperti ADD, SUB, dan CMP secara manual di tingkat assembly. "
            "Masalah besar muncul ketika ekspresi matematika panjang seperti perhitungan lintasan fisika harus ditulis dalam puluhan baris "
            "perintah register sementara. Kesalahan kecil dalam urutan eksekusi gerbang logika menghasilkan nilai kalkulasi yang melenceng drastis."
        ),
        "explanation_technical": (
            "Operator menerima satu (unary), dua (binary), atau tiga (ternary) operand untuk menghasilkan nilai baru. "
            "Kategori operator meliputi: Aritmatika (+, -, *, /, %), Perbandingan (==, !=, <, >, <=, >=), Logika (&&, ||, !), "
            "Bitwise (&, |, ^, ~, <<, >>), dan Assignment (=, +=, -=).\n\n"
            "Evaluasi operator dipandu oleh Operator Precedence (tingkat prioritas, misalnya perkalian dievaluasi sebelum penjumlahan) "
            "dan Associativity (arah evaluasi dari kiri-ke-kanan atau kanan-ke-kiri). Fitur penting lainnya adalah Short-circuit evaluation pada operator boolean: "
            "pada ekspresi (A && B), jika A bernilai false, B tidak akan pernah dieksekusi karena keseluruhan ekspresi sudah pasti false. "
            "Bahasa modern juga membedakan perbandingan identitas referensi (=== di TS/JS atau identical() di Dart) dengan kesetaraan struktural nilai (==)."
        ),
        "misconceptions": [
            {
                "misconception": "Operator == dan === di JavaScript/TypeScript bekerja dengan cara yang sama.",
                "explanation": "== melakukan pemaksaan tipe (type coercion) implisit yang berbahaya (misalnya '0' == false bernilai true), sedangkan === membandingkan tipe dan nilai secara ketat.",
                "spot_in_code": "Menggunakan if (input == false) yang secara tak sengaja mencocokkan string kosong '' atau angka 0."
            },
            {
                "misconception": "Operator pembagian integer selalu menghasilkan nilai pecahan desimal.",
                "explanation": "Di banyak bahasa seperti C, Java, atau operator ~/ di Dart, pembagian dua integer memotong sisa pecahan (truncation) dan menghasilkan integer bulat ke bawah.",
                "spot_in_code": "Perhitungan 5 / 2 yang menghasilkan 2 alih-alih 2.5 pada konteks integer division."
            }
        ],
        "when_to_use": (
            "Gunakan tanda kurung buka-tutup () secara eksplisit dalam ekspresi majemuk untuk memperjelas niat kode tanpa bergantung pada ingatan presedensi. "
            "Manfaatkan short-circuit evaluation untuk guard clauses (misalnya user != null && user.isActive). "
            "Hindari ekspresi baris tunggal yang terlalu padat dengan operator ternary bersarang."
        ),
        "why_vibecoding_matters": (
            "AI sering kali menghasilkan kondisi if dengan operator perbandingan longgar atau presedensi logika yang rancu "
            "(seperti A || B && C yang dievaluasi sebagai A || (B && C) padahal maksud pengguna adalah (A || B) && C). "
            "Saat vibecoding, tanyakan ke AI: 'Tolong beri tanda kurung eksplisit pada ekspresi boolean ini dan jelaskan apakah ada evaluasi short-circuit yang berpotensi melewatkan pemanggilan fungsi penting.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa ekspresi (obj != null && obj.length > 0) tidak menghasilkan error null pointer saat obj bernilai null?",
                "answer": "Karena operator && menerapkan short-circuit: ketika operand kiri (obj != null) bernilai false, operand kanan tidak pernah dieksekusi."
            },
            {
                "question": "Apa perbedaan hasil antara operator kesetaraan nilai struktural dan kesetaraan alamat referensi?",
                "answer": "Kesetaraan nilai struktural memeriksa apakah konten data di dalam objek sama, sedangkan kesetaraan referensi memeriksa apakah kedua variabel menunjuk ke alamat memori yang persis sama di heap."
            }
        ]
    },

    "f-conditionals": {
        "summary": "Membuat keputusan dalam program berdasarkan kondisi benar atau salah.",
        "explanation_simple": (
            "Bayangkan rel kereta api dengan tuas wesel pemindah jalur di persimpangan. Ketika kereta melaju, masinis melihat lampu sinyal: "
            "jika lampu berwarna hijau, tuas mengarahkan kereta ke jalur utama; jika lampu merah, kereta diarahkan ke jalur pemberhentian darurat. "
            "Percabangan (conditionals) dalam kode bekerja seperti wesel rel kereta tersebut.\n\n"
            "Kondisi mengevaluasi apakah suatu pernyataan bernilai benar (true) atau salah (false) pada detik eksekusi, lalu memilih satu lorong instruksi "
            "dan mengabaikan lorong lainnya. Batas analogi ini: rel fisik hanya bisa dilalui satu kereta dalam satu waktu, sedangkan program komputer "
            "bisa bercabang di dalam cabang (nested) atau mengevaluasi puluhan kondisi dalam hitungan mikrodetik."
        ),
        "problem_context": (
            "Tanpa percabangan, program komputer hanya mampu mengeksekusi instruksi linear dari baris pertama sampai terakhir persis sama untuk setiap input. "
            "Program kasir tidak akan bisa membedakan pelanggan VIP yang berhak diskon dengan pelanggan umum. Program login tidak bisa menolak kata sandi salah. "
            "Kebutuhan untuk merespons kondisi dunia nyata yang dinamis menuntut adanya instruksi kondisional di tingkat instruksi mesin."
        ),
        "explanation_technical": (
            "Secara teknis, percabangan mengubah alur eksekusi dari yang biasanya mengalir lurus ke bawah menjadi melompat ke blok kode tertentu jika suatu kondisi pengujian bernilai true. "
            "Jika kondisi bernilai false, blok tersebut dilewati dan program langsung lanjut ke cabang alternatif (else) atau ke baris berikutnya.\n\n"
            "Konstruksi percabangan mencakup struktur if, else if, else, serta switch-case. "
            "Praktek arsitektur modern sangat menganjurkan pola Guard Clauses (Early Return), di mana kondisi kegagalan atau validasi batas "
            "diperiksa dan dihentikan di baris-baris awal fungsi, sehingga logika utama tidak tertimbun di dalam piramida kurung kurawal yang menjorok terlalu dalam. "
            "Konsep truthy dan falsy pada bahasa bertipe dinamis (seperti 0, '', null, undefined di JavaScript) juga harus diwaspadai karena konversi otomatis dapat meloloskan percabangan tak terduga."
        ),
        "misconceptions": [
            {
                "misconception": "Semua blok if-else if pasti mengevaluasi seluruh kondisi yang tertulis di dalamnya.",
                "explanation": "Begitu satu kondisi bernilai true ditemukan, blok kodenya dieksekusi dan seluruh cabang else if serta else di bawahnya langsung dilewati.",
                "spot_in_code": "Menaruh kondisi yang lebih umum di atas kondisi yang sangat spesifik, sehingga kondisi spesifik tidak pernah tercapai."
            },
            {
                "misconception": "Piramida percabangan bersarang 5 tingkat ke dalam adalah hal wajar dalam menangani validasi kompleks.",
                "explanation": "Nesting berlebihan menurunkan keterbacaan kode secara drastis (cognitive overload) dan meningkatkan risiko unhandled edge-cases; gunakan Guard Clauses.",
                "spot_in_code": "Struktur if { if { if { ... } } } yang menjorok sangat dalam ke kanan."
            }
        ],
        "when_to_use": (
            "Gunakan if/else sederhana untuk keputusan 1-2 cabang berbasis kondisi boolean dinamis. "
            "Gunakan switch-case atau pattern matching jika membandingkan satu variabel diskrit terhadap banyak nilai enum atau state tetap. "
            "Terapkan early return guard clauses di awal fungsi untuk memvalidasi masukan kotor sebelum memproses logika inti."
        ),
        "why_vibecoding_matters": (
            "AI sering menghasilkan kode dengan nesting percabangan yang sangat dalam dan lupa menangani kondisi fallback else (misalnya skenario ketika server mengembalikan status 500 alih-alih 200). "
            "Saat mereview kode buatan AI, periksa setiap percabangan: 'Apakah semua kemungkinan nilai ekstrim (null, string kosong, array kosong) sudah di-guard? "
            "Refactor kode ini menggunakan early return guard clauses agar alur utamanya mendatar.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa teknik Guard Clause (Early Return) lebih disukai daripada percabangan if-else bersarang?",
                "answer": "Karena guard clause menyingkirkan kasus gagal/ekstrim di awal dan mengurangi kedalaman indentasi, sehingga alur positif utama program dapat dibaca lurus secara linear."
            },
            {
                "question": "Kapan sebaiknya kita menggunakan struktur switch-case dibandingkan dengan if-else if?",
                "answer": "Gunakan switch-case saat memeriksa satu variabel diskrit terhadap banyak pilihan tetap yang pasti (seperti status pesanan atau enum), dan gunakan if-else if jika setiap cabang memerlukan evaluasi kondisi logika majemuk atau rentang nilai yang berbeda-beda."
            }
        ]
    },

    "f-loops": {
        "summary": "Mengulang perintah berkali-kali sampai batas yang ditentukan.",
        "explanation_simple": (
            "Bayangkan ban berjalan di pabrik pengemasan botol minuman. Setiap kali sebuah botol lewat di depan sensor, "
            "lengan robot menutup tutup botol, lalu konveyor bergeser satu langkah ke botol berikutnya. Proses ini diulang "
            "terus menerus sampai sensor mendeteksi kardus penampung sudah terisi 24 botol, lalu konveyor berhenti.\n\n"
            "Perulangan (loops) mengotomatisasi pekerjaan repetitif agar programmer tidak perlu menuliskan 1.000 baris instruksi yang identik. "
            "Batas analogi pabrik ini: lengan robot pabrik dibatasi oleh kecepatan motor mekanik fisik, sedangkan perulangan komputer dapat "
            "berjalan jutaan kali per detik. Namun, jika sensor penghitung botol rusak dan tidak pernah mencapai angka 24, "
            "mesin akan terjebak dalam putaran abadi (infinite loop) yang membekukan seluruh sistem."
        ),
        "problem_context": (
            "Bayangkan sebuah bank yang harus memproses perhitungan bunga bulanan untuk 500.000 nasabah. "
            "Jika bahasa pemrograman tidak menyediakan mekanisme perulangan, insinyur software harus menyalin baris perhitungan bunga sebanyak 500.000 kali di kode sumber. "
            "File kode akan berukuran puluhan megabyte, tidak mungkin diperbaiki jika ada perubahan rumus, dan memboroskan memori instruksi program."
        ),
        "explanation_technical": (
            "Secara teknis, perulangan bekerja dengan cara memeriksa kondisi pengujian sebelum atau sesudah blok kode dijalankan. "
            "Selama kondisi bernilai true, komputer akan mengeksekusi isi blok dan kembali lagi ke langkah pengujian berikutnya. "
            "Tiga struktur perulangan standar meliputi:\n"
            "1. for loop: digunakan ketika jumlah iterasi sudah diketahui sejak awal (mengelola inisialisasi, kondisi batas, dan penambahan nilai hitungan).\n"
            "2. while loop: digunakan ketika pengulangan bergantung pada kondisi eksternal yang belum pasti kapan berubahnya (kondisi dicek sebelum blok berjalan).\n"
            "3. do-while loop: menjamin tubuh kode dieksekusi minimal satu kali sebelum kondisi diperiksa.\n\n"
            "Dalam eksekusi loop, kata kunci break digunakan untuk keluar seketika dari perulangan, sedangkan continue melewati sisa blok iterasi saat ini "
            "dan langsung melompat ke putaran berikutnya. Kesalahan paling fatal pada loop adalah infinite loop (di mana variabel kondisi tidak pernah mencapai batas berhenti sehingga program macet) "
            "dan off-by-one error (perulangan kelebihan atau kekurangan satu langkah karena keliru menggunakan operator < versus <=)."
        ),
        "misconceptions": [
            {
                "misconception": "Perulangan while dan for memiliki kapabilitas komputasi yang berbeda.",
                "explanation": "Secara teoritis keduanya setara (Turing-complete) dan dapat saling menggantikan; perbedaannya hanya pada ergonomi sintaksis inisialisasi dan inkremen penghitung.",
                "spot_in_code": "Memaksakan for dengan parameter kosong for (; kondisi ;) padahal while (kondisi) jauh lebih bersih."
            },
            {
                "misconception": "Off-by-one error hanyalah ketidaktelitian sepele yang tidak berdampak besar.",
                "explanation": "Off-by-one error adalah penyebab utama out-of-bounds memory access yang dapat memicu crash aplikasi fatal atau celah keamanan buffer overflow.",
                "spot_in_code": "Menulis for (let i = 0; i <= array.length; i++) di mana indeks terakhir melebihi batas array."
            }
        ],
        "when_to_use": (
            "Gunakan for-in atau for-of modern saat mengiterasi elemen koleksi (Array/List/Map) untuk menghindari kesalahan manajemen indeks manual. "
            "Gunakan while saat membaca data stream atau polling status jaringan yang durasinya tak tentu. "
            "Gunakan break dan continue secara terukur; jika logika loop terlalu rumit, pertimbangkan metode fungsional seperti map, filter, atau forEach."
        ),
        "why_vibecoding_matters": (
            "Asisten AI sering menghasilkan perulangan while tanpa jaminan perubahan variabel kontrol di dalam blok catch/error, "
            "sehingga ketika API gagal merespons, aplikasi terjebak dalam infinite loop yang memakan 100% CPU. "
            "Saat vibecoding, teliti batas akhir loop dan tanyakan ke AI: 'Apakah loop ini memiliki batas maksimum iterasi (timeout/guard) "
            "untuk mencegah infinite loop jika koneksi gagal?'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa indeks array pada sebagian besar bahasa pemrograman modern dimulai dari 0 dan bukan 1?",
                "answer": "Karena angka indeks merepresentasikan offset (jarak pergeseran memori) dari alamat awal array: elemen pertama berada pada offset 0 dari alamat dasar pointer."
            },
            {
                "question": "Bagaimana cara mendeteksi potensi infinite loop dalam suatu blok while loop?",
                "answer": "Periksa apakah ada jalur percabangan di dalam tubuh loop di mana variabel kondisi tidak dimutasi menuju titik terminasi, atau tambahkan counter pembatas iterasi maksimum."
            }
        ]
    },

    "f-pattern-matching": {
        "summary": "Mencocokkan bentuk data dan mengambil isinya secara rapi.",
        "explanation_simple": (
            "Bayangkan mesin penyortir surat canggih di kantor pos pusat. Surat masuk tidak hanya diperiksa warna amplopnya, "
            "tetapi mesin langsung memindai bentuknya: jika berbentuk kotak paket dengan berat di atas 2 kg, kirim ke loket kargo; "
            "jika amplop cokelat dengan kode pos berawalan '10', masukkan ke tas kurir Jakarta Pusat sekaligus buka amplop untuk membaca nama penerima.\n\n"
            "Pattern matching bekerja seperti penyortir cerdas ini: ia mencocokkan bentuk struktur data, memvalidasi tipenya, "
            "dan mengekstrak variabel di dalamnya dalam satu langkah deklaratif yang elegan. "
            "Batas analoginya: penyortir pos manual bisa melewatkan surat yang rusak, sedangkan pattern matching modern pada compiler "
            "akan memberikan peringatan keras jika ada kemungkinan bentuk data yang belum kamu tangani (exhaustiveness checking)."
        ),
        "problem_context": (
            "Sebelum fitur pattern matching diadopsi secara luas, programmer harus menulis rentetan panjang if-else yang penuh "
            "dengan type casting manual dan pengecekan properti bertingkat (misalnya: periksa apakah data adalah objek JSON, "
            "lalu periksa apakah properti 'user' ada, lalu periksa apakah 'user' memiliki 'address', lalu cast tipe datanya). "
            "Kode menjadi sangat rapuh, sulit dibaca, dan rentan terhadap runtime null pointer exception jika satu properti terlewat divalidasi."
        ),
        "explanation_technical": (
            "Pattern matching adalah fitur deklaratif yang memadukan pengujian struktur (structure testing), pemeriksaan tipe (type discrimination), "
            "dan destructuring (ekstraksi komponen data ke variabel baru) dalam satu operasi ekspresi.\n\n"
            "Diperkenalkan pada bahasa fungsional dan kini hadir di Dart (sejak Dart 3), TypeScript (via discriminated unions), Python (match-case sejak 3.10), "
            "dan Rust. Keunggulan utamanya adalah Exhaustiveness Checking pada compile-time: jika kamu mencocokkan nilai dari sebuah enum atau sealed class, "
            "compiler akan memaksa programmer menangani setiap varian kasus yang mungkin terjadi. Jika kamu menambah varian baru di kemudian hari, "
            "compiler langsung menunjukkan titik-titik kode mana saja yang belum diperbarui."
        ),
        "misconceptions": [
            {
                "misconception": "Pattern matching hanyalah penulisan lain dari switch-case biasa di bahasa C lama.",
                "explanation": "Switch tradisional hanya mencocokkan nilai skalar primitif sederhana (integer/string), sedangkan pattern matching mampu membongkar struktur objek kompleks, tuple, list, dan tipe data aljabar sekaligus mengikat variabel lokal baru.",
                "spot_in_code": "Mengira match hanya bisa switch (angka) dan tidak menyadari kemampuan match Case (Point(x: var x, y: 0))."
            },
            {
                "misconception": "Menambahkan klausa default / wildcard (_) selalu merupakan praktek terbaik.",
                "explanation": "Pada sealed class atau enum terbatas, memasang wildcard default mematikan fitur exhaustiveness checking kompilator sehingga penambahan tipe baru tidak terdeteksi otomatis.",
                "spot_in_code": "Memasang case _: return; pada pattern matching sealed class state management."
            }
        ],
        "when_to_use": (
            "Gunakan pattern matching saat memproses state aplikasi yang kompleks (seperti Success, Loading, Error state pada Flutter Bloc/Riverpod). "
            "Gunakan untuk mendestrukturisasi respons payload API JSON yang memiliki beberapa kemungkinan skema. "
            "Hindari jika kamu hanya membutuhkan perbandingan boolean biner true/false yang sederhana."
        ),
        "why_vibecoding_matters": (
            "AI sering kali menulis serangkaian if isinstance / if typeof bertingkat yang rawan terlewat menangani skenario edge-case. "
            "Mintalah AI memanfaatkan pattern matching modern: 'Gunakan pattern matching dengan sealed class atau discriminated unions "
            "agar compiler menjamin semua kemungkinan varian state tertangani tanpa ada celah runtime error.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa exhaustiveness checking pada pattern matching sangat bernilai saat melakukan refactoring kode?",
                "answer": "Karena saat developer menambah varian baru pada tipe data, compiler akan memunculkan error di semua ekspresi match yang belum menangani varian baru tersebut, mencegah bug unhandled state."
            },
            {
                "question": "Apa peran destructuring di dalam sebuah ekspresi pattern matching?",
                "answer": "Destructuring secara otomatis membongkar bagian dalam struktur objek/koleksi dan langsung mengikat nilainya ke variabel lokal baru dalam satu langkah deklaratif."
            }
        ]
    },

    "f-functions": {
        "summary": "Membungkus langkah kerja berulang ke dalam satu perintah bernama.",
        "explanation_simple": (
            "Bayangkan resep pembuatan adonan roti di dapur toko roti. Daripada kepala koki mendiktekan takaran terigu, ragi, "
            "dan air setiap kali pesanan baru tiba, resep tersebut dicetak pada selembar kartu bernama 'buatAdonan(jumlahPorsi)'. "
            "Setiap pembuat roti cukup memanggil nama resep tersebut sambil menyerahkan angka berapa porsi yang diinginkan, "
            "dan di akhir proses mereka menerima adonan kalis yang siap dipanggang.\n\n"
            "Fungsi (functions) adalah blok pembangun paling esensial dalam rekayasa perangkat lunak. "
            "Ia membungkus algoritma tertentu sehingga dapat digunakan berulang kali dari berbagai sudut aplikasi tanpa menulis ulang kode. "
            "Batas analogi resep: resep dapur bisa menghasilkan rasa berbeda tergantung suhu tangan koki, sedangkan fungsi murni (pure function) "
            "di komputer bersifat deterministik: input argumen yang sama dijamin 100% selalu menghasilkan nilai kembalian yang sama persis."
        ),
        "problem_context": (
            "Pada masa awal pemrograman dengan instruksi GOTO dan baris bernomor (seperti BASIC kuno), seluruh logika program bercampur "
            "dalam satu aliran linear raksasa (spaghetti code). Jika rumus perhitungan pajak harus digunakan di 15 tempat berbeda, rumus itu disalin 15 kali. "
            "Ketika undang-undang perpajakan berganti, programmer harus mencari dan memperbarui 15 lokasi tersebut satu per satu. "
            "Satu lokasi saja terlewat, pembukuan perusahaan rusak dan timbul audit hukum. Konsep subrutin atau fungsi diciptakan untuk mengatasi bencana redundansi ini."
        ),
        "explanation_technical": (
            "Ketika sebuah fungsi dipanggil (function invocation), sistem operasi dan runtime mengalokasikan Stack Frame baru di Call Stack. "
            "Stack frame ini menampung alamat kembalian instruksi (return address), nilai parameter aktual (argumen), dan alokasi variabel lokal fungsi. "
            "Ketika eksekusi mencapai instruksi return, nilai kembalian diserahkan kembali ke pemanggil, stack frame dimusnahkan (popped), "
            "dan Program Counter CPU melompat kembali ke return address untuk melanjutkan eksekusi program pemanggil.\n\n"
            "Parameter adalah variabel yang terdaftar di deklarasi fungsi, sedangkan argumen adalah nilai nyata yang dikirimkan saat pemanggilan. "
            "Dalam arsitektur modern, fungsi dibedakan menjadi: "
            "1. Pure Functions: tidak memiliki side-effects (tidak mengubah variabel global atau I/O) dan deterministik. "
            "2. Impure Functions: melakukan operasi I/O, mutasi state global, atau bergantung pada waktu/angka acak. "
            "Fungsi juga dapat menjadi First-Class Citizens: dapat disimpan dalam variabel, dikirim sebagai argumen (callback), "
            "dan dikembalikan dari fungsi lain (Higher-Order Functions)."
        ),
        "misconceptions": [
            {
                "misconception": "Parameter dan Argumen adalah dua istilah yang merujuk pada hal yang persis sama.",
                "explanation": "Parameter adalah nama variabel placeholder pada tanda tangan (signature) fungsi, sedangkan argumen adalah nilai konkret yang dipasok saat fungsi dipanggil.",
                "spot_in_code": "Tertukar istilah saat mendiskusikan tanda tangan void hitung(int x) (parameter) vs hitung(10) (argumen)."
            },
            {
                "misconception": "Fungsi yang tidak memiliki return statement tidak melakukan apa-apa di memori.",
                "explanation": "Fungsi void tetap membuat stack frame, dapat mengeksekusi operasi side-effects (seperti menyimpan data ke database), dan mengembalikan nilai khusus seperti void, None, atau undefined.",
                "spot_in_code": "Mengharapkan let hasil = simpanData() bernilai objek padahal fungsinya bertipe void."
            },
            {
                "misconception": "Menulis fungsi raksasa sepanjang 300 baris lebih efisien daripada memecahnya menjadi fungsi-fungsi kecil.",
                "explanation": "Fungsi raksasa sangat sulit diuji, mustahil dipahami secara modular, dan memperbesar risiko bug side-effect tersembunyi; compiler modern mampu melakukan function inlining otomatis.",
                "spot_in_code": "Satu fungsi prosesCheckout() yang menangani validasi, pemotongan stok, panggilan payment gateway, dan kirim email."
            }
        ],
        "when_to_use": (
            "Terapkan prinsip Single Responsibility Principle: satu fungsi harus mengerjakan satu tugas saja dengan baik. "
            "Gunakan pure function untuk semua kalkulasi transformasi data dan logika bisnis agar mudah diuji dengan unit test. "
            "Pecah fungsi yang panjangnya melebihi 30-40 baris menjadi fungsi-fungsi pembantu (helper functions) yang memiliki nama deskriptif."
        ),
        "why_vibecoding_matters": (
            "AI gemar menghasilkan fungsi monolitik raksasa yang mencampuradukkan manipulasi antarmuka pengguna, pembacaan database, dan perhitungan bisnis dalam satu tempat. "
            "Kode semacam ini sangat rapuh saat kamu meminta perubahan kecil. "
            "Terapkan disiplin vibecoding: 'Pecah kode ini menjadi fungsi-fungsi murni kecil dengan batasan parameter yang jelas, "
            "tipe data kembalian eksplisit, dan pisahkan operasi side-effects ke lapisan terpisah.'"
        ),
        "reflection_questions": [
            {
                "question": "Apa yang terjadi pada stack memory ketika pemanggilan fungsi bertingkat berjalan terlalu dalam tanpa henti?",
                "answer": "Alokasi stack frame akan melebihi batas kapasitas Call Stack yang dialokasikan oleh sistem operasi, memicu kesalahan Stack Overflow crash."
            },
            {
                "question": "Mengapa pure function jauh lebih mudah diuji dalam unit test dibandingkan impure function?",
                "answer": "Karena pure function tidak membutuhkan mocking database atau reset state global; pengujian cukup mengirim input parameter dan memeriksa output return value."
            }
        ]
    },

    "f-scope": {
        "summary": "Wilayah dan batas waktu hidup variabel di dalam kode.",
        "explanation_simple": (
            "Bayangkan sebuah gedung perkantoran bertingkat dengan kartu akses ruangan. Barang yang diletakkan di lobi utama gedung (Global Scope) "
            "dapat dilihat dan diambil oleh siapa saja yang berada di dalam gedung. Namun, berkas rahasia yang disimpan di dalam ruang rapat lantai 4 (Local Scope) "
            "hanya bisa diakses oleh orang yang berada di dalam ruangan tersebut. Orang luar tidak bisa melihat apa yang ada di dalam ruang rapat.\n\n"
            "Scope menentukan di mana sebuah variabel 'hidup' dan dari mana saja variabel tersebut sah untuk dibaca atau diubah. "
            "Batas analogi gedung ini: di dunia nyata, jika kamu keluar ruangan, barang di dalam ruangan tetap ada di meja. "
            "Dalam komputasi, begitu eksekusi fungsi selesai keluar dari ruangannya, seluruh variabel lokal di dalamnya otomatis dimusnahkan dari memori, "
            "kecuali jika dipertahankan oleh mekanisme khusus bernama Closure."
        ),
        "problem_context": (
            "Pada bahasa pemrograman awal yang hanya mengenal variabel global (seperti dialek assembly atau BASIC purba), "
            "setiap variabel dapat ditimpa dari baris program mana pun. Jika fungsi pencetakan nota memakai variabel penghitung 'i' dan "
            "fungsi perhitungan diskon juga memakai 'i', kedua fungsi tersebut akan saling merusak nilai penghitung satu sama lain. "
            "Bug misterius ini memicu lahirnya batasan lingkup (Scoping) untuk mengisolasi kehidupan data antar-komponen program."
        ),
        "explanation_technical": (
            "Sebagian besar bahasa modern mengadopsi Lexical Scoping (Static Scoping): batasan lingkup ditentukan oleh posisi fisik kode bersarang "
            "pada saat penulisan kode sumber, bukan berdasarkan urutan pemanggilan dinamis saat runtime. "
            "Ketika sebuah identifier dicari, compiler/runtime menelusuri Scope Chain dari lingkup terdalam (Block/Function Scope) "
            "bergerak keluar ke Outer Scope hingga ke Global Scope. Jika tidak ditemukan di tingkat global, error ReferenceError/undeclared identifier dimunculkan.\n\n"
            "Closure adalah kombinasi antara sebuah fungsi dan lexical environment tempat fungsi tersebut dideklarasikan. "
            "Closure memungkinkan fungsi inner tetap mempertahankan akses ke variabel lokal milik fungsi outer pembungkusnya, "
            "meskipun fungsi outer tersebut sudah selesai dieksekusi dan stack framenya telah ditutup. "
            "Dalam kasus ini, variabel yang tertangkap (captured variable) dipindahkan dari stack ke heap memory agar tidak terhapus."
        ),
        "misconceptions": [
            {
                "misconception": "Variabel global adalah cara paling praktis untuk berbagi data antarfungsi tanpa repot passing parameter.",
                "explanation": "Variabel global menciptakan ketergantungan tersembunyi (spooky action at a distance), membuat alur data tidak dapat dilacak, memicu race conditions pada multithreading, dan menyulitkan testing.",
                "spot_in_code": "Mendeklarasikan let currentUser atau var temp di root file yang diubah-ubah oleh puluhan fungsi."
            },
            {
                "misconception": "Closure otomatis menyebabkan memory leak di setiap aplikasi.",
                "explanation": "Closure adalah fitur fundamental yang aman jika variabel yang dipertahankan memang dibutuhkan; memory leak hanya terjadi jika closure memegang referensi objek besar yang tidak lagi dipakai tanpa pernah dilepas.",
                "spot_in_code": "Memasang event listener closure yang menangkap objek DOM besar tanpa pernah memanggil removeEventListener."
            }
        ],
        "when_to_use": (
            "Batasi cakupan variabel sekecil mungkin (Principle of Least Privilege): deklarasikan variabel sedekat mungkin dengan tempat ia digunakan. "
            "Gunakan closure untuk data encapsulation (menyembunyikan variabel private sebelum adanya sintaks class private field). "
            "Hindari penggunaan variabel global untuk data yang sering mengalami mutasi state."
        ),
        "why_vibecoding_matters": (
            "AI sering kali meletakkan variabel penampung sementara di lingkup file global untuk jalan pintas agar kode bisa berjalan cepat. "
            "Hal ini memicu bug aneh saat fungsi dipanggil untuk kedua kalinya karena state kotor sebelumnya masih tersisa. "
            "Saat vibecoding, instruksikan AI: 'Pastikan semua variabel dideklarasikan di lingkup lokal fungsi terkecil, "
            "dan jangan ada variabel state yang bocor ke lingkup modul global.'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa variabel yang ditangkap oleh closure tidak terhapus saat fungsi pembungkusnya selesai dieksekusi?",
                "answer": "Karena compiler mengalokasikan variabel captured tersebut di heap memory (bukan di call stack) dan runtime mempertahankan referensi selama fungsi closure masih hidup."
            },
            {
                "question": "Apa bahaya dari variabel shadowing (mendeklarasikan variabel lokal dengan nama yang persis sama dengan variabel di outer scope)?",
                "answer": "Variabel lokal akan menutupi variabel outer scope, sehingga programmer berisiko salah membaca atau tidak sengaja memodifikasi variabel yang keliru."
            }
        ]
    },

    "f-type-system": {
        "summary": "Aturan jenis data agar program tidak salah mengolah nilai.",
        "explanation_simple": (
            "Bayangkan pemeriksaan paspor di terminal imigrasi bandara internasional. Setiap paspor memiliki stempel kategori visa: "
            "turis, pekerja ahli, atau diplomat. Petugas imigrasi di gerbang memeriksa paspor sebelum penumpang diizinkan naik pesawat. "
            "Jika seorang turis mencoba bekerja di negara tujuan, aturan imigrasi langsung menolaknya di gerbang sebelum terjadi pelanggaran hukum.\n\n"
            "Sistem tipe (Type System) bertindak sebagai petugas imigrasi kode komputermu. Ia memeriksa apakah operasi yang ingin kamu jalankan "
            "pada sebuah data sah dan sesuai dengan kategori tipe data tersebut. "
            "Batas analogi imigrasi: ada bandara dengan pemeriksaan ketat di muka (Static Typing: periksa sebelum terbang), "
            "dan ada bandara yang mengizinkan siapa saja mendarat lalu baru menangkap pelanggar saat mereka sudah berada di jalan raya (Dynamic Typing: periksa saat program berjalan)."
        ),
        "problem_context": (
            "Tanpa sistem tipe formal, semua data di memori komputer hanyalah deretan biner 0 dan 1 yang anonim. "
            "Sebuah program dapat secara tidak sengaja mencoba membagi teks nama orang dengan angka tanggal lahir, "
            "mengakibatkan prosesor membaca alamat memori acak dan merusak data sistem operasi. "
            "Kerusakan finansial miliaran rupiah dan kegagalan peluncuran roket luar angkasa (seperti roket Ariane 5 yang meledak tahun 1996) "
            "banyak diakibatkan oleh konversi tipe data yang meluap (overflow) tanpa pemeriksaan ketat sistem tipe."
        ),
        "explanation_technical": (
            "Sistem tipe adalah kumpulan aturan traktat logika yang menetapkan properti 'tipe' pada konstruksi program (seperti variabel, ekspresi, fungsi). "
            "Dua dimensi utama klasifikasi sistem tipe adalah: "
            "1. Static vs Dynamic: Static Typing (Dart, TypeScript, Rust) memeriksa keabsahan tipe saat compile-time sebelum kode dijalankan. "
            "Dynamic Typing (Python, JavaScript murni) mengikat tipe ke nilai objek saat runtime.\n"
            "2. Strong vs Weak: Strong Typing menolak pemaksaan operasi antar-tipe yang tidak cocok tanpa konversi eksplisit (Python adalah strongly typed, tidak mengizinkan '5' + 5). "
            "Weak Typing melakukan pemaksaan tipe implisit (JavaScript mengizinkan '5' - 2 menghasilkan 3 dan '5' + 2 menghasilkan '52').\n\n"
            "Perkembangan penting lainnya adalah Sound Null Safety (seperti pada Dart dan Kotlin), di mana sistem tipe membedakan secara tegas tipe yang boleh bernilai null (String?) "
            "dengan tipe non-nullable (String), melenyapkan error legendaris NullPointerException di tingkat kompilasi."
        ),
        "misconceptions": [
            {
                "misconception": "Python adalah bahasa yang lemah sistem tipenya (weakly typed).",
                "explanation": "Python adalah bahasa dinamis yang bertipe kuat (Strongly Typed): Python memeriksa tipe di runtime dan menolak operasi seperti 'apel' + 5 dengan TypeError.",
                "spot_in_code": "Mengira Python akan mengonversi angka ke teks secara otomatis seperti JavaScript."
            },
            {
                "misconception": "TypeScript menjamin keamanan tipe 100% saat aplikasi berjalan di browser pengguna.",
                "explanation": "TypeScript hanyalah alat kompilasi static analysis; setelah dikompilasi ke JavaScript, seluruh anotasi tipe dihapus (type erasure) dan tidak ada validasi runtime otomatis terhadap data API mentah.",
                "spot_in_code": "Menganggap data yang diterima dari fetch() pasti sesuai interface TypeScript tanpa validasi runtime seperti Zod."
            }
        ],
        "when_to_use": (
            "Gunakan bahasa bertipe statis dengan sound null safety untuk membangun aplikasi produksi berskala menengah hingga besar yang melibatkan banyak kolaborator. "
            "Gunakan type inference (seperti var atau final tanpa menulis ulang tipe berulang) untuk menjaga kode tetap bersih tanpa mengorbankan keamanan statis. "
            "Pasang validasi skema runtime (seperti zod atau form validation) di setiap gerbang I/O jaringan."
        ),
        "why_vibecoding_matters": (
            "AI yang diprompt secara sembarangan sering kali menggunakan operator non-null assertion (!) atau type casting paksa (as any) "
            "hanya agar pesan error compiler merah menghilang dari layar IDE. Hal ini menipu developer dan memindahkan ledakan error ke runtime pengguna. "
            "Saat vibecoding, instruksikan AI: 'Perbaiki error tipe dengan cara menyelesaikan akar masalah penanganan null atau konversi tipe, "
            "jangan pernah menggunakan cast paksa as any atau force unwrap !.'"
        ),
        "reflection_questions": [
            {
                "question": "Apa perbedaan antara type checking pada compile-time dan type checking pada runtime?",
                "answer": "Compile-time checking menganalisis kode sumber sebelum program dijalankan dan menolak build jika ada inkonsistensi tipe, sedangkan runtime checking memeriksa tipe data aktual di memori saat instruksi sedang dieksekusi."
            },
            {
                "question": "Mengapa Tony Hoare menyebut penemuan 'null pointer' sebagai 'billion-dollar mistake'?",
                "answer": "Karena mengizinkan referensi null tanpa pengecekan tipe statis telah menyebabkan miliaran insiden crash, celah keamanan, dan biaya perbaikan software yang tak terhitung jumlahnya di seluruh dunia."
            }
        ]
    },

    "f-recursion": {
        "summary": "Fungsi yang memanggil dirinya sendiri untuk memecahkan masalah bertingkat.",
        "explanation_simple": (
            "Bayangkan membuka boneka kayu Rusia (Matryoshka). Saat kamu membuka boneka terluar, di dalamnya terdapat boneka yang bentuknya persis sama "
            "namun berukuran lebih kecil. Kamu membuka boneka kedua, menemukan boneka ketiga, dan seterusnya. Proses membuka ini berhenti ketika kamu "
            "menemukan boneka terkecil yang padat dan tidak bisa dibuka lagi. Dari sana, kamu memasang kembali boneka satu per satu hingga utuh.\n\n"
            "Rekursi (recursion) memecahkan masalah besar dengan meminta fungsi menyelesaikan sub-masalah identik berukuran lebih kecil, "
            "hingga mencapai kondisi dasar (base case) yang bisa dijawab langsung tanpa memanggil dirinya lagi. "
            "Batas analogi: boneka kayu di toko selalu berjumlah terbatas (misalnya 6 lapis). Jika boneka Matryoshka dibuat tanpa boneka terkecil yang padat, "
            "kamu akan terus membuka boneka tanpa henti hingga tanganmu lelah dan meja kerjamu runtuh kehabisan ruang."
        ),
        "problem_context": (
            "Banyak struktur data di dunia nyata tidak memiliki bentuk linear melainkan berstruktur hierarki pohon (tree) atau graf, "
            "seperti struktur folder di harddisk komputer, pohon dokumen HTML DOM, atau bagan silsilah keluarga. "
            "Mencoba menelusuri folder yang memiliki kedalaman sub-folder tak terbatas menggunakan perulangan for atau while biasa "
            "membutuhkan pengelolaan tumpukan manual yang sangat rumit dan mudah memicu kekeliruan logika indeks penelusuran."
        ),
        "explanation_technical": (
            "Setiap fungsi rekursif wajib memiliki dua komponen esensial: "
            "1. Base Case: kondisi terminasi di mana fungsi mengembalikan nilai langsung tanpa melakukan panggilan rekursif. "
            "2. Recursive Step: pemanggilan fungsi ke dirinya sendiri dengan argumen yang berangsur mendekati base case.\n\n"
            "Setiap pemanggilan rekursif menambahkan stack frame baru ke Call Stack sistem operasi. "
            "Jika kedalaman rekursi terlalu tinggi (misalnya 10.000 panggilan bertingkat), call stack akan kehabisan alokasi ruang memori "
            "dan memicu Stack Overflow Error. Beberapa compiler bahasa fungsional mendukung optimasi Tail Call Optimization (TCO): "
            "jika pemanggilan rekursif adalah operasi paling akhir dari fungsi (tail position), compiler dapat mengganti stack frame baru dengan "
            "melakukan jump ke awal fungsi, mengubah eksekusi rekursif menjadi seefisien loop linear biasa tanpa membebani Call Stack."
        ),
        "misconceptions": [
            {
                "misconception": "Rekursi selalu lebih cepat dan lebih hemat memori daripada perulangan loop biasa.",
                "explanation": "Sebaliknya, pada bahasa yang tidak mendukung Tail Call Optimization, pemanggilan fungsi rekursif menimbulkan overhead alokasi stack frame dan pemindahan konteks register CPU untuk setiap langkah pemanggilan.",
                "spot_in_code": "Menghitung deret Fibonacci dengan rekursi naif fib(n-1) + fib(n-2) yang kompleksitasnya meledak menjadi O(2^n)."
            },
            {
                "misconception": "Base case pada fungsi rekursif cukup ditulis di sembarang tempat di dalam tubuh fungsi.",
                "explanation": "Base case harus diperiksa di baris paling awal fungsi (guard) sebelum langkah pemanggilan rekursif dimulai; jika tidak, pemanggilan diri sendiri akan terjadi lebih dulu dan memicu stack overflow.",
                "spot_in_code": "Meletakkan pemanggilan return n * faktorial(n-1); sebelum baris if (n <= 1) return 1;."
            }
        ],
        "when_to_use": (
            "Gunakan rekursi saat mengolah struktur data hierarkis alami seperti pohon (Trees), grafik (Graphs), parsing sintaks AST, atau algoritma Divide-and-Conquer (seperti Merge Sort dan Quick Sort). "
            "Hindari rekursi naif untuk kalkulasi linear bertingkat tinggi jika bahasa targetmu tidak mendukung TCO; gunakan perulangan iteratif atau memoization."
        ),
        "why_vibecoding_matters": (
            "AI sering kali menghasilkan fungsi rekursif yang elegan secara matematika (seperti penghitung kombinatorial atau penelusur struktur JSON bersarang) "
            "tetapi lupa menangani base case ketika masukan bernilai negatif, null, atau memiliki siklus melingkar (circular reference). "
            "Saat vibecoding fungsi rekursif, tanyakan ke AI: 'Di mana base case fungsi ini, dan apa yang terjadi jika graf memiliki referensi sirkular? "
            "Apakah fungsi ini aman dari risiko stack overflow jika kedalaman data mencapai ribuan level?'"
        ),
        "reflection_questions": [
            {
                "question": "Mengapa penghitungan Fibonacci menggunakan fungsi rekursif sederhana tanpa memoization memiliki performa O(2^n)?",
                "answer": "Karena fungsi tersebut memicu pohon pemanggilan cabang ganda yang menghitung ulang nilai sub-masalah yang sama berulang kali secara eksponensial."
            },
            {
                "question": "Apa syarat agar sebuah fungsi rekursif dapat dioptimasi dengan Tail Call Optimization (TCO)?",
                "answer": "Pemanggilan rekursif harus menjadi instruksi paling akhir yang dievaluasi di fungsi tersebut, tanpa ada operasi lanjutan (seperti penjumlahan atau perkalian) yang menunggu hasil kembalian panggilan."
            }
        ]
    }
}
