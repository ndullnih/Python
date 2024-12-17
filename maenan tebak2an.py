import time

def mulai_permainan():
    print("Selamat datang di dunia petualangan misterius!")
    print("Anda adalah seorang petualang yang sedang mencari harta karun kuno.")
    time.sleep(2)
    print("Anda berdiri di depan sebuah gua gelap yang tersembunyi di hutan belantara.")
    time.sleep(2)
    pilihan_masuk_gua()

def pilihan_masuk_gua():
    print("\nApakah Anda ingin masuk ke dalam gua?")
    print("1. Masuk ke dalam gua.")
    print("2. Berbalik dan pergi.")
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

    if pilihan == "1":
        time.sleep(1)
        print("\nAnda memutuskan untuk masuk ke dalam gua. Anda melangkah perlahan, mendengar suara tetesan air dan langkah kaki Anda sendiri.")
        time.sleep(2)
        ruangan_pertama()
    elif pilihan == "2":
        time.sleep(1)
        print("\nAnda memutuskan untuk tidak mengambil risiko dan kembali ke desa. Permainan selesai.")
    else:
        print("Pilihan tidak valid! Coba lagi.")
        pilihan_masuk_gua()

def ruangan_pertama():
    print("\nAnda menemukan sebuah ruangan dengan dua pintu.")
    print("1. Buka pintu kiri.")
    print("2. Buka pintu kanan.")
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

    if pilihan == "1":
        time.sleep(1)
        print("\nAnda membuka pintu kiri dan menemukan sebuah peti harta karun!")
        time.sleep(2)
        peti_harta_karun()
    elif pilihan == "2":
        time.sleep(1)
        print("\nAnda membuka pintu kanan dan menemukan seekor naga yang sedang tidur.")
        time.sleep(2)
        bertemu_naga()
    else:
        print("Pilihan tidak valid! Coba lagi.")
        ruangan_pertama()

def peti_harta_karun():
    print("\nAnda melihat peti harta karun yang terkunci.")
    print("1. Coba buka peti dengan paksa.")
    print("2. Cari kunci di sekitar ruangan.")
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

    if pilihan == "1":
        time.sleep(1)
        print("\nAnda mencoba membuka peti dengan paksa, tetapi tiba-tiba perangkap aktif! Anda terperangkap dalam jaring!")
        print("Permainan selesai.")
    elif pilihan == "2":
        time.sleep(1)
        print("\nAnda mencari di sekitar ruangan dan menemukan kunci di bawah batu. Anda membuka peti dan menemukan harta karun emas!")
        print("Selamat, Anda berhasil menemukan harta karun kuno!")
    else:
        print("Pilihan tidak valid! Coba lagi.")
        peti_harta_karun()

def bertemu_naga():
    print("\nNaga membuka mata dan menatap Anda!")
    print("1. Coba berbicara dengan naga.")
    print("2. Lari ke luar gua.")
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")

    if pilihan == "1":
        time.sleep(1)
        print("\nAnda dengan hati-hati berbicara dengan naga dan ternyata naga itu tidak bermusuhan.")
        time.sleep(2)
        print("Naga menawarkan Anda sekeping emas sebagai tanda persahabatan dan mengizinkan Anda pergi.")
        print("Anda keluar dari gua dengan selamat dan membawa sekeping emas sebagai kenang-kenangan.")
        print("Petualangan Anda selesai dengan damai.")
    elif pilihan == "2":
        time.sleep(1)
        print("\nAnda berlari sekuat tenaga, meninggalkan gua dan berhasil lolos dari pandangan naga.")
        print("Anda selamat, tetapi tanpa membawa harta.")
    else:
        print("Pilihan tidak valid! Coba lagi.")
        bertemu_naga()

# Memulai permainan
mulai_permainan()
