# ==========================================
# FILE: core/genesis_protocol.py
# FUNGSI: Akselerator Pembelajaran 7-Hari & Penentu Strategi Otomatis
# ==========================================

import datetime
from core.config_matrix import AffiliateConfig

class GenesisProtocol:
    def __init__(self):
        self.birth_date_str = AffiliateConfig.SYSTEM_BIRTH_DATE

    def evaluate_system_phase(self):
        """
        Menghitung usia sistem dan menentukan fase taktik harian.
        Sistem perlahan akan membuang 'sampah' dan menjadi lebih presisi.
        """
        # Konversi tanggal lahir string menjadi format kalender
        start_date = datetime.datetime.strptime(self.birth_date_str, "%Y-%m-%d").date()
        today = datetime.datetime.now().date()
        
        # Hitung umur sistem
        active_days = (today - start_date).days + 1
        
        print(f"\n🧬 [Genesis Protocol] Menganalisis Kalender Sistem...")
        print(f"⏳ Sistem beroperasi di: Hari Ke-{active_days}")
        
        # Penentuan Strategi Otonom
        if active_days <= 2:
            strategy = "PHASE_1_RECONNAISSANCE"
            desc = "Misi: Menyebar radar 'Jala Lebar' ke semua target (Volume Prioritas)."
        elif active_days <= 4:
            strategy = "PHASE_2_AB_TESTING"
            desc = "Misi: Rotasi gaya copywriting agresif. Mencari rasio klik tertinggi."
        elif active_days <= 6:
            strategy = "PHASE_3_LASER_FOCUS"
            desc = "Misi: Eliminasi kata kunci gagal. Fokus energi 100% pada target High-Intent."
        else:
            strategy = "PHASE_4_AUTONOMOUS_CRUISE"
            desc = "Misi: Kalibrasi Genesis selesai. Beroperasi dalam Mode Autopilot Otonom Penuh."
            
        print(f"⚙️ Kode Strategi Aktif: {strategy}")
        print(f"🎯 Eksekusi: {desc}\n")
        
        return strategy

# ==========================================
# Blok Pengujian Internal
# ==========================================
if __name__ == "__main__":
    genesis = GenesisProtocol()
    current_strategy = genesis.evaluate_system_phase()
