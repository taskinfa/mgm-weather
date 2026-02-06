# **MGM Weather (FT) \- Home Assistant Integration**

**MGM Weather (FT)** is a custom integration for Home Assistant that retrieves weather data from the Turkish State Meteorological Service (MGM) via a custom proxy API. It provides accurate, localized weather conditions and forecasts for cities in Turkey.

**MGM Weather (FT)**, Türkiye Meteoroloji Genel Müdürlüğü (MGM) verilerini özel bir proxy API üzerinden Home Assistant'a aktaran özel bir entegrasyondur. Türkiye'deki şehirler için en doğru anlık hava durumu ve tahmin verilerini sağlar.

## **🌟 Features / Özellikler**

* **Real-time Data:** Fetches current temperature, humidity, wind speed, pressure, and weather conditions.  
* **Daily Forecast:** Provides a 5-day weather forecast.  
* **Easy Configuration:** Setup directly via the Home Assistant UI (Config Flow).  
* **Multi-City Support:** Add as many cities as you like.  
* **Localized:** Fully compatible with Turkish locations and weather codes.  
* **Anlık Veri:** Sıcaklık, nem, rüzgar hızı, basınç ve hava durumu ikonunu anlık çeker.  
* **Günlük Tahmin:** 5 günlük hava tahmini sunar.  
* **Kolay Kurulum:** Home Assistant arayüzü üzerinden (Config Flow) saniyeler içinde kurulur.  
* **Çoklu Şehir:** İstediğiniz kadar farklı şehir ekleyebilirsiniz.  
* **Yerelleştirilmiş:** Türkiye lokasyonları ve MGM hava durumu kodlarıyla tam uyumludur.

## **🚀 Installation / Kurulum**

### **Method 1: HACS (Recommended) / Yöntem 1: HACS (Önerilen)**

1. Open **HACS** in Home Assistant.  
2. Go to **Integrations** \> click the 3 dots in the top right corner \> **Custom repositories**.  
3. Paste the URL of this repository: https://github.com/USERNAME/REPO\_NAME (Replace with your actual repo URL).  
4. Select **Integration** as the category and click **Add**.  
5. Search for **"MGM Hava Durumu (FT)"** and install it.  
6. **Restart** Home Assistant.  
7. Home Assistant'ta **HACS** menüsünü açın.  
8. **Integrations** (Entegrasyonlar) kısmına gidin \> sağ üstteki üç noktaya tıklayın \> **Custom repositories** (Özel depolar).  
9. Bu reponun adresini yapıştırın: https://github.com/KULLANICIADINIZ/REPO\_ADINIZ (Kendi GitHub linkinizle değiştirin).  
10. Kategori olarak **Integration** seçin ve **Ekle** deyin.  
11. Listeden **"MGM Hava Durumu (FT)"** entegrasyonunu bulup indirin.  
12. Home Assistant'ı **Yeniden Başlatın**.

### **Method 2: Manual / Yöntem 2: Manuel**

1. Download the latest release.  
2. Copy the custom\_components/mgm\_weather folder to your Home Assistant's custom\_components directory.  
3. **Restart** Home Assistant.  
4. En son sürümü indirin.  
5. custom\_components/mgm\_weather klasörünü Home Assistant dizininizdeki custom\_components klasörünün içine kopyalayın.  
6. Home Assistant'ı **Yeniden Başlatın**.

## **⚙️ Configuration / Yapılandırma**

1. Go to **Settings** \> **Devices & Services**.  
2. Click **\+ ADD INTEGRATION** in the bottom right corner.  
3. Search for **"MGM Hava Durumu (FT)"**.  
4. Enter your city name (e.g., Istanbul, Afyonkarahisar, Ankara) in the popup box.  
5. Click **Submit**.  
6. **Ayarlar** \> **Cihazlar ve Hizmetler** menüsüne gidin.  
7. Sağ alttaki **\+ ENTEGRASYON EKLE** butonuna tıklayın.  
8. Arama kutusuna **"MGM Hava Durumu (FT)"** yazın.  
9. Açılan pencereye şehir adını yazın (Örn: Istanbul, Afyonkarahisar, Ankara).  
10. **Gönder** butonuna tıklayın.

## **📊 Dashboard Card Example / Kart Örneği**

You can use the standard weather card or a custom card like Mushroom.

Standart hava durumu kartını veya Mushroom gibi özel kartları kullanabilirsiniz.

type: weather-forecast  
entity: weather.mgm\_afyonkarahisar  
name: Afyonkarahisar (MGM)  
forecast\_type: daily

## **❤️ Credits & Disclaimer**

* **Developer:** Fatih Taşkın  
* **Data Source:** Turkish State Meteorological Service (MGM) via proxy API.

This is a custom integration and is not officially affiliated with MGM.

Bu özel bir entegrasyondur ve MGM ile resmi bir bağlantısı yoktur.