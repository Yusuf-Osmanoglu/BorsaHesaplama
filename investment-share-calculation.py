import yfinance as yf
from datetime import datetime

# Kullanıcıdan hisse kodunu alma
hisse_kodu = input("Lütfen hisse kodunu girin (örneğin, XU100.IS): ")

# Yatırım tutarları
yatirimlar = {
    "2014": 169,
    "2015": 178,
    "2016": 260,
    "2017": 280,
    "2018": 320,
    "2019": 404,
    "2020": 464,
    "2021": 562,
    "2022": 850,
    "2023": 2280,
    "2024": 3560
}

# Hisse senedi verilerini çek
def hisse_verisi_cek(hisse_kodu, baslangic_tarihi, bitis_tarihi):
    hisse = yf.Ticker(hisse_kodu)
    data = hisse.history(start=baslangic_tarihi, end=bitis_tarihi, interval="1mo")
    return data['Close']  # Aylık kapanış fiyatlarını al

# Yatırım getirilerini hesapla
def yatirim_hesapla(hisse_kodu, yatirimlar):
    toplam_kar = 0
    toplam_yatirim = 0
    bugun = datetime.now()

    for yil, aylik_tutar in yatirimlar.items():
        baslangic_tarihi = f"{yil}-01-01"
        bitis_tarihi = f"{yil}-12-31" if yil != "2024" else bugun.strftime("%Y-%m-%d")
        
        kapanis_fiyatlari = hisse_verisi_cek(hisse_kodu, baslangic_tarihi, bitis_tarihi)
        aylik_hisse_adedi = aylik_tutar / kapanis_fiyatlari
        
        toplam_hisse_adedi = aylik_hisse_adedi.sum()
        son_fiyat = kapanis_fiyatlari[-1]  # Yılın son kapanış fiyatı
        
        toplam_kar += toplam_hisse_adedi * son_fiyat  # Yıl sonu değeri
        toplam_yatirim += aylik_tutar * len(kapanis_fiyatlari)  # Yıl boyunca yapılan toplam yatırım
    
    return toplam_kar, toplam_yatirim

# Fonksiyonu çağır ve sonuçları yazdır
toplam_kar, toplam_yatirim = yatirim_hesapla(hisse_kodu, yatirimlar)
toplam_para = toplam_kar + toplam_yatirim  # Kâr ve yatırımların toplamı

print(f"Günümüze kadar toplam kar: {toplam_kar:.2f} TL")
print(f"Günümüze kadar toplam yatırım: {toplam_yatirim:.2f} TL")
print(f"Toplam paranız: {toplam_para:.2f} TL")
