MGM Weather (FT) - Home Assistant Integration

<!-- Dil Seçimi / Language Selection -->

<div align="center">
<h3>
<a href="#english">English</a> | <a href="#türkçe-kılavuz">Türkçe</a>
</h3>
</div>

<a name="english"></a>

🇬🇧 English

MGM Weather (FT) is a custom integration for Home Assistant that retrieves weather data from the Turkish State Meteorological Service (MGM) via a custom proxy API. It provides accurate, localized weather conditions and forecasts for cities in Turkey.

🌟 Features

Real-time Data: Fetches current temperature, humidity, wind speed, pressure, and weather conditions.

Daily Forecast: Provides a 5-day weather forecast.

Easy Configuration: Setup directly via the Home Assistant UI (Config Flow).

Multi-City Support: Add as many cities as you like.

Localized: Fully compatible with Turkish locations and weather codes.

🚀 Installation

Method 1: HACS (Recommended)

Open HACS in Home Assistant.

Go to Integrations > click the 3 dots in the top right corner > Custom repositories.

Paste the URL of this repository: https://github.com/taskinfa/mgm-weather

Select Integration as the category and click Add.

Search for "MGM Hava Durumu (FT)" and install it.

Restart Home Assistant.

Method 2: Manual

Download the latest release.

Copy the custom_components/mgm_weather folder to your Home Assistant's custom_components directory.

Restart Home Assistant.

⚙️ Configuration

Go to Settings > Devices & Services.

Click + ADD INTEGRATION in the bottom right corner.

Search for "MGM Hava Durumu (FT)".

Enter your city name (e.g., Istanbul, Afyonkarahisar, Ankara) in the popup box.

Click Submit.

📊 Dashboard Card Example

You can use the standard weather card or a custom card like Mushroom.

type: weather-forecast
entity: weather.mgm_afyonkarahisar
name: Afyonkarahisar (MGM)
forecast_type: daily


❤️ Credits & Disclaimer

Developer: Fatih Taşkın

Data Source: Turkish State Meteorological Service (MGM) via proxy API.

This is a custom integration and is not officially affiliated with MGM.

<a name="türkçe-kılavuz"></a>

🇹🇷 Türkçe Kılavuz

MGM Weather (FT), Türkiye Meteoroloji Genel Müdürlüğü (MGM) verilerini özel bir proxy API üzerinden Home Assistant'a aktaran özel bir entegrasyondur. Türkiye'deki şehirler için en doğru anlık hava durumu ve tahmin verilerini sağlar.

🌟 Özellikler

Anlık Veri: Sıcaklık, nem, rüzgar hızı, basınç ve hava durumu ikonunu anlık çeker.

Günlük Tahmin: 5 günlük hava tahmini sunar.

Kolay Kurulum: Home Assistant arayüzü üzerinden (Config Flow) saniyeler içinde kurulur.

Çoklu Şehir: İstediğiniz kadar farklı şehir ekleyebilirsiniz.

Yerelleştirilmiş: Türkiye lokasyonları ve MGM hava durumu kodlarıyla tam uyumludur.

🚀 Kurulum

Yöntem 1: HACS (Önerilen)

Home Assistant'ta HACS menüsünü açın.

Integrations (Entegrasyonlar) kısmına gidin > sağ üstteki üç noktaya tıklayın > Custom repositories (Özel depolar).

Bu reponun adresini yapıştırın: https://github.com/taskinfa/mgm-weather

Kategori olarak Integration seçin ve Ekle deyin.

Listeden "MGM Hava Durumu (FT)" entegrasyonunu bulup indirin.

Home Assistant'ı Yeniden Başlatın.

Yöntem 2: Manuel

En son sürümü indirin.

custom_components/mgm_weather klasörünü Home Assistant dizininizdeki custom_components klasörünün içine kopyalayın.

Home Assistant'ı Yeniden Başlatın.

⚙️ Yapılandırma

Ayarlar > Cihazlar ve Hizmetler menüsüne gidin.

Sağ alttaki + ENTEGRASYON EKLE butonuna tıklayın.

Arama kutusuna "MGM Hava Durumu (FT)" yazın.

Açılan pencereye şehir adını yazın (Örn: Istanbul, Afyonkarahisar, Ankara).

Gönder butonuna tıklayın.

📊 Kart Örneği

Standart hava durumu kartını veya Mushroom gibi özel kartları kullanabilirsiniz.

type: weather-forecast
entity: weather.mgm_afyonkarahisar
name: Afyonkarahisar (MGM)
forecast_type: daily


❤️ Emeği Geçenler & Yasal Uyarı

Geliştirici: Fatih Taşkın

Veri Kaynağı: Türkiye Meteoroloji Genel Müdürlüğü (MGM).

Bu özel bir entegrasyondur ve MGM ile resmi bir bağlantısı yoktur.
