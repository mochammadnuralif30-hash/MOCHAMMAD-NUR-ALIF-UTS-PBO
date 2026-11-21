11. OBJECT-ORIENTED PROGRAMMING (OOP)

A. Pengertian OOP

Object-Oriented Programming (OOP) adalah metode pemrograman yang menggunakan objek sebagai dasar dalam pembuatan program. OOP membantu membuat program lebih terstruktur, mudah dikembangkan, dan digunakan kembali.

B. Konsep Dasar OOP

1. Class: Cetakan atau rancangan untuk membuat objek.
2. Object: Hasil nyata dari sebuah class.
3. Attribute: Variabel yang menyimpan data atau karakteristik objek.
4. Method: Fungsi yang berada di dalam class.

C. Empat Pilar OOP

1. Encapsulation: Melindungi data agar tidak diakses atau diubah secara sembarangan.
2. Inheritance: Pewarisan atribut dan method dari class induk ke class anak.
3. Polymorphism: Kemampuan objek menggunakan method dengan bentuk atau perilaku berbeda.
4. Abstraction: Menyembunyikan detail proses dan menampilkan bagian penting saja.

D. Contoh Program OOP

class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def berjalan(self):
        print(self.merek, "sedang berjalan")

mobil1 = Mobil("Toyota", "Merah")

print(mobil1.merek)
print(mobil1.warna)

mobil1.berjalan()

E. Manfaat OOP

1. Membuat program lebih terstruktur.
2. Mempermudah penggunaan kembali kode.
3. Mempermudah pengembangan program.
4. Mempermudah pemeliharaan kode.
5. Membantu mengelola program yang kompleks.

F. Penerapan OOP pada Game Balapan Mobil

Dalam game balapan mobil, konsep OOP dapat diterapkan sebagai berikut:

- Class Mobil: Rancangan kendaraan.
- Object: Mobil pemain dan mobil musuh.
- Attribute: Kecepatan, posisi, warna, dan skor.
- Method: Bergerak, menghindar, dan memperbarui posisi.

G. Kesimpulan

OOP merupakan metode pemrograman berbasis objek yang membuat program lebih terstruktur dan mudah dikembangkan. Konsep ini sangat berguna dalam pembuatan aplikasi dan game menggunakan Python.