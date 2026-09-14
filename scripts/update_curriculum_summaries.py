"""Script to update all topic summaries across the 9 curriculum files with friendly, concise, natural Indonesian summaries.
"""

import re
from pathlib import Path

SUMMARIES = {
    # Fundamental
    "f-programming-logic": "Menyusun instruksi dengan urutan yang masuk akal.",
    "f-variables-data-types": "Menyimpan data dengan nama dan wadah yang sesuai jenisnya.",
    "f-operators": "Simbol untuk menghitung, membandingkan, dan mengolah nilai.",
    "f-conditionals": "Membuat keputusan dalam program berdasarkan kondisi benar atau salah.",
    "f-loops": "Mengulang perintah berkali-kali sampai batas yang ditentukan.",
    "f-pattern-matching": "Mencocokkan bentuk data dan mengambil isinya secara rapi.",
    "f-functions": "Membungkus langkah kerja berulang ke dalam satu perintah bernama.",
    "f-scope": "Wilayah dan batas waktu hidup variabel di dalam kode.",
    "f-type-system": "Aturan jenis data agar program tidak salah mengolah nilai.",
    "f-recursion": "Fungsi yang memanggil dirinya sendiri untuk memecahkan masalah bertingkat.",
    "f-data-structures": "Cara menata dan menyimpan data agar mudah dicari dan diolah.",
    "f-arrays-lists": "Koleksi data terurut yang mudah diakses lewat nomor urut atau indeks.",
    "f-algorithms": "Langkah teratur untuk menyelesaikan masalah komputasi secara efisien.",
    "f-big-o": "Cara mengukur seberapa cepat dan hemat memori kode saat data bertambah banyak.",
    "f-oop": "Menata kode dengan menggabungkan data dan fungsinya ke dalam bentuk objek.",
    "f-functional-programming": "Menulis program dengan fungsi murni tanpa mengubah data secara langsung.",
    "f-clean-code": "Kebiasaan menulis kode yang rapi, mudah dibaca, dan gampang dirawat.",
    "f-design-patterns": "Pola solusi teruji untuk menyelesaikan masalah rancangan kode yang sering berulang.",
    "f-software-architecture": "Rancangan kerangka besar aplikasi agar komponen-komponennya bekerja harmonis.",
    "f-error-handling": "Menyiapkan antisipasi agar aplikasi tidak langsung mati saat terjadi gangguan.",
    "f-debugging": "Cara melacak, menemukan, dan memperbaiki kesalahan logika di dalam kode.",
    "f-testing": "Memeriksa kebenaran kode secara otomatis agar fitur tidak mudah rusak.",
    "f-memory": "Memahami bagaimana program meminjam, memakai, dan mengembalikan memori komputer.",
    "f-references": "Melihat bagaimana variabel merujuk atau menunjuk ke data yang sama di memori.",
    "f-input-output": "Cara program menerima masukan dari pengguna dan menampilkan hasilnya keluar.",
    "f-file-system": "Membaca, menulis, dan mengelola berkas serta folder di media penyimpanan.",
    "f-operating-system": "Peran sistem operasi dalam menjembatani aplikasi dengan perangkat keras komputer.",
    "f-modules-packages": "Memecah kode menjadi berkas-berkas terpisah agar rapi dan mudah dipakai ulang.",
    "f-dependencies": "Memasang dan mengelola pustaka buatan orang lain secara aman dan terkontrol.",
    "f-build-compilation": "Mengubah tulisan kode menjadi berkas aplikasi yang siap dijalankan perangkat.",
    "f-runtime": "Lingkungan tempat kode berjalan dan dieksekusi oleh komputer.",
    "f-git": "Mencatat riwayat perubahan kode dan bekerja bersama tim tanpa saling menimpa.",
    "f-terminal": "Memberi instruksi ke komputer secara langsung lewat baris perintah teks.",
    "f-networking": "Cara komputer saling bertukar data melalui kabel, sinyal, dan internet.",
    "f-http-web": "Aturan komunikasi web untuk meminta dan mengirim halaman atau data.",
    "f-apis": "Pintu penghubung agar dua aplikasi atau sistem berbeda bisa saling berbicara.",
    "f-serialization": "Mengubah data di memori menjadi format teks seperti JSON agar bisa dikirim atau disimpan.",
    "f-databases": "Tempat menyimpan data aplikasi dalam jumlah besar dengan rapi, aman, dan cepat dicari.",
    "f-sql": "Bahasa perintah untuk meminta, menambah, dan mengubah data di basis data relasional.",
    "f-data-modeling": "Merancang struktur tabel dan hubungan antardata sebelum aplikasi dibangun.",
    "f-auth": "Memeriksa siapa pengguna yang masuk dan apa saja hak akses yang dimilikinya.",
    "f-security": "Menjaga aplikasi dari celah bahaya dan serangan pihak yang tidak berhak.",
    "f-concurrency": "Menjalankan beberapa tugas sekaligus agar aplikasi tetap lincah dan tidak macet.",
    "f-async": "Menjalankan proses yang butuh waktu tanpa membuat tampilan aplikasi membeku.",
    "f-deployment": "Menerbangkan aplikasi dari komputer lokal ke server agar bisa diakses pengguna umum.",
    "f-logging-monitoring": "Mencatat aktivitas dan memantau kesehatan aplikasi saat sudah dipakai umum.",
    "f-sdlc-agile": "Langkah kerja dan kebiasaan tim dalam mengembangkan aplikasi secara bertahap.",
    "f-documentation": "Menulis catatan penjelasan agar orang lain dan diri sendiri paham cara kerja sistem.",
    "f-computer-science": "Prinsip dasar sains komputer di balik cara kerja mesin hitung dan perangkat lunak.",

    # Ecosystem
    "e-languages-overview": "Mengenal ragam bahasa pemrograman dan memilih yang paling pas untuk kebutuhanmu.",
    "e-compilers-overview": "Melihat bagaimana compiler menerjemahkan kode menjadi bahasa mesin.",
    "e-runtime-overview": "Mengenal mesin eksekusi seperti Node.js, Bun, dan Dart VM di dunia nyata.",
    "e-package-managers-overview": "Alat pengunduh dan pengelola pustaka eksternal seperti npm, pip, dan pub.",
    "e-build-tools-overview": "Alat otomatisasi untuk merapikan, menggabungkan, dan menyiapkan kode sebelum rilis.",
    "e-frameworks-overview": "Kerangka kerja siap pakai yang memandu struktur dan aturan pembuatan aplikasi.",
    "e-libraries-overview": "Kumpulan fungsi siap pakai yang bisa langsung dipanggil untuk tugas tertentu.",
    "e-orm-overview": "Penghubung agar kita bisa mengolah basis data menggunakan objek kode biasa.",
    "e-frontend-overview": "Dunia pembuatan antarmuka visual dan interaksi yang langsung dilihat oleh pengguna.",
    "e-backend-overview": "Sisi balik layar yang mengurus logika bisnis, simpanan data, dan keamanan server.",
    "e-mobile-overview": "Pengembangan aplikasi untuk ponsel Android dan iOS secara native maupun multiplatform.",
    "e-desktop-overview": "Pembuatan aplikasi untuk komputer desktop Windows, macOS, dan Linux.",
    "e-games-overview": "Dunia pengembangan game, alur visual grafis, dan mesin pembuat game.",
    "e-embedded-overview": "Memprogram perangkat keras kecil seperti mikrokontroler dan alat-alat IoT.",
    "e-graphics-overview": "Pengolahan gambar, animasi, dan visual 2D/3D lewat kartu grafis (GPU).",
    "e-databases-overview": "Membandingkan berbagai jenis database: tabel relasional, dokumen, hingga grafik.",
    "e-api-communication-overview": "Ragam cara menghubungkan layanan: REST, GraphQL, WebSocket, hingga gRPC.",
    "e-message-brokers-overview": "Sistem pengantar pesan dan antrean tugas agar layanan tidak kewalahan.",
    "e-caching-overview": "Menyimpan data populer di memori kilat agar aplikasi merespons lebih cepat.",
    "e-dsa-overview": "Penerapan struktur data dan algoritma canggih di aplikasi industri nyata.",
    "e-paradigms-overview": "Gaya berpikir dalam memprogram: berorientasi objek, fungsional, atau deklaratif.",
    "e-system-programming-overview": "Pemrograman tingkat rendah yang dekat dengan perangkat keras menggunakan C, C++, atau Rust.",
    "e-computer-science-overview": "Gambaran bidang ilmu komputer terapan: kriptografi, teori bahasa, hingga AI.",
    "e-architecture-overview": "Pilihan bentuk arsitektur aplikasi: satu kesatuan utuh atau layanan terpisah-pisah.",
    "e-patterns-overview": "Pola arsitektur tingkat lanjut untuk menangani sistem aplikasi skala besar.",
    "e-distributed-overview": "Tantangan membangun sistem yang tersebar di banyak server di berbagai tempat.",
    "e-networking-overview": "Infrastruktur jaringan internet, alamat IP, nama domain (DNS), dan keamanan data.",
    "e-operating-systems-overview": "Mengenal sistem operasi server seperti Linux, proses latar belakang, dan izin akses.",
    "e-shells-overview": "Menggunakan terminal dan skrip baris perintah untuk mempercepat pekerjaan harian.",
    "e-web-servers-overview": "Aplikasi penerima tamu web seperti Nginx dan Caddy yang mengarahkan lalu lintas data.",
    "e-cloud-overview": "Menyewa komputer dan layanan di awan (AWS, Google Cloud, Azure) tanpa beli server fisik.",
    "e-iac-overview": "Menyiapkan server dan infrastruktur cloud lewat kode otomatis (Infrastructure as Code).",
    "e-orchestration-overview": "Menata dan menjalankan kontainer aplikasi seperti Docker dan Kubernetes.",
    "e-testing-overview": "Lanskap pengujian aplikasi di industri, dari tes fungsi kecil hingga tes tampilan menyeluruh.",
    "e-debugging-overview": "Alat bantu melacak bug di industri, titik henti kode (breakpoints), dan rekaman riwayat.",
    "e-security-overview": "Celah bahaya umum di aplikasi web dan cara menangkalnya sejak awal.",
    "e-cybersecurity-overview": "Prinsip keamanan menyeluruh untuk melindungi data rahasia dan jaringan bisnis.",
    "e-accessibility-overview": "Membuat aplikasi ramah bagi semua pengguna, termasuk penyandang disabilitas.",
    "e-devops-overview": "Budaya dan jalur otomatisasi dari penulisan kode hingga aplikasi siap dinikmati pengguna.",
    "e-observability-overview": "Melihat kondisi jeroan aplikasi lewat log, angka performa, dan jejak panggilan sistem.",
    "e-production-overview": "Strategi memperbarui aplikasi di server produksi dengan aman tanpa memutus layanan pengguna.",
    "e-developer-tools-overview": "Peralatan andalan developer: editor kode, pemeriksa kerapian, dan bantuan otomatis.",
    "e-data-engineering-overview": "Membangun pipa aliran data dari berbagai sumber ke gudang data yang siap dianalisis.",
    "e-data-science-overview": "Menggali pola dan wawasan berharga dari tumpukan data menggunakan statistik dan kode.",
    "e-ai-ml-overview": "Dasar kecerdasan buatan, model bahasa besar (LLM), dan cara memanfaatkannya di aplikasi.",
    "e-version-control-overview": "Strategi percabangan Git dan kerja sama tim dalam mengelola versi aplikasi.",
    "e-engineering-process-overview": "Alur kerja tim rekayasa software: perencanaan tugas, review kode, dan perbaikan berkala.",
    "e-ui-ux-overview": "Prinsip kenyamanan tampilan dan kemudahan penggunaan aplikasi bagi pengguna awam.",
    "e-technical-docs-overview": "Menulis dokumentasi teknis dan panduan API yang jelas bagi developer lain.",
    "e-localization-overview": "Menyiapkan aplikasi agar mudah diterjemahkan ke berbagai bahasa dan budaya dunia.",
    "e-blockchain-overview": "Dasar buku besar terdesentralisasi, kontrak pintar, dan ekosistem Web3.",
    "e-open-source-overview": "Aturan lisensi kode terbuka dan cara berkontribusi di komunitas perangkat lunak.",
}

