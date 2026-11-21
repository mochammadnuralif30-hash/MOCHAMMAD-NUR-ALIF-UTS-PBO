Program OOP Mahasiswa

UTS Pemrograman Berorientasi Objek

class Mahasiswa:

# Constructor
def __init__(self, nama, nim, program_studi):
    self.nama = nama
    self.nim = nim
    self.program_studi = program_studi
    self.nilai = []

# Method untuk menambahkan nilai
def tambah_nilai(self, nilai):
    self.nilai.append(nilai)

# Method menghitung rata-rata
def hitung_rata_rata(self):
    if len(self.nilai) == 0:
        return 0

    return sum(self.nilai) / len(self.nilai)

# Method menampilkan data mahasiswa
def tampilkan_data(self):
    print("\n================================")
    print("       DATA MAHASISWA")
    print("================================")
    print("Nama          :", self.nama)
    print("NIM           :", self.nim)
    print("Program Studi :", self.program_studi)
    print("Daftar Nilai  :", self.nilai)
    print("Rata-rata     :", round(self.hitung_rata_rata(), 2))

    if self.hitung_rata_rata() >= 75:
        print("Status        : LULUS")
    else:
        print("Status        : BELUM LULUS")

    print("================================")

Membuat objek mahasiswa

print("PROGRAM DATA MAHASISWA")

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
program_studi = input("Masukkan Program Studi: ")

mahasiswa = Mahasiswa(nama, nim, program_studi)

Input nilai

jumlah = int(input("Masukkan jumlah nilai: "))

for i in range(jumlah):
nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
mahasiswa.tambah_nilai(nilai)

Menampilkan data

mahasiswa.tampilkan_data()