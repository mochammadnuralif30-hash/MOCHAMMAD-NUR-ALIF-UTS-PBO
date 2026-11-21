20. Event Handling dan Game Loop pada Pygame

A. Pengertian Event Handling

Event Handling adalah proses menangani kejadian atau input dari pengguna saat program berjalan.

Dalam Pygame, event handling digunakan untuk membaca tindakan pengguna, seperti menekan tombol keyboard, menggerakkan mouse, dan menutup jendela game.

B. Contoh Event pada Pygame

1. "pygame.QUIT": Menutup jendela permainan.
2. "pygame.KEYDOWN": Mendeteksi tombol keyboard yang ditekan.
3. "pygame.KEYUP": Mendeteksi tombol keyboard yang dilepaskan.
4. "pygame.MOUSEBUTTONDOWN": Mendeteksi klik tombol mouse.

C. Pengertian Game Loop

Game Loop adalah perulangan utama yang membuat permainan terus berjalan selama game belum dihentikan.

Game Loop digunakan untuk:

- Membaca input pemain.
- Memperbarui posisi objek.
- Memeriksa kondisi permainan.
- Menggambar ulang tampilan game.

D. Contoh Kode Event Handling dan Game Loop

import pygame

pygame.init()

layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Game Loop")

berjalan = True
clock = pygame.time.Clock()

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Tombol spasi ditekan!")

    layar.fill((30, 30, 30))
    pygame.display.update()

    clock.tick(60)

pygame.quit()

E. Penjelasan Kode

- "while berjalan" menjalankan game secara berulang.
- "pygame.event.get()" membaca event yang terjadi.
- "pygame.QUIT" digunakan untuk mendeteksi perintah menutup game.
- "pygame.KEYDOWN" mendeteksi tombol keyboard yang ditekan.
- "pygame.K_SPACE" mendeteksi tombol spasi.
- "pygame.display.update()" memperbarui tampilan.
- "clock.tick(60)" membatasi permainan hingga 60 frame per detik.

F. Penerapan dalam Game Balapan Mobil

Event Handling digunakan untuk mengatur pergerakan mobil pemain ketika tombol panah kiri dan kanan ditekan.

Game Loop digunakan untuk menjalankan seluruh proses permainan, seperti pergerakan mobil musuh, kemunculan koin, perhitungan skor, dan pemeriksaan tabrakan.

Kesimpulan

Event Handling digunakan untuk menangani input dan kejadian dalam game, sedangkan Game Loop merupakan perulangan utama yang menjaga permainan tetap berjalan dan memperbarui seluruh aktivitas game.