12. CLASS DAN OBJECT PYTHON

A. Pengertian Class

Class adalah sebuah cetakan atau rancangan yang digunakan untuk membuat objek. Class berisi atribut dan method yang menentukan karakteristik serta perilaku objek.

B. Pengertian Object

Object adalah hasil atau bentuk nyata dari sebuah class. Setiap objek dapat memiliki nilai atribut yang berbeda meskipun berasal dari class yang sama.

C. Atribut (Attribute)

Attribute adalah variabel yang terdapat di dalam class dan digunakan untuk menyimpan informasi atau karakteristik objek.

Contoh atribut mobil:

- Merek
- Warna
- Kecepatan
- Tahun produksi

D. Method

Method adalah fungsi yang dibuat di dalam class untuk menjalankan tindakan tertentu.

Contoh method:

- Menjalankan mobil.
- Menghentikan mobil.
- Mempercepat mobil.

E. Contoh Program Class dan Object

class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek
        self.warna = warna

    def berjalan(self):
        print(self.merek, "sedang berjalan")

# Membuat objek
mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Hitam")

# Menampilkan atribut
print(mobil1.merek)
print(mobil1.warna)

print(mobil2.merek)
print(mobil2.warna)

# Memanggil method
mobil1.berjalan()
mobil2.berjalan()

F. Perbedaan Class dan Object

Class| Object
Cetakan atau rancangan| Hasil dari class
Menentukan atribut| Memiliki nilai atribut
Menentukan method| Menjalankan method

G. Penerapan pada Game Balapan Mobil

Dalam game balapan mobil:

- Class Mobil digunakan sebagai rancangan kendaraan.
- Object mobil pemain dibuat dari class Mobil.
- Object mobil musuh juga dibuat dari class Mobil.
- Atribut menyimpan posisi dan kecepatan.
- Method digunakan untuk menggerakkan mobil.

H. Kesimpulan

Class merupakan rancangan untuk membuat objek, sedangkan object adalah hasil dari class. Keduanya merupakan konsep dasar dalam pemrograman berorientasi objek (OOP).