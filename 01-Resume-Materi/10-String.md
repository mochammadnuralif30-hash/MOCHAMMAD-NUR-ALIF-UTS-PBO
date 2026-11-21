10. STRING DALAM PYTHON

A. Pengertian String

String adalah tipe data dalam Python yang digunakan untuk menyimpan kumpulan karakter berupa huruf, angka, simbol, maupun teks.

String ditulis menggunakan tanda petik satu (' ') atau tanda petik dua (" ").

B. Ciri-Ciri String

1. Digunakan untuk menyimpan teks.
2. Dapat berisi huruf, angka, dan simbol.
3. Setiap karakter memiliki indeks.
4. Isi string tidak dapat diubah secara langsung.

C. Contoh Program String

nama = "Alif"
alamat = "Indonesia"

print("Nama:", nama)
print("Alamat:", alamat)

D. Operasi String

Beberapa operasi yang dapat digunakan pada string:

1. Penggabungan (+): Menggabungkan dua string.
2. Pengulangan (*): Mengulang string.
3. Len(): Menghitung jumlah karakter.
4. Upper(): Mengubah huruf menjadi kapital.
5. Lower(): Mengubah huruf menjadi kecil.

E. Contoh Penggunaan Operasi String

nama = "Python"

print(nama.upper())
print(nama.lower())
print(len(nama))

depan = "Game"
belakang = "Mobil"

hasil = depan + " " + belakang
print(hasil)

F. Mengambil Karakter String

Karakter dalam string dapat diambil menggunakan indeks.

kata = "PYTHON"

print(kata[0])
print(kata[1])
print(kata[2])

G. Kesimpulan

String merupakan tipe data untuk menyimpan teks atau kumpulan karakter. Python menyediakan berbagai operasi string untuk mengolah dan memanipulasi teks dalam program.