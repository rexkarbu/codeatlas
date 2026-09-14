"""Quizzes definition (36 total: 14 language quizzes, 22 concept quizzes) for CodeAtlas.
Covering fundamental and ecosystem topics across diverse domains.
Each quiz has 4 distinct options with unique IDs and text, a valid correct_option_id, and an Indonesian explanation.
"""

QUIZZES = [
    # --- LANGUAGE QUIZZES (14 quizzes) ---
    {
        "id": "q-lang-01",
        "topic_id": "f-variables-data-types",
        "type": "language",
        "level": "beginner",
        "prompt": "Potongan kode berikut menggunakan deklarasi variabel dalam bahasa apa?",
        "snippet": "let jumlah: number = 10;\nconst aktif: boolean = true;",
        "snippet_language": "typescript",
        "options": [
            {"id": "ts", "text": "TypeScript"},
            {"id": "py", "text": "Python"},
            {"id": "dart", "text": "Dart"},
            {"id": "sql", "text": "SQL"}
        ],
        "correct_option_id": "ts",
        "explanation": "Anotasi tipe ': number' dan ': boolean' setelah nama variabel dengan kata kunci let/const adalah ciri khas TypeScript.",
        "is_active": True
    },
    {
        "id": "q-lang-02",
        "topic_id": "f-functions",
        "type": "language",
        "level": "beginner",
        "prompt": "Bahasa apa yang mendefinisikan fungsi menggunakan kata kunci 'def' dan titik dua seperti di bawah ini?",
        "snippet": "def hitung_luas(panjang, lebar):\n    return panjang * lebar",
        "snippet_language": "python",
        "options": [
            {"id": "py", "text": "Python"},
            {"id": "js", "text": "JavaScript"},
            {"id": "dart", "text": "Dart"},
            {"id": "c", "text": "C"}
        ],
        "correct_option_id": "py",
        "explanation": "Kata kunci 'def' dengan blok indentasi dan titik dua (:) adalah sintaks deklarasi fungsi dalam Python.",
        "is_active": True
    },
    {
        "id": "q-lang-03",
        "topic_id": "f-programming-logic",
        "type": "language",
        "level": "beginner",
        "prompt": "Potongan kode berikut adalah titik masuk (entry point) dalam bahasa apa?",
        "snippet": "void main() {\n  final pesan = 'Halo Dunia';\n  print(pesan);\n}",
        "snippet_language": "dart",
        "options": [
            {"id": "dart", "text": "Dart"},
            {"id": "py", "text": "Python"},
            {"id": "ruby", "text": "Ruby"},
            {"id": "php", "text": "PHP"}
        ],
        "correct_option_id": "dart",
        "explanation": "Fungsi 'void main()' dengan 'final' dan tanda kutip tunggal untuk teks adalah sintaks standar Dart.",
        "is_active": True
    },
    {
        "id": "q-lang-04",
        "topic_id": "f-sql",
        "type": "language",
        "level": "beginner",
        "prompt": "Bahasa deklaratif apa yang digunakan dalam potongan instruksi query data berikut?",
        "snippet": "SELECT id, nama, email\nFROM pengguna\nWHERE aktif = 1\nORDER BY nama ASC;",
        "snippet_language": "sql",
        "options": [
            {"id": "sql", "text": "SQL"},
            {"id": "html", "text": "HTML"},
            {"id": "python", "text": "Python"},
            {"id": "json", "text": "JSON"}
        ],
        "correct_option_id": "sql",
        "explanation": "Klausa SELECT, FROM, WHERE, dan ORDER BY adalah kata kunci standar Structured Query Language (SQL).",
        "is_active": True
    },
    {
        "id": "q-lang-05",
        "topic_id": "f-system-programming" if False else "e-system-programming-overview",
        "type": "language",
        "level": "intermediate",
        "prompt": "Bahasa pemrograman sistem modern apa yang menggunakan kata kunci 'fn' dan pencetakan dengan tanda seru seperti di bawah?",
        "snippet": "fn main() {\n    let pesan = \"Selamat Datang\";\n    println!(\"{}\", pesan);\n}",
        "snippet_language": "rust",
        "options": [
            {"id": "rust", "text": "Rust"},
            {"id": "java", "text": "Java"},
            {"id": "python", "text": "Python"},
            {"id": "dart", "text": "Dart"}
        ],
        "correct_option_id": "rust",
        "explanation": "Deklarasi fungsi dengan 'fn' dan macro print dengan tanda seru 'println!' adalah ciri khas bahasa Rust.",
        "is_active": True
    },
    {
        "id": "q-lang-06",
        "topic_id": "f-terminal",
        "type": "language",
        "level": "beginner",
        "prompt": "Perintah-perintah berikut ditulis untuk dijalankan di lingkungan apa?",
        "snippet": "cd /var/www/html\nmkdir aset\ncp ../gambar.png ./aset/\nls -la",
        "snippet_language": "bash",
        "options": [
            {"id": "bash", "text": "Bash / Unix Terminal"},
            {"id": "sql", "text": "SQL Terminal"},
            {"id": "python", "text": "Python REPL"},
            {"id": "html", "text": "HTML Script"}
        ],
        "correct_option_id": "bash",
        "explanation": "Perintah cd, mkdir, cp, dan ls adalah perintah standar antarmuka baris perintah Unix Shell (Bash/Zsh).",
        "is_active": True
    },
    {
        "id": "q-lang-07",
        "topic_id": "f-dependencies",
        "type": "language",
        "level": "beginner",
        "prompt": "Format berkas konfigurasi dengan indentasi spasi dan tanda titik dua berikut menggunakan format apa?",
        "snippet": "name: codeatlas\ndescription: Ensiklopedia coding pemula\nversion: 1.0.0\ndependencies:\n  flutter:\n    sdk: flutter",
        "snippet_language": "yaml",
        "options": [
            {"id": "yaml", "text": "YAML"},
            {"id": "json", "text": "JSON"},
            {"id": "xml", "text": "XML"},
            {"id": "csv", "text": "CSV"}
        ],
        "correct_option_id": "yaml",
        "explanation": "Format berbasis indentasi kunci: nilai tanpa tanda kurung kurawal atau koma adalah format YAML (seperti pubspec.yaml).",
        "is_active": True
    },
    {
        "id": "q-lang-08",
        "topic_id": "f-serialization",
        "type": "language",
        "level": "beginner",
        "prompt": "Format pertukaran data standar berbasis kurung kurawal dan tanda kutip ganda ini adalah:",
        "snippet": "{\n  \"status\": \"sukses\",\n  \"kode\": 200,\n  \"data\": [\"apel\", \"jeruk\"]\n}",
        "snippet_language": "json",
        "options": [
            {"id": "json", "text": "JSON"},
            {"id": "yaml", "text": "YAML"},
            {"id": "sql", "text": "SQL"},
            {"id": "bash", "text": "Bash"}
        ],
        "correct_option_id": "json",
        "explanation": "Struktur dengan pasangan key-value berkutip ganda dan array dalam tanda kurung siku adalah JavaScript Object Notation (JSON).",
        "is_active": True
    },
    {
        "id": "q-lang-09",
        "topic_id": "e-frontend-overview",
        "type": "language",
        "level": "beginner",
        "prompt": "Bahasa markup dokumen web apa yang menggunakan tag berpasangan seperti di bawah ini?",
        "snippet": "<div class=\"kartu\">\n  <h1>Judul Halaman</h1>\n  <p>Deskripsi artikel.</p>\n</div>",
        "snippet_language": "html",
        "options": [
            {"id": "html", "text": "HTML"},
            {"id": "markdown", "text": "Markdown"},
            {"id": "python", "text": "Python"},
            {"id": "css", "text": "CSS"}
        ],
        "correct_option_id": "html",
        "explanation": "Tag pembuka dan penutup seperti <div>, <h1>, dan <p> adalah sintaks HyperText Markup Language (HTML).",
        "is_active": True
    },
    {
        "id": "q-lang-10",
        "topic_id": "e-frontend-overview",
        "type": "language",
        "level": "beginner",
        "prompt": "Bahasa penataan gaya visual apa yang menggunakan selektor kurung kurawal berikut?",
        "snippet": ".kartu {\n  background-color: #ffffff;\n  padding: 16px;\n  border-radius: 8px;\n}",
        "snippet_language": "css",
        "options": [
            {"id": "css", "text": "CSS"},
            {"id": "javascript", "text": "JavaScript"},
            {"id": "html", "text": "HTML"},
            {"id": "json", "text": "JSON"}
        ],
        "correct_option_id": "css",
        "explanation": "Selektor class '.kartu' dengan aturan properti gaya dan titik koma adalah aturan Cascading Style Sheets (CSS).",
        "is_active": True
    },
    {
        "id": "q-lang-11",
        "topic_id": "f-async",
        "type": "language",
        "level": "intermediate",
        "prompt": "Bahasa apa yang menggunakan deklarasi Promise dan arrow function 'async () =>' seperti potongan ini?",
        "snippet": "const ambilData = async (): Promise<string> => {\n  return await Promise.resolve(\"OK\");\n};",
                "snippet_language": "typescript",
        "options": [
            {"id": "ts", "text": "TypeScript"},
            {"id": "py", "text": "Python"},
            {"id": "c", "text": "C"},
            {"id": "go", "text": "Go"}
        ],
        "correct_option_id": "ts",
        "explanation": "Sintaks arrow function async dengan tipe return ': Promise<string>' adalah sintaks TypeScript.",
        "is_active": True
    },
    {
        "id": "q-lang-12",
        "topic_id": "e-languages-overview",
        "type": "language",
        "level": "intermediate",
        "prompt": "Bahasa pemrograman server modern apa yang menggunakan deklarasi 'package main' dan 'func main()'?",
        "snippet": "package main\n\nimport \"fmt\"\n\nfunc main() {\n    fmt.Println(\"Halo dari server\")\n}",
        "snippet_language": "go",
        "options": [
            {"id": "go", "text": "Go (Golang)"},
            {"id": "python", "text": "Python"},
            {"id": "dart", "text": "Dart"},
            {"id": "ruby", "text": "Ruby"}
        ],
        "correct_option_id": "go",
        "explanation": "Kata kunci 'package main', 'import \"fmt\"', dan 'func main()' adalah struktur program bahasa Go.",
        "is_active": True
    },
    {
        "id": "q-lang-13",
        "topic_id": "f-loops",
        "type": "language",
        "level": "beginner",
        "prompt": "Bahasa apa yang menggunakan fungsi 'range(5)' untuk menghasilkan perulangan seperti potongan ini?",
        "snippet": "for i in range(5):\n    print(i * 2)",
        "snippet_language": "python",
        "options": [
            {"id": "py", "text": "Python"},
            {"id": "ts", "text": "TypeScript"},
            {"id": "dart", "text": "Dart"},
            {"id": "sql", "text": "SQL"}
        ],
        "correct_option_id": "py",
        "explanation": "Sintaks 'for i in range(...):' dengan indentasi adalah perulangan standar bahasa Python.",
        "is_active": True
    },
    {
        "id": "q-lang-14",
        "topic_id": "e-mobile-overview",
        "type": "language",
        "level": "beginner",
        "prompt": "Potongan kode deklarasi Widget StatelessWidget ini ditulis dalam bahasa apa?",
        "snippet": "class TombolAksi extends StatelessWidget {\n  const TombolAksi({super.key});\n  @override\n  Widget build(BuildContext context) => Container();\n}",
        "snippet_language": "dart",
        "options": [
            {"id": "dart", "text": "Dart (Flutter)"},
            {"id": "java", "text": "Java"},
            {"id": "swift", "text": "Swift"},
            {"id": "typescript", "text": "TypeScript"}
        ],
        "correct_option_id": "dart",
        "explanation": "Konstruktor dengan '{super.key}' dan anotasi '@override Widget build' adalah kode widget Flutter dalam bahasa Dart.",
        "is_active": True
    },

    # --- CONCEPT QUIZZES (22 quizzes) ---
    {
        "id": "q-con-01",
        "topic_id": "f-programming-logic",
        "type": "concept",
        "level": "beginner",
        "prompt": "Pola alur apa yang paling jelas ditunjukkan oleh tiga langkah berurutan dari atas ke bawah ini?",
        "snippet": "AMBIL gelas\nTUANG air_ke_gelas\nMINUM air",
        "snippet_language": "pseudocode",
        "options": [
            {"id": "seq", "text": "Urutan langkah (sequence)"},
            {"id": "cond", "text": "Percabangan kondisi (conditional)"},
            {"id": "loop", "text": "Perulangan langkah (loop)"},
            {"id": "rec", "text": "Fungsi memanggil dirinya sendiri (recursion)"}
        ],
        "correct_option_id": "seq",
        "explanation": "Instruksi dijalankan berurutan satu per satu dari atas ke bawah tanpa syarat atau pengulangan.",
        "is_active": True
    },
    {
        "id": "q-con-02",
        "topic_id": "f-operators",
        "type": "concept",
        "level": "beginner",
        "prompt": "Apa hasil evaluasi ekspresi kondisi logika di bawah ini?",
        "snippet": "const saldo = 50000;\nconst harga = 30000;\nconst tokoBuka = true;\nconst hasil = (saldo >= harga) && tokoBuka;",
        "snippet_language": "typescript",
        "options": [
            {"id": "true", "text": "true"},
            {"id": "false", "text": "false"},
            {"id": "null", "text": "null"},
            {"id": "err", "text": "Error sintaks"}
        ],
        "correct_option_id": "true",
        "explanation": "Saldo cukup (50000 >= 30000 = true) DAN toko buka (true). True AND True bernilai true.",
        "is_active": True
    },
    {
        "id": "q-con-03",
        "topic_id": "f-conditionals",
        "type": "concept",
        "level": "beginner",
        "prompt": "Teks apa yang akan dicetak oleh blok kode percabangan berikut?",
        "snippet": "let nilai = 85;\nif (nilai >= 90) {\n  console.log(\"A\");\n} else if (nilai >= 80) {\n  console.log(\"B\");\n} else {\n  console.log(\"C\");\n}",
        "snippet_language": "typescript",
        "options": [
            {"id": "b", "text": "B"},
            {"id": "a", "text": "A"},
            {"id": "c", "text": "C"},
            {"id": "ab", "text": "A dan B"}
        ],
        "correct_option_id": "b",
        "explanation": "85 tidak memenuhi nilai >= 90, tetapi memenuhi cabang berikutnya nilai >= 80, sehingga mencetak 'B'.",
        "is_active": True
    },
    {
        "id": "q-con-04",
        "topic_id": "f-loops",
        "type": "concept",
        "level": "beginner",
        "prompt": "Berapa kali kata 'Halo' akan dicetak oleh perulangan for di bawah ini?",
        "snippet": "for (let i = 0; i < 3; i++) {\n  console.log(\"Halo\");\n}",
        "snippet_language": "typescript",
        "options": [
            {"id": "3", "text": "3 kali (saat i = 0, 1, 2)"},
            {"id": "4", "text": "4 kali (saat i = 0, 1, 2, 3)"},
            {"id": "2", "text": "2 kali"},
            {"id": "inf", "text": "Tak terhingga (infinite loop)"}
        ],
        "correct_option_id": "3",
        "explanation": "Loop berjalan untuk i = 0, i = 1, dan i = 2. Saat i bernilai 3, kondisi i < 3 bernilai false dan loop berhenti.",
        "is_active": True
    },
    {
        "id": "q-con-05",
        "topic_id": "f-scope",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Apa yang terjadi saat baris console.log di baris terakhir dijalankan?",
        "snippet": "function contohScope() {\n  const rahasia = 12345;\n}\ncontohScope();\nconsole.log(rahasia);",
        "snippet_language": "typescript",
        "options": [
            {"id": "err", "text": "Error: rahasia is not defined (di luar scope fungsi)"},
            {"id": "val", "text": "Mencetak angka 12345"},
            {"id": "undef", "text": "Mencetak undefined"},
            {"id": "null", "text": "Mencetak null"}
        ],
        "correct_option_id": "err",
        "explanation": "Variabel 'rahasia' memiliki local scope di dalam fungsi contohScope(). Variabel tersebut tidak ada di global scope luar.",
        "is_active": True
    },
    {
        "id": "q-con-06",
        "topic_id": "f-recursion",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Apa fungsi dari baris 'if (n <= 1) return 1;' pada fungsi rekursif berikut?",
        "snippet": "function faktorial(n) {\n  if (n <= 1) return 1;\n  return n * faktorial(n - 1);\n}",
        "snippet_language": "javascript",
        "options": [
            {"id": "base", "text": "Base Case (kondisi penghenti rekursi agar tidak stack overflow)"},
            {"id": "loop", "text": "Inisialisasi perulangan for"},
            {"id": "param", "text": "Validasi tipe parameter"},
            {"id": "catch", "text": "Penangkap error exception"}
        ],
        "correct_option_id": "base",
        "explanation": "Base case adalah kondisi wajib pada fungsi rekursif yang menghentikan pemanggilan dirinya sendiri.",
        "is_active": True
    },
    {
        "id": "q-con-07",
        "topic_id": "f-data-structures",
        "type": "concept",
        "level": "beginner",
        "prompt": "Struktur data mana yang paling tepat untuk model antrean tiket kasir (yang pertama datang dilayani duluan)?",
        "snippet": "MASUK -> [ Orang A, Orang B, Orang C ] -> KELUAR",
        "snippet_language": "pseudocode",
        "options": [
            {"id": "queue", "text": "Queue (FIFO - First In First Out)"},
            {"id": "stack", "text": "Stack (LIFO - Last In First Out)"},
            {"id": "tree", "text": "Binary Search Tree"},
            {"id": "graph", "text": "Graph"}
        ],
        "correct_option_id": "queue",
        "explanation": "Queue menerapkan prinsip FIFO di mana elemen yang masuk pertama kali akan diproses pertama kali.",
        "is_active": True
    },
    {
        "id": "q-con-08",
        "topic_id": "f-big-o",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Berapa kompleksitas waktu (Big-O) dari dua perulangan bersarang (nested loops) berikut?",
        "snippet": "for (let i = 0; i < n; i++) {\n  for (let j = 0; j < n; j++) {\n    console.log(i, j);\n  }\n}",
        "snippet_language": "typescript",
        "options": [
            {"id": "n2", "text": "O(n^2) - Kuadratik"},
            {"id": "n", "text": "O(n) - Linear"},
            {"id": "1", "text": "O(1) - Konstan"},
            {"id": "logn", "text": "O(log n) - Logaritmik"}
        ],
        "correct_option_id": "n2",
        "explanation": "Loop luar berputar n kali, dan untuk setiap putaran loop dalam juga berputar n kali: total n * n = O(n^2).",
        "is_active": True
    },
    {
        "id": "q-con-09",
        "topic_id": "f-oop",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Prinsip OOP apa yang ditunjukkan dengan membuat field menjadi 'private' dan hanya bisa diubah lewat method?",
        "snippet": "class Rekening {\n  private saldo: number = 0;\n  public setor(jumlah: number) {\n    if (jumlah > 0) this.saldo += jumlah;\n  }\n}",
        "snippet_language": "typescript",
        "options": [
            {"id": "encap", "text": "Encapsulation (Pembungkusan data internal)"},
            {"id": "inher", "text": "Inheritance (Pewarisan sifat)"},
            {"id": "poly", "text": "Polymorphism (Banyak bentuk)"},
            {"id": "recurs", "text": "Recursion"}
        ],
        "correct_option_id": "encap",
        "explanation": "Encapsulation melindungi data internal objek agar tidak bisa diubah sembarangan dari luar tanpa validasi.",
        "is_active": True
    },
    {
        "id": "q-con-10",
        "topic_id": "f-clean-code",
        "type": "concept",
        "level": "beginner",
        "prompt": "Prinsip clean code apa yang dilanggar ketika kita menyalin 20 baris kode yang sama ke 5 file berbeda?",
        "snippet": "// Kode perhitungan pajak disalin ulang di 5 file berbeda",
        "snippet_language": "pseudocode",
        "options": [
            {"id": "dry", "text": "DRY (Don't Repeat Yourself)"},
            {"id": "yagni", "text": "YAGNI (You Aren't Gonna Need It)"},
            {"id": "acid", "text": "ACID"},
            {"id": "kiss", "text": "KISS"}
        ],
        "correct_option_id": "dry",
        "explanation": "Prinsip DRY mengharuskan setiap bagian pengetahuan atau logika dalam sistem memiliki representasi tunggal yang tidak ambigu.",
        "is_active": True
    },
    {
        "id": "q-con-11",
        "topic_id": "f-error-handling",
        "type": "concept",
        "level": "beginner",
        "prompt": "Apa yang akan dicetak di konsol saat potongan kode penanganan kesalahan ini dieksekusi?",
        "snippet": "try {\n  throw new Error(\"Gagal koneksi\");\n} catch (e) {\n  console.log(\"Tertangkap\");\n} finally {\n  console.log(\"Selesai\");\n}",
        "snippet_language": "javascript",
        "options": [
            {"id": "both", "text": "Tertangkap lalu Selesai"},
            {"id": "onlycatch", "text": "Hanya Tertangkap"},
            {"id": "crash", "text": "Program langsung crash"},
            {"id": "onlyfinally", "text": "Hanya Selesai"}
        ],
        "correct_option_id": "both",
        "explanation": "Blok catch menangani error sehingga program tidak crash, dan blok finally SELALU dijalankan di akhir.",
        "is_active": True
    },
    {
        "id": "q-con-12",
        "topic_id": "f-references",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Berapakah nilai obj1.nilai setelah baris terakhir dieksekusi?",
        "snippet": "const obj1 = { nilai: 10 };\nconst obj2 = obj1;\nobj2.nilai = 50;\nconsole.log(obj1.nilai);",
        "snippet_language": "typescript",
        "options": [
            {"id": "50", "text": "50 (karena obj1 dan obj2 berbagi referensi memori yang sama)"},
            {"id": "10", "text": "10 (obj1 nilainya tidak berubah)"},
            {"id": "undef", "text": "undefined"},
            {"id": "err", "text": "Error assignment const"}
        ],
        "correct_option_id": "50",
        "explanation": "Objek disalin berdasarkan referensi (alamat memori). Mengubah properti obj2 juga mengubah properti obj1.",
        "is_active": True
    },
    {
        "id": "q-con-13",
        "topic_id": "f-async",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Apa urutan angka yang dicetak oleh kode asinkron event loop berikut?",
        "snippet": "console.log(1);\nsetTimeout(() => console.log(2), 0);\nconsole.log(3);",
        "snippet_language": "javascript",
        "options": [
            {"id": "132", "text": "1, 3, lalu 2"},
            {"id": "123", "text": "1, 2, lalu 3"},
            {"id": "213", "text": "2, 1, lalu 3"},
            {"id": "321", "text": "3, 2, lalu 1"}
        ],
        "correct_option_id": "132",
        "explanation": "Kode sinkron (1 dan 3) langsung dieksekusi di call stack utama. Callback setTimeout diantrekan ke event loop dan baru berjalan setelah stack kosong.",
        "is_active": True
    },
    {
        "id": "q-con-14",
        "topic_id": "f-git",
        "type": "concept",
        "level": "beginner",
        "prompt": "Perintah Git apa yang digunakan untuk membuat snapshot riwayat perubahan dengan pesan deskripsi?",
        "snippet": "git ... -m \"feat: perbarui tombol navigasi\"",
        "snippet_language": "bash",
        "options": [
            {"id": "commit", "text": "git commit"},
            {"id": "push", "text": "git push"},
            {"id": "pull", "text": "git pull"},
            {"id": "branch", "text": "git branch"}
        ],
        "correct_option_id": "commit",
        "explanation": "'git commit' menyimpan snapshot permanen dari perubahan yang sudah di-stage ke riwayat lokal repositori.",
        "is_active": True
    },
    {
        "id": "q-con-15",
        "topic_id": "f-http-web",
        "type": "concept",
        "level": "beginner",
        "prompt": "HTTP status code berkepala 4xx (seperti 404 Not Found) menunjukkan jenis kesalahan apa?",
        "snippet": "HTTP/1.1 404 Not Found",
        "snippet_language": "http",
        "options": [
            {"id": "client", "text": "Client Error (kesalahan pada permintaan dari sisi klien)"},
            {"id": "server", "text": "Server Error (kesalahan internal di sisi server)"},
            {"id": "success", "text": "Permintaan berhasil diproses"},
            {"id": "redirect", "text": "Pengalihan rute (redirect)"}
        ],
        "correct_option_id": "client",
        "explanation": "Status 4xx menunjukkan Client Error (misal salah ketik URL atau belum login). Kesalahan server ditandai kode 5xx.",
        "is_active": True
    },
    {
        "id": "q-con-16",
        "topic_id": "f-data-modeling",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Apa fungsi dari batasan 'FOREIGN KEY (kategori_id) REFERENCES kategori(id)' pada skema tabel relasional?",
        "snippet": "CREATE TABLE topik (\n  id TEXT PRIMARY KEY,\n  kategori_id TEXT REFERENCES kategori(id)\n);",
        "snippet_language": "sql",
        "options": [
            {"id": "fk", "text": "Menjamin nilai kategori_id harus benar-benar ada di tabel kategori (integritas referensial)"},
            {"id": "sort", "text": "Mengurutkan data secara otomatis"},
            {"id": "enc", "text": "Mengenkripsi teks kategori"},
            {"id": "auto", "text": "Membuat angka unik berurutan"}
        ],
        "correct_option_id": "fk",
        "explanation": "Foreign Key menjaga integritas referensial, mencegah adanya data 'yatim' yang merujuk ke kategori fiktif.",
        "is_active": True
    },
    {
        "id": "q-con-17",
        "topic_id": "f-security",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Mengapa kita harus menggunakan parameterized query 'WHERE email = ?' daripada menyambung teks langsung (string concatenation)?",
        "snippet": "db.execute(\"SELECT * FROM users WHERE email = ?\", [userEmail]);",
        "snippet_language": "typescript",
        "options": [
            {"id": "sqli", "text": "Mencegah serangan pembajakan database (SQL Injection)"},
            {"id": "fast", "text": "Hanya agar query berjalan 10% lebih cepat"},
            {"id": "color", "text": "Agar sintaks berwarna di terminal"},
            {"id": "limit", "text": "Membatasi hasil pencarian maksimal 1"}
        ],
        "correct_option_id": "sqli",
        "explanation": "Parameterized query memisahkan instruksi SQL dari data masukan pengguna, menggagalkan serangan SQL Injection.",
        "is_active": True
    },
    {
        "id": "q-con-18",
        "topic_id": "e-caching-overview",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Apa yang dimaksud dengan kondisi 'Cache Miss' pada sistem penyimpanan cache?",
        "snippet": "// getCache('user_101') -> null",
        "snippet_language": "typescript",
        "options": [
            {"id": "miss", "text": "Data yang dicari tidak ditemukan di cache, sehingga harus diambil dari database utama"},
            {"id": "err", "text": "Server cache mengalami kerusakan fisik"},
            {"id": "hit", "text": "Data berhasil ditemukan langsung di memori RAM"},
            {"id": "del", "text": "Data berhasil dihapus dari memori"}
        ],
        "correct_option_id": "miss",
        "explanation": "Cache Miss terjadi saat data belum ada di memori cepat RAM, memaksa aplikasi membaca dari database yang lebih lambat.",
        "is_active": True
    },
    {
        "id": "q-con-19",
        "topic_id": "e-frameworks-overview",
        "type": "concept",
        "level": "beginner",
        "prompt": "Prinsip utama apa yang membedakan Framework dari Library biasa?",
        "snippet": "// 'Don't call us, we'll call you'",
        "snippet_language": "pseudocode",
        "options": [
            {"id": "ioc", "text": "Inversion of Control (Framework yang mengendalikan alur hidup dan memanggil kodemu)"},
            {"id": "size", "text": "Framework selalu berukuran lebih kecil dari library"},
            {"id": "price", "text": "Framework harus dibeli berbayar"},
            {"id": "speed", "text": "Library tidak bisa dipakai di mobile"}
        ],
        "correct_option_id": "ioc",
        "explanation": "Pada framework berlaku Inversion of Control: framework yang mengatur kapan fungsi/widget buatanmu dipanggil.",
        "is_active": True
    },
    {
        "id": "q-con-20",
        "topic_id": "e-message-brokers-overview",
        "type": "concept",
        "level": "intermediate",
        "prompt": "Apa manfaat utama menggunakan Message Broker (seperti RabbitMQ atau Kafka) di antara dua layanan backend?",
        "snippet": "Layanan Pesanan -> [ Message Queue ] -> Layanan Pengiriman",
        "snippet_language": "pseudocode",
        "options": [
            {"id": "decouple", "text": "Decoupling: layanan pengirim tidak terhambat meski layanan penerima sedang lambat/down"},
            {"id": "ui", "text": "Membuat tampilan antarmuka web jadi lebih indah"},
            {"id": "css", "text": "Mengompresi berkas gambar"},
            {"id": "sql", "text": "Menggantikan seluruh fungsi database SQL"}
        ],
        "correct_option_id": "decouple",
        "explanation": "Message queue memisahkan dependensi waktu (decoupling), menjamin pesan tetap aman dalam antrean saat sistem penerima sibuk.",
        "is_active": True
    },
    {
        "id": "q-con-21",
        "topic_id": "e-cloud-overview",
        "type": "concept",
        "level": "beginner",
        "prompt": "Apa karakteristik utama dari model komputasi Serverless (FaaS seperti AWS Lambda)?",
        "snippet": "export const handler = async (event) => { ... }",
        "snippet_language": "typescript",
        "options": [
            {"id": "scale", "text": "Fungsi hanya menyala saat ada request dan biaya hanya dihitung saat fungsi berjalan"},
            {"id": "noserver", "text": "Benar-benar tidak ada komputer server fisik di dunia"},
            {"id": "free", "text": "Layanan selamanya 100% gratis tanpa batas"},
            {"id": "offline", "text": "Tidak membutuhkan koneksi internet sama sekali"}
        ],
        "correct_option_id": "scale",
        "explanation": "Serverless mengabstraksi manajemen server: fungsi dijalankan on-demand dan biaya dihitung per milidetik eksekusi.",
        "is_active": True
    },
    {
        "id": "q-con-22",
        "topic_id": "e-open-source-overview",
        "type": "concept",
        "level": "beginner",
        "prompt": "Lisensi open source mana yang mengizinkan kodemu digunakan bebas untuk proyek komersial tertutup dengan tetap menyertakan nama pembuat aslinya?",
        "snippet": "SPDX-License-Identifier: MIT",
        "snippet_language": "pseudocode",
        "options": [
            {"id": "mit", "text": "Lisensi Permisif (seperti MIT atau Apache 2.0)"},
            {"id": "gpl", "text": "Lisensi Keras Copyleft (seperti GPL v3)"},
            {"id": "patent", "text": "Hak Paten Tertutup Militer"},
            {"id": "none", "text": "Semua lisensi melarang penggunaan komersial"}
        ],
        "correct_option_id": "mit",
        "explanation": "Lisensi MIT adalah lisensi permisif yang sangat ramah komersial, hanya mensyaratkan pencantuman atribusi hak cipta.",
        "is_active": True
    }
]
