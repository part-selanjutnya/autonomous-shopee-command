# ==========================================
# FILE: core/config_matrix.py
# FUNGSI: Pusat Konfigurasi & Identitas Afiliasi (Mode: Jaring Raksasa)
# ==========================================

class AffiliateConfig:
    # 1. IDENTITAS AFILIASI
    # Terkoneksi langsung dengan akun (Username: hikado)
    SHOPEE_AFFILIATE_ID = "11315710905" 
    
    # 2. TARGET PASAR (NICHE) - "JALA LEBAR"
    # Merangkum kategori spesifik Anda dan berbagai kategori konversi tinggi.
    TARGET_NICHES = [
        # Niche Spesifik Akun (Kesehatan & Aksesoris Fashion)
        "Vitamin C Daya Tahan Tubuh", "Suplemen Kesehatan", "Alat Pijat Elektrik",
        "Jam Tangan Pria Anti Air", "Tas Selempang Wanita Estetik", "Kacamata Hitam Polarized", "Dompet Kulit",
        
        # Niche Shopee Food (Urgensi Harian Tinggi)
        "Voucher Shopee Food Diskon", "Promo Makan Siang Shopee", "Diskon Kopi Susu",
        
        # Niche Elektronik & Gadget (Komisi Menengah - Tinggi)
        "Powerbank Fast Charging", "TWS Bluetooth Earphone Earbuds", "Stand Laptop Ergonomis", 
        "Casing HP Anti Memar", "Smartwatch Murah", "Kabel Data Type C Fast Charging",
        
        # Niche Home Living & Lifestyle (Kebutuhan Harian - Konversi Mudah)
        "Kipas Angin Portable", "Botol Minum 2 Liter Viral", "Panci Elektrik Serbaguna",
        "Lampu Tidur Estetik LED", "Rak Sepatu Susun Minimalis",
        
        # Niche Skincare & Kecantikan (Pembelian Berulang / Repeat Order)
        "Sunscreen SPF 50 Murah", "Serum Jerawat Ampuh", "Lip Matte Tahan Lama"
    ]

    # 3. GENESIS PROTOCOL (Waktu Lahir Sistem)
    # Ditetapkan pada saat mesin utama mulai diaktifkan.
    SYSTEM_BIRTH_DATE = "2026-10-15" 

    # 4. PENGATURAN KEAMANAN (ENTROPY SHIELD)
    # Jeda waktu acak (dalam detik) agar Karyawan Digital tidak terdeteksi sebagai spam.
    MIN_DELAY = 15
    MAX_DELAY = 45

    @classmethod
    def get_tracking_format(cls, platform_name):
        """
        Menghasilkan struktur tautan pelacakan SubID otomatis.
        Contoh hasil: &subid=11315710905_Twitter
        """
        return f"&subid={cls.SHOPEE_AFFILIATE_ID}_{platform_name}"

print("✅ [Config Matrix] Konfigurasi Jala Lebar berhasil dimuat. Siap memindai prospek!")
