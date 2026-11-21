Program Perulangan dan Fungsi Python

UTS Pemrograman Berorientasi Objek

def hitung_total(nilai):
return sum(nilai)

def hitung_rata_rata(nilai):
return hitung_total(nilai) / len(nilai)

print("================================")
print("   PROGRAM PERHITUNGAN NILAI")
print("================================")

jumlah = int(input("Masukkan jumlah nilai: "))

daftar_nilai = []

for i in range(jumlah):
nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
daftar_nilai.append(nilai)

total = hitung_total(daftar_nilai)
rata_rata = hitung_rata_rata(daftar_nilai)

print("\n================================")
print("          HASIL NILAI")
print("================================")

for i, nilai in enumerate(daftar_nilai, start=1):
print(f"Nilai ke-{i}: {nilai}")

print("--------------------------------")
print("Jumlah Nilai :", jumlah)
print("Total Nilai  :", total)
print("Rata-rata    :", round(rata_rata, 2))
print("================================")

if rata_rata >= 75:
print("Keterangan: LULUS")
else:
print("Keterangan: TIDAK LULUS")

print("================================")