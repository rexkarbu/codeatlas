"""Enrichment Part 2: Data Structures, Algorithms, Paradigms, and Architecture (Topics 10 - 19).
"""

CURRICULUM_PART2 = {
    "f-data-structures": {
        "summary": "Format pengorganisasian, penyimpanan, dan pengelolaan data di memori untuk komputasi efisien.",
        "explanation_simple": (
            "Bayangkan lemari arsip di kantor pengacara. Jika dokumen disusun bertumpuk acak di satu kotak kardus, "
            "kamu harus membongkar seluruh kardus selama berjam-jam hanya untuk mencari akta kelahiran seorang klien. "
            "Namun, jika dokumen ditata dalam map gantung bernomor urut atau laci berlabel abjad A-Z, kamu bisa mengambil "
            "berkas yang dibutuhkan dalam hitungan detik.\n\n"
            "Struktur data adalah cetak biru penataan memori agar data dapat dicari, disisipkan, diubah, dan dihapus secara optimal. "
            "Batas analoginya: lemari fisik di kantor memiliki sekat kayu permanen, sedangkan struktur data di komputer "
            "dapat diatur ulang secara dinamis melalui penunjuk alamat memori (pointer) dalam hitungan nanodetik."
        ),
        "problem_context": (
            "Di era komputasi awal, data hanya disimpan dalam array datar berurutan. Ketika volume data melonjak dari ribuan "
            "menjadi jutaan entitas, operasi pencarian data di array membutuhkan penelusuran linear satu per satu dari awal sampai akhir. "
            "Sistem reservasi penerbangan atau indeks basis data bank menjadi sangat lambat hingga berhenti merespons (freeze). "
            "Para peneliti ilmu komputer menyadari bahwa struktur data yang berbeda memiliki karakteristik performa yang berbeda "
            "untuk operasi baca vs tulis, memicu penemuan struktur data non-linear seperti Hash Map, B-Tree, dan Graph."
        ),
        "explanation_technical": (
            "Struktur data diklasifikasikan menjadi: "
            "1. Linear: elemen tersusun berurutan (Array, Linked List, Stack, Queue). Elemen memiliki tetangga sebelum dan sesudah yang jelas. "
            "2. Non-linear: elemen memiliki hubungan hierarkis atau jejaring (Trees, Heaps, Graphs, Hash Tables).\n\n"
            "Pemilihan struktur data didasarkan pada kompromi (trade-offs) kompleksitas waktu operasi utama: akses acak (random access), "
            "pencarian (search), penyisipan (insertion), dan penghapusan (deletion). "
            "Struktur data juga mempengaruhi cache locality: array kontinu memanfaatkan CPU L1/L2 data cache secara maksimal, "
            "sedangkan struktur berbasis node pointer (seperti Linked List) sering memicu cache miss karena node-nodenya tersebar acak di heap memory."
        ),
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
        "when_to_use": (
            "Gunakan Array/List dinamis saat kamu membutuhkan akses elemen cepat berbasis indeks dan ukuran data moderat. "
            "Gunakan Set saat kamu wajib menjamin keunikan data dan butuh pencarian O(1). "
            "Gunakan Map/Dictionary untuk relasi kunci-nilai yang membutuhkan pencarian instan tanpa iterasi linear."
        ),
        "why_vibecoding_matters": (
            "AI sering kali memilih List secara default untuk semua jenis penyimpanan koleksi, bahkan ketika kode melakukan pengecekan duplikasi berulang kali. "
            "Hal ini menimbulkan perlambatan tersembunyi yang baru terasa saat aplikasi menerima data pengguna dalam jumlah besar. "
            "Saat vibecoding, tanyakan ke AI: 'Apakah struktur data yang digunakan di modul ini sudah optimal untuk pola akses query "
            "yang sering dilakukan (baca vs tulis)? Bisakah Set atau Map menggantikan List untuk mengeliminasi pencarian O(n)?'"
        ),
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

    "f-arrays-lists": {
        "summary": "Koleksi data terurut dengan alokasi memori bersebelahan dan akses cepat berbasis indeks numerik.",
        "explanation_simple": (
            "Bayangkan deretan loker bernomor urut 0, 1, 2, 3 di lobi stasiun kereta. Setiap loker memiliki ukuran yang sama persis "
            "dan berjejer berdampingan di dinding yang sama. Jika petugas stasiun memintamu membuka loker nomor 2, "
            "kamu bisa langsung melangkah tepat ke pintu nomor 2 tanpa perlu membuka loker 0 dan 1 terlebih dahulu.\n\n"
            "Array dan List adalah struktur data berurutan paling populer dalam pemrograman. "
            "Batas analogi loker: loker di stasiun memiliki dinding fisik yang tidak bisa digeser. Dalam memori komputer, "
            "jika kamu ingin menyisipkan loker baru di posisi nomor 1, semua loker dari nomor 1 ke atas harus digeser "
            "satu langkah ke kanan, yang membutuhkan banyak waktu jika jumlah lokernya ribuan."
        ),
        "problem_context": (
            "Ketika menulis program yang harus mengolah data banyak entitas (seperti daftar skor 100 pemain game), "
            "membuat 100 variabel manual (skor1, skor2, ... skor100) adalah bencana. Program tidak bisa melakukan pengulangan, "
            "tidak bisa mengurutkan nilai secara dinamis, dan ukuran kode meledak. "
            "Array diciptakan untuk menyatukan sekumpulan elemen sejenis dalam satu penampung bersebelahan yang dapat diakses dengan indeks."
        ),
        "explanation_technical": (
            "Secara memori tingkat rendah, Fixed Array dialokasikan sebagai satu blok byte bersebelahan (contiguous memory). "
            "Alamat elemen ke-i dihitung instan: Base_Address + (Index * Element_Size). Operasi pembacaan dan pembaruan indeks bernilai O(1).\n\n"
            "Namun, penyisipan atau penghapusan elemen di awal atau tengah array bernilai O(n) karena elemen-elemen setelahnya "
            "harus digeser (memory shift) menggunakan instruksi memmove. "
            "Dynamic Array (seperti List di Dart/Python, Array di JavaScript, ArrayList di Java) mengatasi batasan kapasitas tetap "
            "dengan mengalokasikan kapasitas cadangan (capacity). Ketika kapasitas penuh, runtime mengalokasikan blok memori baru "
            "berukuran 1.5x atau 2x lipat (geometric resizing), menyalin semua elemen lama, dan membebaskan blok lama. "
            "Operasi penambahan di akhir (append/push) memiliki kompleksitas teramortisasi (amortized) O(1)."
        ),
        "misconceptions": [
            {
                "misconception": "List di JavaScript dan Python adalah array murni seperti di bahasa C.",
                "explanation": "Di JS dan Python, List/Array adalah objek dinamis tingkat tinggi dengan kapasitas fleksibel dan dapat menampung tipe data campuran, bukan fixed memory array murni bertipe homogen.",
                "spot_in_code": "Mengira array JS mengalokasikan memori byte biner kaku padahal mesin V8 mengoptimasi penyimpanannya di balik layar."
            },
            {
                "misconception": "Operasi menyisipkan elemen di awal array (list.insert(0, val) atau array.unshift()) sama cepatnya dengan menyisipkan di akhir.",
                "explanation": "Menyisipkan di indeks 0 memaksa setiap elemen di dalam array digeser satu posisi ke kanan, berbiaya O(n) dan sangat lambat untuk koleksi besar.",
                "spot_in_code": "Menggunakan list sebagai queue dengan melakukan list.insert(0, data) di dalam loop pemrosesan data."
            }
        ],
        "when_to_use": (
            "Gunakan Array/List ketika kamu membutuhkan urutan data yang stabil dan sering membaca elemen berdasarkan posisi indeks. "
            "Gunakan append/push untuk menambahkan data ke ujung akhir koleksi. "
            "Jika kamu sering menambah dan menghapus elemen dari kedua ujung antrean, gunakan struktur Double-Ended Queue (Deque) alih-alih List biasa."
        ),
        "why_vibecoding_matters": (
            "AI sering menyarankan array.shift() atau list.removeAt(0) di dalam loop untuk memproses antrean tugas. "
            "Operasi ini mengubah kompleksitas pemrosesan dari O(n) menjadi O(n^2), membuat aplikasi melambat drastis saat antrean memanjang. "
            "Saat vibecoding, teliti manipulasi list dan tanyakan ke AI: 'Apakah operasi penghapusan atau penyisipan ini dilakukan di awal list? "
            "Jika ya, gantilah dengan struktur Queue atau kelola pointer indeks agar kompleksitasnya tetap O(1).'"
        ),
        "reflection_questions": [
            {
                "question": "Apa yang dimaksud dengan 'amortized O(1)' pada penambahan elemen dynamic array?",
                "answer": "Mayoritas operasi penambahan hanya butuh 1 langkah O(1); sesekali terjadi operasi ekspansi memori O(n) saat kapasitas penuh, namun biaya ekspansi tersebut terbagi rata ke seluruh operasi sebelumnya sehingga rata-rata tetap O(1)."
            },
            {
                "question": "Mengapa menghapus elemen terakhir dari list jauh lebih murah daripada menghapus elemen pertama?",
                "answer": "Menghapus elemen terakhir hanya memotong panjang array tanpa menggeser data lain O(1), sedangkan menghapus elemen pertama memaksa semua elemen sisa digeser mundur satu posisi O(n)."
            }
        ]
    },

    "f-references": {
        "summary": "Mekanisme pengacuan data di memori melalui pointer dan alias objek.",
        "explanation_simple": (
            "Bayangkan kamu membagikan tautan (link) Google Docs dokumen proposal kepada tiga rekan kerjamu. "
            "Kamu tidak mencetak tiga bundel kertas fisik untuk masing-masing orang, melainkan membagikan alamat URL yang sama. "
            "Jika rekan A menambahkan paragraf baru di Google Docs tersebut, rekan B dan kamu yang membuka dokumen lewat tautan tersebut "
            "akan langsung melihat paragraf tambahan tersebut secara bersamaan.\n\n"
            "Referensi (references) adalah tautan alamat ke lokasi objek di memori heap komputer. "
            "Batas analoginya: jika kamu menyalin selembar uang kertas dengan fotokopi (pass-by-value primitif), "
            "coretan spidol pada fotokopi tidak akan mempengaruhi uang kertas asli. Namun pada tipe referensi, "
            "beberapa variabel hanyalah beberapa nama julukan yang sama-sama menunjuk ke objek data fisik yang identik."
        ),
        "problem_context": (
            "Bayangkan sebuah program game yang memiliki objek peta dunia 3D berukuran 500 Megabyte. "
            "Setiap kali fungsi merender cuaca, menghitung fisika, atau memproses musuh dipanggil, "
            "jika program harus menggandakan 500 MB data tersebut ke stack frame fungsi baru, memori komputer akan habis dalam sekejap "
            "dan game berjalan patah-patah (lag parah). Sistem referensi diciptakan agar fungsi dapat saling berbagi akses ke objek besar "
            "hanya dengan mengirimkan pointer alamat memori berukuran 4 atau 8 byte."
        ),
        "explanation_technical": (
            "Secara arsitektur prosesor, referensi adalah abstraksi aman dari memory pointer yang menyimpan alamat memori virtual (misalnya 0x7FFF1234). "
            "Tipe data primitif (int, float, bool) diteruskan dengan mekanisme Pass-by-Value: nilai bit digandakan ke stack frame baru. "
            "Sebaliknya, objek dan koleksi diteruskan dengan Pass-by-Sharing (atau pass-by-value dari nilai referensi pointer): "
            "alamat objek disalin, tetapi kedua pointer mengarah ke instance data heap yang sama.\n\n"
            "Hal ini memicu fenomena Aliasing: mutasi data internal objek (in-place mutation) melalui satu referensi akan terlihat "
            "oleh semua referensi lain yang mengarah ke objek tersebut. Untuk mencegah efek samping mutasi liar (unintended side-effects), "
            "pola Immutable Objects, Defensive Copying (Shallow Copy vs Deep Copy), atau kata kunci pembatas mutasi (seperti const/readonly) "
            "sangat penting diterapkan dalam arsitektur software modern."
        ),
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
        "when_to_use": (
            "Gunakan referensi untuk membagikan akses ke struktur data besar atau service singleton tanpa overhead penggandaan memori. "
            "Gunakan Deep Copy atau struktur data immutable saat mengirimkan state data ke komponen antarmuka pengguna agar perubahan lokal tidak merusak state pusat. "
            "Waspadai aliasing pada fungsi yang menerima parameter koleksi: jangan mutasi list parameter secara langsung kecuali fungsi tersebut didokumentasikan sebagai mutator eksplisit."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis kode fungsi yang memodifikasi properti objek masukan secara langsung (in-place mutation), "
            "mengakibatkan bug misterius di bagian lain aplikasi yang mengandalkan objek tersebut sebelum termutasi. "
            "Saat vibecoding, instruksikan AI: 'Jangan lakukan mutasi langsung pada parameter objek ini; "
            "buatlah salinan baru (immutable return) menggunakan deep copy atau pattern copyWith.'"
        ),
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

    "f-algorithms": {
        "summary": "Rangkaian langkah logis terdefinisi dengan baik untuk menyelesaikan masalah komputasi secara terukur.",
        "explanation_simple": (
            "Bayangkan kamu tersesat di labirin taman bermain dan ingin menemukan jalan keluar tercepat. "
            "Strategi acak berlari ke segala arah bisa memakan waktu berjam-jam tanpa hasil pasti. "
            "Namun, jika kamu menggunakan aturan 'sentuh dinding sebelah kanan dengan tangan kananmu dan berjalanlah tanpa pernah melepas tangan dari dinding', "
            "kamu dijamin secara matematis akan menemukan jalan keluar dari labirin standar.\n\n"
            "Algoritma adalah resep sistematis langkah demi langkah untuk mengubah masukan menjadi keluaran yang valid. "
            "Batas analoginya: instruksi labirin manusia bisa terhambat rasa lelah atau ragu, sedangkan algoritma komputer "
            "dieksekusi secara konsisten tanpa bias emosional dengan kecepatan miliaran siklus instruksi per detik."
        ),
        "problem_context": (
            "Menghitung rute navigasi terdekat di Google Maps di antara 50 juta persimpangan jalan dunia adalah mustahil "
            "jika komputer mencoba setiap kemungkinan kombinasi rute secara brutal (kombinatorika faktorial akan membutuhkan jutaan tahun). "
            "Algoritma cerdas (seperti Algoritma Dijkstra dan A*) diciptakan agar komputer dapat menemukan jalur terpendek "
            "hanya dalam hitungan beberapa milidetik dengan memangkas rute yang tidak relevan secara sistematis."
        ),
        "explanation_technical": (
            "Algoritma formal wajib memenuhi lima kriteria komputasional klasik (Knuth): "
            "1. Input: menerima nol atau lebih kuantitas masukan. "
            "2. Output: menghasilkan satu atau lebih kuantitas keluaran yang bermakna. "
            "3. Definiteness: setiap langkah instruksi harus jelas, presisi, dan tidak ambigu. "
            "4. Finiteness: algoritma harus selalu berhenti setelah sejumlah langkah berhingga untuk semua kasus masukan. "
            "5. Effectiveness: setiap operasi harus cukup mendasar sehingga secara prinsip dapat dieksekusi oleh mesin dalam waktu terbatas.\n\n"
            "Paradigma perancangan algoritma meliputi: Brute Force (pencarian lengkap), Divide and Conquer (pemecahan masalah menjadi sub-masalah independen, misal Merge Sort), "
            "Greedy (pengambilan keputusan lokal terbaik pada setiap langkah), dan Dynamic Programming (penyimpanan solusi sub-masalah bertumpang-tindih menggunakan memoization)."
        ),
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
        "when_to_use": (
            "Gunakan algoritma terstandarisasi yang sudah teruji di industri (seperti sorting bawaan bahasa, hashing crypto SHA-256) daripada menciptakan algoritma sendiri dari nol. "
            "Gunakan Dynamic Programming saat sub-masalah komputasi memiliki sifat overlapping subproblems (seperti penghitungan rute atau edit distance teks). "
            "Gunakan Greedy Algorithm hanya jika properti optimal substructure terbukti menghasilkan solusi global terbaik."
        ),
        "why_vibecoding_matters": (
            "AI sering kali memilih algoritma Brute Force bersarang O(n^2) atau O(2^n) untuk menyelesaikan masalah pemfilteran atau pencocokan data karena algoritma tersebut paling cepat diketik. "
            "Saat vibecoding, tantang AI: 'Berapa kompleksitas algoritma yang kamu hasilkan ini? "
            "Tolong optimalkan algoritma ini menjadi O(n log n) atau O(n) menggunakan teknik Map/Set atau Divide-and-Conquer.'"
        ),
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

    "f-big-o": {
        "summary": "Notasi matematis untuk mengukur skalabilitas efisiensi waktu dan konsumsi memori saat ukuran data membesar.",
        "explanation_simple": (
            "Bayangkan kamu ingin mengantarkan berkas dokumen ke temanmu. Jika temanmu duduk di meja sebelah, berjalan kaki memakan waktu 10 detik. "
            "Jika temanmu berada di kota lain, terbang naik pesawat memakan waktu 4 jam. "
            "Sekarang bayangkan kamu harus mengirim 1.000 berkas dokumen: berjalan kaki bolak-balik 1.000 kali memakan waktu berjam-jam (tumbuh linear sesuai jumlah berkas). "
            "Tetapi jika kamu memasukkan 1.000 berkas itu ke dalam satu bagasi koper di pesawat yang sama, durasi penerbangannya tetap 4 jam (waktu konstan tidak peduli seberapa banyak berkasnya).\n\n"
            "Notasi Big O adalah cara insinyur software mengukur seberapa cepat kebutuhan waktu atau memori melonjak ketika data pengguna meledak dari 10 menjadi 10.000.000 entitas. "
            "Batas analoginya: di dunia fisik ada batasan berat bagasi pesawat, sedangkan di komputasi Big O menggambarkan tren laju pertumbuhan kurva teoretis murni pada skenario batas ekstrem (asymptotic worst-case)."
        ),
        "problem_context": (
            "Sebuah fitur pencarian produk toko online berjalan lancar dalam 10 milidetik di laptop developer saat diuji dengan 50 produk contoh. "
            "Namun ketika aplikasi diluncurkan ke publik dan database memiliki 500.000 produk, pencarian yang sama tiba-tiba membutuhkan waktu 12 menit dan membuat server crash. "
            "Developer tersebut tidak memahami Big O dan menulis algoritma O(n^2) dengan loop bersarang ganda. "
            "Analisis Big O diciptakan agar insinyur dapat memprediksi perilaku aplikasi pada skala jutaan data tanpa harus menunggu crash di lingkungan produksi."
        ),
        "explanation_technical": (
            "Notasi Big O (Asymptotic Notation) mengukur batas atas (upper bound) laju pertumbuhan konsumsi waktu (Time Complexity) "
            "dan ruang memori tambahan (Space Complexity) seiring nilai n (ukuran input) mendekati tak hingga. "
            "Konstanta pengali dan suku berderajat rendah diabaikan (misalnya rumus 3n^2 + 5n + 100 disederhanakan menjadi O(n^2)) "
            "karena pada nilai n yang masif, suku berderajat tertinggilah yang mendominasi tren pertumbuhan.\n\n"
            "Spektrum efisiensi Big O dari terbaik ke terburuk: "
            "1. O(1) - Konstan: akses elemen array dengan indeks, operasi hash map ideal. "
            "2. O(log n) - Logaritmik: binary search pada data terurut (membelah ruang pencarian menjadi setengah tiap langkah). "
            "3. O(n) - Linear: mencari data di array acak melalui iterasi satu per satu. "
            "4. O(n log n) - Linearitmik: algoritma pengurutan optimal (Merge Sort, Tim Sort). "
            "5. O(n^2) - Kuadratik: loop bersarang dua tingkat (Bubble Sort, perbandingan semua pasangan). "
            "6. O(2^n) - Eksponensial: rekursi cabang ganda tanpa memoization. "
            "7. O(n!) - Faktorial: mencari semua permutasi kemungkinan rute perjalanan (Travelling Salesperson brute-force)."
        ),
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
        "when_to_use": (
            "Gunakan analisis Big O saat merancang query database, API endpoint, atau algoritma pengolahan data yang diperkirakan akan berkembang seiring waktu. "
            "Targetkan kompleksitas O(1) atau O(log n) untuk operasi yang sangat sering dipanggil (seperti pengecekan autentikasi atau lookup cache). "
            "Waspadai algoritma berkategori O(n^2) ke atas: jangan gunakan pada koleksi data yang jumlah elemennya melebihi beberapa ratus tanpa pembatasan pagination."
        ),
        "why_vibecoding_matters": (
            "AI sering menulis kode yang tampak ringkas dan 'elegan' dalam 2 baris (misalnya listA.filter(x => listB.some(y => y.id === x.id))), "
            "tanpa memberitahumu bahwa kode tersebut menyembunyikan kompleksitas kuadratik O(n * m) yang melumpuhkan browser saat data membesar. "
            "Saat vibecoding, mintalah AI mengevaluasi kodenya: 'Berapa time complexity dan space complexity dari kode ini dalam notasi Big O? "
            "Bisakah kamu mengubahnya menjadi O(n) menggunakan Hash Set atau Map?'"
        ),
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

    "f-oop": {
        "summary": "Paradigma pemodelan perangkat lunak berbasis objek yang menggabungkan state data dan perilaku method.",
        "explanation_simple": (
            "Bayangkan pabrik perakitan mobil. Sebelum memproduksi ribuan mobil, insinyur merancang blueprint cetak biru bernama 'Mobil'. "
            "Cetakan ini menentukan bahwa setiap mobil memiliki atribut warna, kapasitas bensin, dan kecepatan, serta kemampuan (method) "
            "seperti 'hidupkanMesin()', 'injakGas()', dan 'rem()'. Dari satu cetakan itu, pabrik dapat mencetak mobil Avanza warna hitam milik Budi "
            "dan mobil Yaris warna merah milik Ani.\n\n"
            "Object-Oriented Programming (OOP) menyatukan data (state) dan fungsi (perilaku) ke dalam satu wadah mandiri bernama Objek. "
            "Batas analogi pabrik: di dunia fisik, mobil yang sudah dirakit tidak bisa tiba-tiba mewarisi fitur perahu amfibi secara instan. "
            "Dalam kode, konsep pewarisan (inheritance) yang berlebihan justru dapat mengikat komponen dalam hierarki kaku yang sulit diubah di kemudian hari."
        ),
        "problem_context": (
            "Dalam pemrograman prosedural murni tanpa enkapsulasi objek, data aplikasi disimpan dalam record/struct terbuka "
            "dan ratusan fungsi bebas memanipulasi field struct tersebut dari mana saja. "
            "Jika variabel 'saldo' pada struct Rekening diubah langsung menjadi negatif tanpa melewati validasi aturan bisnis, "
            "sistem perbankan mengalami korupsi data tanpa bisa melacak fungsi mana yang bersalah. "
            "OOP lahir untuk membentengi data di balik dinding pelindung (Enkapsulasi) dan mengorganisir sistem modular berskala masif."
        ),
        "explanation_technical": (
            "OOP bertumpu pada empat pilar fundamental: "
            "1. Encapsulation: menyembunyikan detail internal objek (private state) dan membatasi interaksi hanya melalui antarmuka publik resmi (getters/methods). "
            "2. Abstraction: menyederhanakan interaksi dengan menyembunyikan kompleksitas implementasi di balik antarmuka abstrak atau interface. "
            "3. Inheritance: kemampuan class turunan (subclass) mewarisi properti dan method dari class induk (superclass) untuk penggunaan kembali kode. "
            "4. Polymorphism: kemampuan objek dari berbagai tipe class turunan untuk merespons pemanggilan method yang sama dengan perilaku spesifik masing-masing (Dynamic Dispatch via vtable).\n\n"
            "Meskipun inheritance sangat populer, arsitektur software modern menganjurkan prinsip 'Composition over Inheritance': "
            "lebih baik menyusun objek dari komponen-komponen mandiri (HAS-A) daripada menciptakan rantai pewarisan hierarki yang dalam (IS-A) "
            "yang memicu masalah rapuhnya class induk (fragile base class problem)."
        ),
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
        "when_to_use": (
            "Gunakan OOP saat memodelkan domain bisnis dengan entitas kaya state yang memiliki siklus hidup dan aturan validasi ketat. "
            "Manfaatkan Interface dan Polimorfisme untuk memisahkan implementasi konkret (misalnya implementasi PaymentGatewayMock vs PaymentGatewayStripe). "
            "Terapkan komposisi daripada pewarisan ketika ingin berbagi kapabilitas perilaku antarkelas."
        ),
        "why_vibecoding_matters": (
            "AI gemar menghasilkan class god-object (satu class raksasa yang mengurus semuanya) atau hierarki pewarisan warisan tua yang kaku. "
            "Saat vibecoding, instruksikan AI menerapkan SOLID principles: 'Rancang modul ini dengan prinsip Single Responsibility, "
            "gunakan interface untuk mendefinisikan kontrak method, dan gunakan dependency injection daripada hardcoding instansiasi di dalam class.'"
        ),
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

    "f-functional-programming": {
        "summary": "Paradigma komputasi yang memperlakukan evaluasi program sebagai fungsi matematika murni tanpa mutasi state.",
        "explanation_simple": (
            "Bayangkan pabrik pengolahan air minum kemasan otomatis. Air mentah dari mata air mengalir melalui pipa filter karbon, "
            "lalu ke tabung sinar ultraviolet, dan berakhir di botol kemasan bersih. "
            "Di setiap stasiun, air diproses dan diteruskan ke tahap berikutnya; tidak ada stasiun yang mengubah atau mengotori mata air asal di hulu. "
            "Jika kamu ingin membuat 1.000 botol, kamu cukup mengalirkan air melalui pipa yang sama berulang kali dengan hasil kemurnian yang identik.\n\n"
            "Functional Programming (FP) memandang program sebagai rangkaian pipa transformasi fungsi matematika. "
            "Batas analoginya: pabrik air fisik membutuhkan listrik dan ruang nyata, sedangkan fungsi matematika dalam FP bersifat murni: "
            "ia tidak pernah mengubah data aslinya (Immutability) dan tidak peduli berapa kali kamu menjalankannya, hasilnya selalu sama persis."
        ),
        "problem_context": (
            "Dalam sistem aplikasi skala besar dengan puluhan thread prosesor yang berjalan paralel (seperti server web multi-core), "
            "paradigma yang mengandalkan mutasi state bersama (shared mutable state) memicu kekacauan besar. "
            "Dua thread yang mencoba mengubah variabel saldo bank yang sama pada mikrodetik yang sama mengakibatkan race condition "
            "dan deadlock yang sangat sulit dilacak. Functional Programming hadir untuk menyelesaikan krisis konkurensi ini "
            "dengan melarang mutasi state secara radikal."
        ),
        "explanation_technical": (
            "Functional Programming berlandaskan pada fondasi teori Lambda Calculus (Church). Tiga pilar intinya meliputi: "
            "1. Pure Functions: fungsi yang outputnya 100% ditentukan oleh input argumennya dan tidak menimbulkan Side Effects (tidak memodifikasi state luar, tidak melakukan penulisan disk/jaringan tanpa abstraksi efek monad). "
            "2. Immutability: sekali data dialokasikan, data tersebut tidak pernah diubah; setiap perubahan menghasilkan salinan data baru dengan state yang diperbarui (menggunakan teknik persistent data structures untuk efisiensi memori). "
            "3. First-Class & Higher-Order Functions: fungsi dapat diperlakukan sebagai nilai (disimpan di variabel, dipassing sebagai parameter, dikembalikan sebagai return value).\n\n"
            "Operasi koleksi FP standar meliputi: map (transformasi 1:1), filter (penyaringan berbasis predikat boolean), "
            "dan reduce/fold (penggabungan seluruh elemen menjadi satu nilai akhir). FP juga memanfaatkan Function Composition dan Currying."
        ),
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
        "when_to_use": (
            "Gunakan fungsi murni (map, filter, reduce) saat melakukan transformasi dan agregasi data koleksi. "
            "Terapkan state immutable pada state management aplikasi antarmuka pengguna (seperti Redux, Bloc, Riverpod) untuk menjamin time-travel debugging dan rendering UI terprediksi. "
            "Gunakan FP pada pipeline pemrosesan data paralel dan komputasi event streaming."
        ),
        "why_vibecoding_matters": (
            "AI sering mencampuradukkan gaya fungsional dan mutasi in-place (seperti memanggil list.map() lalu di dalamnya melakukan variabelLuar++), "
            "menciptakan efek samping tersembunyi yang merusak determinisme kode. "
            "Saat vibecoding, instruksikan AI: 'Tulis logika transformasi data ini dengan gaya fungsional murni tanpa mutasi state luar, "
            "gunakan map/filter/reduce dan pastikan fungsinya bersifat idempotensial serta bebas side-effects.'"
        ),
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

    "f-clean-code": {
        "summary": "Praktek penulisan kode yang memprioritaskan keterbacaan manusia, kesederhanaan struktur, dan kemudahan pemeliharaan.",
        "explanation_simple": (
            "Bayangkan membaca buku teks yang dicetak rapi dengan daftar isi jelas, bab berurutan, paragraf ringkas, "
            "dan tanda baca yang benar, dibandingkan membaca tumpukan catatan kusut yang penuh coretan singkatan aneh tanpa spasi. "
            "Meskipun kedua buku tersebut menyampaikan informasi fakta yang sama, buku yang rapi dapat dipahami dalam sekejap, "
            "sedangkan catatan yang berantakan memakan waktu berjam-jam untuk didekripsi.\n\n"
            "Clean Code adalah seni menulis kode komputer yang bukan hanya dimengerti oleh prosesor mesin, tetapi terutama "
            "mudah dibaca, dipahami, dan dikembangkan oleh manusia rekan kerjamu (atau dirimu sendiri 6 bulan kemudian). "
            "Batas analoginya: buku cetak bersifat statis setelah dicetak, sedangkan kode software adalah dokumen hidup "
            "yang akan terus diubah dan diperluas seiring perkembangan kebutuhan bisnis."
        ),
        "problem_context": (
            "Fakta industri software membuktikan bahwa rasio waktu yang dihabiskan programmer untuk membaca kode berbanding menulis kode baru "
            "mencapai 10 banding 1. Ketika sebuah tim mewarisi codebase legacy yang penuh dengan fungsi 500 baris, variabel singkatan misterius (seperti a, x, temp, d8), "
            "dan logika duplikat di mana-mana, kecepatan rilis fitur baru anjlok mendekati nol. "
            "Setiap perbaikan bug kecil justru memicu dua bug baru di modul lain. Krisis Technical Debt ini melahirkan gerakan Clean Code."
        ),
        "explanation_technical": (
            "Clean Code berakar pada prinsip rekayasa esensial: "
            "1. Meaningful Names: nama variabel, fungsi, dan class harus mencerminkan niat bisnis tanpa butuh komentar penjelas (misalnya daysSinceLastLogin alih-alih d). "
            "2. Small Functions & Single Responsibility: fungsi harus pendek (idealnya di bawah 20 baris) dan hanya mengerjakan satu hal dengan satu level abstraksi. "
            "3. DRY (Don't Repeat Yourself): setiap keping pengetahuan harus memiliki representasi tunggal dan tak ambigu dalam sistem. "
            "4. Avoid Magic Numbers/Strings: ganti nilai harfiah acak dengan konstanta bernama deskriptif (misalnya HTTP_STATUS_OK = 200). "
            "5. Separation of Concerns: pisahkan logika bisnis murni, pengolahan data, dan kode presentasi visual ke modul terpisah.\n\n"
            "Komentar kode hanya digunakan untuk menjelaskan 'MENGAPA' sebuah keputusan arsitektural aneh diambil, "
            "bukan untuk menjelaskan 'APA' yang dilakukan kode. Jika kode membutuhkan komentar untuk menjelaskan apa yang dilakukannya, "
            "artinya kode tersebut belum bersih dan harus direfaktor."
        ),
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
        "when_to_use": (
            "Terapkan Boy Scout Rule: 'Tinggalkan perkemahan kode dalam kondisi lebih bersih daripada saat kamu menemukannya'. "
            "Gunakan linter otomatis dan formatters (seperti dart format, prettier, black) di CI/CD pipeline untuk menegakkan standar gaya penulisan secara otomatis. "
            "Refactor kode saat menambahkan fitur baru, bukan menunda refactoring ke 'nanti kalau ada waktu luang'."
        ),
        "why_vibecoding_matters": (
            "AI asisten memiliki kecenderungan melahirkan kode 'cepat jalan' yang penuh dengan variabel abstrak seperti data, res, item2, "
            "serta menduplikasi blok kode yang sama di berbagai fungsi. "
            "Saat vibecoding, jangan terima kode pertama AI begitu saja. Perintahkan: 'Refactor kode ini mengikuti standar Clean Code: "
            "berikan penamaan yang deskriptif, pecah fungsi besar menjadi fungsi-fungsi modular berorientasi tujuan, dan hilangkan semua magic numbers.'"
        ),
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
    }
}
