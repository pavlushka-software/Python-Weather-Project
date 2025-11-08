# 🌦️ Python Hava Durumu Sorgulama Uygulaması (WeatherAPI)

Bu proje, [WeatherAPI](https://www.weatherapi.com/) servisini kullanarak konsol (terminal) üzerinden anlık hava durumu bilgilerini çeken basit bir Python komut satırı uygulamasıdır.

Kullanıcıdan bir şehir adı alır ve o şehre ait sıcaklık, hissedilen sıcaklık, rüzgar hızı ve UV indeksi gibi güncel verileri gösterir.

* **Geliştirici:** [pavlushka-software](https://github.com/pavlushka-software)

## 📝 Özellikler

* Anlık sıcaklık (°C) ve hissedilen sıcaklık.
* Genel hava durumu (Örn: Parçalı Bulutlu, Güneşli).
* Konum bilgisi ve yerel saat.
* Gündüz veya gece bilgisi.
* Rüzgar hızı (kph).
* UV İndeksi.
* Verinin son güncellenme zamanı.

## 🖥️ Örnek Çıktı

```bash
Lütfen hava durumu bilgisini almak istediğiniz şehri giriniz: Istanbul
API Yanıtı Başarılı:
Tarih / Saat: 2025-11-08 22:30
Konum: Istanbul
Sıcaklık: 15.0°C
Durum: Parçalı Bulutlu
Gündüz mü? - Gece mi?: Gece
Rüzgar Hızı: 11.0 kph
UV İndeksi: 1.0
Hissedilen Sıcaklık: 14.5°C
Son Güncelleme: 2025-11-08 22:15
```

## 🛠️ Kurulum ve Ayarlar

Bu projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### 1. Projeyi Klonlayın (veya İndirin)

```bash
git clone https://github.com/pavlushka-software/Python-Weather-Project.git
cd Python-Weather-Project
```

### 2. Gerekli Kütüphaneleri Yükleyin

Projenin ihtiyaç duyduğu Python kütüphanelerini yükleyin.

```bash
pip install -r requirements.txt
```

### 3. API Anahtarını Ayarlayın (Çok Önemli!)

Bu projenin çalışması için bir WeatherAPI anahtarına ihtiyacınız var.

1.  **API Anahtarı Alın:**
    * [www.weatherapi.com](https://www.weatherapi.com/) adresine gidin ve ücretsiz bir hesap oluşturun.
    * Giriş yaptıktan sonra size özel API anahtarınızı (API Key) kopyalayın.

2.  **`.env` Dosyası Oluşturun:**
    * Projenin ana klasöründe (`main.py` dosyasının yanında) `.env` adında **yeni bir dosya** oluşturun.

3.  **Anahtarınızı Ekleyin:**
    * Oluşturduğunuz bu boş `.env` dosyasını bir metin editörü ile açın.
    * İçine aşağıdaki satırı ekleyin ve tırnak işaretleri arasına WeatherAPI'den aldığınız kendi anahtarınızı yapıştırın:

    ```
    WEATHER_API_KEY="KENDI_API_ANAHTARINIZI_BURAYA_YAPISTIRIN"
    ```

## 🚀 Kullanım

Tüm ayarları yaptıktan sonra uygulamayı aşağıdaki komutla çalıştırabilirsiniz:

```bash
python main.py
```

Sizden bir şehir adı girmeniz istenecek ve ardından hava durumu bilgileri ekrana yazdırılacaktır.

## 💻 Kullanılan Teknolojiler

* **Python 3**
* **requests:** API istekleri yapmak için.
* **python-dotenv:** Çevre değişkenlerini (API anahtarı) güvenli bir şekilde yönetmek için.
* **WeatherAPI:** Hava durumu verilerinin kaynağı.

