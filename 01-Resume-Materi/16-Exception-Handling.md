16. Exception Handling (Penanganan Kesalahan)

A. Pengertian Exception Handling

Exception Handling adalah proses menangani kesalahan yang terjadi saat program dijalankan agar program tidak langsung berhenti secara tiba-tiba.

Dalam Python, Exception Handling menggunakan beberapa perintah, yaitu "try", "except", "else", dan "finally".

B. Fungsi Perintah Exception Handling

1. "try": Menjalankan kode yang berpotensi menimbulkan kesalahan.
2. "except": Menangani kesalahan yang terjadi.
3. "else": Menjalankan kode jika tidak terjadi kesalahan.
4. "finally": Menjalankan kode pada akhir proses, baik terjadi kesalahan maupun tidak.

C. Contoh Kode

try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))

    hasil = angka1 / angka2

except ValueError:
    print("Input harus berupa angka!")

except ZeroDivisionError:
    print("Angka tidak boleh dibagi dengan nol!")

else:
    print("Hasil:", hasil)

finally:
    print("Program selesai.")

D. Penjelasan Kode

- Program meminta pengguna memasukkan dua angka.
- "try" menjalankan proses pembagian.
- "except ValueError" menangani input yang bukan angka.
- "except ZeroDivisionError" menangani pembagian dengan nol.
- "else" menampilkan hasil jika tidak ada kesalahan.
- "finally" menampilkan pesan bahwa program telah selesai.

E. Manfaat Exception Handling

1. Mencegah program berhenti secara tiba-tiba.
2. Membantu menemukan dan menangani kesalahan.
3. Membuat program lebih aman dan stabil.
4. Memberikan pesan kesalahan yang mudah dipahami pengguna.

F. Penerapan dalam Game Balapan Mobil

Exception Handling dapat digunakan untuk menangani kesalahan saat membaca file pengaturan game, memuat data pemain, atau menerima input tertentu.

Dengan begitu, game dapat memberikan pesan kesalahan yang jelas dan menghindari program berhenti secara mendadak.

Kesimpulan

Exception Handling merupakan cara menangani kesalahan saat program berjalan. Dengan menggunakan "try", "except", "else", dan "finally", program Python menjadi lebih aman, stabil, dan mudah digunakan.