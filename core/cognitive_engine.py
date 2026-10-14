# ==========================================
# FILE: core/cognitive_engine.py
# FUNGSI: Otak Analisis Teks & Penilai Niat Beli (High-Intent Sniper)
# ==========================================

import re

class CognitiveEngine:
    def __init__(self):
        # Kata-kata sakti yang menandakan seseorang siap mengeluarkan uang
        self.buying_triggers = [
            "beli dimana", "ada yang tau", "rekomendasi dong", "linknya",
            "spill dong", "spill link", "cari yang murah", "diskonan",
            "pengen beli", "butuh banget", "rusak", "promo shopee food"
        ]
        
        # Kata-kata negatif yang menandakan orang hanya mengeluh/spam (buang)
        self.negative_triggers = [
            "jualan", "cek dm", "open bo", "pinjol", "penipuan",
            "giveaway", "retweet", "rt dan like", "scam"
        ]

    def clean_text(self, raw_text):
        """
        Membersihkan teks dari karakter aneh, emoji berlebihan, 
        atau format yang mengganggu proses analisis otak.
        """
        # Hapus URL yang sudah ada (kita tidak mau membalas orang yang sudah sebar link)
        cleaned = re.sub(r'http\S+', '', raw_text)
        # Hapus mention (@username)
        cleaned = re.sub(r'@\w+', '', cleaned)
        # Hapus spasi berlebih
        cleaned = " ".join(cleaned.split())
        return cleaned.lower()

    def calculate_intent_score(self, text_content, keyword):
        """
        Menilai seberapa "matang" sebuah prospek.
        Mengembalikan nilai 0 sampai 100. Semakin tinggi, semakin siap beli.
        """
        text_lower = self.clean_text(text_content)
        kw_lower = keyword.lower()
        score = 0

        # FILTER 1: Deteksi Sampah (Langsung buang jika ada kata negatif)
        if any(neg in text_lower for neg in self.negative_triggers):
            return 0  # Skor 0, langsung lupakan.

        # FILTER 2: Kedekatan Kata Kunci Utama (+40 Poin)
        if any(k in text_lower for k in kw_lower.split()):
            score += 40
            
            # Jika kata kuncinya persis berurutan (misal: "powerbank fast charging")
            if kw_lower in text_lower:
                score += 20 

        # FILTER 3: Pemicu Niat Beli / Buying Triggers (+15 poin per pemicu)
        for trigger in self.buying_triggers:
            if trigger in text_lower:
                score += 15

        # FILTER 4: Urgensi Panjang Karakter
        # Orang yang serius butuh barang biasanya mengetik agak panjang (bukan sekadar "tes")
        if 20 <= len(text_lower) <= 200:
            score += 10

        # Batasi maksimal skor di angka 99 agar matematisnya stabil
        final_score = min(score, 99)
        return final_score

    def is_target_worthy(self, text_content, keyword):
        """
        Fungsi penentu eksekusi.
        Hanya akan menyetujui penargetan jika skor mencapai 65 atau lebih.
        """
        score = self.calculate_intent_score(text_content, keyword)
        if score >= 65:
            print(f"🎯 [Cognitive Engine] TARGET TERKUNCI! Skor: {score}% | Teks: '{text_content[:30]}...'")
            return True
        else:
            return False

# ==========================================
# (Opsional) Blok pengujian internal
# ==========================================
if __name__ == "__main__":
    engine = CognitiveEngine()
    test_tweet = "Aduh powerbank aku rusak nih, ada yang punya rekomendasi powerbank fast charging yang awet ga ya? Spill link dong!"
    print("Menganalisis contoh teks...")
    engine.is_target_worthy(test_tweet, "Powerbank Fast Charging")
