# Simulasi Layanan *858# - Transfer Pulsa

Program ini adalah simulasi layanan *858# yang memungkinkan pengguna untuk melakukan transfer pulsa atau mengecek saldo pulsa mereka. Program ini menerima input dari pengguna untuk memilih opsi layanan yang diinginkan, seperti **Transfer Pulsa** atau **Cek Pulsa**, dan memprosesnya sesuai dengan logika yang telah ditentukan.

## Fitur Utama

1. **Transfer Pulsa**
   - Pengguna dapat memasukkan nomor tujuan penerima pulsa.
   - Program memvalidasi nomor penerima (panjang karakter 10-12 digit).
   - Pengguna diminta untuk memasukkan jumlah pulsa yang ingin dikirim.
   - Program memeriksa apakah saldo pengguna cukup untuk melakukan transfer.
   - Jika saldo cukup, pengguna diminta untuk mengonfirmasi transfer pulsa.
   - Jika konfirmasi diterima, pulsa dikurangi dari saldo pengguna dan transfer berhasil dilakukan.

2. **Cek Pulsa**
   - Pengguna dapat memilih opsi untuk mengecek saldo pulsa mereka.
   - Program menampilkan sisa pulsa pengguna saat ini.