5. PERCABANGAN DALAM PYTHON

A. Pengertian Percabangan

Percabangan adalah struktur program yang digunakan untuk menentukan tindakan berdasarkan kondisi tertentu. Program akan menjalankan perintah sesuai dengan kondisi yang terpenuhi.

B. Jenis-Jenis Percabangan

1. If: Digunakan untuk menjalankan perintah jika kondisi bernilai benar.
2. If-Else: Digunakan untuk memilih antara dua kondisi.
3. If-Elif-Else: Digunakan untuk memeriksa beberapa kondisi.

C. Fungsi Percabangan

- Membuat keputusan dalam program.
- Memeriksa suatu kondisi.
- Menentukan perintah yang akan dijalankan.
- Membuat program lebih fleksibel.

D. Contoh Program Python

nilai = int(input("Masukkan nilai: "))

if nilai >= 80:
    print("Nilai A")
elif nilai >= 70:
    print("Nilai B")
elif nilai >= 60:
    print("Nilai C")
else:
    print("Nilai D")

E. Contoh Percabangan If-Else

umur = int(input("Masukkan umur: "))

if umur >= 17:
    print("Sudah dewasa")
else:
    print("Belum dewasa")

F. Kesimpulan

Percabangan digunakan untuk membuat keputusan berdasarkan kondisi. Dengan percabangan, program dapat menghasilkan tindakan atau keluaran yang berbeda sesuai dengan nilai yang diperiksa.