FILES = [
    "curriculum_part1_logic_control_func.py",
    "curriculum_part2_data_algo_paradigm.py",
    "curriculum_part3_architecture_quality_memory.py",
    "curriculum_part4a_io_system_networking.py",
    "curriculum_part4b_apis_storage_security_cs.py",
    "curriculum_ecosystem_part1.py",
    "curriculum_ecosystem_part2_platforms_data_arch.py",
    "curriculum_ecosystem_part3_infra_cloud_security_devops.py",
    "curriculum_ecosystem_part4_data_ai_practices.py",
]

def update_file(path: Path):
    content = path.read_text(encoding="utf-8")
    original = content
    updated_count = 0

    for topic_id, new_summary in SUMMARIES.items():
        # Look for the topic block: "topic_id": {\n        "summary": "..."
        # or similar spacing
        pattern = rf'("{re.escape(topic_id)}":\s*\{{[^}}]*?"summary":\s*")[^"]*(")'
        def repl(match):
            nonlocal updated_count
            updated_count += 1
            return f'{match.group(1)}{new_summary}{match.group(2)}'
        content = re.sub(pattern, repl, content, count=1)

    if content != original:
        path.write_text(content, encoding="utf-8")
        print(f"Updated {path.name}: replaced {updated_count} summaries.")
    else:
        print(f"No changes in {path.name} (matched {updated_count}).")

def main():
    root = Path(__file__).resolve().parent
    for fname in FILES:
        p = root / fname
        if p.exists():
            update_file(p)
        else:
            print(f"File not found: {fname}")

if __name__ == "__main__":
    main()
