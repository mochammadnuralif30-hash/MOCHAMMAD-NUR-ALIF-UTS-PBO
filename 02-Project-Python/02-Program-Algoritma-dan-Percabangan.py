Program Algoritma dan Percabangan Python

UTS Pemrograman Berorientasi Objek

print("================================")
print("       PROGRAM NILAI MAHASISWA")
print("================================")

nama = input("Masukkan Nama Mahasiswa: ")

nilai_tugas = float(input("Masukkan Nilai Tugas: "))
nilai_uts = float(input("Masukkan Nilai UTS: "))
nilai_uas = float(input("Masukkan Nilai UAS: "))

Menghitung nilai akhir

nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.3) + (nilai_uas * 0.4)

Menentukan grade menggunakan percabangan

if nilai_akhir >= 85:
grade = "A"
keterangan = "Sangat Baik"
elif nilai_akhir >= 75:
grade = "B"
keterangan = "Baik"
elif nilai_akhir >= 65:
grade = "C"
keterangan = "Cukup"
elif nilai_akhir >= 50:
grade = "D"
keterangan = "Kurang"
else:
grade = "E"
keterangan = "Tidak Lulus"

Menampilkan hasil

print("\n================================")
print("          HASIL NILAI")
print("================================")
print("Nama         :", nama)
print("Nilai Tugas  :", nilai_tugas)
print("Nilai UTS    :", nilai_uts)
print("Nilai UAS    :", nilai_uas)
print("Nilai Akhir  :", round(nilai_akhir, 2))
print("Grade        :", grade)
print("Keterangan   :", keterangan)
print("================================")