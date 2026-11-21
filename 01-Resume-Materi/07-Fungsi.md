7. FUNGSI (FUNCTION) PYTHON

A. Pengertian Fungsi

Function atau fungsi adalah sekumpulan kode program yang dibuat untuk menjalankan tugas tertentu. Fungsi digunakan agar kode lebih terstruktur, mudah digunakan kembali, dan tidak perlu menulis perintah yang sama berulang kali.

B. Jenis-Jenis Fungsi

1. Built-in Function: Fungsi bawaan Python, seperti print(), input(), len(), dan type().
2. User Defined Function: Fungsi yang dibuat sendiri oleh programmer menggunakan def.

C. Cara Membuat Fungsi

Fungsi dibuat menggunakan kata kunci def, diikuti nama fungsi dan tanda kurung.

D. Contoh Fungsi Sederhana

def salam():
    print("Selamat Belajar Python")

salam()

E. Fungsi dengan Parameter

Parameter digunakan untuk menerima nilai yang diberikan kepada fungsi.

def perkenalan(nama):
    print("Nama saya", nama)

perkenalan("Alif")

F. Fungsi dengan Return

Return digunakan untuk mengembalikan hasil dari suatu fungsi.

def tambah(a, b):
    return a + b

hasil = tambah(10, 5)
print("Hasil:", hasil)

G. Manfaat Fungsi

1. Mengurangi pengulangan kode.
2. Mempermudah pemeliharaan program.
3. Membuat kode lebih terstruktur.
4. Mempermudah penggunaan kembali kode.

H. Kesimpulan

Fungsi merupakan bagian penting dalam Python untuk mengelompokkan perintah berdasarkan tugas tertentu. Dengan fungsi, program menjadi lebih rapi, terstruktur, dan mudah dikembangkan.