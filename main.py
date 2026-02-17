import time
import random

# helper to print with dramatic pause
def print_slow(text: str, delay: float = 0.5):
    """Print each line of `text` then wait `delay` seconds."""
    for line in text.split("\n"):
        print(line)
        time.sleep(delay)


# ascii art for outcomes
def show_outcome(victory: bool):
    if victory:
        art = r"""
          /| ________________
O|===|* >________________>
          \|
"""
        print_slow(art, delay=0.1)
        print_slow("Kamu berhasil! Pedang kemenangan muncul di tanganmu.")
    else:
        art = r"""
             .-.
            (o o)
            | O \
             \   \
              `~~~' 
        """
        print_slow(art, delay=0.1)
        print_slow("Sayang! Sebuah tengkorak muncul... Nyawamu berkurang.")



def game_utama():
    print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")
    nyawa = 100
    print_slow(f"Selamat datang, {nama}! Nyawamu: {nyawa}")
    time.sleep(1)

    # loop permainan agar bisa diulang
    while True:
        print_slow("Di hadapanmu terbentang dua jalur misterius:")
        print_slow("1. Lembah Coding - tempat di mana kode mengalir seperti sungai.")
        print_slow("2. Gunung Bug - puncak penuh tantangan dan kesalahan tak terduga.")
        pilihan = input("Pilih jalurmu (1 atau 2): ")

        if pilihan == '1':
            print_slow("Kamu memasuki Lembah Coding. Baris demi baris kode menyapa.")
            # keberuntungan: peluang 60% berhasil
            if random.random() < 0.6:
                show_outcome(True)
            else:
                nyawa -= 30
                show_outcome(False)
        elif pilihan == '2':
            print_slow("Kamu menapaki Gunung Bug. Setiap langkah terasa seperti debugging.")
            # jalur yang sulit, peluang menang 40%
            if random.random() < 0.4:
                show_outcome(True)
            else:
                nyawa -= 30
                show_outcome(False)
        else:
            nyawa -= 20
            print_slow(f"Pilihan tidak dikenal! Nyawamu berkurang menjadi {nyawa}.")

        # cek nyawa
        if nyawa <= 0:
            print_slow("Nyawamu habis! Permainan berakhir.")
            break

        # tanya ulang
        lagi = input("Main lagi? (y/n): ").strip().lower()
        if lagi != 'y':
            print_slow("Terima kasih sudah bermain! Sampai jumpa.")
            break
    
if __name__ == "__main__":
    game_utama()