9. DICTIONARY DAN SET PYTHON

A. Pengertian Dictionary

Dictionary adalah tipe data Python yang digunakan untuk menyimpan data dalam bentuk pasangan Key dan Value (kunci dan nilai).

Dictionary ditulis menggunakan tanda kurung kurawal {}.

B. Ciri-Ciri Dictionary

1. Menyimpan data dalam pasangan Key dan Value.
2. Setiap Key harus unik.
3. Data dapat ditambah dan diubah.
4. Mengakses data menggunakan Key.

C. Contoh Program Dictionary

mahasiswa = {
    "nama": "Alif",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa["nama"])
print(mahasiswa["jurusan"])

mahasiswa["umur"] = 21
print(mahasiswa)

D. Pengertian Set

Set adalah tipe data Python yang digunakan untuk menyimpan kumpulan data unik atau tidak memiliki nilai duplikat.

Set ditulis menggunakan tanda kurung kurawal {}.

E. Ciri-Ciri Set

1. Tidak menyimpan data duplikat.
2. Tidak memiliki indeks.
3. Data dapat ditambahkan dan dihapus.
4. Urutan data tidak tetap.

F. Contoh Program Set

angka = {1, 2, 3, 4, 4, 5}

print(angka)

angka.add(6)
print(angka)

angka.remove(2)
print(angka)

G. Perbedaan Dictionary dan Set

Dictionary| Set
Memiliki Key dan Value| Menyimpan nilai unik
Menggunakan {}| Menggunakan {}
Mengakses data dengan Key| Tidak menggunakan indeks
Key tidak boleh duplikat| Anggota tidak boleh duplikat

H. Kesimpulan

Dictionary digunakan untuk menyimpan data dalam pasangan Key dan Value, sedangkan Set digunakan untuk menyimpan kumpulan data unik tanpa duplikasi.