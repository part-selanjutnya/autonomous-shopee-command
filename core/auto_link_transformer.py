# ==========================================
# FILE: core/auto_link_transformer.py
# FUNGSI: Pabrik Perakitan Link Afiliasi & Injeksi SubID
# ==========================================

import urllib.parse
from core.config_matrix import AffiliateConfig

class LinkTransformer:
    def __init__(self):
        # Mengambil ID Afiliasi Anda dari DNA Sistem (Config Matrix)
        self.affiliate_id = AffiliateConfig.SHOPEE_AFFILIATE_ID

    def create_affiliate_link(self, raw_product_url, platform_source="X_Twitter"):
        """
        Mengubah link produk biasa menjadi link afiliasi siap pakai 
        dengan pelacakan SubID agar komisi masuk ke akun yang tepat.
        """
        # 1. Dapatkan format pelacakan otomatis dari Config Matrix
        tracking_param = AffiliateConfig.get_tracking_format(platform_source)
        
        # 2. Bersihkan URL produk dari karakter spasi/aneh
        clean_url = raw_product_url.strip()
        
        # 3. Suntikkan ID Afiliasi dan SubID ke dalam URL
        # (Dalam operasi nyata, tautan ini siap dipendekkan atau diumpankan ke API)
        separator = "&" if "?" in clean_url else "?"
        transformed_link = f"{clean_url}{separator}aff_id={self.affiliate_id}{tracking_param}"
        
        print(f"🔗 [Link Transformer] Tautan berafiliasi berhasil dirakit untuk sumber: {platform_source}")
        return transformed_link

# ==========================================
# Blok Pengujian Internal
# ==========================================
if __name__ == "__main__":
    transformer = LinkTransformer()
    test_url = "https://shopee.co.id/Powerbank-Fast-Charging-10000mAh"
    hasil = transformer.create_affiliate_link(test_url, "Facebook_Reels")
    print(f"Hasil Link Akhir:\n{hasil}")
