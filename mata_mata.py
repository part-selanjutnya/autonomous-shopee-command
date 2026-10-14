# ==========================================
# FILE: mata_mata.py (Posisi: Root Directory / Luar folder core)
# FUNGSI: Master Orchestrator (Jenderal Penggerak Seluruh Sistem)
# ==========================================

from core.config_matrix import AffiliateConfig
from core.cognitive_engine import CognitiveEngine
from core.entropy_shield import EntropyShield
from core.auto_link_transformer import LinkTransformer
from core.genesis_protocol import GenesisProtocol

def main_execution():
    print("==================================================")
    print("🚀 [SYSTEM BOOT] AUTONOMOUS SHOPEE COMMAND CENTER")
    print("==================================================")

    # 1. Panggilan Pasukan Khusus (Inisialisasi)
    shield = EntropyShield()
    genesis = GenesisProtocol()
    cognitive = CognitiveEngine()
    transformer = LinkTransformer()

    # 2. Cek Fase Operasi Hari Ini (Genesis Protocol)
    # Ini akan membaca tanggal lahir 2026-10-15 dan mencocokkannya dengan hari ini
    current_strategy = genesis.evaluate_system_phase()
    
    # 3. Muat Senjata Jala Lebar (Config Matrix)
    targets = AffiliateConfig.TARGET_NICHES
    print(f"📡 Mengaktifkan {len(targets)} Radar Target dari Config Matrix...")
    
    # 4. Eksekusi Pencarian Target di Awan
    print("\n[Mulai Pemindaian Otonom Lintas Platform...]\n")
    
    # --- SIMULASI KASUS 1: MENEMUKAN SPAMMER ---
    simulated_text_1 = "Cek DM kak, pinjol cair cepat tanpa ribet klik di sini penipuan aman!"
    print(f"👀 Radar menangkap sinyal: '{simulated_text_1}'")
    shield.randomize_delay(1, 3) # Gunakan perisai jeda acak
    
    if cognitive.is_target_worthy(simulated_text_1, targets[0]):
        pass
    else:
        print("❌ [Skip] Sistem membuang prospek ini. Terdeteksi sebagai spam / kualitas rendah.\n")

    # --- SIMULASI KASUS 2: MENEMUKAN PEMBELI POTENSIAL (HIGH-INTENT) ---
    simulated_text_2 = "Aduh cuaca panas banget di kosan, pengen beli kipas angin portable yang awet. Spill link dong yg murah!"
    target_keyword = "Kipas Angin Portable"
    
    print(f"👀 Radar menangkap sinyal: '{simulated_text_2}'")
    shield.randomize_delay(2, 5) # Jeda natural seperti manusia membaca cuitan
    
    # Otak menganalisis teks
    if cognitive.is_target_worthy(simulated_text_2, target_keyword):
        print("✅ [TINDAKAN] Target High-Intent Terkunci! Menyusun draf serangan...")
        
        # Pabrik merakit link dengan ID afiliasi Anda
        raw_url = "https://shopee.co.id/Kipas-Angin-Portable-USB-Mini" 
        final_link = transformer.create_affiliate_link(raw_url, "X_Twitter")
        
        print(f"📝 DRAF PENAWARAN OTOMATIS DIBUAT:")
        print(f"   'Halo kak! Kipas angin portable yang ini kenceng banget dan kebetulan lagi promo. Cek aja langsung: {final_link}'\n")

    print("==================================================")
    print("🏁 [SIKLUS SELESAI] Karyawan Digital kembali ke mode Standby.")
    print("==================================================")

if __name__ == "__main__":
    main_execution()
