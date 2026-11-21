14. Inheritance dan Polymorphism

A. Inheritance (Pewarisan)

Inheritance adalah konsep dalam Object-Oriented Programming (OOP) yang memungkinkan sebuah class mewarisi atribut dan method dari class lain.

Class yang mewariskan disebut Parent Class, sedangkan class yang menerima warisan disebut Child Class.

Contoh Kode:

class Kendaraan:
    def berjalan(self):
        print("Kendaraan sedang berjalan")

class Mobil(Kendaraan):
    def klakson(self):
        print("Mobil berbunyi: Tin Tin!")

mobil = Mobil()
mobil.berjalan()
mobil.klakson()

Penjelasan:

- "Kendaraan" merupakan Parent Class.
- "Mobil" merupakan Child Class.
- Class "Mobil" dapat menggunakan method "berjalan()" dari class "Kendaraan".
- Class "Mobil" juga memiliki method sendiri, yaitu "klakson()".

B. Polymorphism

Polymorphism adalah konsep OOP yang memungkinkan method dengan nama yang sama memiliki perilaku atau hasil yang berbeda, tergantung objek yang menggunakannya.

Contoh Kode:

class Mobil:
    def suara(self):
        print("Mobil berbunyi: Tin Tin!")

class Motor:
    def suara(self):
        print("Motor berbunyi: Beep Beep!")

kendaraan1 = Mobil()
kendaraan2 = Motor()

kendaraan1.suara()
kendaraan2.suara()

Penjelasan:

- Class Mobil dan Motor memiliki method dengan nama yang sama, yaitu "suara()".
- Namun, hasil yang ditampilkan berbeda.
- Inilah yang disebut Polymorphism.

C. Manfaat Inheritance dan Polymorphism

1. Mengurangi penulisan kode yang berulang.
2. Memudahkan pengembangan program.
3. Membuat kode lebih terstruktur.
4. Memudahkan penggunaan method dengan berbagai perilaku.

D. Penerapan dalam Game Balapan Mobil

Inheritance dapat digunakan untuk membuat class dasar "Kendaraan", kemudian class "MobilPemain" dan "MobilMusuh" mewarisi atribut serta method dari class tersebut.

Polymorphism dapat digunakan ketika mobil pemain dan mobil musuh memiliki method yang sama, tetapi menjalankan perilaku yang berbeda.

Kesimpulan

Inheritance merupakan konsep pewarisan atribut dan method dari class lain, sedangkan Polymorphism memungkinkan method yang sama memiliki perilaku berbeda. Keduanya membantu membuat program Python lebih terstruktur dan mudah dikembangkan.