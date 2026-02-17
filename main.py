import time
import random

# ==============================
# VARIABEL GLOBAL
# ==============================
nyawa_awal = 100
nyawa = nyawa_awal

# ==============================
# FUNGSI TAMPILAN TEKS
# ==============================
def dramatic_print(text):
    print(text)
    time.sleep(0.5)

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    time.sleep(0.5)

# ==============================
# ASCII ART
# ==============================
pedang_ascii = r"""
       />------------------------------------>
"""

tengkorak_ascii = r"""
     _____
   .-"     "-.
  /           \
 |  X       X  |
 |     ___     |
  \  (_____)  /
   '-._____.-'
"""

# ==============================
# SISTEM NYAWA
# ==============================
def kurangi_nyawa(jumlah):
    global nyawa
    nyawa -= jumlah
    dramatic_print(f"\n⚠️ Kamu kehilangan {jumlah} nyawa!")
    dramatic_print(f"❤️ Sisa nyawa: {nyawa}\n")

    if nyawa <= 0:
        dramatic_print("\n--- KAMU TUMBANG ---")
        print(tengkorak_ascii)
        dramatic_print("Simulasi berakhir.\n")
        raise SystemExit

# ==============================
# ALUR GAME
# ==============================
def game_utama():
    global nyawa
    nyawa = nyawa_awal  # reset nyawa

    dramatic_print("\n--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")

    slow_print(f"\nSelamat datang, {nama}. Dunia Algoria sedang menunggumu...")

    dramatic_print("\nKamu terbangun di sebuah ruangan bercahaya biru.")
    dramatic_print("Di depanmu ada dua jalur holografis:")
    dramatic_print("1. Jalur Pengetahuan — penuh simbol ungu berputar.")
    dramatic_print("2. Jalur Keberanian — terdengar langkah aneh di dalamnya.")

    pilihan = input("\nPilih jalur (1/2): ")

    if pilihan == "1":
        jalur_pengetahuan(nama)
    elif pilihan == "2":
        jalur_keberanian(nama)
    else:
        dramatic_print("Sistem mendeteksi pilihan yang buruk.")
        kurangi_nyawa(20)

# ==============================
# JALUR 1
# ==============================
def jalur_pengetahuan(nama):
    dramatic_print("\nKamu memasuki Jalur Pengetahuan...")
    dramatic_print("Simbol holografis berputar mengelilingimu.")
    dramatic_print("Sebuah buku digital melayang pelan.")

    dramatic_print("\nApa yang kamu lakukan?")
    dramatic_print("1. Sentuh buku itu.")
    dramatic_print("2. Abaikan.")

    pilih = input("Pilih (1/2): ")

    if pilih == "1":
        hasil = random.choice(["baik", "buruk"])  # elemen keberuntungan

        if hasil == "baik":
            dramatic_print("\nBuku itu bersinar terang!")
            dramatic_print("Kamu mendapatkan pengetahuan rahasia Algoria!")
            print(pedang_ascii)
            dramatic_print("KEMENANGAN KECIL: Kamu memperoleh pedang data!")
        else:
            dramatic_print("\nBuku itu tiba-tiba meledak menjadi cahaya!")
            dramatic_print("Energi tak stabil mengenai tubuhmu.")
            kurangi_nyawa(20)

    elif pilih == "2":
        dramatic_print("\nKamu berjalan melewati buku itu...")
        dramatic_print("Tapi lantai holografis runtuh!")
        kurangi_nyawa(20)
    else:
        dramatic_print("Pilihan tidak dikenali.")
        kurangi_nyawa(20)

# ======
