# Borsa Hesaplama Aracı

Bu proje, belirli bir hisse senedinin geçmiş yıllardaki asgeri ücretlerin %20 kadar yatırımlar üzerinden kârını hesaplayan bir Python uygulamasıdır. Kullanıcı, belirli bir hisse kodunu ve başlangıç yılını girerek, her ay yapılan sabit yatırımlar üzerinden elde edilen kârı görebilir.

## Özellikler

- **Hisse Kodu Girme:** Kullanıcı terminalden takip etmek istediği hisse kodunu girer.
- **Yıllık Yatırım Miktarları:** Her yıl için belirli bir sabit miktar üzerinden yatırım yapılır:
  - 2021: 562 TL
  - 2022: 850 TL
  - 2023: 2280 TL
  - 2024: 3560 TL (şu anki tarihine kadar)
- **Aylık Kâr Hesaplama:** Her ayın 5'inde yapılan yatırım üzerinden kâr hesaplanır.
- **Veri Çekme:** Hisse fiyatları ve diğer veriler, sitesinden otomatik olarak çekilir.
- **Sonuç Görüntüleme:** Kullanıcıya toplam yatırım miktarı ve nihai kâr gösterilir.

## Gereksinimler

- Python 3.x
- Selenium
- ChromeDriver
- chromedriver-autoinstaller

## Kurulum

1. **Depoyu Klonlayın:**

   ```bash
   git clone https://github.com/Yusuf-Osmanoglu/BorsaHesapplama.git
   cd BorsaHesapplama
