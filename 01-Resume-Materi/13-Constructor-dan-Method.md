13. CONSTRUCTOR DAN METHOD PYTHON

A. Pengertian Constructor

Constructor adalah method khusus dalam class yang dijalankan secara otomatis ketika sebuah objek dibuat.

Dalam Python, constructor menggunakan method "__init__()".

B. Fungsi Constructor

1. Memberikan nilai awal pada atribut objek.
2. Menyiapkan data ketika objek dibuat.
3. Mempermudah proses pembuatan objek.

C. Pengertian Method

Method adalah fungsi yang berada di dalam class dan digunakan untuk menjalankan tindakan tertentu pada objek.

D. Jenis Method

1. Instance Method: Method yang menggunakan parameter "self" untuk mengakses atribut objek.
2. Class Method: Method yang menggunakan parameter "cls" untuk mengakses class.
3. Static Method: Method yang tidak membutuhkan parameter "self" maupun "cls".

E. Contoh Program Constructor dan Method

class Mobil:
    def __init__(self, merek, kecepatan):
        self.merek = merek
        self.kecepatan = kecepatan

    def berjalan(self):
        print(self.merek, "sedang berjalan")

    def tambah_kecepatan(self, nilai):
        self.kecepatan += nilai
        print("Kecepatan:", self.kecepatan)

mobil1 = Mobil("Toyota", 60)

mobil1.berjalan()
mobil1.tambah_kecepatan(20)

F. Penjelasan Program

- "__init__()" merupakan constructor.
- "self.merek" menyimpan merek mobil.
- "self.kecepatan" menyimpan kecepatan mobil.
- "berjalan()" merupakan method untuk menjalankan mobil.
- "tambah_kecepatan()" digunakan untuk meningkatkan kecepatan.

G. Penerapan pada Game Balapan Mobil

Constructor digunakan untuk menentukan posisi awal, kecepatan, dan atribut mobil ketika objek dibuat. Method digunakan untuk menggerakkan mobil, mengubah kecepatan, dan memperbarui posisi kendaraan.

H. Kesimpulan

Constructor digunakan untuk menginisialisasi objek ketika dibuat, sedangkan method digunakan untuk menjalankan tindakan tertentu pada objek.