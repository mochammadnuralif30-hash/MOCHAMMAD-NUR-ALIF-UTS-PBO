18. Module dan Package Python

A. Pengertian Module

Module adalah file Python yang berisi kode seperti fungsi, variabel, dan class yang dapat digunakan kembali dalam program lain.

Module membantu programmer agar kode lebih terorganisir dan tidak perlu menulis ulang kode yang sama.

B. Contoh Penggunaan Module

Python menyediakan module bawaan seperti "math" dan "random".

import math

hasil = math.sqrt(25)

print("Akar dari 25 adalah:", hasil)

Penjelasan:

- "import math" digunakan untuk memanggil module math.
- "math.sqrt()" digunakan untuk menghitung akar kuadrat.
- Hasil dari akar kuadrat 25 adalah 5.

C. Pengertian Package

Package adalah kumpulan beberapa module Python yang disusun dalam sebuah folder agar kode lebih mudah dikelola.

Package membantu mengelompokkan program berdasarkan fungsi atau kegunaannya.

D. Contoh Struktur Package

project/
│
├── main.py
│
└── kendaraan/
    ├── __init__.py
    ├── mobil.py
    └── motor.py

E. Contoh Penggunaan Package

Isi file "mobil.py":

def berjalan():
    print("Mobil sedang berjalan")

Isi file "main.py":

from kendaraan.mobil import berjalan

berjalan()

Output:

Mobil sedang berjalan

F. Perbedaan Module dan Package

1. Module merupakan satu file Python yang berisi kode program.
2. Package merupakan folder yang mengelompokkan beberapa module.
3. Module digunakan untuk menyimpan kode tertentu.
4. Package digunakan untuk mengatur kode dalam proyek yang lebih besar.

G. Manfaat Module dan Package

1. Membuat kode lebih rapi dan terstruktur.
2. Memudahkan penggunaan kembali kode.
3. Mempermudah pengembangan program.
4. Memudahkan pemeliharaan proyek.

H. Penerapan dalam Game Balapan Mobil

Module dapat digunakan untuk memisahkan kode game, seperti pengaturan mobil, koin, skor, dan menu permainan.

Package dapat digunakan untuk mengelompokkan module tersebut agar proyek game lebih teratur dan mudah dikembangkan.

Kesimpulan

Module adalah file Python yang berisi kode yang dapat digunakan kembali, sedangkan Package adalah kumpulan module dalam sebuah folder. Keduanya membantu membuat program lebih rapi, terstruktur, dan mudah dikembangkan.