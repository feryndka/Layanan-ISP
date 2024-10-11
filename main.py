def transfer_pulsa():
    saldo_pengguna = 100000  # Default saldo untuk contoh

    # Menampilkan menu utama
    print("Layanan *858#")
    print("1. Transfer Pulsa")
    print("2. Cek Pulsa")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        # Meminta nomor penerima
        nomor_penerima = input("Masukkan nomor penerima: ")

        # Validasi nomor penerima
        if len(nomor_penerima) < 10 or len(nomor_penerima) > 12:
            print("Nomor tidak valid!")
            return

        # Meminta nominal jumlah pulsa
        jumlah_pulsa = int(input("Masukkan jumlah pulsa: "))

        # Cek saldo pengguna
        if jumlah_pulsa > saldo_pengguna:
            print("Saldo tidak cukup!")
            return

        # Konfirmasi transfer
        print(f"Anda akan mengirim pulsa sebesar Rp.{jumlah_pulsa},00 ke {nomor_penerima}")
        konfirmasi = input("Apakah Anda yakin? (Ya/Tidak): ")

        if konfirmasi.lower() == "ya":
            # Proses transfer pulsa
            saldo_pengguna -= jumlah_pulsa
            print("Transfer berhasil!")
            print(f"Sisa saldo Anda: Rp.{saldo_pengguna},00")
        else:
            print("Transfer dibatalkan.")
    
    elif pilihan == "2":
        print(f"Pulsa anda sebesar Rp.{saldo_pengguna},00")
    
    else:
        print("Pilihan tidak valid!")

# Menjalankan fungsi transfer pulsa
transfer_pulsa()