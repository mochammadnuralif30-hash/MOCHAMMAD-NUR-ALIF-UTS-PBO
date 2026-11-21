17. File Handling (Pengolahan File)

A. Pengertian File Handling

File Handling adalah proses membaca, membuat, menulis, dan mengelola file menggunakan bahasa pemrograman Python.

File Handling berguna untuk menyimpan data agar tetap tersedia meskipun program sudah ditutup.

B. Mode Penggunaan File

Python memiliki beberapa mode untuk mengelola file:

1. "r" (Read): Membaca isi file.
2. "w" (Write): Menulis file dan mengganti isi sebelumnya.
3. "a" (Append): Menambahkan isi di akhir file.
4. "x" (Create): Membuat file baru dan menghasilkan kesalahan jika file sudah ada.

C. Contoh Menulis File

with open("data.txt", "w") as file:
    file.write("Belajar Python File Handling")

print("Data berhasil disimpan.")

D. Contoh Membaca File

with open("data.txt", "r") as file:
    isi = file.read()

print(isi)

E. Contoh Menambahkan Data

with open("data.txt", "a") as file:
    file.write("\nBelajar Pemrograman Berorientasi Objek")

print("Data berhasil ditambahkan.")

F. Penjelasan Kode

- "open()" digunakan untuk membuka file.
- "data.txt" merupakan nama file yang digunakan.
- ""w"" digunakan untuk menulis data.
- ""r"" digunakan untuk membaca data.
- ""a"" digunakan untuk menambahkan data.
- "write()" digunakan untuk menulis isi file.
- "read()" digunakan untuk membaca isi file.
- "with" membantu menutup file secara otomatis setelah proses selesai.

G. Manfaat File Handling

1. Menyimpan data secara permanen.
2. Membaca data yang sudah disimpan.
3. Memperbarui informasi dalam file.
4. Memudahkan pengelolaan data program.

H. Penerapan dalam Game Balapan Mobil

File Handling dapat digunakan untuk menyimpan skor tertinggi pemain, nama pemain, dan pengaturan game ke dalam file.

Dengan demikian, data permainan dapat dibaca kembali ketika game dijalankan.

Kesimpulan

File Handling merupakan fitur Python untuk mengelola file, mulai dari membaca, menulis, hingga menambahkan data. Fitur ini membantu program menyimpan dan menggunakan data secara lebih teratur.