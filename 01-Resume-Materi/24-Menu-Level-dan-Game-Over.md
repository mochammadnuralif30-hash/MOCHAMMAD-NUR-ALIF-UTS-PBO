24. Menu, Level, dan Game Over pada Pygame

A. Pengertian Menu Game

Menu Game adalah tampilan awal permainan yang digunakan untuk memberikan pilihan kepada pemain sebelum memulai permainan.

Contoh menu dalam game:

1. Start Game: Memulai permainan.
2. Difficulty: Memilih tingkat kesulitan.
3. Settings: Mengatur permainan.
4. Exit: Keluar dari permainan.

B. Pengertian Level Game

Level adalah tingkatan kesulitan dalam permainan yang menentukan seberapa besar tantangan yang harus dihadapi pemain.

Contoh tingkat kesulitan:

- Easy: Tingkat mudah dengan kecepatan rendah.
- Medium: Tingkat sedang dengan kecepatan lebih tinggi.
- Hard: Tingkat sulit dengan kecepatan dan tantangan lebih besar.

C. Pengertian Game Over

Game Over adalah kondisi ketika permainan berakhir karena pemain gagal menyelesaikan tantangan atau mengalami kekalahan.

Dalam game balapan mobil, Game Over dapat terjadi ketika mobil pemain bertabrakan dengan mobil musuh.

D. Contoh Kode Menu dan Kondisi Game Over

import pygame

pygame.init()

layar = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Game Balapan")

font = pygame.font.Font(None, 50)

menu = True
game_over = False
berjalan = True

while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False

            if event.key == pygame.K_r:
                game_over = False
                menu = False

    layar.fill((30, 30, 30))

    if menu:
        teks = font.render("START GAME", True, (255, 255, 255))
        layar.blit(teks, (140, 170))

    elif game_over:
        teks = font.render("GAME OVER", True, (255, 0, 0))
        layar.blit(teks, (140, 170))

    else:
        teks = font.render("PLAYING", True, (0, 255, 0))
        layar.blit(teks, (170, 170))

    pygame.display.update()

pygame.quit()

E. Penjelasan Kode

- "menu = True" menentukan kondisi awal permainan berada di menu.
- "game_over = False" menentukan permainan belum berakhir.
- "pygame.K_SPACE" digunakan untuk memulai permainan.
- "pygame.K_r" digunakan untuk mengatur ulang kondisi permainan.
- "font.render()" digunakan untuk membuat teks.
- "layar.blit()" digunakan untuk menampilkan teks pada layar.

F. Manfaat Menu, Level, dan Game Over

1. Memudahkan pemain memulai permainan.
2. Memberikan pilihan tingkat kesulitan.
3. Membuat permainan lebih terstruktur.
4. Memberikan informasi ketika permainan berakhir.
5. Memberikan kesempatan pemain untuk bermain kembali.

G. Penerapan dalam Game Balapan Mobil

Pada Game Balapan Mobil, menu digunakan untuk menampilkan tombol Start, pilihan Easy, Medium, dan Hard, serta tombol Exit.

Level digunakan untuk mengatur kecepatan mobil musuh dan tingkat tantangan. Game Over ditampilkan ketika mobil pemain mengalami tabrakan dengan mobil musuh.

Pemain juga dapat memilih untuk bermain kembali atau kembali ke menu utama.

Kesimpulan

Menu, Level, dan Game Over merupakan bagian penting dalam pembuatan game. Menu memberikan pilihan kepada pemain, Level mengatur tingkat kesulitan, sedangkan Game Over menunjukkan bahwa permainan telah berakhir.