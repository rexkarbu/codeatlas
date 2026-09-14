"""Fundamental Topics (47 topics) for CodeAtlas with 8 structured pedagogical dimensions."""

true = True
false = False
null = None

FUNDAMENTAL_TOPICS = [
    {
        "id": "f-programming-logic",
        "category_id": "f-logic",
        "title": "Programming Logic",
        "level": "beginner",
        "summary": "Menyusun instruksi dengan urutan yang masuk akal.",
        "explanation_simple": "Bayangkan kamu meminta seseorang yang baru pertama kali ke dapur untuk membuat mie instan. Jika kamu memberi instruksi: 'Rebus mie 3 menit, tuang mie ke mangkuk, buka bungkus mie', ia akan bingung atau bahkan merebus mie beserta plastik pembungkusnya. Urutan yang benar dan masuk akal adalah: buka bungkus mie, rebus mie dalam air mendidih, lalu tuang ke mangkuk bersama bumbu.\n\nKomputer bekerja persis seperti asisten dapur tersebut: sangat patuh, bekerja secepat kilat, tetapi tidak punya inisiatif atau akal sehat untuk menebak apa maksud kita. Komputer hanya menjalankan setiap instruksi secara harfiah, baris demi baris, sesuai urutan yang kita tuliskan. Jika urutannya terbalik, komputer tidak akan membetulkannya sendiri. Logika pemrograman adalah cara kita menyusun urutan langkah yang masuk akal agar komputer menyelesaikan tugas persis seperti yang kita harapkan.",
        "explanation_technical": "Untuk membangun alur program yang benar, ada tiga fondasi logika utama yang selalu digunakan di semua bahasa pemrograman:\n\n1. Sekuensial (Sequence / Berurutan):\nInstruksi dijalankan baris demi baris dari atas ke bawah. Langkah kedua baru berjalan setelah langkah pertama tuntas. Misalnya: mengambil data pengguna, baru kemudian menyapa namanya.\n\n2. Percabangan (Selection / Branching):\nProgram mengambil keputusan untuk memilih jalur instruksi yang berbeda berdasarkan kondisi benar (true) atau salah (false). Misalnya: jika saldo mencukupi, potong saldo dan kirim barang; jika saldo tidak cukup, tampilkan peringatan 'Saldo Kurang'.\n\n3. Perulangan (Iteration / Looping):\nProgram mengulang sekumpulan instruksi berkali-kali selama kondisi tertentu masih terpenuhi. Misalnya: mengirim notifikasi ke 100 pengguna satu per satu sampai daftar penerima habis.\n\nTeknik Menelusuri Kode (Step Tracing):\nTracing adalah kebiasaan membaca kode baris demi baris seperti komputer, sambil mencatat nilai variabel pada secarik kertas atau di kepala kita pada setiap langkah. Tracing melatih kita melihat apa yang sebenarnya terjadi di setiap baris, bukan apa yang kita bayangkan terjadi.\n\nMembedakan Dua Jenis Kesalahan:\n- Syntax Error (Kesalahan Tata Bahasa): Terjadi saat aturan penulisan bahasa dilanggar (misalnya lupa tanda kurung atau salah ketik kata kunci). Komputer langsung menolak menjalankan program dan memberi tahu letak baris yang rusak. Ini mudah ditemukan.\n- Logical Error (Kesalahan Logika): Program ditulis rapi, tidak ada salah ketik, dan berjalan lancar tanpa pesan error, tetapi hasilnya salah (misalnya rumus diskon yang terbalik atau salah langkah). Kesalahan logika lebih menantang karena hanya bisa ditemukan dengan menelusuri alur berpikir dalam kode.",
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
        "related_topic_ids": [
            "f-variables-data-types",
            "f-operators"
        ],
        "why_vibecoding_matters": "Saat vibecoding dengan asisten AI, model bahasa sering menghasilkan baris kode yang tampak rapi, canggih, dan bebas syntax error. Namun, AI kerap melakukan kesalahan urutan secara halus—misalnya memperbarui tampilan sebelum data siap, atau menutup koneksi sebelum proses simpan selesai. Jika kamu paham logika pemrograman, kamu tidak akan menelan mentah-mentah kode dari AI. Kamu bisa menelusuri urutan instruksi dan bertanya pada AI: 'Jelaskan urutan jalannya kode ini langkah demi langkah, dan tunjukkan nilai data di setiap langkah untuk memastikan alurnya sudah masuk akal.'",
        "keywords": [
            "logika",
            "urutan",
            "sequence",
            "alur program"
        ],
        "estimated_minutes": 5,
        "sort_order": 1,
        "is_active": true,
        "problem_context": "Masalah terbesar bagi pemula dan orang yang sering meminta AI membuatkan kode (vibecoding) adalah berasumsi bahwa komputer paham tujuan akhir aplikasi secara ajaib. Padahal, komputer hanya membaca kode dari atas ke bawah.\n\nSebagai contoh, bayangkan alur pembayaran di toko online:\n- Urutan yang salah: Program menghitung potongan harga sebelum pembeli memasukkan kode promo. Karena kode promo belum dibaca, potongan harga tetap nol dan pembeli membayar harga penuh.\n- Urutan yang benar: Program menerima kode promo terlebih dahulu, memeriksa apakah promo valid, menghitung potongan harga, lalu menampilkan total akhir yang harus dibayar.\n\nDi kedua skenario di atas, komputer tidak menampilkan pesan kesalahan apa pun karena instruksinya sah. Namun di skenario pertama, hasil bisnisnya salah total. Logika pemrograman memastikan setiap bahan atau data sudah siap sebelum digunakan oleh langkah berikutnya.",
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
        "when_to_use": "Gunakan pemikiran logika terstruktur setiap kali merancang alur fitur baru sebelum mulai menulis kode. Uraikan masalah besar menjadi urutan langkah kecil: apa yang harus terjadi pertama kali, kondisi apa yang perlu dicek, dan bagian mana yang perlu diulang. Terapkan teknik tracing langkah demi langkah setiap kali menemukan bug di mana program berjalan tanpa pesan error tetapi hasilnya meleset dari harapan.",
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
    {
        "id": "f-variables-data-types",
        "category_id": "f-logic",
        "title": "Variables & Data Types",
        "level": "beginner",
        "summary": "Menyimpan data dengan nama dan wadah yang sesuai jenisnya.",
        "explanation_simple": "Bayangkan deretan toples kaca berlabel di dapur rumahmu. Toples berlabel 'Gula Pasir' dirancang untuk menampung butiran padat, botol berlabel 'Kecap Asin' untuk cairan, dan saklar lampu di dinding hanya memiliki dua posisi: menyala atau mati. Label pada toples adalah nama variabel, isi di dalamnya adalah nilainya, dan bentuk wadahnya adalah tipe data. Jika kamu mencoba menuangkan kecap cair ke dalam kotak kardus tisu, wadah tersebut akan rusak dan dapur menjadi berantakan.\n\nVariabel memungkinkan programmer memberi nama yang mudah dipahami pada lokasi penyimpanan memori komputer tanpa perlu mengingat deretan angka biner atau heksadesimal. Namun analogi toples memiliki batasan penting yang bergantung pada bahasa:\n1. Di bahasa bertipe statis (seperti Dart atau C++), 'wadahnya' memiliki tipe tetap yang dikunci sejak awal deklarasi (`int x = 10;`). Sebaliknya, di bahasa bertipe dinamis (seperti Python atau JavaScript), variabel hanyalah label penunjuk yang bebas dipindahkan: pada satu baris label 'x' dapat menunjuk ke angka, lalu di baris berikutnya dipindahkan menunjuk ke teks string (`x = 10; x = 'halo'`).\n2. Variabel tipe referensi bukanlah toples fisik yang berat, melainkan kartu alamat penunjuk (pointer/reference); dua label nama berbeda bisa saja sama-sama memegang alamat yang menunjuk ke satu objek fisik yang sama di ruang memori.",
        "explanation_technical": "Secara arsitektural, variabel adalah binding simbolik antara sebuah identifier nama dengan nilai atau alamat di memori virtual. Sistem tipe data mengatur bagaimana bit ditafsirkan (misal two's complement untuk signed integer, IEEE-754 untuk floating point, UTF-8 untuk teks string) serta himpunan operasi yang diizinkan.\n\nPerbedaan krusial dalam sistem tipe dan alokasi memori:\n1. Bahasa Bertipe Statis vs Dinamis: Pada bahasa statis (Dart, TypeScript/C++), validasi kesesuaian tipe dilakukan oleh kompilator sebelum program berjalan. Pada bahasa dinamis (Python, JavaScript), tipe data terikat pada nilai/objek di runtime, bukan pada nama variabelnya.\n2. Alokasi Memori (Stack vs Heap) — Bukan Aturan Universal:\n- Pada bahasa tingkat rendah seperti C/C++, variabel primitif lokal dialokasikan di Call Stack dengan akses cepat, sedangkan objek dinamis dialokasikan di Heap. - Namun aturan ini BUKAN hukum mutlak di seluruh bahasa! Di Python, seluruh nilai adalah objek di Heap (bahkan angka kecil seperti `42` adalah alokasi `PyObject` di heap). - Di Dart dan Java, variabel primitif yang menjadi atribut (field) di dalam sebuah instance class atau tertangkap di dalam closure fungsi akan disimpan di Heap bersama objek pemiliknya. Mesin virtual modern juga menerapkan escape analysis untuk mengoptimasi alokasi objek ke stack atau register jika objek tidak lolos keluar dari fungsi lokal.\n3. Perbandingan Nilai vs Identitas Objek (`==`):\nPerilaku operator perbandingan sangat bervariasi antarbaha:\n- JavaScript/TypeScript: Operator `==` melakukan konversi tipe otomatis (type coercion: `'5' == 5` adalah true), sedangkan `===` memeriksa kesamaan nilai tanpa konversi. Namun untuk objek, `===` hanya memeriksa identitas referensi memori (`{a: 1} === {a: 1}` bernilai false).\n- Python: Operator `==` memanggil metode `__eq__()` untuk memeriksa kesamaan nilai konten (`[1, 2] == [1, 2]` bernilai True), sedangkan operator `is` memeriksa identitas referensi memori fisik (`id(a) == id(b)`).\n- Dart: Operator `==` memanggil method yang dapat di-override untuk memeriksa kesamaan nilai struktural, sedangkan fungsi bawaan `identical(a, b)` digunakan khusus untuk memeriksa apakah dua variabel menunjuk ke instans memori yang sama.",
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
        "prerequisite_ids": [
            "f-programming-logic"
        ],
        "related_topic_ids": [
            "f-programming-logic",
            "f-operators",
            "f-type-system"
        ],
        "why_vibecoding_matters": "AI sering menulis kode perbandingan objek menggunakan == di JavaScript yang gagal saat memeriksa kesamaan konten, atau memicu bug type coercion yang fatal (seperti menganggap input form '50' sebagai angka padahal teks string, sehingga '50' + 10 menghasilkan '5010'). Saat vibecoding, teliti deklarasi variabel dan instruksikan AI sesuai konteks bahasa: 'Gunakan perbandingan nilai yang tepat (gunakan deep equality untuk objek di JS/TS, atau override operator == di Dart), dan pastikan konversi tipe data masukan form dilakukan secara eksplisit sebelum operasi matematika!'",
        "keywords": [
            "variabel",
            "tipe data",
            "string",
            "number",
            "boolean",
            "let",
            "const",
            "final"
        ],
        "estimated_minutes": 7,
        "sort_order": 2,
        "is_active": true,
        "problem_context": "Pada tingkat perangkat keras murni, memori komputer (RAM) hanyalah deretan panjang sel biner bernilai 0 dan 1 tanpa label arti apa pun. Pola bit biner `01000001` dapat bermakna angka desimal 65, karakter huruf `'A'`, atau penggalan instruksi biner CPU. Tanpa sistem tipe data, prosesor dan compiler tidak memiliki cara untuk mengetahui berapa byte yang harus dibaca, bagaimana cara menafsirkannya, atau operasi apa yang sah dilakukan (misalnya, mengalikan dua huruf teks tentu tidak masuk akal). Variabel dan tipe data diciptakan sebagai kontrak keamanan dan makna semantik agar pemrosesan data di memori tetap teratur dan bebas salah tafsir.",
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
        "when_to_use": "Gunakan deklarasi tipe statis eksplisit pada aplikasi berskala besar untuk mendeteksi inkonsistensi tipe sejak fase kompilasi. Gunakan operator identitas ketat (=== di JavaScript, is di Python, atau identical() di Dart) saat ingin memverifikasi kesamaan instans memori murni. Gunakan variabel immutable (final/const) secara default untuk mencegah mutasi nilai yang tidak disengaja.",
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
    {
        "id": "f-operators",
        "category_id": "f-logic",
        "title": "Operators",
        "level": "beginner",
        "summary": "Simbol untuk menghitung, membandingkan, dan mengolah nilai.",
        "explanation_simple": "Bayangkan tanda timbangan neraca dan kalkulator saku di meja kasir. Operator aritmatika seperti tambah (+) dan kali (*) menghitung total tagihan belanjaanmu. Operator perbandingan seperti lebih besar (>) memastikan apakah uang pembayaranmu cukup. Operator logika seperti DAN (AND) memeriksa apakah toko sedang buka DAN stok barang masih tersedia.\n\nOperator adalah kata kerja dalam bahasa pemrograman yang memanipulasi operand (kata benda/nilai). Batas analoginya: kalkulator biasa menghitung secara langsung dari kiri ke kanan sesuai tombol yang kamu tekan, sedangkan bahasa pemrograman memiliki aturan presedensi (hirarki prioritas operasi) yang ketat, serta mekanisme efisiensi seperti short-circuit evaluation yang bisa membatalkan evaluasi sebelah kanan jika hasil sebelah kiri sudah menentukan.",
        "explanation_technical": "Operator menerima satu (unary), dua (binary), atau tiga (ternary) operand untuk menghasilkan nilai baru. Kategori operator meliputi: Aritmatika (+, -, *, /, %), Perbandingan (==, !=, <, >, <=, >=), Logika (&&, ||, !), Bitwise (&, |, ^, ~, <<, >>), dan Assignment (=, +=, -=).\n\nEvaluasi operator dipandu oleh Operator Precedence (tingkat prioritas, misalnya perkalian dievaluasi sebelum penjumlahan) dan Associativity (arah evaluasi dari kiri-ke-kanan atau kanan-ke-kiri). Fitur penting lainnya adalah Short-circuit evaluation pada operator boolean: pada ekspresi (A && B), jika A bernilai false, B tidak akan pernah dieksekusi karena keseluruhan ekspresi sudah pasti false. Bahasa modern juga membedakan perbandingan identitas referensi (=== di TS/JS atau identical() di Dart) dengan kesetaraan struktural nilai (==).",
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
        "prerequisite_ids": [
            "f-variables-data-types"
        ],
        "related_topic_ids": [
            "f-programming-logic",
            "f-variables-data-types",
            "f-conditionals"
        ],
        "why_vibecoding_matters": "AI sering kali menghasilkan kondisi if dengan operator perbandingan longgar atau presedensi logika yang rancu (seperti A || B && C yang dievaluasi sebagai A || (B && C) padahal maksud pengguna adalah (A || B) && C). Saat vibecoding, tanyakan ke AI: 'Tolong beri tanda kurung eksplisit pada ekspresi boolean ini dan jelaskan apakah ada evaluasi short-circuit yang berpotensi melewatkan pemanggilan fungsi penting.'",
        "keywords": [
            "operator",
            "aritmetika",
            "perbandingan",
            "logika",
            "AND",
            "assignment"
        ],
        "estimated_minutes": 7,
        "sort_order": 3,
        "is_active": true,
        "problem_context": "Sebelum adanya operator terstandarisasi dalam bahasa tingkat tinggi, programmer harus memprogram rangkaian gerbang logika (AND, OR, NOT, XOR) dan instruksi aritmatika ALU (Arithmetic Logic Unit) seperti ADD, SUB, dan CMP secara manual di tingkat assembly. Masalah besar muncul ketika ekspresi matematika panjang seperti perhitungan lintasan fisika harus ditulis dalam puluhan baris perintah register sementara. Kesalahan kecil dalam urutan eksekusi gerbang logika menghasilkan nilai kalkulasi yang melenceng drastis.",
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
        "when_to_use": "Gunakan tanda kurung buka-tutup () secara eksplisit dalam ekspresi majemuk untuk memperjelas niat kode tanpa bergantung pada ingatan presedensi. Manfaatkan short-circuit evaluation untuk guard clauses (misalnya user != null && user.isActive). Hindari ekspresi baris tunggal yang terlalu padat dengan operator ternary bersarang.",
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
    {
        "id": "f-conditionals",
        "category_id": "f-logic",
        "title": "Conditional Statements",
        "level": "beginner",
        "summary": "Membuat keputusan dalam program berdasarkan kondisi benar atau salah.",
        "explanation_simple": "Bayangkan rel kereta api dengan tuas wesel pemindah jalur di persimpangan. Ketika kereta melaju, masinis melihat lampu sinyal: jika lampu berwarna hijau, tuas mengarahkan kereta ke jalur utama; jika lampu merah, kereta diarahkan ke jalur pemberhentian darurat. Percabangan (conditionals) dalam kode bekerja seperti wesel rel kereta tersebut.\n\nKondisi mengevaluasi apakah suatu pernyataan bernilai benar (true) atau salah (false) pada detik eksekusi, lalu memilih satu lorong instruksi dan mengabaikan lorong lainnya. Batas analogi ini: rel fisik hanya bisa dilalui satu kereta dalam satu waktu, sedangkan program komputer bisa bercabang di dalam cabang (nested) atau mengevaluasi puluhan kondisi dalam hitungan mikrodetik.",
        "explanation_technical": "Secara teknis, percabangan mengubah alur eksekusi dari yang biasanya mengalir lurus ke bawah menjadi melompat ke blok kode tertentu jika suatu kondisi pengujian bernilai true. Jika kondisi bernilai false, blok tersebut dilewati dan program langsung lanjut ke cabang alternatif (else) atau ke baris berikutnya.\n\nKonstruksi percabangan mencakup struktur if, else if, else, serta switch-case. Praktek arsitektur modern sangat menganjurkan pola Guard Clauses (Early Return), di mana kondisi kegagalan atau validasi batas diperiksa dan dihentikan di baris-baris awal fungsi, sehingga logika utama tidak tertimbun di dalam piramida kurung kurawal yang menjorok terlalu dalam. Konsep truthy dan falsy pada bahasa bertipe dinamis (seperti 0, '', null, undefined di JavaScript) juga harus diwaspadai karena konversi otomatis dapat meloloskan percabangan tak terduga.",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "conditionals",
                "label": "Pemeriksaan kelulusan nilai",
                "code": "const nilai = 75;\nif (nilai >= 70) {\n  console.log(\"Lulus\");\n} else {\n  console.log(\"Remedial\");\n}",
                "explanation": "Jika nilai minimal 70, tampilkan 'Lulus', selain itu tampilkan 'Remedial'.",
                "expected_output": "Lulus"
            },
            {
                "language": "python",
                "comparison_key": "conditionals",
                "label": "Percabangan yang sama dalam Python",
                "code": "nilai = 75\nif nilai >= 70:\n    print(\"Lulus\")\nelse:\n    print(\"Remedial\")",
                "explanation": "Python menggunakan indentasi spasi untuk menandai blok kode di dalam if dan else.",
                "expected_output": "Lulus"
            },
            {
                "language": "dart",
                "comparison_key": "conditionals",
                "label": "Percabangan yang sama dalam Dart",
                "code": "void main() {\n  const nilai = 75;\n  if (nilai >= 70) {\n    print(\"Lulus\");\n  } else {\n    print(\"Remedial\");\n  }\n}",
                "explanation": "Struktur if-else Dart serupa dengan JavaScript/TypeScript menggunakan tanda kurung kurawal.",
                "expected_output": "Lulus"
            }
        ],
        "prerequisite_ids": [
            "f-operators"
        ],
        "related_topic_ids": [
            "f-operators",
            "f-loops"
        ],
        "why_vibecoding_matters": "AI sering menghasilkan kode dengan nesting percabangan yang sangat dalam dan lupa menangani kondisi fallback else (misalnya skenario ketika server mengembalikan status 500 alih-alih 200). Saat mereview kode buatan AI, periksa setiap percabangan: 'Apakah semua kemungkinan nilai ekstrim (null, string kosong, array kosong) sudah di-guard? Refactor kode ini menggunakan early return guard clauses agar alur utamanya mendatar.'",
        "keywords": [
            "if",
            "else",
            "percabangan",
            "conditional",
            "switch",
            "ternary"
        ],
        "estimated_minutes": 6,
        "sort_order": 4,
        "is_active": true,
        "problem_context": "Tanpa percabangan, program komputer hanya mampu mengeksekusi instruksi linear dari baris pertama sampai terakhir persis sama untuk setiap input. Program kasir tidak akan bisa membedakan pelanggan VIP yang berhak diskon dengan pelanggan umum. Program login tidak bisa menolak kata sandi salah. Kebutuhan untuk merespons kondisi dunia nyata yang dinamis menuntut adanya instruksi kondisional di tingkat instruksi mesin.",
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
        "when_to_use": "Gunakan if/else sederhana untuk keputusan 1-2 cabang berbasis kondisi boolean dinamis. Gunakan switch-case atau pattern matching jika membandingkan satu variabel diskrit terhadap banyak nilai enum atau state tetap. Terapkan early return guard clauses di awal fungsi untuk memvalidasi masukan kotor sebelum memproses logika inti.",
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
    {
        "id": "f-loops",
        "category_id": "f-logic",
        "title": "Loops",
        "level": "beginner",
        "summary": "Mengulang perintah berkali-kali sampai batas yang ditentukan.",
        "explanation_simple": "Bayangkan ban berjalan di pabrik pengemasan botol minuman. Setiap kali sebuah botol lewat di depan sensor, lengan robot menutup tutup botol, lalu konveyor bergeser satu langkah ke botol berikutnya. Proses ini diulang terus menerus sampai sensor mendeteksi kardus penampung sudah terisi 24 botol, lalu konveyor berhenti.\n\nPerulangan (loops) mengotomatisasi pekerjaan repetitif agar programmer tidak perlu menuliskan 1.000 baris instruksi yang identik. Batas analogi pabrik ini: lengan robot pabrik dibatasi oleh kecepatan motor mekanik fisik, sedangkan perulangan komputer dapat berjalan jutaan kali per detik. Namun, jika sensor penghitung botol rusak dan tidak pernah mencapai angka 24, mesin akan terjebak dalam putaran abadi (infinite loop) yang membekukan seluruh sistem.",
        "explanation_technical": "Secara teknis, perulangan bekerja dengan cara memeriksa kondisi pengujian sebelum atau sesudah blok kode dijalankan. Selama kondisi bernilai true, komputer akan mengeksekusi isi blok dan kembali lagi ke langkah pengujian berikutnya. Tiga struktur perulangan standar meliputi:\n1. for loop: digunakan ketika jumlah iterasi sudah diketahui sejak awal (mengelola inisialisasi, kondisi batas, dan penambahan nilai hitungan).\n2. while loop: digunakan ketika pengulangan bergantung pada kondisi eksternal yang belum pasti kapan berubahnya (kondisi dicek sebelum blok berjalan).\n3. do-while loop: menjamin tubuh kode dieksekusi minimal satu kali sebelum kondisi diperiksa.\n\nDalam eksekusi loop, kata kunci break digunakan untuk keluar seketika dari perulangan, sedangkan continue melewati sisa blok iterasi saat ini dan langsung melompat ke putaran berikutnya. Kesalahan paling fatal pada loop adalah infinite loop (di mana variabel kondisi tidak pernah mencapai batas berhenti sehingga program macet) dan off-by-one error (perulangan kelebihan atau kekurangan satu langkah karena keliru menggunakan operator < versus <=).",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "loops",
                "label": "Menghitung dari 1 sampai 3",
                "code": "for (let i = 1; i <= 3; i++) {\n  console.log(\"Angka: \" + i);\n}",
                "explanation": "Inisialisasi i=1, berjalan selama i<=3, bertambah 1 setiap putaran.",
                "expected_output": "Angka: 1\nAngka: 2\nAngka: 3"
            },
            {
                "language": "python",
                "comparison_key": "loops",
                "label": "Perulangan yang sama dalam Python",
                "code": "for i in range(1, 4):\n    print(f\"Angka: {i}\")",
                "explanation": "Fungsi range(1, 4) menghasilkan deret 1, 2, 3 (batas atas 4 tidak disertakan).",
                "expected_output": "Angka: 1\nAngka: 2\nAngka: 3"
            },
            {
                "language": "dart",
                "comparison_key": "loops",
                "label": "Perulangan yang sama dalam Dart",
                "code": "void main() {\n  for (var i = 1; i <= 3; i++) {\n    print(\"Angka: $i\");\n  }\n}",
                "explanation": "Sintaks for loop standar dalam Dart menggunakan interpolasi teks $i.",
                "expected_output": "Angka: 1\nAngka: 2\nAngka: 3"
            }
        ],
        "prerequisite_ids": [
            "f-conditionals"
        ],
        "related_topic_ids": [
            "f-conditionals",
            "f-data-structures"
        ],
        "why_vibecoding_matters": "Asisten AI sering menghasilkan perulangan while tanpa jaminan perubahan variabel kontrol di dalam blok catch/error, sehingga ketika API gagal merespons, aplikasi terjebak dalam infinite loop yang memakan 100% CPU. Saat vibecoding, teliti batas akhir loop dan tanyakan ke AI: 'Apakah loop ini memiliki batas maksimum iterasi (timeout/guard) untuk mencegah infinite loop jika koneksi gagal?'",
        "keywords": [
            "loop",
            "for",
            "while",
            "iterasi",
            "perulangan"
        ],
        "estimated_minutes": 6,
        "sort_order": 5,
        "is_active": true,
        "problem_context": "Bayangkan sebuah bank yang harus memproses perhitungan bunga bulanan untuk 500.000 nasabah. Jika bahasa pemrograman tidak menyediakan mekanisme perulangan, insinyur software harus menyalin baris perhitungan bunga sebanyak 500.000 kali di kode sumber. File kode akan berukuran puluhan megabyte, tidak mungkin diperbaiki jika ada perubahan rumus, dan memboroskan memori instruksi program.",
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
        "when_to_use": "Gunakan for-in atau for-of modern saat mengiterasi elemen koleksi (Array/List/Map) untuk menghindari kesalahan manajemen indeks manual. Gunakan while saat membaca data stream atau polling status jaringan yang durasinya tak tentu. Gunakan break dan continue secara terukur; jika logika loop terlalu rumit, pertimbangkan metode fungsional seperti map, filter, atau forEach.",
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
    {
        "id": "f-functions",
        "category_id": "f-logic",
        "title": "Functions",
        "level": "beginner",
        "summary": "Membungkus langkah kerja berulang ke dalam satu perintah bernama.",
        "explanation_simple": "Bayangkan resep pembuatan adonan roti di dapur toko roti. Daripada kepala koki mendiktekan takaran terigu, ragi, dan air setiap kali pesanan baru tiba, resep tersebut dicetak pada selembar kartu bernama 'buatAdonan(jumlahPorsi)'. Setiap pembuat roti cukup memanggil nama resep tersebut sambil menyerahkan angka berapa porsi yang diinginkan, dan di akhir proses mereka menerima adonan kalis yang siap dipanggang.\n\nFungsi (functions) adalah blok pembangun paling esensial dalam rekayasa perangkat lunak. Ia membungkus algoritma tertentu sehingga dapat digunakan berulang kali dari berbagai sudut aplikasi tanpa menulis ulang kode. Batas analogi resep: resep dapur bisa menghasilkan rasa berbeda tergantung suhu tangan koki, sedangkan fungsi murni (pure function) di komputer bersifat deterministik: input argumen yang sama dijamin 100% selalu menghasilkan nilai kembalian yang sama persis.",
        "explanation_technical": "Ketika sebuah fungsi dipanggil (function invocation), sistem operasi dan runtime mengalokasikan Stack Frame baru di Call Stack. Stack frame ini menampung alamat kembalian instruksi (return address), nilai parameter aktual (argumen), dan alokasi variabel lokal fungsi. Ketika eksekusi mencapai instruksi return, nilai kembalian diserahkan kembali ke pemanggil, stack frame dimusnahkan (popped), dan Program Counter CPU melompat kembali ke return address untuk melanjutkan eksekusi program pemanggil.\n\nParameter adalah variabel yang terdaftar di deklarasi fungsi, sedangkan argumen adalah nilai nyata yang dikirimkan saat pemanggilan. Dalam arsitektur modern, fungsi dibedakan menjadi: 1. Pure Functions: tidak memiliki side-effects (tidak mengubah variabel global atau I/O) dan deterministik. 2. Impure Functions: melakukan operasi I/O, mutasi state global, atau bergantung pada waktu/angka acak. Fungsi juga dapat menjadi First-Class Citizens: dapat disimpan dalam variabel, dikirim sebagai argumen (callback), dan dikembalikan dari fungsi lain (Higher-Order Functions).",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "functions",
                "label": "Fungsi menjumlahkan dua angka",
                "code": "function tambah(a: number, b: number): number {\n  return a + b;\n}\nconst hasil = tambah(4, 5);\nconsole.log(hasil);",
                "explanation": "Fungsi tambah menerima dua parameter bertipe number dan mengembalikan hasil penjumlahannya.",
                "expected_output": "9"
            },
            {
                "language": "python",
                "comparison_key": "functions",
                "label": "Fungsi yang sama dalam Python",
                "code": "def tambah(a, b):\n    return a + b\n\nhasil = tambah(4, 5)\nprint(hasil)",
                "explanation": "Kata kunci def digunakan untuk mendeklarasikan fungsi di Python.",
                "expected_output": "9"
            },
            {
                "language": "dart",
                "comparison_key": "functions",
                "label": "Fungsi yang sama dalam Dart",
                "code": "int tambah(int a, int b) {\n  return a + b;\n}\n\nvoid main() {\n  final hasil = tambah(4, 5);\n  print(hasil);\n}",
                "explanation": "Di Dart, tipe return ditulis sebelum nama fungsi (int tambah).",
                "expected_output": "9"
            }
        ],
        "prerequisite_ids": [
            "f-conditionals"
        ],
        "related_topic_ids": [
            "f-scope",
            "f-recursion",
            "f-clean-code"
        ],
        "why_vibecoding_matters": "AI gemar menghasilkan fungsi monolitik raksasa yang mencampuradukkan manipulasi antarmuka pengguna, pembacaan database, dan perhitungan bisnis dalam satu tempat. Kode semacam ini sangat rapuh saat kamu meminta perubahan kecil. Terapkan disiplin vibecoding: 'Pecah kode ini menjadi fungsi-fungsi murni kecil dengan batasan parameter yang jelas, tipe data kembalian eksplisit, dan pisahkan operasi side-effects ke lapisan terpisah.'",
        "keywords": [
            "fungsi",
            "function",
            "parameter",
            "argumen",
            "return",
            "def"
        ],
        "estimated_minutes": 7,
        "sort_order": 6,
        "is_active": true,
        "problem_context": "Pada masa awal pemrograman dengan instruksi GOTO dan baris bernomor (seperti BASIC kuno), seluruh logika program bercampur dalam satu aliran linear raksasa (spaghetti code). Jika rumus perhitungan pajak harus digunakan di 15 tempat berbeda, rumus itu disalin 15 kali. Ketika undang-undang perpajakan berganti, programmer harus mencari dan memperbarui 15 lokasi tersebut satu per satu. Satu lokasi saja terlewat, pembukuan perusahaan rusak dan timbul audit hukum. Konsep subrutin atau fungsi diciptakan untuk mengatasi bencana redundansi ini.",
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
        "when_to_use": "Terapkan prinsip Single Responsibility Principle: satu fungsi harus mengerjakan satu tugas saja dengan baik. Gunakan pure function untuk semua kalkulasi transformasi data dan logika bisnis agar mudah diuji dengan unit test. Pecah fungsi yang panjangnya melebihi 30-40 baris menjadi fungsi-fungsi pembantu (helper functions) yang memiliki nama deskriptif.",
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
    {
        "id": "f-scope",
        "category_id": "f-logic",
        "title": "Scope",
        "level": "intermediate",
        "summary": "Wilayah dan batas waktu hidup variabel di dalam kode.",
        "explanation_simple": "Bayangkan sebuah gedung perkantoran bertingkat dengan kartu akses ruangan. Barang yang diletakkan di lobi utama gedung (Global Scope) dapat dilihat dan diambil oleh siapa saja yang berada di dalam gedung. Namun, berkas rahasia yang disimpan di dalam ruang rapat lantai 4 (Local Scope) hanya bisa diakses oleh orang yang berada di dalam ruangan tersebut. Orang luar tidak bisa melihat apa yang ada di dalam ruang rapat.\n\nScope menentukan di mana sebuah variabel 'hidup' dan dari mana saja variabel tersebut sah untuk dibaca atau diubah. Batas analogi gedung ini: di dunia nyata, jika kamu keluar ruangan, barang di dalam ruangan tetap ada di meja. Dalam komputasi, begitu eksekusi fungsi selesai keluar dari ruangannya, seluruh variabel lokal di dalamnya otomatis dimusnahkan dari memori, kecuali jika dipertahankan oleh mekanisme khusus bernama Closure.",
        "explanation_technical": "Sebagian besar bahasa modern mengadopsi Lexical Scoping (Static Scoping): batasan lingkup ditentukan oleh posisi fisik kode bersarang pada saat penulisan kode sumber, bukan berdasarkan urutan pemanggilan dinamis saat runtime. Ketika sebuah identifier dicari, compiler/runtime menelusuri Scope Chain dari lingkup terdalam (Block/Function Scope) bergerak keluar ke Outer Scope hingga ke Global Scope. Jika tidak ditemukan di tingkat global, error ReferenceError/undeclared identifier dimunculkan.\n\nClosure adalah kombinasi antara sebuah fungsi dan lexical environment tempat fungsi tersebut dideklarasikan. Closure memungkinkan fungsi inner tetap mempertahankan akses ke variabel lokal milik fungsi outer pembungkusnya, meskipun fungsi outer tersebut sudah selesai dieksekusi dan stack framenya telah ditutup. Dalam kasus ini, variabel yang tertangkap (captured variable) dipindahkan dari stack ke heap memory agar tidak terhapus.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Scope lokal di dalam blok if",
                "code": "const globalVar = \"Luar\";\nif (true) {\n  const localVar = \"Dalam\";\n  console.log(globalVar); // Bisa diakses\n  console.log(localVar);  // Bisa diakses\n}\n// localVar tidak bisa diakses di sini",
                "explanation": "localVar hanya hidup di dalam kurung kurawal blok if. Mengaksesnya di luar akan menyebabkan ReferenceError.",
                "expected_output": "Luar\nDalam"
            }
        ],
        "prerequisite_ids": [
            "f-functions"
        ],
        "related_topic_ids": [
            "f-variables-data-types",
            "f-functions"
        ],
        "why_vibecoding_matters": "AI sering kali meletakkan variabel penampung sementara di lingkup file global untuk jalan pintas agar kode bisa berjalan cepat. Hal ini memicu bug aneh saat fungsi dipanggil untuk kedua kalinya karena state kotor sebelumnya masih tersisa. Saat vibecoding, instruksikan AI: 'Pastikan semua variabel dideklarasikan di lingkup lokal fungsi terkecil, dan jangan ada variabel state yang bocor ke lingkup modul global.'",
        "keywords": [
            "scope",
            "global",
            "lokal",
            "closure",
            "shadowing",
            "block scope"
        ],
        "estimated_minutes": 6,
        "sort_order": 7,
        "is_active": true,
        "problem_context": "Pada bahasa pemrograman awal yang hanya mengenal variabel global (seperti dialek assembly atau BASIC purba), setiap variabel dapat ditimpa dari baris program mana pun. Jika fungsi pencetakan nota memakai variabel penghitung 'i' dan fungsi perhitungan diskon juga memakai 'i', kedua fungsi tersebut akan saling merusak nilai penghitung satu sama lain. Bug misterius ini memicu lahirnya batasan lingkup (Scoping) untuk mengisolasi kehidupan data antar-komponen program.",
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
        "when_to_use": "Batasi cakupan variabel sekecil mungkin (Principle of Least Privilege): deklarasikan variabel sedekat mungkin dengan tempat ia digunakan. Gunakan closure untuk data encapsulation (menyembunyikan variabel private sebelum adanya sintaks class private field). Hindari penggunaan variabel global untuk data yang sering mengalami mutasi state.",
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
    {
        "id": "f-type-system",
        "category_id": "f-logic",
        "title": "Type System",
        "level": "intermediate",
        "summary": "Aturan jenis data agar program tidak salah mengolah nilai.",
        "explanation_simple": "Bayangkan pemeriksaan paspor di terminal imigrasi bandara internasional. Setiap paspor memiliki stempel kategori visa: turis, pekerja ahli, atau diplomat. Petugas imigrasi di gerbang memeriksa paspor sebelum penumpang diizinkan naik pesawat. Jika seorang turis mencoba bekerja di negara tujuan, aturan imigrasi langsung menolaknya di gerbang sebelum terjadi pelanggaran hukum.\n\nSistem tipe (Type System) bertindak sebagai petugas imigrasi kode komputermu. Ia memeriksa apakah operasi yang ingin kamu jalankan pada sebuah data sah dan sesuai dengan kategori tipe data tersebut. Batas analogi imigrasi: ada bandara dengan pemeriksaan ketat di muka (Static Typing: periksa sebelum terbang), dan ada bandara yang mengizinkan siapa saja mendarat lalu baru menangkap pelanggar saat mereka sudah berada di jalan raya (Dynamic Typing: periksa saat program berjalan).",
        "explanation_technical": "Sistem tipe adalah kumpulan aturan traktat logika yang menetapkan properti 'tipe' pada konstruksi program (seperti variabel, ekspresi, fungsi). Dua dimensi utama klasifikasi sistem tipe adalah: 1. Static vs Dynamic: Static Typing (Dart, TypeScript, Rust) memeriksa keabsahan tipe saat compile-time sebelum kode dijalankan. Dynamic Typing (Python, JavaScript murni) mengikat tipe ke nilai objek saat runtime.\n2. Strong vs Weak: Strong Typing menolak pemaksaan operasi antar-tipe yang tidak cocok tanpa konversi eksplisit (Python adalah strongly typed, tidak mengizinkan '5' + 5). Weak Typing melakukan pemaksaan tipe implisit (JavaScript mengizinkan '5' - 2 menghasilkan 3 dan '5' + 2 menghasilkan '52').\n\nPerkembangan penting lainnya adalah Sound Null Safety (seperti pada Dart dan Kotlin), di mana sistem tipe membedakan secara tegas tipe yang boleh bernilai null (String?) dengan tipe non-nullable (String), melenyapkan error legendaris NullPointerException di tingkat kompilasi.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Pengecekan tipe saat kompilasi",
                "code": "let umur: number = 20;\n// umur = \"dua puluh\"; // Error saat kompilasi!\nconsole.log(umur);",
                "explanation": "TypeScript melarang menugaskan string ke variabel yang telah dideklarasikan sebagai number.",
                "expected_output": "20"
            }
        ],
        "prerequisite_ids": [
            "f-variables-data-types"
        ],
        "related_topic_ids": [
            "f-variables-data-types",
            "f-build-compilation"
        ],
        "why_vibecoding_matters": "AI yang diprompt secara sembarangan sering kali menggunakan operator non-null assertion (!) atau type casting paksa (as any) hanya agar pesan error compiler merah menghilang dari layar IDE. Hal ini menipu developer dan memindahkan ledakan error ke runtime pengguna. Saat vibecoding, instruksikan AI: 'Perbaiki error tipe dengan cara menyelesaikan akar masalah penanganan null atau konversi tipe, jangan pernah menggunakan cast paksa as any atau force unwrap !.'",
        "keywords": [
            "type system",
            "static typing",
            "dynamic typing",
            "strong",
            "weak",
            "typescript"
        ],
        "estimated_minutes": 7,
        "sort_order": 8,
        "is_active": true,
        "problem_context": "Tanpa sistem tipe formal, semua data di memori komputer hanyalah deretan biner 0 dan 1 yang anonim. Sebuah program dapat secara tidak sengaja mencoba membagi teks nama orang dengan angka tanggal lahir, mengakibatkan prosesor membaca alamat memori acak dan merusak data sistem operasi. Kerusakan finansial miliaran rupiah dan kegagalan peluncuran roket luar angkasa (seperti roket Ariane 5 yang meledak tahun 1996) banyak diakibatkan oleh konversi tipe data yang meluap (overflow) tanpa pemeriksaan ketat sistem tipe.",
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
        "when_to_use": "Gunakan bahasa bertipe statis dengan sound null safety untuk membangun aplikasi produksi berskala menengah hingga besar yang melibatkan banyak kolaborator. Gunakan type inference (seperti var atau final tanpa menulis ulang tipe berulang) untuk menjaga kode tetap bersih tanpa mengorbankan keamanan statis. Pasang validasi skema runtime (seperti zod atau form validation) di setiap gerbang I/O jaringan.",
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
    {
        "id": "f-recursion",
        "category_id": "f-logic",
        "title": "Recursion",
        "level": "intermediate",
        "summary": "Fungsi yang memanggil dirinya sendiri untuk memecahkan masalah bertingkat.",
        "explanation_simple": "Bayangkan membuka boneka kayu Rusia (Matryoshka). Saat kamu membuka boneka terluar, di dalamnya terdapat boneka yang bentuknya persis sama namun berukuran lebih kecil. Kamu membuka boneka kedua, menemukan boneka ketiga, dan seterusnya. Proses membuka ini berhenti ketika kamu menemukan boneka terkecil yang padat dan tidak bisa dibuka lagi. Dari sana, kamu memasang kembali boneka satu per satu hingga utuh.\n\nRekursi (recursion) memecahkan masalah besar dengan meminta fungsi menyelesaikan sub-masalah identik berukuran lebih kecil, hingga mencapai kondisi dasar (base case) yang bisa dijawab langsung tanpa memanggil dirinya lagi. Batas analogi: boneka kayu di toko selalu berjumlah terbatas (misalnya 6 lapis). Jika boneka Matryoshka dibuat tanpa boneka terkecil yang padat, kamu akan terus membuka boneka tanpa henti hingga tanganmu lelah dan meja kerjamu runtuh kehabisan ruang.",
        "explanation_technical": "Setiap fungsi rekursif wajib memiliki dua komponen esensial: 1. Base Case: kondisi terminasi di mana fungsi mengembalikan nilai langsung tanpa melakukan panggilan rekursif. 2. Recursive Step: pemanggilan fungsi ke dirinya sendiri dengan argumen yang berangsur mendekati base case.\n\nSetiap pemanggilan rekursif menambahkan stack frame baru ke Call Stack sistem operasi. Jika kedalaman rekursi terlalu tinggi (misalnya 10.000 panggilan bertingkat), call stack akan kehabisan alokasi ruang memori dan memicu Stack Overflow Error. Beberapa compiler bahasa fungsional mendukung optimasi Tail Call Optimization (TCO): jika pemanggilan rekursif adalah operasi paling akhir dari fungsi (tail position), compiler dapat mengganti stack frame baru dengan melakukan jump ke awal fungsi, mengubah eksekusi rekursif menjadi seefisien loop linear biasa tanpa membebani Call Stack.",
        "code_examples": [
            {
                "language": "python",
                "label": "Faktorial bilangan secara rekursif",
                "code": "def faktorial(n):\n    if n <= 1:\n        return 1\n    return n * faktorial(n - 1)\n\nprint(faktorial(4))",
                "explanation": "4 * faktorial(3) -> 3 * faktorial(2) -> 2 * faktorial(1) -> 1. Hasil akhir adalah 24.",
                "expected_output": "24"
            }
        ],
        "prerequisite_ids": [
            "f-functions"
        ],
        "related_topic_ids": [
            "f-functions",
            "f-algorithms",
            "f-memory"
        ],
        "why_vibecoding_matters": "AI sering kali menghasilkan fungsi rekursif yang elegan secara matematika (seperti penghitung kombinatorial atau penelusur struktur JSON bersarang) tetapi lupa menangani base case ketika masukan bernilai negatif, null, atau memiliki siklus melingkar (circular reference). Saat vibecoding fungsi rekursif, tanyakan ke AI: 'Di mana base case fungsi ini, dan apa yang terjadi jika graf memiliki referensi sirkular? Apakah fungsi ini aman dari risiko stack overflow jika kedalaman data mencapai ribuan level?'",
        "keywords": [
            "recursion",
            "rekursi",
            "base case",
            "call stack",
            "faktorial"
        ],
        "estimated_minutes": 7,
        "sort_order": 9,
        "is_active": true,
        "problem_context": "Banyak struktur data di dunia nyata tidak memiliki bentuk linear melainkan berstruktur hierarki pohon (tree) atau graf, seperti struktur folder di harddisk komputer, pohon dokumen HTML DOM, atau bagan silsilah keluarga. Mencoba menelusuri folder yang memiliki kedalaman sub-folder tak terbatas menggunakan perulangan for atau while biasa membutuhkan pengelolaan tumpukan manual yang sangat rumit dan mudah memicu kekeliruan logika indeks penelusuran.",
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
        "when_to_use": "Gunakan rekursi saat mengolah struktur data hierarkis alami seperti pohon (Trees), grafik (Graphs), parsing sintaks AST, atau algoritma Divide-and-Conquer (seperti Merge Sort dan Quick Sort). Hindari rekursi naif untuk kalkulasi linear bertingkat tinggi jika bahasa targetmu tidak mendukung TCO; gunakan perulangan iteratif atau memoization.",
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
    },
    {
        "id": "f-data-structures",
        "category_id": "f-data-algorithms",
        "title": "Data Structures",
        "level": "beginner",
        "summary": "Cara menata dan menyimpan data agar mudah dicari dan diolah.",
        "explanation_simple": "Bayangkan lemari arsip di kantor pengacara. Jika dokumen disusun bertumpuk acak di satu kotak kardus, kamu harus membongkar seluruh kardus selama berjam-jam hanya untuk mencari akta kelahiran seorang klien. Namun, jika dokumen ditata dalam map gantung bernomor urut atau laci berlabel abjad A-Z, kamu bisa mengambil berkas yang dibutuhkan dalam hitungan detik.\n\nStruktur data adalah cetak biru penataan memori agar data dapat dicari, disisipkan, diubah, dan dihapus secara optimal. Batas analoginya: lemari fisik di kantor memiliki sekat kayu permanen, sedangkan struktur data di komputer dapat diatur ulang secara dinamis melalui penunjuk alamat memori (pointer) dalam hitungan nanodetik.",
        "explanation_technical": "Struktur data diklasifikasikan menjadi: 1. Linear: elemen tersusun berurutan (Array, Linked List, Stack, Queue). Elemen memiliki tetangga sebelum dan sesudah yang jelas. 2. Non-linear: elemen memiliki hubungan hierarkis atau jejaring (Trees, Heaps, Graphs, Hash Tables).\n\nPemilihan struktur data didasarkan pada kompromi (trade-offs) kompleksitas waktu operasi utama: akses acak (random access), pencarian (search), penyisipan (insertion), dan penghapusan (deletion). Struktur data juga mempengaruhi cache locality: array kontinu memanfaatkan CPU L1/L2 data cache secara maksimal, sedangkan struktur berbasis node pointer (seperti Linked List) sering memicu cache miss karena node-nodenya tersebar acak di heap memory.",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "lists",
                "label": "Manipulasi list buah",
                "code": "const buah: string[] = [\"Apel\", \"Jeruk\"];\nbuah.push(\"Mangga\");\nconsole.log(buah[0], buah.length);",
                "explanation": "Array dibuat dengan tanda kurung siku, elemen diakses melalui indeks berbasis 0, dan push menambah item baru.",
                "expected_output": "Apel 3"
            },
            {
                "language": "python",
                "comparison_key": "lists",
                "label": "List buah dalam Python",
                "code": "buah = [\"Apel\", \"Jeruk\"]\nbuah.append(\"Mangga\")\nprint(buah[0], len(buah))",
                "explanation": "Python menggunakan metode append untuk menambah elemen dan fungsi len() untuk menghitung jumlah item.",
                "expected_output": "Apel 3"
            },
            {
                "language": "dart",
                "comparison_key": "lists",
                "label": "List buah dalam Dart",
                "code": "void main() {\n  final buah = [\"Apel\", \"Jeruk\"];\n  buah.add(\"Mangga\");\n  print(\"${buah[0]} ${buah.length}\");\n}",
                "explanation": "Di Dart, tipe List memiliki metode add dan properti length.",
                "expected_output": "Apel 3"
            }
        ],
        "prerequisite_ids": [
            "f-variables-data-types"
        ],
        "related_topic_ids": [
            "f-algorithms",
            "f-big-o"
        ],
        "why_vibecoding_matters": "AI sering kali memilih List secara default untuk semua jenis penyimpanan koleksi, bahkan ketika kode melakukan pengecekan duplikasi berulang kali. Hal ini menimbulkan perlambatan tersembunyi yang baru terasa saat aplikasi menerima data pengguna dalam jumlah besar. Saat vibecoding, tanyakan ke AI: 'Apakah struktur data yang digunakan di modul ini sudah optimal untuk pola akses query yang sering dilakukan (baca vs tulis)? Bisakah Set atau Map menggantikan List untuk mengeliminasi pencarian O(n)?'",
        "keywords": [
            "struktur data",
            "array",
            "list",
            "map",
            "dictionary",
            "set",
            "queue",
            "stack"
        ],
        "estimated_minutes": 8,
        "sort_order": 10,
        "is_active": true,
        "problem_context": "Di era komputasi awal, data hanya disimpan dalam array datar berurutan. Ketika volume data melonjak dari ribuan menjadi jutaan entitas, operasi pencarian data di array membutuhkan penelusuran linear satu per satu dari awal sampai akhir. Sistem reservasi penerbangan atau indeks basis data bank menjadi sangat lambat hingga berhenti merespons (freeze). Para peneliti ilmu komputer menyadari bahwa struktur data yang berbeda memiliki karakteristik performa yang berbeda untuk operasi baca vs tulis, memicu penemuan struktur data non-linear seperti Hash Map, B-Tree, dan Graph.",
        "misconceptions": [
            {
                "misconception": "Ada satu struktur data 'sempurna' yang cocok dan paling cepat untuk semua kebutuhan aplikasi.",
                "explanation": "Setiap struktur data adalah kompromi rekayasa: struktur yang cepat untuk pencarian (seperti Hash Table) sering kali boros memori dan lambat untuk pengurutan berurutan.",
                "spot_in_code": "Memaksakan penggunaan Hash Map untuk data yang selalu butuh diurutkan berdasarkan tanggal secara kontinu."
            },
            {
                "misconception": "Struktur data hanya relevan untuk wawancara kerja akademis dan tidak berdampak pada aplikasi nyata.",
                "explanation": "Salah memilih struktur data pada aplikasi produksi (misalnya menggunakan List alih-alih Set untuk pengecekan keunikan 100.000 user) dapat memperlambat server dari 5 milidetik menjadi 30 detik.",
                "spot_in_code": "Melakukan if (list.contains(id)) berulang di dalam perulangan loop besar alih-alih memanfaatkan Set."
            }
        ],
        "when_to_use": "Gunakan Array/List dinamis saat kamu membutuhkan akses elemen cepat berbasis indeks dan ukuran data moderat. Gunakan Set saat kamu wajib menjamin keunikan data dan butuh pencarian O(1). Gunakan Map/Dictionary untuk relasi kunci-nilai yang membutuhkan pencarian instan tanpa iterasi linear.",
        "reflection_questions": [
            {
                "question": "Mengapa akses array berbasis indeks array[i] memiliki kompleksitas waktu konstan O(1)?",
                "answer": "Karena array dialokasikan secara bersebelahan (kontinu) di memori, sehingga CPU dapat menghitung alamat target secara instan menggunakan rumus: alamat_awal + (indeks * ukuran_tipe_data)."
            },
            {
                "question": "Apa kelemahan utama dari struktur data Linked List dibandingkan Array dalam arsitektur perangkat keras modern?",
                "answer": "Linked list memiliki cache locality yang buruk karena setiap node dialokasikan terpisah di heap, mengakibatkan CPU cache misses yang menurunkan performa pembacaan secara nyata."
            }
        ]
    },
    {
        "id": "f-algorithms",
        "category_id": "f-data-algorithms",
        "title": "Algorithms",
        "level": "intermediate",
        "summary": "Langkah teratur untuk menyelesaikan masalah komputasi secara efisien.",
        "explanation_simple": "Bayangkan kamu tersesat di labirin taman bermain dan ingin menemukan jalan keluar tercepat. Strategi acak berlari ke segala arah bisa memakan waktu berjam-jam tanpa hasil pasti. Namun, jika kamu menggunakan aturan 'sentuh dinding sebelah kanan dengan tangan kananmu dan berjalanlah tanpa pernah melepas tangan dari dinding', kamu dijamin secara matematis akan menemukan jalan keluar dari labirin standar.\n\nAlgoritma adalah resep sistematis langkah demi langkah untuk mengubah masukan menjadi keluaran yang valid. Batas analoginya: instruksi labirin manusia bisa terhambat rasa lelah atau ragu, sedangkan algoritma komputer dieksekusi secara konsisten tanpa bias emosional dengan kecepatan miliaran siklus instruksi per detik.",
        "explanation_technical": "Algoritma formal wajib memenuhi lima kriteria komputasional klasik (Knuth): 1. Input: menerima nol atau lebih kuantitas masukan. 2. Output: menghasilkan satu atau lebih kuantitas keluaran yang bermakna. 3. Definiteness: setiap langkah instruksi harus jelas, presisi, dan tidak ambigu. 4. Finiteness: algoritma harus selalu berhenti setelah sejumlah langkah berhingga untuk semua kasus masukan. 5. Effectiveness: setiap operasi harus cukup mendasar sehingga secara prinsip dapat dieksekusi oleh mesin dalam waktu terbatas.\n\nParadigma perancangan algoritma meliputi: Brute Force (pencarian lengkap), Divide and Conquer (pemecahan masalah menjadi sub-masalah independen, misal Merge Sort), Greedy (pengambilan keputusan lokal terbaik pada setiap langkah), dan Dynamic Programming (penyimpanan solusi sub-masalah bertumpang-tindih menggunakan memoization).",
        "code_examples": [
            {
                "language": "python",
                "label": "Pencarian biner (Binary Search)",
                "code": "def binary_search(data, target):\n    low, high = 0, len(data) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if data[mid] == target: return mid\n        elif data[mid] < target: low = mid + 1\n        else: high = mid - 1\n    return -1\nprint(binary_search([10, 20, 30, 40], 30))",
                "explanation": "Mencari angka pada list terurut dengan membelah dua rentang pencarian di setiap langkah.",
                "expected_output": "2"
            }
        ],
        "prerequisite_ids": [
            "f-loops",
            "f-data-structures"
        ],
        "related_topic_ids": [
            "f-data-structures",
            "f-big-o"
        ],
        "why_vibecoding_matters": "AI sering kali memilih algoritma Brute Force bersarang O(n^2) atau O(2^n) untuk menyelesaikan masalah pemfilteran atau pencocokan data karena algoritma tersebut paling cepat diketik. Saat vibecoding, tantang AI: 'Berapa kompleksitas algoritma yang kamu hasilkan ini? Tolong optimalkan algoritma ini menjadi O(n log n) atau O(n) menggunakan teknik Map/Set atau Divide-and-Conquer.'",
        "keywords": [
            "algoritma",
            "sorting",
            "searching",
            "binary search",
            "logika masalah"
        ],
        "estimated_minutes": 8,
        "sort_order": 11,
        "is_active": true,
        "problem_context": "Menghitung rute navigasi terdekat di Google Maps di antara 50 juta persimpangan jalan dunia adalah mustahil jika komputer mencoba setiap kemungkinan kombinasi rute secara brutal (kombinatorika faktorial akan membutuhkan jutaan tahun). Algoritma cerdas (seperti Algoritma Dijkstra dan A*) diciptakan agar komputer dapat menemukan jalur terpendek hanya dalam hitungan beberapa milidetik dengan memangkas rute yang tidak relevan secara sistematis.",
        "misconceptions": [
            {
                "misconception": "Algoritma dan program komputer adalah hal yang persis sama.",
                "explanation": "Algoritma adalah konsep logika dan metode abstrak pemecahan masalah, sedangkan program adalah implementasi konkret dari algoritma tersebut dalam bahasa pemrograman tertentu.",
                "spot_in_code": "Mengira algoritma Binary Search hanya ada di Python dan tidak bisa ditulis dalam Dart atau C++."
            },
            {
                "misconception": "Algoritma tercepat selalu merupakan algoritma yang paling rumit dan berbobot besar.",
                "explanation": "Untuk volume data kecil (n < 50), algoritma sederhana seperti Insertion Sort sering kali lebih cepat secara praktis daripada Quick Sort karena overhead inisialisasi yang rendah dan cache locality yang ramah.",
                "spot_in_code": "Menerapkan struktur data pohon B-Tree rumit untuk menyimpan 20 item pengaturan aplikasi lokal."
            }
        ],
        "when_to_use": "Gunakan algoritma terstandarisasi yang sudah teruji di industri (seperti sorting bawaan bahasa, hashing crypto SHA-256) daripada menciptakan algoritma sendiri dari nol. Gunakan Dynamic Programming saat sub-masalah komputasi memiliki sifat overlapping subproblems (seperti penghitungan rute atau edit distance teks). Gunakan Greedy Algorithm hanya jika properti optimal substructure terbukti menghasilkan solusi global terbaik.",
        "reflection_questions": [
            {
                "question": "Mengapa sebuah algoritma wajib memiliki sifat 'finiteness' (pasti berhenti)?",
                "answer": "Jika suatu prosedur komputasi tidak memiliki jaminan terminasi, sistem akan mengalami hang/infinite loop tanpa pernah menghasilkan output yang dijanjikan."
            },
            {
                "question": "Apa perbedaan mendasar antara teknik Divide and Conquer dan Dynamic Programming?",
                "answer": "Divide and Conquer memecah masalah menjadi sub-masalah independen yang diselesaikan terpisah (seperti Merge Sort), sedangkan Dynamic Programming menangani sub-masalah yang saling bertumpang tindih (overlapping) dengan menyimpan hasil perhitungan sebelumnya agar tidak dihitung ulang."
            }
        ]
    },
    {
        "id": "f-big-o",
        "category_id": "f-data-algorithms",
        "title": "Big-O Notation",
        "level": "intermediate",
        "summary": "Cara mengukur seberapa cepat dan hemat memori kode saat data bertambah banyak.",
        "explanation_simple": "Bayangkan kamu ingin mengantarkan berkas dokumen ke temanmu. Jika temanmu duduk di meja sebelah, berjalan kaki memakan waktu 10 detik. Jika temanmu berada di kota lain, terbang naik pesawat memakan waktu 4 jam. Sekarang bayangkan kamu harus mengirim 1.000 berkas dokumen: berjalan kaki bolak-balik 1.000 kali memakan waktu berjam-jam (tumbuh linear sesuai jumlah berkas). Tetapi jika kamu memasukkan 1.000 berkas itu ke dalam satu bagasi koper di pesawat yang sama, durasi penerbangannya tetap 4 jam (waktu konstan tidak peduli seberapa banyak berkasnya).\n\nNotasi Big O adalah cara insinyur software mengukur seberapa cepat kebutuhan waktu atau memori melonjak ketika data pengguna meledak dari 10 menjadi 10.000.000 entitas. Batas analoginya: di dunia fisik ada batasan berat bagasi pesawat, sedangkan di komputasi Big O menggambarkan tren laju pertumbuhan kurva teoretis murni pada skenario batas ekstrem (asymptotic worst-case).",
        "explanation_technical": "Notasi Big O (Asymptotic Notation) mengukur batas atas (upper bound) laju pertumbuhan konsumsi waktu (Time Complexity) dan ruang memori tambahan (Space Complexity) seiring nilai n (ukuran input) mendekati tak hingga. Konstanta pengali dan suku berderajat rendah diabaikan (misalnya rumus 3n^2 + 5n + 100 disederhanakan menjadi O(n^2)) karena pada nilai n yang masif, suku berderajat tertinggilah yang mendominasi tren pertumbuhan.\n\nSpektrum efisiensi Big O dari terbaik ke terburuk: 1. O(1) - Konstan: akses elemen array dengan indeks, operasi hash map ideal. 2. O(log n) - Logaritmik: binary search pada data terurut (membelah ruang pencarian menjadi setengah tiap langkah). 3. O(n) - Linear: mencari data di array acak melalui iterasi satu per satu. 4. O(n log n) - Linearitmik: algoritma pengurutan optimal (Merge Sort, Tim Sort). 5. O(n^2) - Kuadratik: loop bersarang dua tingkat (Bubble Sort, perbandingan semua pasangan). 6. O(2^n) - Eksponensial: rekursi cabang ganda tanpa memoization. 7. O(n!) - Faktorial: mencari semua permutasi kemungkinan rute perjalanan (Travelling Salesperson brute-force).",
        "code_examples": [
            {
                "language": "typescript",
                "label": "O(1) vs O(n) dalam JavaScript",
                "code": "const data = [10, 20, 30, 40, 50];\n// O(1) - Mengakses elemen pertama instan\nconst pertama = data[0];\n// O(n) - Loop memeriksa setiap elemen satu per satu\nlet ada = false;\nfor (const x of data) {\n  if (x === 30) ada = true;\n}\nconsole.log(pertama, ada);",
                "explanation": "Akses indeks langsung konstan O(1), sedangkan pencarian linear memerlukan iterasi sepanjang n elemen O(n).",
                "expected_output": "10 true"
            }
        ],
        "prerequisite_ids": [
            "f-algorithms"
        ],
        "related_topic_ids": [
            "f-algorithms",
            "f-data-structures"
        ],
        "why_vibecoding_matters": "AI sering menulis kode yang tampak ringkas dan 'elegan' dalam 2 baris (misalnya listA.filter(x => listB.some(y => y.id === x.id))), tanpa memberitahumu bahwa kode tersebut menyembunyikan kompleksitas kuadratik O(n * m) yang melumpuhkan browser saat data membesar. Saat vibecoding, mintalah AI mengevaluasi kodenya: 'Berapa time complexity dan space complexity dari kode ini dalam notasi Big O? Bisakah kamu mengubahnya menjadi O(n) menggunakan Hash Set atau Map?'",
        "keywords": [
            "big-o",
            "kompleksitas",
            "time complexity",
            "space complexity",
            "skalabilitas",
            "performa"
        ],
        "estimated_minutes": 8,
        "sort_order": 12,
        "is_active": true,
        "problem_context": "Sebuah fitur pencarian produk toko online berjalan lancar dalam 10 milidetik di laptop developer saat diuji dengan 50 produk contoh. Namun ketika aplikasi diluncurkan ke publik dan database memiliki 500.000 produk, pencarian yang sama tiba-tiba membutuhkan waktu 12 menit dan membuat server crash. Developer tersebut tidak memahami Big O dan menulis algoritma O(n^2) dengan loop bersarang ganda. Analisis Big O diciptakan agar insinyur dapat memprediksi perilaku aplikasi pada skala jutaan data tanpa harus menunggu crash di lingkungan produksi.",
        "misconceptions": [
            {
                "misconception": "Big O mengukur jumlah detik atau milidetik nyata yang dibutuhkan kode saat berjalan.",
                "explanation": "Big O mengukur jumlah operasi relatif terhadap ukuran data (skalabilitas kurva), bukan detik waktu nyata; detik nyata dipengaruhi oleh kecepatan hardware CPU, bahasa, dan optimasi compiler.",
                "spot_in_code": "Mengira algoritma O(n) pasti selalu berjalan lebih cepat daripada O(n^2) pada data yang hanya berjumlah 3 item."
            },
            {
                "misconception": "Menghilangkan loop kedua di dalam loop pertama selalu otomatis menjadikan kode bernilai O(n).",
                "explanation": "Jika di dalam loop tunggal kamu memanggil method bawaan bahasa seperti array.includes(), list.indexOf(), atau string concatenation berulang, method tersebut sebenarnya melakukan loop tersembunyi O(n) sehingga totalnya tetap O(n^2).",
                "spot_in_code": "for (const item of listA) { if (listB.includes(item)) ... } yang berkinerja O(n * m)."
            }
        ],
        "when_to_use": "Gunakan analisis Big O saat merancang query database, API endpoint, atau algoritma pengolahan data yang diperkirakan akan berkembang seiring waktu. Targetkan kompleksitas O(1) atau O(log n) untuk operasi yang sangat sering dipanggil (seperti pengecekan autentikasi atau lookup cache). Waspadai algoritma berkategori O(n^2) ke atas: jangan gunakan pada koleksi data yang jumlah elemennya melebihi beberapa ratus tanpa pembatasan pagination.",
        "reflection_questions": [
            {
                "question": "Mengapa konstanta pengali (misalnya perbedaan antara 2n dan 100n) diabaikan dalam notasi Big O?",
                "answer": "Karena Big O berfokus pada bentuk tren kurva pertumbuhan saat n membesar menuju tak hingga; konstanta pengali tidak mengubah klasifikasi pertumbuhan linear, kuadratik, atau eksponensial."
            },
            {
                "question": "Jika input bertambah dari 1.000 menjadi 1.000.000 elemen, bagaimana dampak waktu eksekusi pada algoritma O(n) vs O(n^2)?",
                "answer": "Pada O(n), beban operasi naik 1.000 kali lipat (linear), sedangkan pada O(n^2), beban operasi melonjak 1.000.000 kali lipat (kuadratik), yang dapat mengubah waktu tunggu dari 1 detik menjadi 11 hari."
            }
        ]
    },
    {
        "id": "f-oop",
        "category_id": "f-code-quality",
        "title": "OOP",
        "level": "intermediate",
        "summary": "Menata kode dengan menggabungkan data dan fungsinya ke dalam bentuk objek.",
        "explanation_simple": "Bayangkan pabrik perakitan mobil. Sebelum memproduksi ribuan mobil, insinyur merancang blueprint cetak biru bernama 'Mobil'. Cetakan ini menentukan bahwa setiap mobil memiliki atribut warna, kapasitas bensin, dan kecepatan, serta kemampuan (method) seperti 'hidupkanMesin()', 'injakGas()', dan 'rem()'. Dari satu cetakan itu, pabrik dapat mencetak mobil Avanza warna hitam milik Budi dan mobil Yaris warna merah milik Ani.\n\nObject-Oriented Programming (OOP) menyatukan data (state) dan fungsi (perilaku) ke dalam satu wadah mandiri bernama Objek. Batas analogi pabrik: di dunia fisik, mobil yang sudah dirakit tidak bisa tiba-tiba mewarisi fitur perahu amfibi secara instan. Dalam kode, konsep pewarisan (inheritance) yang berlebihan justru dapat mengikat komponen dalam hierarki kaku yang sulit diubah di kemudian hari.",
        "explanation_technical": "OOP bertumpu pada empat pilar fundamental: 1. Encapsulation: menyembunyikan detail internal objek (private state) dan membatasi interaksi hanya melalui antarmuka publik resmi (getters/methods). 2. Abstraction: menyederhanakan interaksi dengan menyembunyikan kompleksitas implementasi di balik antarmuka abstrak atau interface. 3. Inheritance: kemampuan class turunan (subclass) mewarisi properti dan method dari class induk (superclass) untuk penggunaan kembali kode. 4. Polymorphism: kemampuan objek dari berbagai tipe class turunan untuk merespons pemanggilan method yang sama dengan perilaku spesifik masing-masing (Dynamic Dispatch via vtable).\n\nMeskipun inheritance sangat populer, arsitektur software modern menganjurkan prinsip 'Composition over Inheritance': lebih baik menyusun objek dari komponen-komponen mandiri (HAS-A) daripada menciptakan rantai pewarisan hierarki yang dalam (IS-A) yang memicu masalah rapuhnya class induk (fragile base class problem).",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "classes",
                "label": "Class Mobil dalam TypeScript",
                "code": "class Mobil {\n  constructor(public merk: string, private kecepatan: number = 0) {}\n  gas(): void { this.kecepatan += 10; }\n  status(): string { return `${this.merk}: ${this.kecepatan} km/h`; }\n}\nconst m = new Mobil(\"Toyota\");\nm.gas();\nconsole.log(m.status());",
                "explanation": "Mendefinisikan class dengan constructor, field publik/privat, dan method gas.",
                "expected_output": "Toyota: 10 km/h"
            },
            {
                "language": "python",
                "comparison_key": "classes",
                "label": "Class Mobil dalam Python",
                "code": "class Mobil:\n    def __init__(self, merk):\n        self.merk = merk\n        self.kecepatan = 0\n    def gas(self):\n        self.kecepatan += 10\n    def status(self):\n        return f\"{self.merk}: {self.kecepatan} km/h\"\nm = Mobil(\"Toyota\")\nm.gas()\nprint(m.status())",
                "explanation": "Python menggunakan __init__ dan self untuk mengakses instance objek.",
                "expected_output": "Toyota: 10 km/h"
            },
            {
                "language": "dart",
                "comparison_key": "classes",
                "label": "Class Mobil dalam Dart",
                "code": "class Mobil {\n  final String merk;\n  int kecepatan = 0;\n  Mobil(this.merk);\n  void gas() => kecepatan += 10;\n  String status() => \"$merk: $kecepatan km/h\";\n}\nvoid main() {\n  final m = Mobil(\"Toyota\");\n  m.gas();\n  print(m.status());\n}",
                "explanation": "Dart sangat kental dengan OOP, menjadi dasar dari seluruh Widget di Flutter.",
                "expected_output": "Toyota: 10 km/h"
            }
        ],
        "prerequisite_ids": [
            "f-functions",
            "f-data-structures"
        ],
        "related_topic_ids": [
            "f-design-patterns",
            "f-clean-code"
        ],
        "why_vibecoding_matters": "AI gemar menghasilkan class god-object (satu class raksasa yang mengurus semuanya) atau hierarki pewarisan warisan tua yang kaku. Saat vibecoding, instruksikan AI menerapkan SOLID principles: 'Rancang modul ini dengan prinsip Single Responsibility, gunakan interface untuk mendefinisikan kontrak method, dan gunakan dependency injection daripada hardcoding instansiasi di dalam class.'",
        "keywords": [
            "oop",
            "class",
            "object",
            "inheritance",
            "encapsulation",
            "polymorphism",
            "instance"
        ],
        "estimated_minutes": 8,
        "sort_order": 13,
        "is_active": true,
        "problem_context": "Dalam pemrograman prosedural murni tanpa enkapsulasi objek, data aplikasi disimpan dalam record/struct terbuka dan ratusan fungsi bebas memanipulasi field struct tersebut dari mana saja. Jika variabel 'saldo' pada struct Rekening diubah langsung menjadi negatif tanpa melewati validasi aturan bisnis, sistem perbankan mengalami korupsi data tanpa bisa melacak fungsi mana yang bersalah. OOP lahir untuk membentengi data di balik dinding pelindung (Enkapsulasi) dan mengorganisir sistem modular berskala masif.",
        "misconceptions": [
            {
                "misconception": "Semakin dalam hierarki inheritance (misalnya class A turunan B, turunan C, turunan D), semakin bagus desain arsitekturnya.",
                "explanation": "Inheritance bertingkat menciptakan kopling yang sangat ketat; perubahan kecil di class puncak dapat merusak seluruh class di bawahnya. Komposisi jauh lebih fleksibel.",
                "spot_in_code": "Class SuperAdminUser extends AdminUser extends MemberUser extends BaseUser extends EntityObject."
            },
            {
                "misconception": "Polimorfisme hanya bisa dicapai melalui class inheritance tradisional.",
                "explanation": "Polimorfisme modern dapat dicapai melalui interface implementation, abstract classes, protocols, atau duck typing (di bahasa dinamis seperti Python).",
                "spot_in_code": "Membuat class induk kosong tiruan hanya untuk mendapatkan polimorfisme padahal interface sudah cukup."
            }
        ],
        "when_to_use": "Gunakan OOP saat memodelkan domain bisnis dengan entitas kaya state yang memiliki siklus hidup dan aturan validasi ketat. Manfaatkan Interface dan Polimorfisme untuk memisahkan implementasi konkret (misalnya implementasi PaymentGatewayMock vs PaymentGatewayStripe). Terapkan komposisi daripada pewarisan ketika ingin berbagi kapabilitas perilaku antarkelas.",
        "reflection_questions": [
            {
                "question": "Mengapa prinsip 'Composition over Inheritance' sangat ditekankan dalam rekayasa perangkat lunak modern?",
                "answer": "Karena komposisi memungkinkan perilaku objek diubah dan diganti secara dinamis saat runtime tanpa mengikat struktur class ke hierarki statis yang rapuh terhadap perubahan class induk."
            },
            {
                "question": "Bagaimana polimorfisme memfasilitasi arsitektur perangkat lunak yang loosely coupled (tidak terikat erat)?",
                "answer": "Kode pemanggil hanya perlu bergantung pada kontrak abstraksi/interface tingkat tinggi tanpa perlu tahu class konkret apa yang sedang dieksekusi di baliknya."
            }
        ]
    },
    {
        "id": "f-functional-programming",
        "category_id": "f-code-quality",
        "title": "Functional Programming Basics",
        "level": "intermediate",
        "summary": "Menulis program dengan fungsi murni tanpa mengubah data secara langsung.",
        "explanation_simple": "Bayangkan pabrik pengolahan air minum kemasan otomatis. Air mentah dari mata air mengalir melalui pipa filter karbon, lalu ke tabung sinar ultraviolet, dan berakhir di botol kemasan bersih. Di setiap stasiun, air diproses dan diteruskan ke tahap berikutnya; tidak ada stasiun yang mengubah atau mengotori mata air asal di hulu. Jika kamu ingin membuat 1.000 botol, kamu cukup mengalirkan air melalui pipa yang sama berulang kali dengan hasil kemurnian yang identik.\n\nFunctional Programming (FP) memandang program sebagai rangkaian pipa transformasi fungsi matematika. Batas analoginya: pabrik air fisik membutuhkan listrik dan ruang nyata, sedangkan fungsi matematika dalam FP bersifat murni: ia tidak pernah mengubah data aslinya (Immutability) dan tidak peduli berapa kali kamu menjalankannya, hasilnya selalu sama persis.",
        "explanation_technical": "Functional Programming berlandaskan pada fondasi teori Lambda Calculus (Church). Tiga pilar intinya meliputi: 1. Pure Functions: fungsi yang outputnya 100% ditentukan oleh input argumennya dan tidak menimbulkan Side Effects (tidak memodifikasi state luar, tidak melakukan penulisan disk/jaringan tanpa abstraksi efek monad). 2. Immutability: sekali data dialokasikan, data tersebut tidak pernah diubah; setiap perubahan menghasilkan salinan data baru dengan state yang diperbarui (menggunakan teknik persistent data structures untuk efisiensi memori). 3. First-Class & Higher-Order Functions: fungsi dapat diperlakukan sebagai nilai (disimpan di variabel, dipassing sebagai parameter, dikembalikan sebagai return value).\n\nOperasi koleksi FP standar meliputi: map (transformasi 1:1), filter (penyaringan berbasis predikat boolean), dan reduce/fold (penggabungan seluruh elemen menjadi satu nilai akhir). FP juga memanfaatkan Function Composition dan Currying.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Transformasi data dengan map dan filter",
                "code": "const angka = [1, 2, 3, 4];\nconst genapKuadrat = angka\n  .filter(n => n % 2 === 0)\n  .map(n => n * n);\nconsole.log(genapKuadrat);\nconsole.log(angka); // Array asli tidak berubah",
                "explanation": "filter menyaring angka genap [2, 4], lalu map menguadratkannya menjadi [4, 16]. Array asal tetap utuh.",
                "expected_output": "[ 4, 16 ]\n[ 1, 2, 3, 4 ]"
            }
        ],
        "prerequisite_ids": [
            "f-functions"
        ],
        "related_topic_ids": [
            "f-oop",
            "f-clean-code"
        ],
        "why_vibecoding_matters": "AI sering mencampuradukkan gaya fungsional dan mutasi in-place (seperti memanggil list.map() lalu di dalamnya melakukan variabelLuar++), menciptakan efek samping tersembunyi yang merusak determinisme kode. Saat vibecoding, instruksikan AI: 'Tulis logika transformasi data ini dengan gaya fungsional murni tanpa mutasi state luar, gunakan map/filter/reduce dan pastikan fungsinya bersifat idempotensial serta bebas side-effects.'",
        "keywords": [
            "functional programming",
            "pure function",
            "immutability",
            "map",
            "filter",
            "side effects"
        ],
        "estimated_minutes": 7,
        "sort_order": 14,
        "is_active": true,
        "problem_context": "Dalam sistem aplikasi skala besar dengan puluhan thread prosesor yang berjalan paralel (seperti server web multi-core), paradigma yang mengandalkan mutasi state bersama (shared mutable state) memicu kekacauan besar. Dua thread yang mencoba mengubah variabel saldo bank yang sama pada mikrodetik yang sama mengakibatkan race condition dan deadlock yang sangat sulit dilacak. Functional Programming hadir untuk menyelesaikan krisis konkurensi ini dengan melarang mutasi state secara radikal.",
        "misconceptions": [
            {
                "misconception": "Immutability membuat aplikasi boros memori dan super lambat karena terus-menerus menyalin objek baru.",
                "explanation": "Runtime dan compiler FP modern menggunakan teknik Structural Sharing: data lama dan baru berbagi node memori yang tidak berubah, sehingga salinan baru hanya mengalokasikan perbedaan perubahannya saja.",
                "spot_in_code": "Takut menggunakan state immutable di Flutter/React karena khawatir memori HP cepat habis."
            },
            {
                "misconception": "Aplikasi dunia nyata bisa dibuat 100% dari pure functions tanpa ada side-effects sama sekali.",
                "explanation": "Aplikasi tanpa side-effects tidak bisa menampilkan piksel ke layar, tidak bisa menyimpan data ke database, dan tidak bisa menerima input pengguna; FP mengisolasi side-effects ke lapisan luar (I/O boundaries) dan menjaga inti bisnis tetap murni.",
                "spot_in_code": "Mencoba membuat operasi database murni tanpa efek samping I/O."
            }
        ],
        "when_to_use": "Gunakan fungsi murni (map, filter, reduce) saat melakukan transformasi dan agregasi data koleksi. Terapkan state immutable pada state management aplikasi antarmuka pengguna (seperti Redux, Bloc, Riverpod) untuk menjamin time-travel debugging dan rendering UI terprediksi. Gunakan FP pada pipeline pemrosesan data paralel dan komputasi event streaming.",
        "reflection_questions": [
            {
                "question": "Mengapa pure functions secara inheren aman untuk dijalankan dalam lingkungan multithreading paralel?",
                "answer": "Karena pure function tidak pernah mengubah shared mutable state, sehingga mustahil terjadi race condition atau benturan penulisan memori antar-thread."
            },
            {
                "question": "Apa perbedaan konseptual antara operasi map dan reduce pada transformasi koleksi data?",
                "answer": "Map mentransformasi setiap elemen koleksi menjadi elemen baru dengan jumlah elemen tetap sama (1:1), sedangkan reduce mengakumulasi seluruh elemen koleksi menjadi satu nilai tunggal akhir."
            }
        ]
    },
    {
        "id": "f-clean-code",
        "category_id": "f-code-quality",
        "title": "Clean Code",
        "level": "beginner",
        "summary": "Kebiasaan menulis kode yang rapi, mudah dibaca, dan gampang dirawat.",
        "explanation_simple": "Bayangkan membaca buku teks yang dicetak rapi dengan daftar isi jelas, bab berurutan, paragraf ringkas, dan tanda baca yang benar, dibandingkan membaca tumpukan catatan kusut yang penuh coretan singkatan aneh tanpa spasi. Meskipun kedua buku tersebut menyampaikan informasi fakta yang sama, buku yang rapi dapat dipahami dalam sekejap, sedangkan catatan yang berantakan memakan waktu berjam-jam untuk didekripsi.\n\nClean Code adalah seni menulis kode komputer yang bukan hanya dimengerti oleh prosesor mesin, tetapi terutama mudah dibaca, dipahami, dan dikembangkan oleh manusia rekan kerjamu (atau dirimu sendiri 6 bulan kemudian). Batas analoginya: buku cetak bersifat statis setelah dicetak, sedangkan kode software adalah dokumen hidup yang akan terus diubah dan diperluas seiring perkembangan kebutuhan bisnis.",
        "explanation_technical": "Clean Code berakar pada prinsip rekayasa esensial: 1. Meaningful Names: nama variabel, fungsi, dan class harus mencerminkan niat bisnis tanpa butuh komentar penjelas (misalnya daysSinceLastLogin alih-alih d). 2. Small Functions & Single Responsibility: fungsi harus pendek (idealnya di bawah 20 baris) dan hanya mengerjakan satu hal dengan satu level abstraksi. 3. DRY (Don't Repeat Yourself): setiap keping pengetahuan harus memiliki representasi tunggal dan tak ambigu dalam sistem. 4. Avoid Magic Numbers/Strings: ganti nilai harfiah acak dengan konstanta bernama deskriptif (misalnya HTTP_STATUS_OK = 200). 5. Separation of Concerns: pisahkan logika bisnis murni, pengolahan data, dan kode presentasi visual ke modul terpisah.\n\nKomentar kode hanya digunakan untuk menjelaskan 'MENGAPA' sebuah keputusan arsitektural aneh diambil, bukan untuk menjelaskan 'APA' yang dilakukan kode. Jika kode membutuhkan komentar untuk menjelaskan apa yang dilakukannya, artinya kode tersebut belum bersih dan harus direfaktor.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Nama variabel jelas vs nama misterius",
                "code": "// Buruk: const d = 86400;\n// Bersih:\nconst DETIK_DALAM_SEHARI = 24 * 60 * 60;\nfunction hitungTotalDetik(hari: number): number {\n  return hari * DETIK_DALAM_SEHARI;\n}\nconsole.log(hitungTotalDetik(2));",
                "explanation": "Mengganti angka acak (magic number) dengan konstanta bernama membuat maksud kode langsung dipahami tanpa perlu menebak.",
                "expected_output": "172800"
            }
        ],
        "prerequisite_ids": [
            "f-functions"
        ],
        "related_topic_ids": [
            "f-documentation",
            "f-software-architecture"
        ],
        "why_vibecoding_matters": "AI asisten memiliki kecenderungan melahirkan kode 'cepat jalan' yang penuh dengan variabel abstrak seperti data, res, item2, serta menduplikasi blok kode yang sama di berbagai fungsi. Saat vibecoding, jangan terima kode pertama AI begitu saja. Perintahkan: 'Refactor kode ini mengikuti standar Clean Code: berikan penamaan yang deskriptif, pecah fungsi besar menjadi fungsi-fungsi modular berorientasi tujuan, dan hilangkan semua magic numbers.'",
        "keywords": [
            "clean code",
            "readability",
            "refactoring",
            "DRY",
            "magic numbers",
            "penamaan"
        ],
        "estimated_minutes": 6,
        "sort_order": 15,
        "is_active": true,
        "problem_context": "Fakta industri software membuktikan bahwa rasio waktu yang dihabiskan programmer untuk membaca kode berbanding menulis kode baru mencapai 10 banding 1. Ketika sebuah tim mewarisi codebase legacy yang penuh dengan fungsi 500 baris, variabel singkatan misterius (seperti a, x, temp, d8), dan logika duplikat di mana-mana, kecepatan rilis fitur baru anjlok mendekati nol. Setiap perbaikan bug kecil justru memicu dua bug baru di modul lain. Krisis Technical Debt ini melahirkan gerakan Clean Code.",
        "misconceptions": [
            {
                "misconception": "Clean Code berarti menulis kode sesingkat mungkin dalam satu baris menggunakan trik sintaks pintar.",
                "explanation": "One-liner code yang terlalu padat sering kali menjadi kode yang paling sulit dibaca (write-only code); kode yang bersih mengutamakan kejelasan (clarity) di atas kepadatan (brevity).",
                "spot_in_code": "Menggabungkan tiga ternary dan regex rumit dalam satu baris alih-alih menulis blok percabangan yang jelas."
            },
            {
                "misconception": "Komentar di setiap baris kode adalah bukti bahwa programmer menulis kode yang bersih dan profesional.",
                "explanation": "Komentar yang berlebihan sering kali menjadi kompensasi atas penamaan kode yang buruk dan cepat usang/berbohong saat kode diubah tanpa memperbarui komentarnya.",
                "spot_in_code": "// Menambah i dengan 1 di atas baris i++;."
            }
        ],
        "when_to_use": "Terapkan Boy Scout Rule: 'Tinggalkan perkemahan kode dalam kondisi lebih bersih daripada saat kamu menemukannya'. Gunakan linter otomatis dan formatters (seperti dart format, prettier, black) di CI/CD pipeline untuk menegakkan standar gaya penulisan secara otomatis. Refactor kode saat menambahkan fitur baru, bukan menunda refactoring ke 'nanti kalau ada waktu luang'.",
        "reflection_questions": [
            {
                "question": "Mengapa komentar kode sering dianggap sebagai 'kegagalan mengekspresikan maksud melalui kode' oleh para praktisi Clean Code?",
                "answer": "Karena kode yang dirancang bersih dengan penamaan variabel dan fungsi yang tepat sudah dapat mendokumentasikan dirinya sendiri (self-documenting) tanpa butuh penjelasan tambahan."
            },
            {
                "question": "Apa bahaya dari technical debt (utang teknis) yang diabaikan terlalu lama dalam proyek software?",
                "answer": "Codebase akan membusuk (code rot), meningkatkan frekuensi bug regresi, menurunkan moral tim, dan memperlambat kecepatan rilis fitur baru hingga sistem harus ditulis ulang dari nol."
            }
        ]
    },
    {
        "id": "f-design-patterns",
        "category_id": "f-code-quality",
        "title": "Design Patterns Basics",
        "level": "intermediate",
        "summary": "Pola solusi teruji untuk menyelesaikan masalah rancangan kode yang sering berulang.",
        "explanation_simple": "Bayangkan seorang arsitek yang merancang gedung perkantoran modern. Arsitek tersebut tidak perlu menemukan kembali cara membuat tangga darurat, pintu geser otomatis, atau instalasi pipa air dari nol. Mereka menggunakan standar desain arsitektur yang sudah terbukti kokoh, aman, dan efisien selama puluhan tahun di ribuan bangunan lain.\n\nDesign Patterns (Pola Desain) adalah cetak biru solusi tingkat konseptual untuk masalah struktur kode yang sering dihadapi insinyur software. Batas analoginya: kamu tidak bisa sekadar menyalin fisik tangga darurat dan menempelkannya sembarangan di ruang tamu kecil rumah tinggal. Design pattern adalah pola pikir (mindset) dan strategi relasi antarkelas, bukan potongan kode kaku yang bisa di-copy-paste tanpa penyesuaian konteks.",
        "explanation_technical": "Design Patterns GoF dikelompokkan ke dalam tiga rumpun besar: 1. Creational Patterns (Penciptaan): mengisolasi mekanisme instansiasi objek agar sistem independen dari cara objek dibuat, dikomposisi, dan direpresentasikan. Contoh: Singleton (menjamin satu instance global), Factory Method (mendelegasikan instansiasi ke subclass), Builder (merakit objek kompleks bertahap). 2. Structural Patterns (Struktur): menyusun class dan objek menjadi struktur yang lebih besar namun tetap fleksibel. Contoh: Adapter (menjembatani antarmuka tak kompatibel), Decorator (menambah tanggung jawab dinamis tanpa inheritance), Facade (menyediakan antarmuka ringkas ke subsistem kompleks). 3. Behavioral Patterns (Perilaku): mengatur komunikasi, algoritma, dan pembagian tanggung jawab antar-objek. Contoh: Observer (mekanisme pub/sub event), Strategy (menukar algoritma runtime), Command (mengenkapsulasi permintaan aksi).\n\nPola modern menekankan Inversion of Control (IoC) dan Dependency Injection (DI) untuk memutus ketergantungan langsung antar-kelas layanan.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Singleton Pattern sederhana",
                "code": "class DatabaseConnection {\n  private static instance: DatabaseConnection;\n  private constructor() {}\n  public static getInstance(): DatabaseConnection {\n    if (!DatabaseConnection.instance) {\n      DatabaseConnection.instance = new DatabaseConnection();\n    }\n    return DatabaseConnection.instance;\n  }\n}\nconst conn1 = DatabaseConnection.getInstance();\nconst conn2 = DatabaseConnection.getInstance();\nconsole.log(conn1 === conn2);",
                "explanation": "Singleton menjamin hanya ada satu instance koneksi database di seluruh siklus hidup aplikasi.",
                "expected_output": "true"
            }
        ],
        "prerequisite_ids": [
            "f-oop"
        ],
        "related_topic_ids": [
            "f-oop",
            "f-software-architecture"
        ],
        "why_vibecoding_matters": "AI sering kali memaksakan penerapan Singleton atau Factory yang berlebihan pada modul-modul kecil karena pola tersebut dominan dalam data latihannya. Saat vibecoding, kritik arsitektur AI: 'Apakah penggunaan Factory Pattern di sini benar-benar diperlukan, ataukah cukup dengan fungsi biasa? Sederhanakan kode jika pola ini menambah lapisan boilerplate yang tidak memberikan fleksibilitas nyata.'",
        "keywords": [
            "design pattern",
            "singleton",
            "factory",
            "observer",
            "gof",
            "arsitektur kode"
        ],
        "estimated_minutes": 8,
        "sort_order": 16,
        "is_active": true,
        "problem_context": "Ketika sistem software berkembang besar, kode yang awalnya sederhana mulai membelit: pembuatan objek baru tersebar di 50 file berbeda, satu perubahan format data mengharuskan pengubahan puluhan class, dan modul notifikasi terikat mati dengan modul transaksi. Sistem menjadi rapuh dan kaku terhadap perubahan. Pada tahun 1994, empat insinyur software (Gang of Four / GoF) mengkatalogkan 23 pola desain teruji untuk membebaskan software dari belitan kopling ketat ini.",
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
        "when_to_use": "Gunakan Observer Pattern saat kamu merancang sistem reaktif (seperti event bus atau state management UI). Gunakan Strategy Pattern jika kamu memiliki beberapa variasi algoritma yang harus bisa ditukar saat runtime (misal berbagai opsi kalkulasi ongkos kirim). Gunakan Adapter saat menghubungkan library pihak ketiga ke domain kode internal aplikasimu.",
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
    {
        "id": "f-software-architecture",
        "category_id": "f-code-quality",
        "title": "Software Architecture Basics",
        "level": "intermediate",
        "summary": "Rancangan kerangka besar aplikasi agar komponen-komponennya bekerja harmonis.",
        "explanation_simple": "Bayangkan tata ruang kota metropolitan modern. Perencana kota memisahkan dengan tegas antara zona perumahan warga, zona industri pabrik pengolahan limbah, dan zona pusat perkantoran komersial. Pipa air bersih dan kabel listrik bawah tanah dihubungkan melalui koridor utilitas terstandarisasi. Pemisahan zonasi ini mencegah limbah pabrik mencemari air minum perumahan dan memastikan kota dapat berkembang tanpa kekacauan.\n\nArsitektur Perangkat Lunak (Software Architecture) adalah penataan zonasi modul kode dalam skala besar. Batas analoginya: bangunan gedung di kota terikat tanah fisik permanen, sedangkan arsitektur software dapat dimigrasikan dari monolit ke microservices atau dari arsitektur berlapis ke event-driven seiring pertumbuhan skala organisasi dan bisnis.",
        "explanation_technical": "Arsitektur perangkat lunak memandu pembagian tanggung jawab subsistem (Separation of Concerns). Pola-pola arsitektur kanonikal meliputi: 1. Layered Architecture (N-Tier): membagi sistem menjadi Presentation Layer, Business Logic Layer, Data Access Layer, dan Database. Aturan ketatnya: layer atas boleh memanggil layer di bawahnya, tetapi layer bawah dilarang mengetahui layer di atasnya. 2. Clean Architecture / Hexagonal Architecture (Ports & Adapters): menempatkan Domain Entities dan Use Cases murni di pusat terdalam, sedangkan UI, Database, dan Framework eksternal diletakkan di lingkaran terluar. Aturan ketergantungan (Dependency Rule) mengharuskan panah dependensi kode hanya boleh mengarah ke dalam (ke arah domain murni yang bebas dari framework eksternal).\n\n3. Microservices vs Monolith: Monolith menyatukan seluruh subsistem dalam satu deployment unit tunggal (sederhana untuk tim kecil), sedangkan Microservices memecah domain bisnis menjadi layanan-layanan independen yang berkomunikasi melalui jaringan (REST/gRPC/Kafka) untuk mendukung skalabilitas tim besar dengan biaya kompleksitas operasional terdistribusi.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Pemisahan lapisan Data vs Presentasi",
                "code": "// Layer Data: bertugas fetch data saja\nclass UserRepository {\n  getUser() { return { id: 1, name: \"Budi\" }; }\n}\n// Layer UI: bertugas menampilkan saja\nfunction renderUserProfile(repo: UserRepository) {\n  const user = repo.getUser();\n  return `<h1>Halo, ${user.name}</h1>`;\n}\nconsole.log(renderUserProfile(new UserRepository()));",
                "explanation": "UI tidak langsung melakukan query database, melainkan meminta data lewat abstraksi Repository.",
                "expected_output": "<h1>Halo, Budi</h1>"
            }
        ],
        "prerequisite_ids": [
            "f-clean-code"
        ],
        "related_topic_ids": [
            "f-clean-code",
            "f-design-patterns"
        ],
        "why_vibecoding_matters": "AI yang diminta membuat fitur baru cenderung meletakkan panggilan jaringan HTTP atau query database langsung di dalam komponen UI atau controller. Hal ini melanggar pemisahan lapisan dan membuat kode tidak bisa diuji secara terisolasi. Saat vibecoding, instruksikan AI: 'Patuhi arsitektur berlapis: pisahkan Presentation (UI), Domain (Use Cases/Logika Bisnis), dan Data (Repository/API Client) ke modul terpisah dengan antarmuka yang bersih.'",
        "keywords": [
            "software architecture",
            "clean architecture",
            "mvc",
            "separation of concerns",
            "layering"
        ],
        "estimated_minutes": 8,
        "sort_order": 17,
        "is_active": true,
        "problem_context": "Tanpa batasan arsitektur yang jelas, seiring bertambahnya programmer dan fitur baru, proyek akan terjerumus ke dalam arsitektur 'Big Ball of Mud'. Kode antarmuka visual (UI) langsung memanggil query SQL mentah ke database, perhitungan diskon bisnis tertanam di tombol klik frontend, dan modul pembayaran bergantung langsung pada format tampilan layar. Ketika tampilan aplikasi ingin diperbarui ke platform mobile, seluruh sistem runtuh karena logika bisnis tidak dapat dipisahkan dari tampilan.",
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
        "when_to_use": "Gunakan Clean Architecture pada sistem inti bisnis (Core Domain) yang diperkirakan akan beroperasi jangka panjang dan butuh pengujian unit test tanpa database. Gunakan Layered Architecture konvensional untuk aplikasi berbasis CRUD yang alurnya lurus. Tegakkan pemisahan layer melalui pembagian direktori dan aturan linting arsitektur modul.",
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
    {
        "id": "f-error-handling",
        "category_id": "f-errors",
        "title": "Error Handling",
        "level": "beginner",
        "summary": "Menyiapkan antisipasi agar aplikasi tidak langsung mati saat terjadi gangguan.",
        "explanation_simple": "Bayangkan pertunjukan akrobatik sirkus di udara. Meskipun para pemain akrobat sudah berlatih ribuan kali, pengelola sirkus selalu memasang jaring pengaman lentur di bawah ayunan tali. Jika seorang pemain terpeleset dari tali, mereka tidak jatuh menghantam lantai semen yang fatal, melainkan mendarat empuk di jaring, berdiri kembali, dan pertunjukan sirkus dapat dilanjutkan dengan aman.\n\nPenanganan Kesalahan (Error Handling) adalah jaring pengaman aplikasi komputermu. Ia mengantisipasi bahwa kegagalan (seperti koneksi internet putus, file tidak ditemukan, atau format kartu kredit salah) pasti akan terjadi di dunia nyata. Batas analogi jaring sirkus: jaring fisik hanya menangkap jatuhnya tubuh, sedangkan error handling dalam kode dapat menganalisis penyebab kecelakaan, mencatat diagnosis di buku log, dan mencoba kembali operasi yang gagal secara otomatis.",
        "explanation_technical": "Strategi penanganan error modern terbagi menjadi dua paradigma dominan: 1. Exception Mechanism (try-catch-finally): Ketika kondisi abnormal terjadi di titik manapun, instruksi throw membuat objek Exception dan meluncurkan proses Stack Unwinding: runtime menelusuri Call Stack ke atas untuk mencari blok catch yang cocok. Blok finally dijamin selalu dieksekusi untuk menutup sumber daya fisik (seperti menutup koneksi database atau file handle).\n\n2. Result Type / Railway Oriented Programming (Rust, Go, Kotlin, fp-dart): Menghindari exception untuk kesalahan yang dapat diantisipasi dengan mengembalikan tipe data serikat Result<Success, Failure> atau Either. Pendekatan ini memaksa programmer menangani kasus gagal secara eksplisit melalui pattern matching sebelum nilai sukses dapat diakses.\n\nPenting membedakan antara: - Recoverable Errors (misal: koneksi timeout, validasi form): harus ditangkap dan diberi umpan balik ramah ke pengguna. - Programmer Errors / Fatal Bugs (misal: out of bounds, null assertion failed): harus di-crash dini (Fail-Fast) agar bug segera diperbaiki.",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "error-handling",
                "label": "Konversi string 'abc' dan penanganan error di TypeScript",
                "code": "function parseAngka(teks: string): number {\n  const hasil = Number(teks);\n  if (Number.isNaN(hasil)) {\n    throw new TypeError(`Gagal konversi: \"${teks}\" bukan angka valid`);\n  }\n  return hasil;\n}\n\ntry {\n  const n = parseAngka(\"abc\");\n  console.log(n);\n} catch (err: any) {\n  console.log(\"Terjadi error: \" + err.message);\n} finally {\n  console.log(\"Pembersihan resource selesai.\");\n}",
                "explanation": "Di TypeScript, Number('abc') menghasilkan NaN alih-alih melempar error. Oleh karena itu, diperlukan validasi eksplisit dengan Number.isNaN() untuk melempar TypeError ke blok catch.",
                "expected_output": "Terjadi error: Gagal konversi: \"abc\" bukan angka valid\nPembersihan resource selesai."
            },
            {
                "language": "python",
                "comparison_key": "error-handling",
                "label": "Konversi string 'abc' dan try-except di Python",
                "code": "try:\n    angka = int(\"abc\")\n    print(angka)\nexcept ValueError as e:\n    print(f\"Terjadi error: {e}\")\nfinally:\n    print(\"Pembersihan resource selesai.\")",
                "explanation": "Fungsi int('abc') di Python langsung melempar ValueError saat teks bukan representasi angka bulat yang valid.",
                "expected_output": "Terjadi error: invalid literal for int() with base 10: 'abc'\nPembersihan resource selesai."
            },
            {
                "language": "dart",
                "comparison_key": "error-handling",
                "label": "Konversi string 'abc' dan try-catch di Dart",
                "code": "void main() {\n  try {\n    final n = int.parse(\"abc\");\n    print(n);\n  } on FormatException catch (e) {\n    print(\"Terjadi error: ${e.message}\");\n  } catch (e) {\n    print(\"Terjadi error: $e\");\n  } finally {\n    print(\"Pembersihan resource selesai.\");\n  }\n}",
                "explanation": "Metode int.parse('abc') di Dart melempar FormatException yang dapat ditangkap secara spesifik menggunakan klausa 'on FormatException'.",
                "expected_output": "Terjadi error: Invalid radix-10 number (at character 1)\nabc\n^\nPembersihan resource selesai."
            }
        ],
        "prerequisite_ids": [
            "f-conditionals"
        ],
        "related_topic_ids": [
            "f-debugging",
            "f-testing"
        ],
        "why_vibecoding_matters": "AI sering menulis blok catch yang hanya mencetak print(e) ke konsol tanpa memberikan penanganan state pemulihan ke pengguna, membuat layar aplikasi macet di indikator 'loading...' selamanya saat API offline. Saat vibecoding, perintahkan AI: 'Tambahkan penanganan error yang komprehensif: tangkap exception jaringan secara spesifik, tampilkan pesan error yang ramah kepada pengguna, sediakan tombol coba lagi (retry), dan log detail teknisnya ke error tracker.'",
        "keywords": [
            "error handling",
            "try",
            "catch",
            "exception",
            "crash",
            "throw"
        ],
        "estimated_minutes": 7,
        "sort_order": 18,
        "is_active": true,
        "problem_context": "Pada bahasa C lama sebelum mekanisme Exception diperkenalkan, fungsi mengindikasikan kegagalan dengan mengembalikan nilai integer khusus (misalnya mengembalikan -1 atau NULL). Masalah fatalnya: programmer sering malas atau lupa memeriksa nilai kembalian tersebut (misalnya tidak mengecek if (file == NULL)). Program melanjutkan eksekusi dengan pointer kosong, memicu crash mendadak (Segmentation Fault) atau merusak data pengguna secara diam-diam (silent corruption) tanpa ada peringatan.",
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
        "when_to_use": "Gunakan try-catch di sekitar operasi I/O eksternal (panggilan API jaringan, pembacaan file disk, parsing JSON). Gunakan Result/Either type pada lapisan logika bisnis inti untuk mendokumentasikan kegagalan bisnis secara eksplisit di tanda tangan fungsi. Selalu bersihkan sumber daya (resource cleanup) di blok finally atau gunakan sintaks otomatis (using di C#, with di Python).",
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
    {
        "id": "f-debugging",
        "category_id": "f-errors",
        "title": "Debugging",
        "level": "beginner",
        "summary": "Cara melacak, menemukan, dan memperbaiki kesalahan logika di dalam kode.",
        "explanation_simple": "Bayangkan seorang detektif forensik yang sedang menyelidiki tempat kejadian perkara. Detektif yang berpengalaman tidak menebak-nebak secara acak atau menuduh sembarang orang berdasarkan firasat semata. Mereka mengumpulkan bukti fisik sidik jari, memeriksa rekaman kamera CCTV detik demi detik, merekonstruksi urutan peristiwa secara kronologis, dan menguji hipotesis mereka sampai pelakunya terbukti secara meyakinkan.\n\nDebugging adalah proses investigasi ilmiah untuk menemukan 'siapa pelaku' yang menyebabkan program komputer bertingkah aneh. Batas analogi detektif: tempat kejadian perkara di dunia nyata tidak bisa diulang persis sama, sedangkan dalam software, kamu dapat menciptakan kembali kondisi bug secara berulang-ulang melalui tes reproduksi deterministik.",
        "explanation_technical": "Metodologi debugging ilmiah mengikuti siklus empat tahap: 1. Reproduce: membuat langkah reproduksi minimal (Minimal Reproducible Example) yang konsisten memicu bug. 2. Isolate: mempersempit ruang pencarian menggunakan teknik Binary Search debugging (misalnya git bisect) atau inspeksi Call Stack. 3. Hypothesize & Verify: merumuskan hipotesis ilmiah ('Mengapa nilai variabel X menjadi null di baris 45?') dan membuktikannya menggunakan alat debugger. 4. Fix & Test Regress: memperbaiki akar masalah dan menulis Automated Regression Test agar bug yang sama tidak pernah kambuh lagi.\n\nAlat debugging modern meliputi: - Breakpoints: menghentikan eksekusi program di baris tertentu untuk memeriksa status variabel memori secara interaktif. - Step Over, Step Into, Step Out: menavigasi instruksi eksekusi baris per baris. - Conditional Breakpoints: hanya menghentikan eksekusi jika kondisi tertentu terpenuhi (misal userId === '999'). - Memory Heap Profiler: melacak memory leak dan objek yang tidak dibersihkan oleh Garbage Collector.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Membaca pesan stack trace",
                "code": "function hitungDiskon(total: number) {\n  if (total < 0) throw new Error(\"Total tidak boleh minus!\");\n  return total * 0.1;\n}\ntry {\n  hitungDiskon(-500);\n} catch (e: any) {\n  console.log(\"Nama error:\", e.name);\n  console.log(\"Pesan:\", e.message);\n}",
                "explanation": "Mencetak informasi error terstruktur untuk memudahkan pelacakan baris kode yang rusak.",
                "expected_output": "Nama error: Error\nPesan: Total tidak boleh minus!"
            }
        ],
        "prerequisite_ids": [
            "f-error-handling"
        ],
        "related_topic_ids": [
            "f-error-handling",
            "f-logging-monitoring",
            "f-testing"
        ],
        "why_vibecoding_matters": "Saat terjadi bug, developer sering mem-paste pesan error ke AI dan langsung menerima solusi tambal sulam yang diberikan AI. AI sering kali hanya menambahkan blok try-catch kosong atau pengecekan null defensif yang menyamarkan bug asli. Saat vibecoding, instruksikan AI secara kritis: 'Analisis stack trace ini: apa akar penyebab (root cause) dari error ini? Tunjukkan di mana data pertama kali menjadi tidak valid sebelum baris yang meledak ini dieksekusi.'",
        "keywords": [
            "debugging",
            "stack trace",
            "breakpoint",
            "bug",
            "troubleshooting",
            "investigasi"
        ],
        "estimated_minutes": 7,
        "sort_order": 19,
        "is_active": true,
        "problem_context": "Ketika bug terjadi di sistem produksi perbankan atau rumah sakit, programmer pemula sering panik dan mengubah-ubah baris kode secara serampangan dengan harapan bug hilang secara ajaib (Shotgun Debugging). Tindakan tanpa metode ilmiah ini hampir selalu melahirkan tiga bug baru yang lebih parah dan merusak integritas sistem. Disiplin debugging formal diciptakan untuk menyediakan metode sistematis dalam melacak bug ke akar penyebabnya (Root Cause).",
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
        "when_to_use": "Gunakan debugger IDE (VS Code / Android Studio) dengan breakpoints interaktif untuk menyelidiki alur logika yang kompleks atau rekursif. Gunakan logging terstruktur dengan level log (DEBUG, INFO, WARN, ERROR) untuk sistem backend yang berjalan di server remote. Selalu buat tes regresi otomatis (regression test) sebelum menandai perbaikan bug selesai.",
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
    {
        "id": "f-testing",
        "category_id": "f-errors",
        "title": "Testing",
        "level": "beginner",
        "summary": "Memeriksa kebenaran kode secara otomatis agar fitur tidak mudah rusak.",
        "explanation_simple": "Bayangkan pabrik perakitan mobil uji tabrak. Sebelum mobil diizinkan meluncur di jalan raya bersama pengemudi nyata, setiap komponen diuji bertahap: bilah rem diuji tekanannya di mesin lab mekanik (Unit Test), lalu rem dipasang bersama pedal dan roda untuk menguji apakah hidrolik bekerja terintegrasi (Integration Test), dan terakhir mobil utuh dinaiki boneka uji coba untuk menabrak dinding beton dalam simulasi kecelakaan nyata (End-to-End Test).\n\nPengujian Otomatis (Testing) adalah jaminan keselamatan softwaremu. Ia memastikan bahwa fitur yang kamu buat hari ini tidak merusak sepuluh fitur lama yang kamu buat tiga bulan lalu (mencegah regresi). Batas analoginya: uji tabrak mobil menghancurkan mobil fisik yang mahal, sedangkan pengujian otomatis software dapat dijalankan ribuan kali dalam hitungan detik tanpa biaya fisik tambahan.",
        "explanation_technical": "Piramida Pengujian (Test Pyramid - Mike Cohn) membagi strategi pengujian menjadi tiga tingkatan: 1. Unit Tests (Dasar piramida, porsi terbesar ~70%): Menguji fungsi atau class terkecil secara terisolasi tanpa database atau jaringan nyata. Eksekusi dalam hitungan milidetik, deterministik, dan murah. Menggunakan Test Doubles (Mocks, Stubs, Fakes) untuk mengisolasi dependensi eksternal. 2. Integration Tests (Tengah piramida ~20%): Memverifikasi interaksi antarmodul atau integrasi kode dengan komponen nyata (seperti SQLite DB, file system, atau HTTP endpoints). 3. End-to-End (E2E) / UI Tests (Puncak piramida ~10%): Menguji alur pengguna nyata dari sudut pandang browser/layar HP (misal: registrasi -> checkout -> terima email). Paling lambat, mahal, dan rawan flakiness (kegagalan semu).\n\nPola penulisan tes terstandarisasi menggunakan pola AAA: - Arrange: menyiapkan data masukan dan mock. - Act: memanggil fungsi atau mengeksekusi operasi target. - Assert: memvalidasi bahwa hasil keluaran sesuai dengan ekspektasi matematis.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Unit test sederhana menggunakan assertion",
                "code": "function kaliDua(n: number): number { return n * 2; }\n// Skenario pengujian\nconst hasil = kaliDua(4);\nconst ekspektasi = 8;\nif (hasil === ekspektasi) {\n  console.log(\"TEST PASS: Hasil sesuai!\");\n} else {\n  console.log(`TEST FAIL: Dapat ${hasil}, harusnya ${ekspektasi}`);\n}",
                "explanation": "Assertion dasar: jika hasil fungsi sama dengan ekspektasi, tes dinyatakan lulus.",
                "expected_output": "TEST PASS: Hasil sesuai!"
            }
        ],
        "prerequisite_ids": [
            "f-functions",
            "f-debugging"
        ],
        "related_topic_ids": [
            "f-error-handling",
            "f-debugging"
        ],
        "why_vibecoding_matters": "Kelemahan terbesar vibecoding adalah kamu tidak membaca setiap baris kode yang dihasilkan AI. Satu-satunya cara aman untuk memastikan kode AI bekerja benar adalah dengan mewajibkan AI menuliskan Unit Test yang komprehensif. Saat vibecoding, beri prompt tegas: 'Tulis unit test yang mencakup: skenario sukses standar, kasus masukan kosong/null, kasus nilai batas ekstrem, dan kasus kegagalan jaringan. Jalankan tes tersebut dan pastikan semua lulus!'",
        "keywords": [
            "testing",
            "unit test",
            "assertion",
            "regresi",
            "verifikasi",
            "test runner"
        ],
        "estimated_minutes": 7,
        "sort_order": 20,
        "is_active": true,
        "problem_context": "Di tim software yang tidak memiliki tes otomatis, setiap kali ada perubahan kode sekecil apapun, para developer atau tim QA harus mengklik manual ratusan tombol di layar aplikasi untuk memastikan tidak ada fitur yang rusak. Pengujian manual ini sangat lambat, membosankan, rawan kelalaian manusia, dan membuat rilis software tertunda berminggu-minggu. Satu fitur checkout toko online rusak saat promo Midnight Sale dapat membakar jutaan transaksi dalam satu malam.",
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
        "when_to_use": "Terapkan Test-Driven Development (TDD) atau tulis unit test bersamaan dengan implementasi logika bisnis inti (kalkulasi uang, autentikasi, algoritma). Jalankan seluruh rangkaian unit test secara otomatis di CI/CD pipeline pada setiap Pull Request. Gunakan E2E test hanya untuk alur transaksi paling kritis (smoke test login dan pembayaran utama).",
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
    {
        "id": "f-memory",
        "category_id": "f-systems",
        "title": "Memory Basics",
        "level": "intermediate",
        "summary": "Memahami bagaimana program meminjam, memakai, dan mengembalikan memori komputer.",
        "explanation_simple": "Bayangkan sebuah meja kerja di bengkel kayu. Di atas meja kerja yang dekat dengan tanganmu (Call Stack), kamu meletakkan alat-alat kecil yang sedang kamu pakai sekarang (obeng, penggaris). Begitu pekerjaan selesai, meja langsung dibersihkan dalam sekejap. Namun, balok-balok kayu besar dan lemari setengah jadi disimpan di gudang luas di belakang bengkel (Heap Memory). Barang di gudang bisa bertahan berhari-hari dan diakses kapan saja, tetapi kamu membutuhkan petugas kebersihan berkala (Garbage Collector) untuk menyapu potongan kayu sisa agar gudang tidak penuh sesak.\n\nManajemen memori mengatur bagaimana program meminjam RAM dari sistem operasi dan mengembalikannya setelah selesai. Batas analogi bengkel: ruang RAM komputer menggunakan alamat virtual matematis yang dipetakan oleh kernel sistem operasi, sehingga program tidak pernah menyentuh keping RAM fisik secara sembarangan.",
        "explanation_technical": "Sistem operasi modern menyediakan Virtual Address Space untuk setiap proses terisolasi. Arsitektur memori program terbagi menjadi: 1. Text/Code Segment: instruksi biner mesin yang read-only. 2. Data & BSS Segment: variabel global dan statis. 3. Call Stack: struktur LIFO super cepat untuk alokasi stack frames fungsi, variabel lokal primitif, dan return addresses. Alokasi dan dealokasi stack hanya menggeser Stack Pointer register CPU (SP).\n\n4. Heap Memory: area memori dinamis untuk objek berukuran fleksibel yang dialokasikan runtime. Bahasa modern (Dart, JavaScript, Python, Go, Java) menggunakan Automatic Garbage Collection (GC). Algoritma GC umum adalah Tracing GC (Mark-and-Sweep dan Generational GC): GC menelusuri objek yang masih dapat dijangkau dari GC Roots (stack variables, global references). Objek yang tidak lagi memiliki rantai referensi dari roots ditandai sebagai sampah dan dibebaskan. Generational GC membagi heap menjadi Young Generation (objek baru yang sering mati muda) dan Old Generation untuk meminimalkan durasi jeda GC (stop-the-world pause).",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Ilustrasi referensi memori",
                "code": "let objA: any = { data: \"Penting\" };\nlet objB = objA; // objB merujuk ke memori yang sama\nobjA = null;    // objA dilepas, tapi memori belum dihapus karena masih ada objB\nconsole.log(objB.data);",
                "explanation": "Garbage Collector hanya menghapus data dari RAM jika tidak ada lagi variabel apa pun yang memegang referensinya.",
                "expected_output": "Penting"
            }
        ],
        "prerequisite_ids": [
            "f-variables-data-types"
        ],
        "related_topic_ids": [
            "f-references",
            "f-operating-system"
        ],
        "why_vibecoding_matters": "AI gemar membuat stream subscription atau timer berkala tanpa melengkapinya dengan method pembatalan (cancellation/dispose). Aplikasi yang dibuat dengan vibecoding mungkin tampak lancar di awal, tetapi setelah berpindah halaman 10 kali, HP pengguna mulai terasa panas dan baterai cepat habis karena puluhan objek tertinggal di memori. Saat vibecoding, selalu tanyakan: 'Di mana kode pembersihan (dispose/cleanup) untuk controller, timer, atau listener ini agar tidak terjadi memory leak?'",
        "keywords": [
            "memory",
            "ram",
            "stack",
            "heap",
            "garbage collector",
            "memory leak",
            "alokasi"
        ],
        "estimated_minutes": 7,
        "sort_order": 21,
        "is_active": true,
        "problem_context": "Pada bahasa pemrograman manual seperti C dan C++, programmer wajib memesan memori dengan malloc() dan membebaskannya dengan free(). Jika programmer lupa memanggil free(), memori RAM akan terus terpakai hingga server kehabisan RAM dan crash (Memory Leak). Sebaliknya, jika programmer membebaskan memori terlalu cepat tetapi masih mencoba mengaksesnya, terjadi celah keamanan fatal (Dangling Pointer / Use-After-Free) yang menjadi sumber dari 70% kerentanan keamanan perangkat lunak di dunia.",
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
        "when_to_use": "Pahami siklus hidup alokasi memori saat merancang aplikasi mobile atau game yang membutuhkan FPS 60/120 yang mulus tanpa stutter. Hindari alokasi objek sementara di dalam loop render berkecepatan tinggi agar tidak memicu GC thrashing (GC bekerja terlalu sering). Selalu bersihkan listener, stream subscriptions, dan controllers di method dispose() komponen.",
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
    {
        "id": "f-references",
        "category_id": "f-systems",
        "title": "Pointers/References",
        "level": "intermediate",
        "summary": "Melihat bagaimana variabel merujuk atau menunjuk ke data yang sama di memori.",
        "explanation_simple": "Bayangkan kamu membagikan tautan (link) Google Docs dokumen proposal kepada tiga rekan kerjamu. Kamu tidak mencetak tiga bundel kertas fisik untuk masing-masing orang, melainkan membagikan alamat URL yang sama. Jika rekan A menambahkan paragraf baru di Google Docs tersebut, rekan B dan kamu yang membuka dokumen lewat tautan tersebut akan langsung melihat paragraf tambahan tersebut secara bersamaan.\n\nReferensi (references) adalah tautan alamat ke lokasi objek di memori heap komputer. Batas analoginya: jika kamu menyalin selembar uang kertas dengan fotokopi (pass-by-value primitif), coretan spidol pada fotokopi tidak akan mempengaruhi uang kertas asli. Namun pada tipe referensi, beberapa variabel hanyalah beberapa nama julukan yang sama-sama menunjuk ke objek data fisik yang identik.",
        "explanation_technical": "Secara arsitektur prosesor, referensi adalah abstraksi aman dari memory pointer yang menyimpan alamat memori virtual (misalnya 0x7FFF1234). Tipe data primitif (int, float, bool) diteruskan dengan mekanisme Pass-by-Value: nilai bit digandakan ke stack frame baru. Sebaliknya, objek dan koleksi diteruskan dengan Pass-by-Sharing (atau pass-by-value dari nilai referensi pointer): alamat objek disalin, tetapi kedua pointer mengarah ke instance data heap yang sama.\n\nHal ini memicu fenomena Aliasing: mutasi data internal objek (in-place mutation) melalui satu referensi akan terlihat oleh semua referensi lain yang mengarah ke objek tersebut. Untuk mencegah efek samping mutasi liar (unintended side-effects), pola Immutable Objects, Defensive Copying (Shallow Copy vs Deep Copy), atau kata kunci pembatas mutasi (seperti const/readonly) sangat penting diterapkan dalam arsitektur software modern.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Pass-by-value vs Pass-by-reference",
                "code": "// Nilai primitif (kopi mandiri)\nlet a = 10;\nlet b = a;\nb = 20;\n// Objek (referensi bersama)\nconst obj1 = { val: 10 };\nconst obj2 = obj1;\nobj2.val = 99;\nconsole.log(\"a:\", a, \"b:\", b);\nconsole.log(\"obj1.val:\", obj1.val);",
                "explanation": "Variabel a tetap bernilai 10, tetapi obj1.val ikut berubah menjadi 99 karena obj1 dan obj2 berbagi objek memori yang sama.",
                "expected_output": "a: 10 b: 20\nobj1.val: 99"
            }
        ],
        "prerequisite_ids": [
            "f-memory"
        ],
        "related_topic_ids": [
            "f-memory",
            "f-variables-data-types"
        ],
        "why_vibecoding_matters": "AI sering menulis kode fungsi yang memodifikasi properti objek masukan secara langsung (in-place mutation), mengakibatkan bug misterius di bagian lain aplikasi yang mengandalkan objek tersebut sebelum termutasi. Saat vibecoding, instruksikan AI: 'Jangan lakukan mutasi langsung pada parameter objek ini; buatlah salinan baru (immutable return) menggunakan deep copy atau pattern copyWith.'",
        "keywords": [
            "reference",
            "pointer",
            "pass by value",
            "pass by reference",
            "mutasi",
            "cloning"
        ],
        "estimated_minutes": 7,
        "sort_order": 22,
        "is_active": true,
        "problem_context": "Bayangkan sebuah program game yang memiliki objek peta dunia 3D berukuran 500 Megabyte. Setiap kali fungsi merender cuaca, menghitung fisika, atau memproses musuh dipanggil, jika program harus menggandakan 500 MB data tersebut ke stack frame fungsi baru, memori komputer akan habis dalam sekejap dan game berjalan patah-patah (lag parah). Sistem referensi diciptakan agar fungsi dapat saling berbagi akses ke objek besar hanya dengan mengirimkan pointer alamat memori berukuran 4 atau 8 byte.",
        "misconceptions": [
            {
                "misconception": "Pernyataan b = a pada objek JavaScript atau Dart membuat salinan objek baru yang independen.",
                "explanation": "b = a hanya menyalin alamat referensi pointer; a dan b merujuk ke satu objek yang sama di heap memory.",
                "spot_in_code": "const clone = original; clone.items.push('baru'); mendapati original.items ikut berubah."
            },
            {
                "misconception": "Shallow copy (seperti Object.assign({}, obj) atau spread operator {...obj}) menyalin objek secara total hingga ke anak-anaknya.",
                "explanation": "Shallow copy hanya menggandakan properti level teratas; properti objek atau array bersarang di dalamnya tetap diteruskan sebagai referensi yang sama.",
                "spot_in_code": "const copy = {...user}; copy.profile.address = 'baru'; membuat user.profile.address ikut berubah."
            }
        ],
        "when_to_use": "Gunakan referensi untuk membagikan akses ke struktur data besar atau service singleton tanpa overhead penggandaan memori. Gunakan Deep Copy atau struktur data immutable saat mengirimkan state data ke komponen antarmuka pengguna agar perubahan lokal tidak merusak state pusat. Waspadai aliasing pada fungsi yang menerima parameter koleksi: jangan mutasi list parameter secara langsung kecuali fungsi tersebut didokumentasikan sebagai mutator eksplisit.",
        "reflection_questions": [
            {
                "question": "Apa perbedaan esensial antara Shallow Copy dan Deep Copy pada sebuah objek bersarang?",
                "answer": "Shallow Copy hanya menduplikasi properti tingkat pertama dan tetap membagikan referensi objek dalamnya, sedangkan Deep Copy menyalin seluruh pohon objek bersarang secara rekursif sehingga tercipta objek mandiri sepenuhnya."
            },
            {
                "question": "Mengapa paradigma fungsional mewajibkan immutability (data yang tidak boleh dimutasi)?",
                "answer": "Untuk mengeliminasi bug aliasing dan efek samping tersembunyi, sehingga kode menjadi dapat diprediksi secara matematis dan aman saat diakses bersamaan oleh multiple threads."
            }
        ]
    },
    {
        "id": "f-input-output",
        "category_id": "f-systems",
        "title": "Input/Output",
        "level": "beginner",
        "summary": "Cara program menerima masukan dari pengguna dan menampilkan hasilnya keluar.",
        "explanation_simple": "Bayangkan pintu gerbang dermaga pelabuhan peti kemas. Kapal kargo dari samudera lepas (input) membongkar muatan kontainer barang ke area dermaga. Pekerja dermaga menyortir dan mencatat barang tersebut di gudang (pemrosesan program), lalu memuat barang-barang yang sudah dipaketkan ke dalam truk pengantar untuk dikirim ke konsumen di darat (output).\n\nInput/Output (I/O) adalah jembatan komunikasi program dengan dunia nyata: membaca ketikan keyboard, menampilkan piksel di layar, atau bertukar data melalui kabel serat optik internet. Batas analogi dermaga: kapal fisik membutuhkan waktu berhari-hari untuk bersandar, sedangkan I/O komputer modern menggunakan ruang penyangga memori (Buffer) berkecepatan tinggi agar CPU tidak perlu menunggu setiap tetes bit data satu per satu.",
        "explanation_technical": "Operasi I/O dikelola melalui abstraksi File Descriptors di tingkat kernel sistem operasi (standar POSIX: 0 untuk stdin, 1 untuk stdout, 2 untuk stderr). Dua model eksekusi I/O: 1. Synchronous / Blocking I/O: Thread pemanggil ditangguhkan oleh kernel hingga operasi transfer byte tuntas. 2. Asynchronous / Non-blocking I/O: Panggilan I/O langsung kembali seketika dengan status EWOULDBLOCK/EAGAIN; sistem operasi memberitahukan penyelesaian data melalui mekanisme multiplexing I/O tingkat tinggi seperti epoll (Linux), kqueue (macOS/BSD), atau IOCP (Windows).\n\nKonsep Stream dan Buffer sangat penting: Stream mengalirkan data berukuran besar secara bertahap (chunk by chunk) tanpa perlu memuat seluruh file gigabyte ke dalam RAM sekaligus, memanfaatkan prinsip Backpressure untuk mengendalikan kecepatan aliran data agar penerima tidak tenggelam kehabisan memori.",
        "code_examples": [
            {
                "language": "python",
                "label": "Membaca input teks dan mencetak output",
                "code": "# Simulasi I/O standar\nnama = \"Budi\" # Di terminal interaktif: input(\"Nama: \")\npesan = f\"Halo, {nama}! Selamat datang.\"\nprint(pesan)",
                "explanation": "Program menerima nama sebagai input teks dan mengembalikan pesan yang diformat ke output.",
                "expected_output": "Halo, Budi! Selamat datang."
            }
        ],
        "prerequisite_ids": [
            "f-programming-logic"
        ],
        "related_topic_ids": [
            "f-file-system",
            "f-networking"
        ],
        "why_vibecoding_matters": "AI sering menulis fungsi pembacaan file dengan memuat seluruh isi file sekaligus ke satu variabel string (readAll). Kode ini langsung mengalami Out of Memory crash saat pengguna mengunggah file sungguhan di lingkungan produksi. Saat vibecoding, mintalah AI: 'Gunakan stream chunking dengan backpressure untuk membaca dan memproses data I/O ini agar konsumsi RAM stabil dan tidak membeku saat menangani file besar.'",
        "keywords": [
            "input",
            "output",
            "io",
            "stdin",
            "stdout",
            "stream",
            "periferal"
        ],
        "estimated_minutes": 6,
        "sort_order": 23,
        "is_active": true,
        "problem_context": "Prosesor komputer mampu beroperasi dalam hitungan nanodetik, sedangkan perangkat I/O fisik (seperti harddisk mekanik atau kartu jaringan) bekerja dalam hitungan milidetik — satu juta kali lebih lambat dari CPU! Jika setiap kali program membaca 1 byte dari keyboard CPU harus berhenti total menunggu jari manusia menekan tuts, seluruh daya komputasi komputer modern akan terbuang sia-sia dalam keadaan menganggur (idle). Arsitektur I/O modern (Interrupts, DMA, Buffering, Streams) diciptakan untuk membebaskan CPU dari belenggu kelambatan fisik ini.",
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
        "when_to_use": "Gunakan I/O Streams saat mengunggah, mengunduh, atau memproses file berukuran besar (gambar, video, dataset CSV). Gunakan buffered I/O untuk mengurangi jumlah system calls ke kernel. Selalu gunakan non-blocking async I/O pada aplikasi server web berkonkurensi tinggi.",
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
    {
        "id": "f-file-system",
        "category_id": "f-systems",
        "title": "File System Basics",
        "level": "beginner",
        "summary": "Membaca, menulis, dan mengelola berkas serta folder di media penyimpanan.",
        "explanation_simple": "Bayangkan lemari arsip baja di kantor kearsipan nasional. Setiap laci memiliki map berkas gantung, dan di dalam map terdapat formulir dokumen resmi. Di bagian depan setiap dokumen terdapat stiker label: nama dokumen, ukuran ketebalan lembar, tanggal pembuatan, serta stempel izin rahasia 'Hanya Boleh Dibaca Pimpinan'.\n\nSistem Berkas (File System) adalah cara sistem operasi menata dan melacak data yang disimpan di media permanen (SSD atau Flash Drive) agar data tidak hilang saat komputer dimatikan. Batas analogi lemari arsip: lemari fisik hanya bisa dibuka satu orang pada satu laci, sedangkan sistem berkas komputer mendukung akses ratusan proses secara konkuren dengan sistem penguncian file (file locking) dan jurnal pemulihan otomatis (Journaling).",
        "explanation_technical": "Sistem berkas modern (EXT4 di Linux, NTFS di Windows, APFS di macOS) mengelola dua lapisan utama: 1. Metadata Layer (Inode pada sistem UNIX-like): menyimpan informasi izin akses (permissions rwxrwxrwx), kepemilikan (UID/GID), ukuran file, timestamp (ctime, atime, mtime), dan daftar pointer ke blok data disk. Nama file dan struktur pohon direktori disimpan terpisah sebagai direktori entri (dentry) yang memetakan string nama ke nomor Inode.\n\n2. Data Block Layer: blok fisik tempat konten byte sebenarnya disimpan. Fitur vital lainnya adalah Journaling: mencatat perubahan yang akan dilakukan ke dalam log jurnal sebelum ditulis ke blok utama disk. Jika listrik padam di tengah penulisan file, sistem berkas dapat memulihkan diri (replay log) dalam hitungan detik tanpa merusak konsistensi disk.",
        "code_examples": [
            {
                "language": "python",
                "label": "Menulis dan membaca file dengan safe context",
                "code": "# Menulis teks ke file\nwith open(\"catatan.txt\", \"w\") as f:\n    f.write(\"Belajar File System\")\n# Membaca kembali teks dari file\nwith open(\"catatan.txt\", \"r\") as f:\n    isi = f.read()\nprint(isi)",
                "explanation": "Blok with memastikan file otomatis ditutup dengan aman meskipun terjadi kegagalan pembacaan.",
                "expected_output": "Belajar File System"
            }
        ],
        "prerequisite_ids": [
            "f-input-output"
        ],
        "related_topic_ids": [
            "f-operating-system",
            "f-databases"
        ],
        "why_vibecoding_matters": "AI sering menulis kode penulisan file dengan menggabungkan path string manual (misalnya folder + '/' + filename) tanpa memvalidasi apakah filename mengandung karakter berbahaya '../' yang bisa menimpa file sistem operasi penting. Saat vibecoding, instruksikan AI: 'Gunakan path library resmi lintas platform, terapkan validasi pencegahan path traversal, dan gunakan teknik atomic write untuk penulisan file kritis.'",
        "keywords": [
            "file system",
            "file",
            "folder",
            "direktori",
            "path",
            "read",
            "write",
            "storage"
        ],
        "estimated_minutes": 7,
        "sort_order": 24,
        "is_active": true,
        "problem_context": "Media penyimpanan fisik (seperti chip flash NAND pada SSD) hanya memahami blok byte mentah bernomor sektor 0, 1, 2... Jika programmer harus mengingat di sektor byte nomor berapa file 'laporan.pdf' disimpan, dan bagaimana menyatukan kembali file tersebut jika pecahannya tersebar di 5 sektor terpisah karena fragmentasi, pembuatan software akan menjadi mimpi buruk. File System diciptakan untuk menyediakan abstraksi direktori hierarki yang manusiawi dan menjamin keutuhan data terhadap pemadaman listrik mendadak.",
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
        "when_to_use": "Gunakan library path utility terstandarisasi (seperti path.join di Node.js atau package:path di Dart) untuk memastikan kompatibilitas lintas OS (Windows vs Linux/Mac). Gunakan Atomic File Writes (menulis ke file sementara lalu melakukan rename instan) untuk mencegah file korup jika aplikasi crash di tengah penulisan. Selalu sanitasi nama file masukan dari pengguna untuk mencegah serangan Path Traversal (../../etc/passwd).",
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
    {
        "id": "f-operating-system",
        "category_id": "f-systems",
        "title": "Operating System Basics",
        "level": "beginner",
        "summary": "Peran sistem operasi dalam menjembatani aplikasi dengan perangkat keras komputer.",
        "explanation_simple": "Bayangkan manajer gedung pencakar langit yang sangat disiplin. Gedung tersebut memiliki fasilitas bersama: generator listrik, saluran pendingin udara AC, dan lift penumpang. Para penyewa kantor di lantai 5 tidak boleh begitu saja membongkar kabel listrik gedung atau memonopoli seluruh lift untuk diri mereka sendiri. Penyewa harus mengajukan izin ke manajer gedung, dan sang manajer membagi aliran listrik serta giliran lift secara adil dan aman.\n\nSistem Operasi (Operating System - OS) adalah manajer gedung komputermu. Ia mengelola CPU, memori RAM, dan kartu grafis agar ratusan aplikasi yang berjalan tidak saling bertabrakan atau mencuri data satu sama lain. Batas analogi gedung: jika manajer gedung manusia bisa tertipu atau terlambat, kernel OS modern mengeksekusi aturan proteksi perangkat keras melalui sirkuit prosesor (Ring 0 vs Ring 3) dalam hitungan nanodetik.",
        "explanation_technical": "Arsitektur OS modern berpusat pada Kernel yang berjalan di tingkat hak istimewa tertinggi CPU (Kernel Mode / Ring 0), sedangkan aplikasi pengguna berjalan di User Mode (Ring 3) yang dibatasi. Aplikasi meminta layanan perangkat keras melalui System Calls (syscalls: seperti read, write, fork, socket) yang memicu peralihan konteks perangkat keras (software interrupt / trap).\n\nTanggung jawab inti OS meliputi: 1. Process & Thread Management: Proses adalah unit isolasi memori mandiri dengan ruang alamat virtual sendiri; Thread adalah unit eksekusi terkecil di dalam proses. OS Scheduler (seperti CFS di Linux) mengatur pembagian jatah waktu CPU (time-slicing). 2. Virtual Memory Management: Paging dan TLB memetakan memori virtual ke frame RAM fisik, melindungi proses dari saling mengintip memori. 3. Device Drivers & Hardware Abstraction: menyederhanakan komunikasi beragam kartu grafis, mouse, dan disk ke antarmuka standar.",
        "code_examples": [
            {
                "language": "python",
                "label": "Melihat informasi OS dari kode",
                "code": "import os, platform\nprint(\"OS:\", platform.system())\nprint(\"Process ID saat ini:\", os.getpid() > 0)",
                "explanation": "Modul os dan platform memungkinkan kode berinteraksi dengan API kernel sistem operasi.",
                "expected_output": "OS: Windows\nProcess ID saat ini: True"
            }
        ],
        "prerequisite_ids": [
            "f-file-system"
        ],
        "related_topic_ids": [
            "f-terminal",
            "f-concurrency"
        ],
        "why_vibecoding_matters": "AI sering membuat aplikasi backend yang langsung mati mendadak saat menerima sinyal shutdown dari sistem operasi, mengakibatkan data transaksi yang sedang disimpan menjadi terpotong dan korup di database. Saat vibecoding, beri instruksi ke AI: 'Tambahkan penanganan sinyal SIGTERM dan SIGINT untuk mengimplementasikan graceful shutdown: hentikan penerimaan request baru, tunggu koneksi yang aktif selesai, dan tutup koneksi database dengan rapi.'",
        "keywords": [
            "operating system",
            "os",
            "kernel",
            "process",
            "thread",
            "system call",
            "permissions"
        ],
        "estimated_minutes": 7,
        "sort_order": 25,
        "is_active": true,
        "problem_context": "Pada komputer generasi pertama, hanya ada satu program yang boleh berjalan dalam satu waktu. Jika program tersebut mengalami error crash atau memasuki loop abadi, seluruh komputer membeku dan tombol reset daya harus ditekan. Aplikasi juga bebas mengakses perangkat keras printer atau memori aplikasi lain secara telanjang tanpa proteksi keamanan apapun. Sistem Operasi diciptakan untuk menyediakan isolasi proses yang kokoh, penjadwalan CPU yang adil, dan keamanan memori berlapis.",
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
        "when_to_use": "Pahami konsep proses dan sinyal OS (seperti SIGINT, SIGTERM, SIGKILL) saat merancang aplikasi backend atau microservices agar server dapat melakukan Graceful Shutdown (menyelesaikan transaksi yang sedang berjalan sebelum dimatikan oleh orkestrator seperti Kubernetes). Gunakan multi-processing saat membutuhkan isolasi kegagalan total (crash di satu worker tidak mematikan worker lain).",
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
    {
        "id": "f-modules-packages",
        "category_id": "f-tooling",
        "title": "Modules & Packages",
        "level": "beginner",
        "summary": "Memecah kode menjadi berkas-berkas terpisah agar rapi dan mudah dipakai ulang.",
        "explanation_simple": "Bayangkan bermain dengan satu set balok mainan Lego bertema kastil. Di dalam kotak, kepingan balok tidak dicampur aduk berantakan dalam satu kantong plastik besar. Balok dinding dikemas dalam kantong nomor 1, kepingan gerbang hidrolik di kantong nomor 2, dan ksatria di kantong nomor 3. Setiap kantong memiliki buku instruksi mandiri yang jelas, dan kamu bisa merakit gerbang kastil tanpa harus membuka kantong ksatria.\n\nModul dan Paket adalah kantong-kantong pengorganisasian kode perangkat lunak. Batas analogi Lego: balok Lego fisik hanya bisa dihubungkan jika geriginya pas secara mekanis, sedangkan modul perangkat lunak mengekspos antarmuka publik (public API) resmi dan menyembunyikan fungsi internal rahasia di balik dinding namespace.",
        "explanation_technical": "Sistem modularitas modern (ES Modules di JavaScript, package system di Dart, modul di Python/Rust/Go) memberikan batas leksikal terisolasi untuk setiap file kode. Variabel yang dideklarasikan di dalam modul bersifat privat secara default, kecuali jika diekspor secara eksplisit menggunakan kata kunci export (atau penamaan tanpa underscore di Dart).\n\nStandar modularitas meliputi: 1. ES Modules (ESM): standar resmi web modern menggunakan sintaks import dan export statis yang dapat dianalisis pada compile-time untuk optimasi Tree Shaking (memangkas fungsi yang tidak pernah dipanggil dari biner akhir). 2. CommonJS (CJS): standar historis Node.js menggunakan require() dan module.exports yang bersifat dinamis saat runtime.\n\nPaket (Package) adalah kumpulan satu atau lebih modul terorganisir yang dilengkapi file manifest metadata (seperti pubspec.yaml di Dart/Flutter, package.json di Node.js, pyproject.toml di Python) yang mendefinisikan versi, entry point, dan dependensi.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Ekspor dan impor modul",
                "code": "// File matematika.ts (simulasi)\nconst PI = 3.14;\nfunction hitungLuas(r: number) { return PI * r * r; }\n// File utama: import { hitungLuas } from \"./matematika\";\nconsole.log(\"Luas lingkaran r=10:\", hitungLuas(10));",
                "explanation": "Fungsi diekspor dari satu berkas dan diimpor oleh berkas lain secara eksplisit.",
                "expected_output": "Luas lingkaran r=10: 314"
            }
        ],
        "prerequisite_ids": [
            "f-functions"
        ],
        "related_topic_ids": [
            "f-dependencies",
            "f-clean-code"
        ],
        "why_vibecoding_matters": "AI sering kali menghasilkan dependensi sirkular (circular imports) saat kamu meminta penambahan relasi antarmodul secara terburu-buru. Kode akan menampilkan error aneh seperti 'Cannot access variable before initialization' saat dijalankan. Saat vibecoding, instruksikan AI: 'Pastikan tidak ada ketergantungan sirkular antarmodul; jika Modul A dan Modul B membutuhkan tipe data yang sama, ekstrak tipe data tersebut ke modul Model bersama terpisah.'",
        "keywords": [
            "module",
            "package",
            "import",
            "export",
            "namespace",
            "modularitas"
        ],
        "estimated_minutes": 6,
        "sort_order": 26,
        "is_active": true,
        "problem_context": "Ketika sebuah aplikasi web bertambah besar hingga mencapai 100.000 baris kode, menyatukan seluruh kode dalam satu file atau memuat 200 file JavaScript melalui tag <script> di HTML memicu tabrakan nama variabel global (Global Namespace Pollution). Jika file A memiliki fungsi formatTanggal() dan file B juga memiliki formatTanggal() dengan implementasi berbeda, file yang dimuat terakhir akan menimpa fungsi pertama secara diam-diam. Sistem modul diciptakan untuk menciptakan dinding pemisah yang aman.",
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
        "when_to_use": "Pecah modul saat satu file kode mulai melampaui 300-400 baris atau memiliki lebih dari satu tanggung jawab domain. Gunakan ES Modules (import/export) sebagai standar penulisan kode modern daripada CommonJS (require). Gunakan Barrel Files (index.dart / index.ts) untuk mengekspor antarmuka publik fitur secara terpusat dan rapi.",
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
    {
        "id": "f-dependencies",
        "category_id": "f-tooling",
        "title": "Dependency Management",
        "level": "beginner",
        "summary": "Memasang dan mengelola pustaka buatan orang lain secara aman dan terkontrol.",
        "explanation_simple": "Bayangkan kamu membuka restoran pizza Italia. Kamu adalah koki ahli yang membuat adonan pizza lezat dengan resep rahasia sendiri. Namun, kamu tidak perlu beternak sapi sendiri untuk memerah keju mozzarella, dan tidak perlu menanam ladang gandum sendiri untuk menggiling terigu. Kamu memesan keju dan terigu dari pemasok logistik terpercaya di pasar. Jika pemasok mengirim keju kadaluarsa atau tiba-tiba menghentikan pengiriman, operasional tokomu bisa lumpuh seketika.\n\nDependensi (Dependencies) adalah pustaka (libraries) buatan developer lain yang kamu pasang di aplikasimu untuk mempercepat development. Batas analogi pemasok: bahan makanan fisik habis saat dipakai, sedangkan library kode perangkat lunak dapat diunduh gratis dari repositori publik (seperti pub.dev, npm, PyPI) dan digunakan jutaan kali tanpa pernah aus.",
        "explanation_technical": "Manajemen dependensi modern berlandaskan pada konvensi Semantic Versioning (SemVer: MAJOR.MINOR.PATCH): - PATCH (misal 1.0.1): perbaikan bug kompatibel mundur (backward compatible). - MINOR (misal 1.1.0): penambahan fitur baru yang tetap kompatibel mundur. - MAJOR (misal 2.0.0): perubahan yang merusak kompatibilitas (breaking changes).\n\nResolusi dependensi menggunakan algoritma pemuas batasan (Constraint Satisfaction / PubGrub algorithm pada Dart) untuk menemukan kombinasi versi yang cocok bagi seluruh pohon ketergantungan. Komponen paling krusial adalah Lockfile (seperti pubspec.lock, package-lock.json): mencatat versi eksak hingga checksum hash biner dari setiap library yang diinstal. Lockfile WAJIB dimasukkan ke dalam Git repository agar setiap developer di tim dan server CI/CD menggunakan kepingan kode yang 100% identik tanpa perbedaan tak terduga.",
        "code_examples": [
            {
                "language": "yaml",
                "label": "Contoh konfigurasi pubspec.yaml",
                "code": "name: codeatlas\ndependencies:\n  flutter:\n    sdk: flutter\n  sqflite: ^2.4.1\n  path: ^1.9.1",
                "explanation": "Menyatakan bahwa aplikasi membutuhkan paket sqflite versi kompatibel 2.4.1 untuk operasi database.",
                "expected_output": "Valid YAML"
            }
        ],
        "prerequisite_ids": [
            "f-modules-packages"
        ],
        "related_topic_ids": [
            "f-modules-packages",
            "f-build-compilation"
        ],
        "why_vibecoding_matters": "AI asisten sering menyarankan penginstalan paket baru untuk setiap masalah sepele, bahkan paket yang sudah usang atau paket halusinasi yang tidak pernah ada di registry publik (Hallucinated Package Attack). Saat vibecoding, jangan sembarangan menjalankan npm install atau flutter pub add yang disarankan AI. Periksa terlebih dahulu: 'Apakah masalah ini bisa diselesaikan dengan library standar bawaan bahasa? Berapa reputasi dan status pemeliharaan library ini di pub.dev/npm?'",
        "keywords": [
            "dependency",
            "package manager",
            "pubspec",
            "npm",
            "semver",
            "lockfile",
            "library"
        ],
        "estimated_minutes": 7,
        "sort_order": 27,
        "is_active": true,
        "problem_context": "Pada awal industri software, developer menyalin file kode orang lain secara manual ke folder proyek. Ketika library tersebut merilis perbaikan celah keamanan kritis, tidak ada cara otomatis untuk memperbaruinya. Lebih buruk lagi, terjadi 'Dependency Hell': Library A membutuhkan Library C versi 1.0, sedangkan Library B membutuhkan Library C versi 2.0 yang bertentangan. Package Manager modern (seperti pub, npm, pip, cargo) diciptakan untuk mengotomatisasi pengunduhan, verifikasi integritas, dan resolusi konflik versi.",
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
        "when_to_use": "Gunakan library pihak ketiga yang teruji dan memiliki komunitas aktif untuk masalah non-bisnis yang rumit (seperti enkripsi cryptography, parsing tanggal lintas zona waktu, koneksi HTTP/WebSockets). Jalankan audit keamanan berkala (misal flutter pub audit atau npm audit) untuk mendeteksi kerentanan CVE pada library usang. Selalu commit lockfile ke dalam version control repository.",
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
    {
        "id": "f-build-compilation",
        "category_id": "f-tooling",
        "title": "Build & Compilation Basics",
        "level": "intermediate",
        "summary": "Mengubah tulisan kode menjadi berkas aplikasi yang siap dijalankan perangkat.",
        "explanation_simple": "Bayangkan menulis naskah film berbahasa Indonesia lalu ingin memutarnya di bioskop Jepang. Proses produksi tidak hanya menerjemahkan teks dialog ke huruf Kanji, tetapi juga merekam dubbing suara pengisi suara Jepang, menyesuaikan resolusi video ke standar proyektor bioskop, memotong adegan yang tidak lolos sensor, dan menggabungkan seluruh rol film serta audio menjadi satu kaset DCP digital yang siap diputar di proyektor bioskop manapun.\n\nBuild & Compilation adalah pabrik perakitan yang mengubah teks kode sumber yang kamu ketik menjadi artefak akhir (file biner .exe, file .apk untuk Android, atau bundel .js untuk web). Batas analogi film: rol film hanya diputar lurus, sedangkan artefak biner komputer berisi jutaan instruksi logika yang berinteraksi secara dinamis dengan prosesor dan memori perangkat keras.",
        "explanation_technical": "Pipeline kompilasi klasik (Compiler Pipeline) melewati beberapa fase formal: 1. Lexical Analysis (Scanning): memecah teks kode menjadi aliran token (keywords, identifiers, literals). 2. Syntax Analysis (Parsing): menyusun token menjadi pohon sintaksis pohon abstrak (Abstract Syntax Tree - AST) sesuai tata bahasa formal. 3. Semantic Analysis: memeriksa kepatuhan tipe data, scope variabel, dan deklarasi identifikasi. 4. Intermediate Representation (IR) Optimization: mesin kompilator modern (seperti LLVM) menyederhanakan IR untuk membuang kode mati, melakukan loop unrolling, dan inlining function tanpa terikat arsitektur hardware tertentu. 5. Code Generation & Linking: menghasilkan kode mesin biner target (Assembler) dan Linker menggabungkan modul biner mandiri dengan library eksternal menjadi satu file eksekusi (executable).\n\nDua model kompilasi utama: - Ahead-Of-Time (AOT): kompilasi selesai sebelum program dirilis; eksekusi awal super cepat (Dart release mode, Rust, Go, C++). - Just-In-Time (JIT): kompilasi dilakukan saat program berjalan; mendukung Hot Reload dinamis namun membutuhkan waktu pemanasan awal (Dart debug mode, Java JVM, browser V8).",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Perbedaan file sumber vs hasil kompilasi",
                "code": "// Sumber TypeScript (ada tipe data):\nconst sapa = (nama: string): string => `Halo, ${nama}`;\n// Hasil kompilasi JavaScript biasa:\n// var sapa = function (nama) { return \"Halo, \" + nama; };\nconsole.log(sapa(\"Dunia\"));",
                "explanation": "TypeScript dikompilasi (transpiled) menjadi JavaScript standar yang dapat dipahami oleh runtime browser atau Node.js.",
                "expected_output": "Halo, Dunia"
            }
        ],
        "prerequisite_ids": [
            "f-modules-packages"
        ],
        "related_topic_ids": [
            "f-runtime",
            "f-type-system"
        ],
        "why_vibecoding_matters": "Developer sering mengeluh aplikasi yang dibuat dengan vibecoding terasa lambat atau berukuran raksasa saat dicoba di HP, hanya karena mereka menguji build debug yang menyertakan seluruh tool developer dan server JIT internal. Saat vibecoding, pastikan kamu menguji build produksi yang sesungguhnya: 'Jalankan command flutter build apk --release atau npm run build, dan verifikasi performa serta ukuran file pada bundel rilis final.'",
        "keywords": [
            "build",
            "kompilasi",
            "compiler",
            "aot",
            "jit",
            "transpiler",
            "hot reload"
        ],
        "estimated_minutes": 8,
        "sort_order": 28,
        "is_active": true,
        "problem_context": "Prosesor komputer tidak mengerti kata kunci 'if', 'class', atau 'function'; prosesor hanya memahami voltase bit biner 0 dan 1 instruksi arsitektur spesifik (seperti x86_64, ARM64, RISC-V). Jika developer harus menulis biner mesin manual untuk setiap tipe HP Android dan laptop yang berbeda di pasaran, pembuatan software global tidak akan pernah terwujud. Compiler diciptakan untuk menjembatani bahasa tingkat tinggi manusia ke efisiensi biner mesin tanpa developer perlu memahami sirkuit silikon mikroprosesor secara mendalam.",
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
        "when_to_use": "Gunakan mode JIT selama siklus pengembangan aktif untuk menikmati fitur Hot Reload / Hot Module Replacement yang instan. Selalu gunakan mode AOT / Production Build saat melakukan benchmarking performa, profiling konsumsi baterai, atau rilis ke pengguna akhir. Aktifkan Minification dan Tree Shaking pada web build untuk memangkas ukuran download aset.",
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
    {
        "id": "f-runtime",
        "category_id": "f-tooling",
        "title": "Runtime Basics",
        "level": "intermediate",
        "summary": "Lingkungan tempat kode berjalan dan dieksekusi oleh komputer.",
        "explanation_simple": "Bayangkan panggung pertunjukan teater musikal. Naskah drama dan partitur musik yang ditulis sutradara adalah kode program. Namun agar pertunjukan dapat dinikmati penonton, dibutuhkan panggung megah yang dilengkapi lampu sorot, pengeras suara mikrofon, lantai hidrolik, dan kru panggung yang sigap mengganti dekorasi di balik layar. Tanpa fasilitas panggung dan kru tersebut, naskah drama hanyalah tumpukan kertas mati yang tidak bisa ditonton siapa pun.\n\nRuntime Engine adalah panggung pertunjukan tempat kodemu dieksekusi secara nyata. Batas analogi panggung: panggung fisik teater bersifat tetap, sedangkan runtime modern (seperti Node.js, browser V8, Dart VM) mengoptimalkan kinerjanya secara adaptif selagi kode berjalan menggunakan teknik profiling dinamis.",
        "explanation_technical": "Runtime Environment mencakup sekumpulan komponen esensial yang aktif mendampingi program selama berjalan: 1. Virtual Machine / Execution Engine (misalnya V8 di Chrome/Node.js, Dart VM, JVM di Java): menerjemahkan bytecode atau mengeksekusi instruksi AOT. 2. Memory Manager: mengelola Garbage Collection, alokasi heap, dan batas call stack. 3. Concurrency / Event Scheduler: mengelola thread pool sistem operasi dan memutar Event Loop untuk penjadwalan callback asinkron. 4. Standard Built-in APIs: menyediakan akses ke antarmuka I/O dasar, waktu sistem (timers), kriptografi, dan manipulasi teks.\n\nPerbedaan lingkungan runtime sangat mempengaruhi kapabilitas kode: - Runtime Browser (V8/JavaScriptCore): diisolasi ketat dalam security sandbox (tidak memiliki akses langsung ke sistem berkas disk lokal atau socket TCP mentah). - Runtime Server (Node.js/Bun/Deno): memiliki akses penuh ke sistem berkas disk, jaringan server port binding, dan proses sistem operasi.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Event loop runtime mengantrekan tugas",
                "code": "console.log(\"1. Mulai\");\nsetTimeout(() => {\n  console.log(\"2. Timer selesai\");\n}, 0);\nconsole.log(\"3. Selesai\");",
                "explanation": "Meskipun timeout diset 0ms, callback dimasukkan ke antrean event loop dan baru dieksekusi setelah kode sinkron utama selesai.",
                "expected_output": "1. Mulai\n3. Selesai\n2. Timer selesai"
            }
        ],
        "prerequisite_ids": [
            "f-build-compilation"
        ],
        "related_topic_ids": [
            "f-build-compilation",
            "f-async"
        ],
        "why_vibecoding_matters": "AI sering mencampuradukkan API runtime yang tidak kompatibel: menyarankan pemanggilan modul Node.js (seperti 'fs' atau 'crypto' native) di dalam komponen frontend React browser, yang langsung memicu build error 'Module not found: Can't resolve fs'. Saat vibecoding, tegaskan konteks runtime ke AI: 'Kode ini akan dijalankan di runtime browser klien, jangan gunakan API internal server Node.js atau modul native platform.'",
        "keywords": [
            "runtime",
            "environment",
            "dart vm",
            "v8",
            "event loop",
            "call stack",
            "eksekusi"
        ],
        "estimated_minutes": 7,
        "sort_order": 29,
        "is_active": true,
        "problem_context": "Setiap sistem operasi dan arsitektur hardware memiliki antarmuka yang sangat berbeda: panggilan sistem Linux tidak sama dengan Windows, dan prosesor Intel tidak memahami perintah prosesor Apple M-series. Jika bahasa pemrograman tidak memiliki runtime terstandarisasi, programmer harus menulis kode manajemen memori dan interaksi hardware yang berbeda untuk setiap platform. Lingkungan runtime diciptakan untuk menyediakan sandbox eksekusi terstandarisasi yang konsisten di berbagai platform fisik (Write Once, Run Anywhere).",
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
        "when_to_use": "Pahami batasan runtime tempat kodemu akan dieksekusi: gunakan Browser Runtime untuk antarmuka pengguna visual interaktif, dan gunakan Server Runtime (Node.js/Go/Dart) saat membutuhkan akses database atau file system lokal. Manfaatkan fitur runtime modern seperti WebAssembly (Wasm) jika kamu butuh mengeksekusi komputasi bahasa biner di dalam browser.",
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
    {
        "id": "f-git",
        "category_id": "f-tooling",
        "title": "Version Control/Git",
        "level": "beginner",
        "summary": "Mencatat riwayat perubahan kode dan bekerja bersama tim tanpa saling menimpa.",
        "explanation_simple": "Bayangkan sebuah mesin waktu untuk naskah buku yang sedang kamu tulis bersama sepuluh penulis lain. Setiap kali kamu mencapai kemajuan penting (misalnya menyelesaikan Bab 1), kamu menekan tombol simpan khusus yang mengambil foto rontgen instan (Snapshot / Commit) dari seluruh naskah lengkap dengan catatan tanggal dan namamu. Jika di Bab 3 alur cerita menjadi buntu, kamu bisa memutar balik waktu ke kondisi Bab 1 dengan satu sentuhan. Lebih hebat lagi, rekanmu bisa membuat cabang cerita alternatif (Branch) tanpa mengganggu naskah utamamu, lalu menggabungkannya kembali (Merge) saat alur alternatif tersebut terbukti bagus.\n\nGit adalah sistem kendali versi paling dominan di dunia rekayasa perangkat lunak. Batas analogi mesin waktu: mesin waktu fiksi bisa membingungkan paradoks sejarah, sedangkan Git menggunakan matematika kriptografi graf (DAG berbasis SHA-1/SHA-256) yang menjamin riwayat perubahan tidak bisa dipalsukan atau dirusak secara diam-diam.",
        "explanation_technical": "Arsitektur internal Git berbasis pada Content-Addressable Storage yang memetakan konten data ke hash kriptografi (kunci 40 karakter). Empat objek inti Git: 1. Blob: menyimpan konten mentah file. 2. Tree: merepresentasikan struktur direktori dan nama file. 3. Commit: menyimpan pointer ke root tree, metadata pembuat (author/committer), timestamp, pesan log, dan pointer ke commit induk (parent commit). 4. Tag/Branch: penunjuk simbolik (pointer referensi ringan) ke hash commit tertentu.\n\nTiga area kerja Git di komputer lokal: - Working Directory: file nyata yang sedang kamu edit. - Staging Area (Index): berkas yang sudah kamu tandai (git add) untuk dimasukkan ke foto komit berikutnya. - Repository (.git folder): database objek riwayat permanen (git commit).\n\nOperasi Merge menyatukan dua cabang independen (Fast-Forward jika lurus, atau 3-Way Merge yang melahirkan merge commit). Jika baris kode yang sama diubah berbeda di kedua cabang, Git menghentikan proses dan meminta manusia menyelesaikan Merge Conflict.",
        "code_examples": [
            {
                "language": "bash",
                "label": "Perintah dasar alur kerja Git",
                "code": "git status          # Melihat file yang berubah\ngit add .           # Memilih semua perubahan\ngit commit -m \"feat: tambah fitur login\" # Simpan snapshot\ngit log -n 1 --oneline # Lihat commit terakhir",
                "explanation": "Alur standar menyimpan riwayat pekerjaan secara bertahap dan rapi.",
                "expected_output": "[main a1b2c3d] feat: tambah fitur login"
            }
        ],
        "prerequisite_ids": [
            "f-terminal"
        ],
        "related_topic_ids": [
            "f-terminal",
            "f-clean-code"
        ],
        "why_vibecoding_matters": "Saat vibecoding, AI dapat dengan cepat mengubah ratusan baris kode sekaligus dalam hitungan detik. Jika kamu tidak melakukan commit sebelum meminta AI melakukan refactoring besar, dan ternyata kode yang dihasilkan AI rusak total, kamu akan kehilangan seluruh pekerjaanmu sebelumnya tanpa jalan mundur. Jadikan aturan besi vibecoding: 'Selalu lakukan git commit kondisi kerja yang stabil sebelum memberikan prompt perubahan besar kepada AI!'",
        "keywords": [
            "git",
            "version control",
            "commit",
            "branch",
            "github",
            "merge",
            "snapshot"
        ],
        "estimated_minutes": 7,
        "sort_order": 30,
        "is_active": true,
        "problem_context": "Sebelum adanya version control modern, programmer mencadangkan folder proyek dengan cara manual yang kacau: skripsi_final.zip, skripsi_final_beneran.zip, skripsi_final_revisi_dosen_OK_banget.zip. Ketika dua programmer mengedit file yang sama di server kantor pada hari yang sama, pekerjaan salah satu programmer pasti tertimpa dan hilang permanen tanpa jejak. Git diciptakan oleh Linus Torvalds pada tahun 2005 untuk memfasilitasi kolaborasi ribuan pengembang kernel Linux di seluruh dunia secara terdistribusi tanpa bergantung pada satu server pusat yang rapuh.",
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
        "when_to_use": "Lakukan commit secara teratur dengan cakupan perubahan kecil yang atomik (Atomic Commits) dan pesan deskriptif. Gunakan cabang fitur (Feature Branches: misal feature/login-page) untuk setiap tugas baru agar cabang utama (main) selalu stabil dan siap rilis. Gunakan .gitignore untuk mengabaikan file build binary, dependency cache (node_modules), dan file kredensial rahasia (.env).",
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
    {
        "id": "f-terminal",
        "category_id": "f-tooling",
        "title": "Command Line/Terminal",
        "level": "beginner",
        "summary": "Memberi instruksi ke komputer secara langsung lewat baris perintah teks.",
        "explanation_simple": "Bayangkan memesan makanan di restoran mewah melalui pelayan yang membawa buku menu bergambar (Antarmuka Grafis / GUI): kamu menunjuk foto makanan, memilih dari opsi yang sudah disediakan, dan prosesnya terasa santai serta visual. Sekarang bayangkan kamu berbicara langsung ke kepala koki di dapur melalui walkie-talkie instruksi singkat (Terminal / CLI): 'Panggang daging tingkat medium-well 200 gram, tanpa garam, tambahkan lada hitam giling kasar'. Instruksi radio baris perintah membutuhkan kamu tahu istilah tepatnya, tetapi ia memberikan kebebasan mutlak, presisi tinggi, dan kecepatan tanpa batas.\n\nTerminal adalah pintu gerbang komunikasi paling murni antara manusia dan sistem operasi komputer. Batas analoginya: walkie-talkie fisik memiliki jangkauan suara terbatas, sedangkan terminal komputer modern dapat mengendalikan ribuan server di benua lain melalui protokol terenkripsi SSH.",
        "explanation_technical": "Terminal bekerja melalui arsitektur Shell (seperti Bash, Zsh di Linux/macOS, PowerShell di Windows). Shell beroperasi dalam siklus REPL (Read-Eval-Print Loop): membaca baris perintah teks, mem-parsing token, mengevaluasi argumen dan variabel environment, menjalankan proses biner yang diminta, dan menampilkan output teks ke konsol.\n\nPrinsip fundamental filosofi UNIX dalam CLI: 1. Standard Streams: setiap program CLI memiliki tiga saluran aliran byte: Standard Input (stdin / 0), Standard Output (stdout / 1), dan Standard Error (stderr / 2). 2. Redirection: mengarahkan output ke file menggunakan operator > (timpa) atau >> (tambah ke akhir file). 3. Pipes (|): menghubungkan stdout dari Program A langsung menjadi stdin bagi Program B tanpa file perantara (misal: cat log.txt | grep 'ERROR' | wc -l). Komposisi perintah-perintah kecil yang fokus (do one thing well) melahirkan kapabilitas otomatisasi yang tak terbatas.",
        "code_examples": [
            {
                "language": "bash",
                "label": "Perintah navigasi terminal umum",
                "code": "pwd              # Cetak folder kerja saat ini\nls -la           # Tampilkan daftar file lengkap\nmkdir proyek_baru # Buat folder baru\ncd proyek_baru   # Masuk ke folder baru",
                "explanation": "Perintah dasar navigasi sistem file menggunakan teks di antarmuka baris perintah.",
                "expected_output": "/Users/developer/proyek_baru"
            }
        ],
        "prerequisite_ids": [
            "f-operating-system"
        ],
        "related_topic_ids": [
            "f-operating-system",
            "f-git"
        ],
        "why_vibecoding_matters": "AI sering menyarankan perintah terminal untuk dieksekusi pengguna (misalnya perintah rm -rf, konfigurasi environment variables, atau instalasi global). Jika kamu mengeksekusi perintah terminal AI secara buta tanpa memahaminya, perintah yang keliru bisa menghapus seluruh file harddisk komputermu secara permanen. Saat vibecoding, teliti setiap perintah shell: 'Jelaskan apa yang dilakukan oleh setiap flag pada perintah terminal ini sebelum saya menjalankannya!'",
        "keywords": [
            "terminal",
            "command line",
            "cli",
            "shell",
            "bash",
            "powershell",
            "perintah"
        ],
        "estimated_minutes": 6,
        "sort_order": 31,
        "is_active": true,
        "problem_context": "Antarmuka visual grafis (GUI) seperti jendela tombol dan klik mouse sangat ramah untuk pengguna biasa, tetapi sangat buruk untuk otomatisasi pekerjaan massal. Jika kamu diminta mengubah nama 10.000 file foto dari 'IMG_001.jpg' menjadi 'Liburan_001.jpg', melakukannya dengan klik mouse akan memakan waktu tiga minggu penuh. Di terminal CLI, satu baris perintah loop atau pipe dapat menyelesaikan tugas tersebut dalam waktu 2 detik.",
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
        "when_to_use": "Gunakan terminal untuk menjalankan build tools, package managers, generator kode, dan otomasi skrip deployment. Gunakan piping (|) dan utilitas text-processing (grep, awk, sed, jq) untuk menganalisis log sistem berukuran ratusan megabyte secara instan di server. Kuasai navigasi dasar: cd, ls/dir, pwd, rm, mkdir, cat/type, dan curl.",
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
    {
        "id": "f-networking",
        "category_id": "f-web",
        "title": "Networking Basics",
        "level": "beginner",
        "summary": "Cara komputer saling bertukar data melalui kabel, sinyal, dan internet.",
        "explanation_simple": "Bayangkan mengirim surat pos dari Jakarta ke sahabatmu di pedalaman London. Kamu memasukkan surat ke dalam amplop, menuliskan nama penerima, alamat jalan, kode pos kota, dan negara tujuan. Petugas kantor pos Jakarta tidak langsung terbang mengantar suratmu ke London; surat dibawa ke kantor pos kecamatan, lalu ke bandara kargo udara, dipindahkan ke pesawat transit di Dubai, tiba di bandara Heathrow London, disortir oleh van pos regional, dan akhirnya dimasukkan kurir ke kotak pos rumah sahabatmu.\n\nJaringan Komputer (Networking) adalah sistem pengiriman paket data digital melintasi kabel tembaga, serat optik bawah laut, dan gelombang radio Wi-Fi. Batas analogi pos: surat pos fisik bisa basah atau hilang di jalan, sedangkan jaringan komputer modern memiliki protokol cerdas (seperti TCP) yang memotong pesan menjadi ribuan paket kecil bernomor urut, dan meminta pengiriman ulang otomatis jika ada satu paket yang hilang di tengah jalan.",
        "explanation_technical": "Komunikasi jaringan diabstraksikan melalui Model 7 Lapisan OSI (Open Systems Interconnection) dan arsitektur praktis Internet Protocol Suite (TCP/IP 4 Lapisan): 1. Physical Layer: sinyal listrik bit biner pada kabel fisik, serat optik, atau radio Wi-Fi. 2. Data Link Layer (Ethernet, Wi-Fi MAC Address): transmisi frame data antar-perangkat di jaringan lokal yang sama (LAN). 3. Network Layer (IP - Internet Protocol): perutean paket (routing) melintasi berbagai jaringan menggunakan IP Address (IPv4 32-bit / IPv6 128-bit). 4. Transport Layer: komunikasi antar-proses aplikasi menggunakan port (Port 0-65535).\n\nDua protokol Transport paling esensial: - TCP (Transmission Control Protocol): Connection-oriented, Three-Way Handshake (SYN -> SYN-ACK -> ACK), menjamin urutan paket, retransmisi paket hilang, dan pengendalian kemacetan (Congestion Control). Digunakan oleh HTTP, Web, Email, SSH. - UDP (User Datagram Protocol): Connectionless, tanpa handshake, tanpa jaminan urutan atau pengiriman ulang, overhead minimal dan latensi sangat rendah. Digunakan oleh Voice VoIP, Live Video Streaming, DNS query, dan Game Online real-time.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Konsep IP address dan port tujuan",
                "code": "const host = \"127.0.0.1\"; // Localhost (alamat komputer ini)\nconst port = 8080;        // Pintu masuk spesifik aplikasi\nconsole.log(`Server siap mendengar di http://${host}:${port}`);",
                "explanation": "Kombinasi IP address dan nomor port mengidentifikasi aplikasi spesifik di suatu mesin server.",
                "expected_output": "Server siap mendengar di http://127.0.0.1:8080"
            }
        ],
        "prerequisite_ids": [
            "f-input-output"
        ],
        "related_topic_ids": [
            "f-http-web",
            "f-apis"
        ],
        "why_vibecoding_matters": "AI sering menulis kode jaringan tanpa memperhitungkan latensi dunia nyata (Network Latency) dan paket yang putus sesaat (packet drop), menganggap komunikasi jaringan selalu secepat membaca memori RAM lokal. Saat vibecoding, ingatkan AI: 'Jaringan internet bersifat tidak stabil (unreliable network): tambahkan konfigurasi timeout yang masuk akal, mekanisme exponential backoff retry, dan penanganan status offline pada aplikasi ini.'",
        "keywords": [
            "networking",
            "jaringan",
            "ip",
            "tcp",
            "udp",
            "dns",
            "port",
            "paket data"
        ],
        "estimated_minutes": 7,
        "sort_order": 32,
        "is_active": true,
        "problem_context": "Ketika dua komputer terhubung kabel secara fisik, voltase listrik yang melintasi kabel mudah mengalami interferensi derau (noise), tabrakan paket (packet collisions), dan keterbatasan jarak sinyal. Lebih rumit lagi ketika miliaran komputer di seluruh dunia dengan sistem operasi dan kecepatan jaringan yang berbeda ingin saling mengobrol. Standarisasi protokol jaringan berlapis diciptakan agar setiap lapisan teknologi (dari kabel fisik hingga aplikasi web) dapat berevolusi secara independen tanpa merusak komunikasi global.",
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
        "when_to_use": "Gunakan TCP (melalui HTTP/HTTPS/WebSockets) untuk transfer dokumen, transaksi keuangan, autentikasi, dan API di mana integritas data 100% mutlak. Gunakan UDP (atau WebRTC data channels) untuk streaming audio/video langsung, telemetry sensor IoT berkecepatan tinggi, dan transmisi posisi game real-time. Pahami batasan MTU (Maximum Transmission Unit, biasanya 1.500 byte) saat merancang paket jaringan mentah.",
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
    {
        "id": "f-http-web",
        "category_id": "f-web",
        "title": "HTTP/Web Fundamentals",
        "level": "beginner",
        "summary": "Aturan komunikasi web untuk meminta dan mengirim halaman atau data.",
        "explanation_simple": "Bayangkan memesan hidangan di restoran mewah melalui pelayan. Kamu sebagai tamu (Client / Browser) membaca daftar menu lalu menyampaikan pesanan ke pelayan: 'Tolong ambilkan Nasi Goreng Spesial' (HTTP Request). Pelayan membawa pesanan ke dapur koki (Server), menunggu hidangan dimasak, lalu kembali ke mejamu sambil membawa piring dan berkata: 'Ini Nasi Gorengnya, status 200 Sukses' (HTTP Response). Jika stok ayam habis, pelayan kembali dan berkata: 'Maaf, menu tidak tersedia, status 404 Not Found'.\n\nHTTP (Hypertext Transfer Protocol) adalah tata krama percakapan resmi antara browser web atau aplikasi HP dengan server di internet. Batas analogi restoran: pelayan restoran biasanya mengingat wajahmu di meja nomor 4, sedangkan protokol HTTP secara default bersifat Stateless (lupa ingatan): setiap kali kamu memesan piring kedua, server menganggapmu sebagai orang asing yang baru datang, sehingga aplikasi membutuhkan Cookie atau Token untuk membuktikan identitasmu.",
        "explanation_technical": "HTTP adalah protokol Application Layer (di atas TCP/IP) berbasis siklus Request-Response: 1. HTTP Request terdiri dari: - Method / Verb: niat aksi (GET: membaca, POST: membuat baru, PUT: mengganti total, PATCH: mengubah sebagian, DELETE: menghapus). - URL / Path: alamat sumber daya target (misal: /api/v1/users/42). - Headers: metadata kontekstual (User-Agent, Content-Type, Authorization, Accept). - Body: muatan payload data (biasanya berformat JSON pada REST API).\n\n2. HTTP Response terdiri dari: - Status Code: kode numerik 3 digit indikator hasil (1xx: Informasi, 2xx: Sukses [200 OK, 201 Created], 3xx: Pengalihan [301, 302], 4xx: Kesalahan Klien [400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found], 5xx: Kesalahan Server [500 Internal Error, 502 Bad Gateway]). - Response Headers: metadata server (Content-Type, Set-Cookie, Cache-Control). - Response Body: payload data hasil (HTML, JSON, file biner).\n\nEvolusi protokol: HTTP/1.1 (koneksi teks, rawan Head-of-Line blocking), HTTP/2 (biner, multiplexing beberapa request dalam satu koneksi TCP), dan HTTP/3 (berbasis protokol QUIC di atas UDP untuk mengatasi packet loss dan koneksi instan 0-RTT).",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Mengirim HTTP GET request dengan fetch",
                "code": "// async function ambilData() {\n//   const res = await fetch(\"https://api.example.com/items\");\n//   console.log(\"Status:\", res.status);\n// }\nconsole.log(\"HTTP Method: GET, URL: /items, Status Harapan: 200\");",
                "explanation": "Client mengirim permintaan GET dan server merespons dengan kode status 200 jika data ditemukan.",
                "expected_output": "HTTP Method: GET, URL: /items, Status Harapan: 200"
            }
        ],
        "prerequisite_ids": [
            "f-networking"
        ],
        "related_topic_ids": [
            "f-networking",
            "f-apis",
            "f-security"
        ],
        "why_vibecoding_matters": "AI sering kali menghasilkan endpoint API yang mencampuradukkan HTTP methods (misalnya menggunakan POST untuk mengambil data detail, atau GET untuk menghapus akun). Selain melanggar konvensi web, hal ini merusak mekanisme caching browser dan membuka celah keamanan CSRF. Saat vibecoding, instruksikan AI: 'Patuhi standar semantik HTTP: gunakan HTTP verbs yang sesuai, kembalikan status code yang presisi (200, 201, 400, 401, 404, 500), dan gunakan HTTPS dengan header keamanan standar.'",
        "keywords": [
            "http",
            "request",
            "response",
            "get",
            "post",
            "status code",
            "headers",
            "web"
        ],
        "estimated_minutes": 7,
        "sort_order": 33,
        "is_active": true,
        "problem_context": "Ketika Tim Berners-Lee merancang World Wide Web pada tahun 1989, para ilmuwan membutuhkan cara sederhana dan terbuka untuk bertukar dokumen teks hiperteks antar-komputer universitas di seluruh dunia tanpa mempedulikan jenis sistem operasinya. Diperlukan sebuah protokol berbasis teks yang universal, fleksibel, dan tidak memerlukan sambungan kabel eksklusif yang terus terbuka. HTTP diciptakan sebagai protokol Request-Response sederhana yang kini menjadi fondasi seluruh ekonomi digital internet modern.",
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
        "when_to_use": "Gunakan GET untuk membaca data, POST untuk pembuatan entitas baru, PUT/PATCH untuk pembaruan, dan DELETE untuk penghapusan sesuai kaidah arsitektur REST. Selalu gunakan HTTPS (HTTP over TLS/SSL port 443) untuk mengenkripsi lalu lintas data dari serangan penyadapan Man-in-the-Middle. Manfaatkan header Cache-Control untuk menghemat kuota server dan mempercepat loading aplikasi klien.",
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
    },
    {
        "id": "f-apis",
        "category_id": "f-web",
        "title": "API Fundamentals",
        "level": "beginner",
        "summary": "Pintu penghubung agar dua aplikasi atau sistem berbeda bisa saling berbicara.",
        "explanation_simple": "Bayangkan colokan listrik dinding di rumahmu. Perusahaan listrik PLN tidak mengizinkanmu menyambungkan kabel tembaga telanjang langsung ke gardu trafo tegangan tinggi. Sebagai gantinya, mereka menyediakan stopkontak dua lubang berstandar 220 Volt di dinding kamar. Pabrikan pembuat kulkas, TV, dan charger laptop cukup membuat steker dua kaki yang cocok dengan stopkontak tersebut. Kulkasmu tidak perlu tahu apakah listrik PLN dibangkitkan dari tenaga surya, air, atau batubara; ia hanya butuh stopkontak yang bekerja.\n\nAPI (Application Programming Interface) adalah stopkontak resmi perangkat lunak. Batas analoginya: stopkontak listrik mengalirkan arus satu arah ke alatmu, sedangkan API modern adalah percakapan cerdas dua arah yang memvalidasi otorisasi, memfilter data, dan membatasi kuota panggilan (Rate Limiting).",
        "explanation_technical": "API mendefinisikan kontrak formal (Interface Contract) antara penyedia layanan (Provider) dan konsumen (Consumer). Paradigma arsitektur API modern mencakup: 1. REST (Representational State Transfer): Berbasis resource URI (/users, /orders), menggunakan HTTP verbs semantik (GET, POST, PUT, DELETE), stateless, dan merespons dalam format JSON standar. 2. GraphQL: Klien dapat menentukan dengan presisi field data apa saja yang dibutuhkan dalam satu query, mengeliminasi masalah over-fetching dan under-fetching. 3. gRPC: Berbasis Remote Procedure Call (RPC) di atas HTTP/2 menggunakan biner Protocol Buffers (Protobuf) untuk komunikasi server-to-server berlatensi ultra-rendah.\n\nMekanisme pelindung API meliputi: - Rate Limiting / Throttling (algoritma Token Bucket / Leaky Bucket) untuk mencegah serangan DoS. - API Versioning (URI /v1/ atau HTTP Header) untuk menjamin pembaruan backend tidak merusak aplikasi mobile klien versi lama.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Struktur endpoint REST API",
                "code": "const endpoint = \"https://api.toko.com/v1/produk/101\";\nconsole.log(\"Endpoint:\", endpoint);\nconsole.log(\"Aksi: Ambil detail produk dengan ID 101\");",
                "explanation": "URL endpoint REST mencerminkan entitas sumber daya data yang ingin diakses.",
                "expected_output": "Endpoint: https://api.toko.com/v1/produk/101\nAksi: Ambil detail produk dengan ID 101"
            }
        ],
        "prerequisite_ids": [
            "f-http-web"
        ],
        "related_topic_ids": [
            "f-http-web",
            "f-serialization",
            "f-auth"
        ],
        "why_vibecoding_matters": "AI sering menulis kode konsumsi API yang mengabaikan kemungkinan respons error status (seperti 429 Too Many Requests atau 503 Maintenance). Akibatnya, saat kuota API gratisanmu habis di tengah jalan, aplikasi langsung crash tanpa pesan yang jelas. Saat vibecoding, beri prompt: 'Buatlah API Client yang tangguh: tangani status code 429 dengan exponential backoff retry, lakukan validasi skema data respons, dan tangani skenario koneksi timeout.'",
        "keywords": [
            "api",
            "rest",
            "endpoint",
            "json",
            "client server",
            "integrasi"
        ],
        "estimated_minutes": 7,
        "sort_order": 34,
        "is_active": true,
        "problem_context": "Di masa lalu, jika aplikasi mobile ingin memesan ojek atau memproses pembayaran kartu kredit, perusahaan ojek harus memberikan akses langsung ke kode sumber internal database mereka kepada pihak luar. Hal ini menimbulkan bencana keamanan, risiko kebocoran data pengguna, dan merusak stabilitas server pusat. API diciptakan sebagai gerbang perantara resmi yang mengekspos fungsi yang diizinkan saja dengan kontrak data yang ketat.",
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
        "when_to_use": "Gunakan REST API untuk antarmuka publik atau integrasi pihak ketiga yang membutuhkan kesederhanaan dan kemudahan konsumsi oleh berbagai platform. Gunakan GraphQL jika aplikasi mobile frontend memiliki banyak layar dengan kebutuhan variasi data yang dinamis dan kompleks. Gunakan gRPC untuk komunikasi antarlayanan microservices internal yang membutuhkan performa dan efisiensi biner maksimum.",
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
    {
        "id": "f-serialization",
        "category_id": "f-web",
        "title": "Data Serialization (JSON/XML/YAML)",
        "level": "beginner",
        "summary": "Mengubah data di memori menjadi format teks seperti JSON agar bisa dikirim atau disimpan.",
        "explanation_simple": "Bayangkan kamu membeli lemari pakaian kayu besar dari toko furnitur online. Pihak toko tidak bisa mengirimkan lemari yang sudah terpasang utuh begitu saja ke dalam mobil kurir kecil karena ukurannya memakan tempat. Sebagai gantinya, toko membongkar lemari tersebut menjadi papan-papan kayu pipih berlabel rapi, memasukkannya ke dalam satu kardus datar (Serialisasi), lalu mengirimkannya melalui kurir. Begitu kardus tiba di kamar rumahmu, kamu membaca buku petunjuk dan merakit kembali papan-papan tersebut menjadi lemari pakaian utuh yang siap dipakai (Deserialisasi).\n\nSerialisasi mengubah objek memori kompleks menjadi aliran teks (JSON, YAML) atau biner (Protobuf) agar bisa dikirim melintasi kabel jaringan atau disimpan ke disk. Batas analoginya: papan kayu furnitur tidak bisa disusupi virus, sedangkan deserialisasi data teks asing dari internet bisa disusupi kode berbahaya (Deserialization Injection Attacks) jika tidak divalidasi dengan ketat.",
        "explanation_technical": "Serialisasi (Marshaling / Encoding) mengubah graph objek runtime menjadi deretan byte berurutan (linear stream). Deserialisasi (Unmarshaling / Decoding) membangun kembali instance objek runtime yang setara dari deretan byte tersebut.\n\nFormat serialisasi populer terbagi menjadi: 1. Human-Readable Text: - JSON (JavaScript Object Notation): standar emas API web; ringan, berbasis teks, tipe data sederhana (string, number, boolean, array, object, null). - YAML: ramah konfigurasi manusia (indentasi). 2. Binary Formats (Mesin): Protocol Buffers (Protobuf), MessagePack, FlatBuffers. Menggunakan integer varint dan field tags biner untuk menghasilkan ukuran payload hingga 70% lebih kecil dan waktu parsing 10x lebih cepat daripada JSON.\n\nKeamanan deserialisasi adalah isu kritis: Deserialisasi objek secara polimorfik tanpa validasi skema ketat (seperti pickle di Python atau Java ObjectInputStream) memungkinkan penyerang menyisipkan muatan Remote Code Execution (RCE) yang mengeksekusi perintah shell berbahaya di server.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "JSON Stringify dan Parse",
                "code": "const objek = { nama: \"Buku Coding\", harga: 50000 };\n// Serialisasi: Objek -> Teks JSON\nconst jsonString = JSON.stringify(objek);\nconsole.log(\"Teks JSON:\", jsonString);\n// Deserialisasi: Teks JSON -> Objek lagi\nconst kembali = JSON.parse(jsonString);\nconsole.log(\"Nama:\", kembali.nama);",
                "explanation": "JSON.stringify mengubah objek memori menjadi string teks untuk dikirim, JSON.parse mengembalikannya jadi objek.",
                "expected_output": "Teks JSON: {\"nama\":\"Buku Coding\",\"harga\":50000}\nNama: Buku Coding"
            }
        ],
        "prerequisite_ids": [
            "f-variables-data-types"
        ],
        "related_topic_ids": [
            "f-apis",
            "f-file-system"
        ],
        "why_vibecoding_matters": "AI sering menulis parsing JSON manual yang mengasumsikan semua field selalu ada (misal data['user']['profile']['avatar']), sehingga saat server mengembalikan null atau format field sedikit berbeda, seluruh halaman aplikasi meledak dengan TypeError / Null Check Operator error. Saat vibecoding, instruksikan AI: 'Gunakan model serialisasi type-safe yang memetakan JSON ke Data Class konkret dengan nilai default yang aman dan validasi skema untuk setiap field nullable.'",
        "keywords": [
            "serialization",
            "json",
            "xml",
            "yaml",
            "encode",
            "decode",
            "stringify",
            "parse"
        ],
        "estimated_minutes": 6,
        "sort_order": 35,
        "is_active": true,
        "problem_context": "Sebuah objek User di dalam memori komputer berupa pohon pointer pointer heksadesimal yang tersebar di blok heap memory RAM. Alamat memori 0x7FFF tersebut hanya bermakna di dalam laptop pengembang pada detik itu. Jika kamu mencoba mengirimkan byte pointer mentah tersebut ke laptop temanmu atau ke server Linux di cloud, komputer penerima tidak akan mengerti apa-apa dan mengalami crash seketika. Serialisasi diciptakan untuk menerjemahkan data memori ke dalam format teks/biner universal yang dapat dipahami oleh mesin apapun di dunia.",
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
        "when_to_use": "Gunakan JSON untuk komunikasi API publik web dan antarmuka aplikasi mobile karena kemudahan inspeksi dan debugging. Gunakan Protocol Buffers (Protobuf) untuk sistem antarlayanan internal berkapasitas tinggi (microservices) atau game multiplayer yang sensitif kuota bandwidth. Selalu gunakan pustaka pemodelan yang menghasilkan serialisasi type-safe (seperti json_serializable di Dart atau Zod di TypeScript).",
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
    {
        "id": "f-databases",
        "category_id": "f-data",
        "title": "Database Fundamentals",
        "level": "beginner",
        "summary": "Tempat menyimpan data aplikasi dalam jumlah besar dengan rapi, aman, dan cepat dicari.",
        "explanation_simple": "Bayangkan buku besar pencatatan kas di bank desa. Jika pencatatan uang nasabah hanya ditulis di secarik kertas catatan tempel, kertas tersebut bisa terbang tertiup angin, basah terkena kopi, atau salah dijumlahkan saat pembukuan akhir tahun. Oleh karena itu, bank menggunakan brankas pembukuan baja: setiap transaksi setoran dan penarikan dicatat permanen dengan tinta emas, memiliki nomor halaman urut, dan ditandatangani oleh dua teller resmi.\n\nBasis Data (Database) adalah brankas penyimpanan permanen aplikasi komputermu. Ia memastikan bahwa data pengguna (akun, pesanan, saldo) tetap tersimpan aman meskipun server mati listrik mendadak. Batas analogi buku kas: buku fisik hanya bisa dibaca satu orang dalam satu waktu, sedangkan sistem basis data modern dapat melayani puluhan ribu transaksi baca dan tulis secara bersamaan dalam hitungan milidetik.",
        "explanation_technical": "Sistem basis data terbagi menjadi dua paradigma utama: 1. Relational Databases (RDBMS: PostgreSQL, MySQL, SQLite): data disimpan dalam tabel bertaut dengan skema kaku, menjamin integritas referensial (Foreign Keys), dan menjunjung tinggi standar transaksi ACID: - Atomicity: seluruh langkah transaksi berhasil semua, atau dibatalkan total jika satu langkah gagal (Rollback). - Consistency: data selalu mematuhi semua aturan validasi dan relasi skema. - Isolation: transaksi konkuren yang berjalan paralel tidak saling mengintip data setengah jadi (Isolation Levels: Read Committed, Serializable). - Durability: data yang sudah di-commit dijamin selamat di disk permanen (via Write-Ahead Logging / WAL).\n\n2. NoSQL Databases (MongoDB, Redis, Cassandra): mengorbankan sebagian garansi ACID demi fleksibilitas skema horizontal (Document-store, Key-Value, Columnar, Graph), berfokus pada skalabilitas terdistribusi (Teorema CAP: Consistency vs Availability).",
        "code_examples": [
            {
                "language": "sql",
                "label": "Konsep tabel relasional dalam database",
                "code": "CREATE TABLE pengguna (\n  id INTEGER PRIMARY KEY,\n  nama TEXT NOT NULL,\n  email TEXT UNIQUE NOT NULL\n);",
                "explanation": "Mendefinisikan skema tabel dengan batasan integritas (PRIMARY KEY, NOT NULL, UNIQUE).",
                "expected_output": "Tabel pengguna terbuat"
            }
        ],
        "prerequisite_ids": [
            "f-file-system"
        ],
        "related_topic_ids": [
            "f-sql",
            "f-data-modeling"
        ],
        "why_vibecoding_matters": "AI sering menyarankan pembaruan data tanpa transaksi (tanpa blok BEGIN TRANSACTION ... COMMIT), sehingga jika operasi kedua gagal, operasi pertama tetap tersimpan dan meninggalkan data 'yatim piatu' (corrupt state). Saat vibecoding modul database, perintahkan AI: 'Bungkus operasi multi-tabel ini dalam transaksi ACID: pastikan terjadi rollback otomatis jika ada operasi yang melempar exception, dan buat indeks pada kolom foreign key.'",
        "keywords": [
            "database",
            "dbms",
            "sql",
            "nosql",
            "sqlite",
            "acid",
            "tabel",
            "persisten"
        ],
        "estimated_minutes": 7,
        "sort_order": 36,
        "is_active": true,
        "problem_context": "Menyimpan data aplikasi hanya dengan menulis file teks JSON atau CSV biasa di disk menimbulkan tiga bencana besar: 1. Ketiadaan Transaksi: jika server mati di tengah proses transfer uang (uang pengirim sudah dipotong tetapi uang penerima belum ditambah), saldo hilang selamanya. 2. Concurrency Conflict: jika dua pengguna membeli barang terakhir di toko secara bersamaan, kedua transaksi berhasil dan stok menjadi minus. 3. Kecepatan: mencari satu pengguna di antara 10 juta baris file teks CSV memakan waktu berjam-jam. Database Management System (DBMS) diciptakan untuk menjamin integritas transaksi dan pencarian instan.",
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
        "when_to_use": "Gunakan Relational Database (PostgreSQL / SQLite) sebagai pilihan utama default untuk mayoritas produk bisnis yang membutuhkan integritas relasi dan konsistensi transaksi uang/data. Gunakan Key-Value Store (seperti Redis) untuk caching in-memory berkecepatan tinggi atau sesi login sementara. Gunakan SQLite untuk penyimpanan lokal di aplikasi mobile (Android/iOS) dan desktop.",
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
    {
        "id": "f-sql",
        "category_id": "f-data",
        "title": "SQL",
        "level": "beginner",
        "summary": "Bahasa perintah untuk meminta, menambah, dan mengubah data di basis data relasional.",
        "explanation_simple": "Bayangkan kamu memesan hidangan prasmanan ke penyedia katering pesta. Kamu tidak perlu memberi tahu juru masak: 'Ambil pisau, iris bawang, nyalakan kompor gas suhu 150 derajat selama 12 menit'. Kamu cukup menyatakan apa yang kamu inginkan secara jelas: 'Tolong siapkan 100 porsi Rendang Sapi yang tidak pedus, urutkan pengantarannya mulai dari meja tamu VVIP'. Koki katering yang ahli akan memikirkan sendiri rute memasak dan bahan baku yang paling efisien.\n\nSQL (Structured Query Language) adalah bahasa deklaratif untuk berbicara dengan basis data. Kamu menyatakan DATA APA yang kamu inginkan, bukan BAGAIMANA LANGKAH MENCARINYA. Batas analoginya: katering pesta hanya memasak makanan, sedangkan mesin database modern memiliki Query Optimizer canggih yang menganalisis statistik tabel untuk memilih rute pencarian data tercepat.",
        "explanation_technical": "Instruksi SQL dikategorikan menjadi sub-bahasa formal: 1. DDL (Data Definition Language): mendefinisikan struktur skema (CREATE TABLE, ALTER TABLE, DROP, TRUNCATE). 2. DML (Data Manipulation Language): memanipulasi data baris (INSERT, UPDATE, DELETE). 3. DQL (Data Query Language): meminta data (SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT).\n\nOperasi relasi paling mendasar adalah JOIN untuk menggabungkan dua tabel berbasis kunci kecocokan: - INNER JOIN: mengembalikan baris yang memiliki kecocokan di kedua tabel. - LEFT JOIN: mengembalikan semua baris dari tabel kiri ditambah baris yang cocok dari tabel kanan (atau NULL jika tidak ada). - FULL OUTER JOIN: mengembalikan semua baris dari kedua belah pihak.\n\nDi balik layar, Database Query Planner mengubah teks query SQL menjadi pohon eksekusi relasional aljabar, memilih algoritma join optimal (Nested Loop, Hash Join, Merge Join) berdasarkan ketersediaan Indeks B-Tree.",
        "code_examples": [
            {
                "language": "sql",
                "label": "Query membaca produk aktif",
                "code": "SELECT id, nama, harga\nFROM produk\nWHERE harga < 100000 AND status = \"tersedia\"\nORDER BY harga ASC\nLIMIT 5;",
                "explanation": "Mengambil 5 produk termurah yang harganya di bawah 100.000 dan berstatus tersedia.",
                "expected_output": "Baris data hasil filter produk"
            }
        ],
        "prerequisite_ids": [
            "f-databases"
        ],
        "related_topic_ids": [
            "f-databases",
            "f-data-modeling"
        ],
        "why_vibecoding_matters": "AI yang diprompt cepat sering kali menyusun query mentah dengan penggabungan string (string interpolation) yang membuka celah SQL Injection fatal pada aplikasimu. Saat vibecoding, tegaskan standar keamanan: 'Gunakan parameter binding / prepared statements untuk query ini; jangan ada penggabungan string langsung ke sintaks SQL!'",
        "keywords": [
            "sql",
            "select",
            "insert",
            "update",
            "delete",
            "where",
            "join",
            "query"
        ],
        "estimated_minutes": 7,
        "sort_order": 37,
        "is_active": true,
        "problem_context": "Sebelum ada SQL, programmer harus menulis kode imperatif yang rumit dengan membuka file pointer biner disk, melakukan perulangan loop baris per baris, dan memfilter data secara manual. Jika ada perubahan struktur kolom file, ribuan baris kode pencarian harus ditulis ulang. E.F. Codd memperkenalkan model relasional dan bahasa SQL pada tahun 1970-an untuk memisahkan logika query data manusia dari detail fisik penyimpanan perangkat keras komputer.",
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
        "when_to_use": "Gunakan Parameterized Queries / Prepared Statements secara mutlak tanpa pengecualian untuk setiap parameter input dari luar. Gunakan klausa EXPLAIN QUERY PLAN untuk memeriksa apakah query-mu memanfaatkan index atau melakukan Full Table Scan lambat. Hindari SELECT * pada query produksi; sebutkan hanya nama kolom yang benar-benar dibutuhkan untuk menghemat bandwidth I/O.",
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
    {
        "id": "f-data-modeling",
        "category_id": "f-data",
        "title": "Data Modeling",
        "level": "intermediate",
        "summary": "Merancang struktur tabel dan hubungan antardata sebelum aplikasi dibangun.",
        "explanation_simple": "Bayangkan kamu sedang merancang denah arsitektur rumah bertingkat sebelum tukang bangunan meletakkan batu bata pertama. Kamu memutuskan kamar tidur berada di lantai dua, dapur di lantai satu dekat saluran pipa air, dan pintu garasi memiliki akses langsung ke jalan raya. Jika kamu salah merancang denah dan menaruh kamar mandi di tengah ruang tamu tanpa saluran pembuangan, membongkar dinding beton yang sudah kering setelah rumah jadi akan menelan biaya renovasi yang luar biasa mahal.\n\nPemodelan Data (Data Modeling) adalah denah cetak biru struktur informasi bisnismu di dalam database. Batas analoginya: denah rumah menampung benda fisik, sedangkan pemodelan data mendefinisikan entitas abstrak (Pengguna, Pesanan, Produk, Pembayaran) dan aturan relasi keterikatan di antara mereka.",
        "explanation_technical": "Pemodelan data relasional menggunakan diagram Entity-Relationship (ERD) dan aturan Normalisasi (Normal Forms): - 1NF (First Normal Form): setiap kolom hanya berisi nilai tunggal atomik (tidak ada array bersarang atau koma ganda dalam satu sel). - 2NF: memenuhi 1NF dan seluruh atribut non-kunci bergantung penuh pada seluruh Primary Key (menghilangkan partial dependency). - 3NF: memenuhi 2NF dan tidak ada dependensi transitif (kolom non-kunci tidak boleh bergantung pada kolom non-kunci lainnya).\n\nRelasi entitas terbagi menjadi: 1. One-to-One (1:1): satu pengguna memiliki satu kartu identitas KTP. 2. One-to-Many (1:N): satu pengguna memiliki banyak pesanan belanjaan (Foreign Key diletakkan di sisi tabel pesanan). 3. Many-to-Many (M:N): satu mahasiswa mengambil banyak mata kuliah, dan satu mata kuliah diikuti banyak mahasiswa (diwajibkan menggunakan Junction/Junction Table perantara dengan foreign keys komposit).\n\nDalam arsitektur data warehouse analitik, teknik Denormalisasi (seperti Star Schema) sengaja diterapkan demi kecepatan baca aggregasi query analitik.",
        "code_examples": [
            {
                "language": "sql",
                "label": "Tabel berelasi dengan Foreign Key",
                "code": "CREATE TABLE kategori (\n  id TEXT PRIMARY KEY,\n  nama TEXT NOT NULL\n);\nCREATE TABLE topik (\n  id TEXT PRIMARY KEY,\n  kategori_id TEXT REFERENCES kategori(id),\n  judul TEXT NOT NULL\n);",
                "explanation": "kategori_id di tabel topik merujuk ke id di tabel kategori. Database akan menolak topik yang kategorinya tidak ada.",
                "expected_output": "Skema relasional berhasil didefinisikan"
            }
        ],
        "prerequisite_ids": [
            "f-databases"
        ],
        "related_topic_ids": [
            "f-databases",
            "f-sql"
        ],
        "why_vibecoding_matters": "AI sering kali merancang skema database yang malas dengan menumpuk atribut relasional ke dalam satu kolom teks JSON atau string koma, yang membuat pembuatan fitur laporan atau filter data di masa depan menjadi mimpi buruk. Saat merancang database bersama AI, berikan prompt tegas: 'Rancang skema relasional yang ternormalisasi (3NF): buatkan tabel entitas terpisah, tentukan primary key dan foreign key yang eksplisit, dan gunakan junction table untuk relasi many-to-many.'",
        "keywords": [
            "data modeling",
            "relasi",
            "foreign key",
            "primary key",
            "normalisasi",
            "one to many",
            "skema"
        ],
        "estimated_minutes": 8,
        "sort_order": 38,
        "is_active": true,
        "problem_context": "Jika developer menyimpan data transaksi toko online dengan menggabungkan nama pelanggan, alamat rumah, nama produk, dan harga dalam satu tabel raksasa yang datar, timbul tiga anomali database yang mematikan: 1. Insertion Anomaly: tidak bisa menambahkan produk baru sebelum ada pelanggan yang membelinya. 2. Update Anomaly: jika pelanggan pindah alamat rumah, programmer harus memperbarui 100 baris riwayat pesanan lama; satu terlewat, data menjadi inkonsisten. 3. Deletion Anomaly: menghapus riwayat pesanan terakhir seorang pelanggan ikut menghapus data master pelanggan tersebut dari sistem selamanya.",
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
        "when_to_use": "Terapkan pemodelan relasional 3NF untuk sistem transaksional operasional (OLTP) agar integritas data terjamin dan bebas anomali update. Gunakan Junction Table untuk setiap hubungan Many-to-Many dengan foreign key cascade delete yang terdefinisi jelas. Lakukan denormalisasi hanya jika terbukti ada bottleneck performa nyata pada query baca tertentu setelah dilakukan indexing.",
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
    {
        "id": "f-auth",
        "category_id": "f-security-access",
        "title": "Authentication & Authorization",
        "level": "intermediate",
        "summary": "Memeriksa siapa pengguna yang masuk dan apa saja hak akses yang dimilikinya.",
        "explanation_simple": "Bayangkan pergi menonton festival konser musik internasional. Di pintu gerbang terluar, petugas keamanan memeriksa KTP dan wajahmu untuk memastikan kamu adalah orang yang sesungguhnya (Autentikasi / Authentication: Siapa Kamu?). Setelah terbukti asli, kamu diberi gelang tiket khusus bertuliskan 'Akses Reguler'. Ketika kamu mencoba berjalan masuk ke panggung VIP di belakang layar, petugas panggung memeriksa gelangmu dan melarangmu masuk karena tiketmu tidak memiliki izin akses panggung (Otorisasi / Authorization: Apa yang Boleh Kamu Lakukan?).\n\nAutentikasi membuktikan identitasmu, sedangkan Otorisasi menentukan batas kekuasaanmu. Batas analogi konser: gelang konser bisa dipotong atau dipinjamkan ke teman, sedangkan dalam keamanan digital, kredensial token dilengkapi tanda tangan digital kriptografi yang tidak bisa dipalsukan.",
        "explanation_technical": "Perbedaan esensial: - Authentication (AuthN): Memvalidasi identitas (Username/Password, MFA/2FA, OAuth2, Biometrik). - Authorization (AuthZ): Memvalidasi hak akses setelah terotentikasi (Role-Based Access Control - RBAC, Attribute-Based Access Control - ABAC).\n\nKeamanan Kata Sandi: Kata sandi DILARANG KERAS disimpan dalam teks polos atau hash cepat biasa (MD5/SHA-256). Wajib menggunakan Adaptive Slow Hashing Functions yang dilengkapi Salt acak: bcrypt, Argon2, atau scrypt. Algoritma ini sengaja dirancang lambat secara CPU dan memori untuk menggagalkan serangan Brute-Force dan Rainbow Table.\n\nManajemen Sesi Digital: 1. Session-Based: Server menyimpan session ID di memori/Redis dan mengirimkannya ke klien via HTTP-Only Secure Cookie. Stateful. 2. Token-Based (JWT - JSON Web Token): Klien menyimpan token yang ditandatangani secara kriptografi (HMAC-SHA256 atau RSA). Stateless, tetapi sulit di-revoke sebelum masa expired habis kecuali menggunakan blacklist/refresh token pattern.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Pemeriksaan izin akses (Otorisasi)",
                "code": "interface User { id: number; role: \"admin\" | \"member\"; }\nfunction hapusArtikel(user: User) {\n  if (user.role !== \"admin\") {\n    throw new Error(\"403 Forbidden: Hanya admin yang boleh menghapus!\");\n  }\n  return \"Artikel berhasil dihapus\";\n}\nconsole.log(hapusArtikel({ id: 1, role: \"admin\" }));",
                "explanation": "Otorisasi memeriksa apakah peran pengguna memiliki hak yang memadai sebelum menjalankan aksi kritis.",
                "expected_output": "Artikel berhasil dihapus"
            }
        ],
        "prerequisite_ids": [
            "f-security"
        ],
        "related_topic_ids": [
            "f-security",
            "f-apis"
        ],
        "why_vibecoding_matters": "AI sering menulis sistem login yang membandingkan password dengan string biasa atau menggunakan algoritma hash usang (MD5/SHA1), serta lupa memeriksa otorisasi kepemilikan data pada endpoint API (misalnya user A bisa mengedit data user B hanya dengan mengganti parameter URL id). Saat vibecoding modul auth, perintahkan AI: 'Gunakan bcrypt untuk hashing password, terapkan JWT dengan access token dan refresh token pattern, dan pastikan setiap endpoint memeriksa apakah resource yang diakses benar-benar milik pengguna yang sedang login!'",
        "keywords": [
            "authentication",
            "authorization",
            "auth",
            "login",
            "jwt",
            "token",
            "rbac",
            "keamanan"
        ],
        "estimated_minutes": 8,
        "sort_order": 39,
        "is_active": true,
        "problem_context": "Pada awal internet sebelum ada protokol otentikasi standar, situs web menyimpan kata sandi pengguna dalam bentuk teks polos (plaintext). Ketika database dicuri peretas, jutaan kata sandi bocor seketika. Selain itu, server web harus mengingat sesi login pengguna di tengah protokol HTTP yang stateless. Standar autentikasi modern diciptakan untuk mengamankan kredensial pengguna menggunakan hashing satu arah dan mengelola sesi login tanpa kebocoran data.",
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
        "when_to_use": "Gunakan bcrypt atau Argon2id dengan work factor terkalibrasi untuk setiap penyimpanan password akun. Gunakan HTTP-Only, Secure, SameSite cookies untuk menyimpan token sesi di web browser guna menangkal serangan pencurian token via XSS. Terapkan prinsip Role-Based Access Control (RBAC) pada setiap endpoint API sensitif.",
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
    {
        "id": "f-security",
        "category_id": "f-security-access",
        "title": "Security Basics",
        "level": "intermediate",
        "summary": "Menjaga aplikasi dari celah bahaya dan serangan pihak yang tidak berhak.",
        "explanation_simple": "Bayangkan brankas penyimpanan uang emas di bank sentral. Bank tidak hanya mengandalkan satu pintu pagar depan yang tipis. Mereka menerapkan pertahanan berlapis (Defense in Depth): ada pos penjaga bersenjata di gerbang luar, kamera pengawas sensor gerak, pintu baja brankas dengan kunci kombinasi ganda yang membutuhkan dua staf berbeda, dan sensor panas di dalam ruangan brankas. Jika seorang penyusup berhasil melewati pos gerbang luar, mereka tetap akan tertahan oleh pintu baja berikutnya.\n\nKeamanan Perangkat Lunak (Software Security) adalah penerapan pertahanan berlapis pada setiap baris kode aplikasimu. Batas analoginya: perampok bank fisik terlihat oleh mata manusia, sedangkan penyerang siber di internet dapat berupa bot otomatis yang memindai jutaan celah kode di seluruh dunia 24 jam sehari tanpa suara.",
        "explanation_technical": "Standar keamanan industri software dipandu oleh OWASP Top 10 (Open Worldwide Application Security Project). Tiga pilar keamanan CIA Triad: - Confidentiality: data hanya boleh dibaca oleh pihak berwenang (Enkripsi at-rest dan in-transit via TLS/HTTPS). - Integrity: data dijamin tidak dimanipulasi di tengah jalan (Digital Signatures & HMAC). - Availability: sistem tetap dapat melayani pengguna saat diserang (DDoS protection & Rate limiting).\n\nKerentanan kode paling berbahaya dan mitigasinya: 1. Injection (SQLi, Command Injection): Penyerang menyelipkan instruksi kode ke dalam input teks. Mitigasi: Input Sanitization & Parameterized Queries. 2. Cross-Site Scripting (XSS): Penyerang menyisipkan script jahat ke dalam tampilan pengguna lain. Mitigasi: Output Encoding, HTML Escaping, dan Content Security Policy (CSP). 3. Cross-Site Request Forgery (CSRF): Memaksa browser korban mengeksekusi aksi tak diinginkan pada web yang sedang login. Mitigasi: Anti-CSRF Tokens dan SameSite Cookies.\n\nPrinsip fundamental: 'Never Trust User Input' (Anggap semua data masukan dari internet bermusuhan).",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Mencegah SQL Injection dengan parameterized query",
                "code": "// BURUK: `SELECT * FROM users WHERE email = '${userInput}'`\n// BAIK (Parameterized Query):\nconst sql = \"SELECT * FROM users WHERE email = ?\";\nconst params = [\"pengguna@mail.com\"];\nconsole.log(\"Query aman:\", sql, \"dengan parameter terpisah\");",
                "explanation": "Parameter query memisahkan instruksi SQL dari data masukan pengguna, menggagalkan serangan injeksi SQL.",
                "expected_output": "Query aman: SELECT * FROM users WHERE email = ? dengan parameter terpisah"
            }
        ],
        "prerequisite_ids": [
            "f-http-web"
        ],
        "related_topic_ids": [
            "f-auth",
            "f-http-web"
        ],
        "why_vibecoding_matters": "Kode yang dihasilkan AI sering kali rentan terhadap kerentanan OWASP karena AI memprioritaskan kode yang 'berhasil jalan' dengan cepat. AI sering menulis query mentah, mengeksekusi shell command menggunakan exec(), atau me-render HTML mentah tanpa escaping (dangerouslySetInnerHTML). Saat vibecoding, jalankan pemeriksaan keamanan ketat: 'Audit kode ini terhadap OWASP Top 10: apakah ada celah SQL Injection, XSS, insecure direct object references (IDOR), atau penanganan rahasia kredensial yang bocor?'",
        "keywords": [
            "security",
            "keamanan",
            "sql injection",
            "xss",
            "enkripsi",
            "owasp",
            "api key",
            "hashing"
        ],
        "estimated_minutes": 8,
        "sort_order": 40,
        "is_active": true,
        "problem_context": "Satu celah keamanan kecil pada kode aplikasi dapat meruntuhkan reputasi perusahaan dan menimbulkan denda hukum ratusan miliar rupiah. Setiap tahun, ribuan institusi mengalami peretasan karena kerentanan klasik seperti SQL Injection, pencurian sesi (Session Hijacking), dan pembobolan akses server. Asumsi keliru bahwa 'aplikasi saya kecil dan tidak ada yang mau meretas' adalah pintu masuk utama bagi bot otomatis malware global yang tidak pandang bulu dalam mengeksploitasi kelemahan software.",
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
        "when_to_use": "Terapkan Principle of Least Privilege: berikan hak akses seminimal mungkin bagi setiap akun database, API keys, dan proses sistem operasi. Sanitasi dan validasi setiap input pengguna pada batas terluar server controller. Gunakan library keamanan resmi dan audit dependensi secara berkala (Dependency Vulnerability Scanning).",
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
    {
        "id": "f-concurrency",
        "category_id": "f-concurrency-group",
        "title": "Concurrency/Parallelism",
        "level": "advanced",
        "summary": "Menjalankan beberapa tugas sekaligus agar aplikasi tetap lincah dan tidak macet.",
        "explanation_simple": "Bayangkan dapur restoran yang sibuk. Jika hanya ada satu koki dan dapur hanya bisa mengerjakan satu hal sekali waktu, koki harus berdiri diam selama 20 menit menatap oven roti yang sedang memanggang sebelum boleh mulai memotong sayuran sup. Namun koki yang cerdas menerapkan konkurensi: ia memasukkan roti ke oven, menyetel alarm timer, lalu sambil menunggu oven berbunyi, ia memotong wortel. Jika restoran sangat kaya, mereka mempekerjakan empat koki sekaligus yang masing-masing memegang pisaunya sendiri di meja terpisah (Paralelisme murni).\n\nKonkurensi adalah tentang menstrukturkan program agar banyak hal dapat ditangani secara tumpang tindih. Batas analogi dapur: jika dua koki mencoba memotong wortel di talenan yang sama menggunakan pisau yang sama pada detik yang sama tanpa koordinasi, jari mereka akan terluka (Race Condition).",
        "explanation_technical": "Perbedaan krusial yang wajib dipahami insinyur software: - Concurrency: berurusan dengan struktur (dealing with a lot of things at once) — mengelola banyak tugas yang bersaing dalam interval waktu yang sama. - Parallelism: berurusan dengan eksekusi fisik (doing a lot of things at once) — menjalankan tugas secara bersamaan pada core CPU perangkat keras yang berbeda.\n\nModel konkurensi meliputi: 1. Multi-threading dengan Shared Memory: beberapa thread OS berbagi ruang memori heap yang sama. Rentan terhadap Race Conditions dan Deadlock. Membutuhkan primitif sinkronisasi seperti Mutex (Mutual Exclusion Locks), Semaphores, atau Atomic Operations. 2. Message Passing / Actor Model (Erlang, Go Channels, Dart Isolates): setiap thread/worker memiliki memorinya sendiri yang terisolasi sepenuhnya. Komunikasi dilakukan murni melalui pengiriman pesan (Share memory by communicating, not communicate by sharing memory), mengeliminasi race condition memori.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Konkurensi dua tugas independen",
                "code": "console.log(\"Mulai tugas A dan B\");\nPromise.all([\n  Promise.resolve(\"Hasil A\"),\n  Promise.resolve(\"Hasil B\")\n]).then(hasil => {\n  console.log(\"Keduanya selesai:\", hasil);\n});",
                "explanation": "Dua tugas asinkron berjalan secara konkuren tanpa saling menghalangi.",
                "expected_output": "Mulai tugas A dan B\nKeduanya selesai: [ 'Hasil A', 'Hasil B' ]"
            }
        ],
        "prerequisite_ids": [
            "f-operating-system"
        ],
        "related_topic_ids": [
            "f-async",
            "f-operating-system"
        ],
        "why_vibecoding_matters": "Kode konkurensi yang dibuat AI sering kali mengandung bug race condition tersembunyi yang lolos pengujian developer karena bug tersebut hanya muncul sesekali di perangkat pengguna dengan timing tak terduga. Saat meminta AI membuat fitur konkurensi, tanyakan: 'Apakah ada data yang diakses atau dimodifikasi oleh beberapa thread secara bersamaan? Bagaimana cara kode ini menjamin thread-safety tanpa memicu risiko deadlock?'",
        "keywords": [
            "concurrency",
            "parallelism",
            "multithreading",
            "race condition",
            "deadlock",
            "isolate"
        ],
        "estimated_minutes": 8,
        "sort_order": 41,
        "is_active": true,
        "problem_context": "Ketika komputer berevolusi dari satu core prosesor menjadi multi-core (seperti prosesor HP modern yang memiliki 8 core), program yang hanya berjalan di satu thread tunggal hanya bisa memanfaatkan 12.5% dari total tenaga prosesor. Lebih parah lagi, ketika aplikasi melakukan operasi lambat (seperti mengunduh file besar dari internet), seluruh antarmuka layar membeku (ANR - Application Not Responding) jika operasi tersebut memblokir thread utama antarmuka pengguna.",
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
        "when_to_use": "Gunakan background worker thread (seperti Dart Isolates, Web Workers, atau thread pool) untuk komputasi CPU-heavy yang berat (seperti kompresi video, enkripsi file besar, atau parsing JSON raksasa) agar UI tetap responsif 60 FPS. Gunakan model pesan terisolasi (Isolates/Workers) daripada shared-memory lock jika bahasamu mendukungnya untuk menghindari bug deadlock.",
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
    {
        "id": "f-async",
        "category_id": "f-concurrency-group",
        "title": "Asynchronous Programming",
        "level": "intermediate",
        "summary": "Menjalankan proses yang butuh waktu tanpa membuat tampilan aplikasi membeku.",
        "explanation_simple": "Bayangkan memesan makanan cepat saji di kasir restoran modern. Setelah kamu memesan dan membayar burger, kasir tidak menyuruhmu berdiri diam mematung di depan meja kasir selama 15 menit menunggu burger dimasak. Kasir memberikanmu sebuah alat pager nirkabel kecil (buzzer) yang bisa kamu bawa ke meja makan. Kamu bebas duduk santai, membuka media sosial, atau mengobrol. Ketika burger selesai dimasak oleh tim dapur, pager bergetar dan berbunyi, menandakan kamu bisa berjalan mengambil nampan makananmu.\n\nPemrograman Asinkron (Asynchronous Programming) bekerja seperti pager restoran tersebut. Alat pager adalah representasi dari objek Promise atau Future: janji bahwa hasil data akan tiba di masa depan. Batas analogi pager kafe: pager hanyalah pengingat pesanan fisik; dalam komputer, mekanisme asinkron dikoordinasikan oleh mesin bernama Event Loop yang memutar antrean pesan tugas saat thread utama sedang menganggur.",
        "explanation_technical": "Pemrograman asinkron pada runtime modern (seperti Dart Event Loop, Node.js libuv, Python asyncio) bertumpu pada arsitektur Event Loop non-blocking. Event Loop memantau dua antrean utama: Event Queue / Task Queue (berisi event I/O, timer, klik pengguna) dan Microtask Queue (tugas prioritas tinggi). Thread utama mengeksekusi kode sinkron di Call Stack hingga kosong, lalu Event Loop mengambil task berikutnya dari antrean untuk dieksekusi.\n\nEvolusi sintaks asinkron bergerak dari Callback (rawan Callback Hell / Piramida Kematian), ke objek Promise/Future (yang merepresentasikan tiga status: pending, fulfilled/resolved, rejected), hingga ke sintaksis modern async/await. Kata kunci await menangguhkan (suspend) eksekusi fungsi lokal saat itu dan mengembalikan kontrol ke Event Loop, lalu melanjutkan sisa fungsi tersebut setelah Future/Promise selesai.\n\nKOREKSI PENTING: Perintah koordinasi seperti Future.wait di Dart, Promise.all di JavaScript, atau asyncio.gather di Python berfungsi untuk mengoordinasikan beberapa pekerjaan asinkron agar dapat ditunggu secara serempak. Mekanisme ini TIDAK dengan sendirinya membuat pekerjaan komputasi CPU berjalan secara paralel di multi-core; operasi CPU-bound tetap membutuhkan thread/isolate terpisah untuk dapat dieksekusi secara paralel murni.",
        "code_examples": [
            {
                "language": "typescript",
                "comparison_key": "async",
                "label": "Async/await di TypeScript",
                "code": "async function fetchPesan(): Promise<string> {\n  return \"Data berhasil diambil!\";\n}\nasync function main() {\n  console.log(\"Tunggu sebentar...\");\n  const hasil = await fetchPesan();\n  console.log(hasil);\n}\nmain();",
                "explanation": "Di TypeScript, pemanggilan fungsi async langsung berjalan sinkron hingga ekspresi await pertama, lalu mengembalikan Promise (status penyelesaian bergantung pada operasi).",
                "expected_output": "Tunggu sebentar...\nData berhasil diambil!"
            },
            {
                "language": "python",
                "comparison_key": "async",
                "label": "Async/await di Python",
                "code": "import asyncio\nasync def fetch_pesan():\n    return \"Data berhasil diambil!\"\nasync def main():\n    print(\"Tunggu sebentar...\")\n    hasil = await fetch_pesan()\n    print(hasil)\nasyncio.run(main())",
                "explanation": "Di Python, memanggil fetch_pesan() menghasilkan objek coroutine yang tubuhnya belum berjalan sampai dijadwalkan atau di-await pada event loop.",
                "expected_output": "Tunggu sebentar...\nData berhasil diambil!"
            },
            {
                "language": "dart",
                "comparison_key": "async",
                "label": "Async/await di Dart",
                "code": "Future<String> fetchPesan() async {\n  return \"Data berhasil diambil!\";\n}\nvoid main() async {\n  print(\"Tunggu sebentar...\");\n  final hasil = await fetchPesan();\n  print(hasil);\n}",
                "explanation": "Di Dart, fungsi async mengembalikan Future<T>; kode sinkron awal berjalan langsung hingga await pertama, membebaskan event loop selama menunggu penyelesaian operasi.",
                "expected_output": "Tunggu sebentar...\nData berhasil diambil!"
            }
        ],
        "prerequisite_ids": [
            "f-functions"
        ],
        "related_topic_ids": [
            "f-concurrency",
            "f-http-web",
            "f-runtime"
        ],
        "why_vibecoding_matters": "AI sering lupa menyematkan kata kunci await di depan pemanggilan fungsi asinkron atau tidak menangani blok try-catch pada fungsi async, sehingga kegagalan jaringan menjadi Unhandled Promise Rejection yang mematikan proses server backend. Saat vibecoding, teliti setiap fungsi asinkron dan tanyakan ke AI: 'Pastikan semua pemanggilan Future/Promise menggunakan await yang tepat, apakah Future.wait menangani kegagalan salah satu request secara elegan, dan apakah komputasi berat di sini membutuhkan Isolate/Worker terpisah?'",
        "keywords": [
            "async",
            "await",
            "promise",
            "future",
            "asinkron",
            "event loop",
            "non blocking"
        ],
        "estimated_minutes": 8,
        "sort_order": 42,
        "is_active": true,
        "problem_context": "Mengambil data dari server internet membutuhkan waktu 200 hingga 1.000 milidetik, waktu yang sangat lama bagi CPU modern yang dapat mengeksekusi 3 miliar siklus instruksi per detik. Jika fungsi pembacaan data jaringan bersifat Sinkron (Blocking), seluruh aplikasi akan macet total: animasi terhenti, sentuhan layar ponsel tidak direspon, dan sistem operasi menganggap aplikasi rusak (hang). Asynchronous programming diciptakan agar CPU dapat terus melayani animasi antarmuka dan interaksi pengguna selagi menunggu data jaringan tiba.",
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
        "when_to_use": "Gunakan async/await untuk setiap operasi yang melibatkan komunikasi jaringan (HTTP, WebSocket), pembacaan/penulisan basis data, file system, atau penundaan waktu (timer). Gunakan Future.wait / Promise.all untuk menjalankan beberapa permintaan I/O jaringan independen secara bersamaan (misal mengambil data profil dan data notifikasi secara paralel I/O). Jika kamu memiliki pekerjaan CPU-heavy (enkripsi, image processing), delegasikan ke Worker Thread atau Dart Isolate, jangan hanya dibungkus fungsi async biasa.",
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
    },
    {
        "id": "f-deployment",
        "category_id": "f-process",
        "title": "Deployment Basics",
        "level": "intermediate",
        "summary": "Menerbangkan aplikasi dari komputer lokal ke server agar bisa diakses pengguna umum.",
        "explanation_simple": "Bayangkan merakit pesawat terbang komersial. Kamu dan tim teknisi merakit dan menguji mesin pesawat di hanggar tertutup pabrik (Lingkungan Development). Setelah pesawat siap, kamu membawanya ke landasan uji coba khusus yang meniru kondisi cuaca asli untuk uji terbang simulasi pilot (Lingkungan Staging). Baru setelah seluruh izin penerbangan dan inspeksi lulus 100%, pesawat tersebut diisi oleh ratusan penumpang nyata untuk terbang di rute penerbangan komersial internasional (Lingkungan Produksi).\n\nDeployment adalah perjalanan membawa aplikasi dari laptop pengembang ke tangan pengguna nyata di seluruh dunia. Batas analoginya: pesawat fisik diterbangkan satu per satu, sedangkan deployment perangkat lunak modern dilakukan secara otomatis melalui pipeline CI/CD tanpa ada jeda mati (Zero-Downtime Deployment).",
        "explanation_technical": "Pipeline Deployment modern bertumpu pada konsep CI/CD (Continuous Integration / Continuous Deployment): - CI (Continuous Integration): setiap kode baru yang di-push otomatis menjalankan linter, static analysis, dan seluruh automated tests di lingkungan virtual bersih. - CD (Continuous Delivery/Deployment): jika seluruh tes lulus, artefak otomatis dikemas dan dirilis ke server target.\n\nContainerization dengan Docker mengemas kode aplikasi beserta runtime, konfigurasi OS, dan pustaka dependensinya ke dalam satu Image terisolasi yang dijamin berperilaku 100% identik di lingkungan mana pun.\n\nStrategi Zero-Downtime Deployment: 1. Blue-Green Deployment: memiliki dua lingkungan identik (Blue yang aktif melayani pengguna, Green yang dipasangi versi baru). Setelah Green teruji sehat, router traffic dialihkan seketika dari Blue ke Green. 2. Canary Deployment: mengalirkan versi baru hanya ke 5% pengguna terlebih dahulu; jika metrik error normal, perlahan dinaikkan ke 100%.",
        "code_examples": [
            {
                "language": "bash",
                "label": "Perintah build rilis aplikasi mobile",
                "code": "# Membangun bundle rilis Android yang teroptimasi\nflutter build appbundle --release\n# Menghasilkan file di build/app/outputs/bundle/release/",
                "explanation": "Perintah build rilis membuang semua kode debugging dan mengompresi aset untuk performa maksimal.",
                "expected_output": "app-release.aab siap diunggah ke Google Play Store"
            }
        ],
        "prerequisite_ids": [
            "f-build-compilation"
        ],
        "related_topic_ids": [
            "f-build-compilation",
            "f-logging-monitoring"
        ],
        "why_vibecoding_matters": "AI sering menyarankan cara cepat menjalankan aplikasi di server dengan mengetik node server.js atau python app.py di terminal SSH, yang akan langsung mati seketika begitu jendela terminal ditutup atau server kehabisan memori. Saat vibecoding untuk deployment, mintalah arsitektur produksi: 'Buatlah konfigurasi Dockerfile multi-stage build yang aman dan minimalis, serta siapkan file workflow CI/CD GitHub Actions untuk menjalankan automated test dan deployment otomatis.'",
        "keywords": [
            "deployment",
            "release",
            "production",
            "environment variables",
            "hosting",
            "build rilis"
        ],
        "estimated_minutes": 7,
        "sort_order": 43,
        "is_active": true,
        "problem_context": "Di masa lalu, deployment dilakukan secara manual dan menegangkan pada tengah malam: developer menyalin file kode via FTP ke server produksi hidup, mengubah konfigurasi database manual, dan berdoa agar aplikasi tidak rusak. Sering kali terjadi masalah klasik 'di laptop saya jalan normal, tetapi di server meledak error' karena versi sistem operasi dan library server berbeda dengan laptop developer. Containerization (Docker) dan CI/CD diciptakan untuk membuat proses rilis menjadi otomatis, deterministik, dan dapat diulang tanpa kepanikan.",
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
        "when_to_use": "Gunakan Docker Container untuk mengemas backend services agar terhindar dari ketidakcocokan lingkungan host OS. Otomatisasikan build dan testing menggunakan CI/CD (GitHub Actions, GitLab CI) pada setiap Pull Request. Gunakan Blue-Green atau Rolling updates untuk aplikasi produksi yang tidak boleh mengalami masa henti layanan (zero downtime).",
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
    {
        "id": "f-logging-monitoring",
        "category_id": "f-process",
        "title": "Logging & Monitoring Basics",
        "level": "beginner",
        "summary": "Mencatat aktivitas dan memantau kesehatan aplikasi saat sudah dipakai umum.",
        "explanation_simple": "Bayangkan ruang kokpit pesawat terbang modern. Di hadapan pilot terdapat ratusan instrumen dasbor: indikator ketinggian altimeter, kompas navigasi, sisa bahan bakar avtur, dan lampu peringatan tekanan kabin. Di bagian belakang pesawat terpasang kotak hitam (Black Box) yang merekam setiap percakapan radio dan parameter mesin secara terus-menerus. Pilot tidak menerbangkan pesawat hanya dengan melihat jendela luar; mereka mengandalkan instrumen dasbor tersebut untuk mengantisipasi badai dan mendiagnosis anomali mesin sebelum terjadi malapetaka.\n\nLogging & Monitoring adalah kokpit dan kotak hitam aplikasi komputermu di lingkungan produksi. Batas analoginya: kotak hitam pesawat baru dibuka setelah terjadi kecelakaan, sedangkan sistem observabilitas software modern memberikan peringatan alarm otomatis (Alerting) ke ponsel tim insinyur di detik pertama saat grafik error mulai melonjak.",
        "explanation_technical": "Tiga pilar utama Observabilitas Sistem (The Three Pillars of Observability): 1. Logs: Catatan diskrit peristiwa berstempel waktu (Timestamped Events). Wajib menggunakan format Structured Logging (JSON) dengan level terstandarisasi: - DEBUG: informasi diagnostik detail saat development. - INFO: konfirmasi alur normal (misal: 'User ID 42 berhasil checkout'). - WARN: anomali yang tidak mematikan sistem (misal: 'Koneksi lambat, retry ke-2'). - ERROR: kegagalan operasi yang harus ditangani (misal: 'Gagal menghubungi payment gateway'). - FATAL: sistem tidak dapat melanjutkan eksekusi.\n\n2. Metrics: Data agregasi numerik yang dapat dihitung dari waktu ke waktu (Time-Series: CPU usage, Memory heap, Request Per Second, P99 Latency). 3. Distributed Tracing: Melacak perjalanan sebuah permintaan pengguna melintasi puluhan microservices independen menggunakan Correlation ID (Trace ID).",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Logging berjenjang sesuai level",
                "code": "console.info(\"[INFO] Pengguna id:42 berhasil login.\");\nconsole.warn(\"[WARN] Kuota penyimpanan sisa 10%.\");\nconsole.error(\"[ERROR] Gagal menyambung ke database!\");",
                "explanation": "Membedakan level log mempermudah penyaringan pesan penting di server produksi.",
                "expected_output": "[INFO] Pengguna id:42 berhasil login.\n[WARN] Kuota penyimpanan sisa 10%.\n[ERROR] Gagal menyambung ke database!"
            }
        ],
        "prerequisite_ids": [
            "f-debugging"
        ],
        "related_topic_ids": [
            "f-debugging",
            "f-deployment"
        ],
        "why_vibecoding_matters": "Kode yang dihasilkan AI sering kali hanya berisi console.log teks mentah yang tidak terstruktur dan tidak memiliki tingkatan level log, sehingga mustahil difilter saat aplikasi berjalan di server cloud. Saat vibecoding, instruksikan AI: 'Gunakan structured logging library: format log dalam JSON, gunakan level log yang tepat (INFO/ERROR), sertakan konteks userId dan requestId, dan pastikan data sensitif seperti password disanitasi/masking dari output log!'",
        "keywords": [
            "logging",
            "monitoring",
            "log level",
            "info",
            "warn",
            "error",
            "sentry",
            "crash report"
        ],
        "estimated_minutes": 6,
        "sort_order": 44,
        "is_active": true,
        "problem_context": "Ketika pengguna di belahan dunia lain mengeluhkan aplikasi sering macet atau transaksi gagal, developer yang tidak memiliki sistem logging terstruktur hanya bisa kebingungan dan menebak-nebak di ruang gelap. Tanpa catatan log, kamu tidak tahu parameter apa yang dikirim pengguna, query database mana yang lambat, atau server mana yang sedang kehabisan RAM. Logging dan monitoring diciptakan untuk memberikan pandangan tembus pandang (Observability) ke dalam jeroan sistem produksi.",
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
        "when_to_use": "Gunakan Structured Logging (JSON format) agar log dapat diindeks dan dicari secara instan oleh agregator log (seperti Datadog, ELK Stack, Grafana Loki). Semprotkan Correlation ID / Trace ID di header setiap permintaan HTTP antarlayanan untuk memudahkan penelusuran error lintas server. Pasang alert alarm otomatis jika metrik error rate 5xx melampaui ambang batas 1%.",
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
    {
        "id": "f-sdlc-agile",
        "category_id": "f-process",
        "title": "SDLC & Agile Basics",
        "level": "beginner",
        "summary": "Langkah kerja dan kebiasaan tim dalam mengembangkan aplikasi secara bertahap.",
        "explanation_simple": "Bayangkan memesan lukisan potret keluarga ke seorang pelukis kanvas. Metode lama (Waterfall) bekerja seperti pelukis yang mengunci diri di kamar selama 6 bulan tanpa komunikasi, lalu keluar membawa lukisan utuh yang ternyata salah warna baju dan pose wajahnya tidak disukai keluargamu. Sebaliknya, metode tangkas (Agile) bekerja seperti pelukis yang menunjukkan sketsa pensil kasar di minggu pertama untuk meminta masukan, lalu mewarnai latar belakang di minggu kedua, dan menyempurnakan detail wajah di minggu ketiga bersama keluargamu.\n\nSDLC (Software Development Life Cycle) dan Agile adalah cara tim mengatur alur kerja dari ide hingga rilis. Batas analoginya: lukisan kanvas tidak bisa diubah begitu cat minyak kering, sedangkan perangkat lunak modern adalah artefak digital fleksibel yang dapat terus disempurnakan setiap dua minggu berdasarkan umpan balik pengguna nyata.",
        "explanation_technical": "Fase standar dalam SDLC (Software Development Life Cycle): 1. Requirements & Discovery -> 2. Design & Architecture -> 3. Implementation (Coding) -> 4. Verification (Testing) -> 5. Deployment -> 6. Maintenance & Feedback.\n\nPrinsip Inti Agile (Agile Manifesto): - Individu dan interaksi lebih penting daripada proses dan alat bantu. - Software yang berfungsi lebih penting daripada dokumentasi yang komprehensif. - Kolaborasi dengan pelanggan lebih penting daripada negosiasi kontrak. - Tanggap terhadap perubahan lebih penting daripada mengikuti rencana kaku.\n\nFramework Agile populer: - Scrum: Membagi pekerjaan ke dalam siklus waktu tetap bernama Sprints (biasanya 2 minggu), dengan peran Product Owner, Scrum Master, Developers, dan ritual Sprint Planning, Daily Standup, Sprint Review, dan Retrospective. - Kanban: Memvisualisasikan alur kerja di papan kartu (To Do, In Progress, Done) dengan pembatasan Work In Progress (WIP Limits) untuk mencegah bottleneck tim.",
        "code_examples": [
            {
                "language": "markdown",
                "label": "Contoh User Story standar Agile",
                "code": "**Format User Story:**\nSebagai *pengguna vibecoding*,\nSaya ingin *melihat penjelasan analogi awam sebelum istilah teknis*,\nAgar *saya paham konsep dasarnya tanpa bingung oleh jargon.*",
                "explanation": "User story merumuskan kebutuhan dari sudut pandang nilai manfaat bagi pengguna akhir.",
                "expected_output": "User story yang jelas dan terarah"
            }
        ],
        "prerequisite_ids": [
            "f-git"
        ],
        "related_topic_ids": [
            "f-documentation",
            "f-clean-code"
        ],
        "why_vibecoding_matters": "Dengan adanya AI, kecepatan menulis kode meningkat 10x lipat, namun risiko membangun 'fitur yang salah' juga meningkat 10x lipat. Tanpa pemahaman siklus iterasi Agile, kamu bisa menghasilkan ribuan baris kode AI yang sia-sia karena tidak pernah memvalidasinya ke pengguna nyata. Terapkan mindset Agile dalam vibecoding: 'Rancang potongan fitur terkecil yang fungsional (MVP), uji bersama pengguna atau penguji internal, kumpulkan umpan balik, lalu lakukan iterasi berikutnya bersama AI.'",
        "keywords": [
            "sdlc",
            "agile",
            "scrum",
            "sprint",
            "mvp",
            "iterasi",
            "user story",
            "manajemen proyek"
        ],
        "estimated_minutes": 7,
        "sort_order": 45,
        "is_active": true,
        "problem_context": "Pada dekade 1980-an dan 1990-an, industri software didominasi oleh metode Waterfall yang kaku: analisis kebutuhan berbulan-bulan, perancangan dokumen tebal, penulisan kode setahun, dan pengujian di akhir. Hasil riset membuktikan lebih dari 60% proyek software gagal total: ketika proyek selesai dua tahun kemudian, kebutuhan pasar sudah berubah total dan software yang dibangun tidak lagi dibutuhkan. Manifesto Agile dideklarasikan pada tahun 2001 untuk menggantikan birokrasi dokumen kaku dengan adaptabilitas dan iterasi cepat.",
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
        "when_to_use": "Gunakan Scrum atau Kanban saat membangun produk digital baru yang kebutuhan fiturnya masih berkembang dan butuh validasi pasar yang cepat. Pecah tugas besar menjadi User Stories kecil yang dapat diselesaikan dalam hitungan hari. Manfaatkan Sprint Retrospective untuk terus memperbaiki proses kerja dan komunikasi tim.",
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
    {
        "id": "f-documentation",
        "category_id": "f-process",
        "title": "Kebiasaan Dokumentasi",
        "level": "beginner",
        "summary": "Menulis catatan penjelasan agar orang lain dan diri sendiri paham cara kerja sistem.",
        "explanation_simple": "Bayangkan membeli lemari kabinet modern dari toko furnitur yang dikirim dalam bentuk 50 kepingan kayu dan 100 baut kecil, tetapi di dalam kardus tidak disertakan selembar pun buku petunjuk perakitan bergambar. Meskipun bahan kayu dan bautnya berkualitas super, kamu akan menghabiskan waktu berhari-hari dalam frustrasi mencoba menebak baut mana yang masuk ke lubang mana, dan lemari yang kamu pasang mungkin miring atau roboh saat diisi pakaian.\n\nDokumentasi Teknis (Technical Documentation) adalah buku manual perakitan dan peta penunjuk jalan bagi kodemu. Batas analoginya: buku manual furnitur tidak pernah berubah setelah dicetak, sedangkan dokumentasi software adalah artefak hidup yang wajib diperbarui seirama dengan setiap perubahan kode sumber aplikasi.",
        "explanation_technical": "Kategori dokumentasi teknis dalam rekayasa perangkat lunak: 1. In-Code Documentation: Docstrings terstandarisasi (Dartdoc ///, JSDoc /** */, Python Docstrings \"\"\") yang menjelaskan parameter fungsi, tipe kembalian, dan kemungkinan exceptions. Tooling IDE menampilkan docstring ini saat developer mengarahkan kursor (hover). 2. Project Onboarding (README.md): Instruksi prasyarat sistem, langkah instalasi dependensi, cara menjalankan aplikasi lokal, dan cara mengeksekusi tes. 3. API Specifications (OpenAPI / Swagger): Spesifikasi formal mesin-terbaca yang mendokumentasikan endpoint, skema request/response, dan status code secara interaktif. 4. Architecture Decision Records (ADR): Dokumen ringkas satu halaman yang mencatat konteks 'MENGAPA' sebuah keputusan arsitektural besar diambil (misal: 'ADR-005: Memilih PostgreSQL daripada MongoDB untuk ledger transaksi').",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Komentar menjelaskan 'kenapa', bukan 'apa'",
                "code": "// BURUK: // Menambah i dengan 1\n// i += 1;\n\n// BAIK: \n// Tambah buffer 5 detik untuk mengatasi selisih waktu server bank\nconst batasWaktu = waktuServer + 5;",
                "explanation": "Komentar yang baik menjelaskan konteks dan alasan bisnis di balik sebuah keputusan teknis.",
                "expected_output": "Kode terdokumentasi dengan baik"
            }
        ],
        "prerequisite_ids": [
            "f-clean-code"
        ],
        "related_topic_ids": [
            "f-clean-code",
            "f-sdlc-agile"
        ],
        "why_vibecoding_matters": "AI asisten sangat terbantu oleh dokumentasi yang jelas: jika repositorimu memiliki README dan docstrings yang rapi, AI dapat memahami konteks kancah aplikasimu dengan presisi tinggi dan menghasilkan kode yang konsisten dengan arsitekturmu. Gunakan kapabilitas AI untuk mendokumentasikan sistemmu: 'Tuliskan dokumentasi OpenAPI (Swagger) untuk endpoint ini, dan buatkan Architecture Decision Record (ADR) ringkas yang merangkum alasan pemilihan arsitektur modular yang baru kita buat.'",
        "keywords": [
            "dokumentasi",
            "readme",
            "comments",
            "docstrings",
            "markdown",
            "panduan"
        ],
        "estimated_minutes": 6,
        "sort_order": 46,
        "is_active": true,
        "problem_context": "Ketika developer utama pembuat sistem mengundurkan diri (resign) dari perusahaan tanpa meninggalkan dokumentasi, tim yang ditinggalkan mengalami krisis fatal (Bus Factor problem). Tidak ada yang berani menyentuh modul pembayaran karena tidak ada yang tahu mengapa kode tertentu ditulis seperti itu. Fitur onboarding developer baru memakan waktu 4 bulan hanya untuk menyiapkan lingkungan laptop. Dokumentasi teknis diciptakan untuk melembagakan pengetahuan agar sistem tidak bergantung pada ingatan rapuh satu individu.",
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
        "when_to_use": "Tulis file README.md yang jelas pada setiap repositori proyek sejak hari pertama. Gunakan Docstrings (/// di Dart) untuk mendokumentasikan semua class dan fungsi publik pada modul bersama (Shared Libraries). Tulis ADR (Architecture Decision Record) setiap kali tim memutuskan adopsi teknologi baru atau perubahan arsitektur besar.",
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
    {
        "id": "f-computer-science",
        "category_id": "f-overview",
        "title": "Computer Science Fundamentals",
        "level": "beginner",
        "summary": "Prinsip dasar sains komputer di balik cara kerja mesin hitung dan perangkat lunak.",
        "explanation_simple": "Bayangkan ilmu arsitektur sipil yang mempelajari kekuatan beton dan gravitasi bumi, dibandingkan dengan tukang bangunan yang memegang sendok semen dan batu bata. Tukang bangunan tahu cara menyusun batu bata agar lurus, tetapi insinyur sipil memahami hukum mekanika fisika mengapa sebuah jembatan gantung tidak akan ambruk saat diterpa badai angin topan.\n\nIlmu Komputer (Computer Science) adalah hukum fisika dan sains di balik setiap ketukan jarimu di keyboard. Ia mempelajari apa yang secara matematis BISA dihitung oleh mesin dan apa yang TIDAK PERNAH BISA diselesaikan oleh komputer tercepat sekalipun. Batas analoginya: gravitasi bumi adalah hukum alam mutlak, sedangkan fondasi ilmu komputer berakar pada traktat matematika murni (logika formal, otomata, dan teori komputabilitas) yang melampaui keterbatasan teknologi silikon fisik.",
        "explanation_technical": "Disiplin Ilmu Komputer berakar pada pilar-pilar teoretis fundamental: 1. Teori Komputabilitas & Automata (Turing Machine, Chomsky Hierarchy): Mesin Turing adalah model komputasi matematis abstrak yang memanipulasi simbol pada pita pita tak terbatas sesuai tabel aturan; mendefinisikan batas kemampuan komputasi modern (Turing Completeness). 2. Teori Kompleksitas Komputasi (P vs NP Problem): Mengklasifikasikan masalah berdasarkan sumber daya yang dibutuhkan untuk menyelesaikannya. - Kelas P: masalah yang dapat diselesaikan dalam waktu polinomial O(n^k). - Kelas NP: masalah yang solusinya sulit dicari tetapi dapat diverifikasi kebenarannya dalam waktu polinomial. 3. Teori Informasi (Claude Shannon): Mengukur kuantitas informasi, redundansi, kompresi data (entropi Shannon), dan batas transmisi sinyal data pada saluran derau berisik.",
        "code_examples": [
            {
                "language": "typescript",
                "label": "Representasi biner sederhana dalam komputer",
                "code": "const angka = 5;\nconsole.log(\"Desimal:\", angka);\nconsole.log(\"Biner (bit 0 & 1):\", angka.toString(2));",
                "explanation": "Semua data teks, gambar, dan kode pada tingkat terdalam direpresentasikan sebagai kombinasi saklar biner 0 dan 1.",
                "expected_output": "Desimal: 5\nBiner (bit 0 & 1): 101"
            }
        ],
        "prerequisite_ids": [],
        "related_topic_ids": [
            "f-programming-logic",
            "f-data-structures",
            "f-algorithms"
        ],
        "why_vibecoding_matters": "Saat vibecoding dengan AI, kamu mungkin meminta AI menyelesaikan masalah optimasi kombinatorial yang sebenarnya tergolong NP-Hard. Jika kamu tidak memahami batas komputasi, AI akan menghasilkan kode pencarian eksak yang membeku selamanya saat dijalankan pada data nyata. Pemahaman ilmu komputer membantumu mengarahkan AI: 'Masalah ini tergolong NP-Hard; jangan cari solusi eksak brute-force, gunakan pendekatan algoritma heuristik greedy atau aproksimasi genetik!'",
        "keywords": [
            "computer science",
            "ilmu komputer",
            "biner",
            "turing",
            "komputasi",
            "fondasi",
            "teori"
        ],
        "estimated_minutes": 7,
        "sort_order": 47,
        "is_active": true,
        "problem_context": "Banyak orang mengira komputer super canggih dapat memecahkan masalah apapun di dunia jika diberi waktu dan memori yang cukup. Pada tahun 1936, sebelum komputer elektronik pertama selesai dirakit, Alan Turing secara brilian membuktikan bahwa ada masalah matematika yang mustahil dipecahkan oleh program komputer apapun (The Halting Problem). Memahami batas fundamental komputasi mencegah insinyur membuang miliaran rupiah mencoba menyelesaikan masalah yang secara matematis terbukti mustahil diselesaikan (NP-Complete / Undecidable problems).",
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
        "when_to_use": "Manfaatkan teori State Machine (Finite State Automata - FSA) saat merancang alur status transaksi kompleks (misal: Cart -> Checkout -> Paid -> Shipped) untuk mencegah invalid transitions. Pahami klasifikasi masalah NP-Hard (seperti Travelling Salesperson atau Knapsack problem) agar kamu tidak membuang waktu mencari solusi eksak brute force; gunakan algoritma Heuristik atau Aproksimasi. Terapkan prinsip Information Theory saat merancang skema kompresi dan encoding data.",
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
]
