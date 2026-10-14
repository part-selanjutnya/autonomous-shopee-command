# ==========================================
# FILE: core/entropy_shield.py
# FUNGSI: Perisai Anti-Deteksi & Manipulasi Waktu (Humanizer)
# ==========================================

import time
import random

class EntropyShield:
    def __init__(self):
        # Kumpulan topeng identitas browser (User-Agents)
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        ]

    def get_random_header(self):
        """
        Menghasilkan HTTP Header palsu agar sistem terlihat seperti 
        manusia normal yang berselancar menggunakan browser biasa.
        """
        header = {
            "User-Agent": random.choice(self.user_agents),
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive"
        }
        return header

    def randomize_delay(self, min_seconds, max_seconds):
        """
        Menjeda eksekusi sistem dengan waktu acak (Jitter).
        Fungsi ini membuat jeda menjadi sangat acak (misal: 17.82 detik).
        """
        # Tambahkan desimal acak (noise) agar tidak pernah bulat
        noise = random.uniform(0.1, 3.5) 
        delay = random.randint(min_seconds, max_seconds) + noise
        
        print(f"🛡️ [Entropy Shield] Mengaktifkan kamuflase jeda waktu selama {delay:.2f} detik...")
        time.sleep(delay)

# ==========================================
# (Opsional) Blok pengujian internal
# ==========================================
if __name__ == "__main__":
    shield = EntropyShield()
    print("Mengambil identitas palsu...")
    print(shield.get_random_header())
    print("\nMenguji jeda acak (3-5 detik)...")
    shield.randomize_delay(3, 5)
    print("Pengujian Entropy Shield berhasil!")
