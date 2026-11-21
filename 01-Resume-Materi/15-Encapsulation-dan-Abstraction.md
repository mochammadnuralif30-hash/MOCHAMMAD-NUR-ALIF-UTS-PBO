15. Encapsulation dan Abstraction

A. Encapsulation (Enkapsulasi)

Encapsulation adalah konsep OOP yang digunakan untuk melindungi data di dalam class agar tidak dapat diakses atau diubah secara langsung dari luar class.

Encapsulation membantu menjaga keamanan dan keteraturan data.

Contoh Kode:

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.__nilai = nilai

    def tampilkan_nilai(self):
        print("Nilai:", self.__nilai)

mhs = Mahasiswa("Alif", 90)
mhs.tampilkan_nilai()

Penjelasan:

- "Mahasiswa" merupakan nama class.
- "nama" adalah atribut yang dapat diakses secara langsung.
- "__nilai" merupakan atribut private yang penggunaannya dibatasi.
- "tampilkan_nilai()" digunakan untuk menampilkan nilai mahasiswa.

B. Abstraction (Abstraksi)

Abstraction adalah konsep OOP yang menyembunyikan detail proses di dalam program dan hanya menampilkan bagian penting yang perlu digunakan.

Contoh Kode:

from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def berjalan(self):
        pass

class Mobil(Kendaraan):
    def berjalan(self):
        print("Mobil sedang berjalan")

mobil = Mobil()
mobil.berjalan()

Penjelasan:

- "ABC" digunakan untuk membuat class abstrak.
- "abstractmethod" digunakan untuk membuat method abstrak.
- Class "Mobil" harus membuat implementasi method "berjalan()".
- Pengguna cukup menjalankan method tanpa perlu mengetahui seluruh detail prosesnya.

C. Manfaat Encapsulation dan Abstraction

1. Melindungi data agar tidak mudah diubah sembarangan.
2. Menyembunyikan proses yang tidak perlu diketahui pengguna.
3. Membuat program lebih aman dan terstruktur.
4. Mempermudah pemeliharaan dan pengembangan program.

D. Penerapan dalam Game Balapan Mobil

Encapsulation dapat digunakan untuk melindungi data seperti skor dan nyawa pemain agar tidak diubah secara sembarangan.

Abstraction dapat digunakan dengan menyediakan method seperti "mulai_game()" atau "hitung_skor()" sehingga pengguna cukup memanggil method tersebut tanpa mengetahui seluruh proses di dalamnya.

Kesimpulan

Encapsulation digunakan untuk melindungi data dalam class, sedangkan Abstraction digunakan untuk menyembunyikan detail proses dan menampilkan fungsi yang penting. Keduanya membantu membuat program lebih aman, rapi, dan mudah dikembangkan.