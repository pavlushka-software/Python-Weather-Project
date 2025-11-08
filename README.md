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
git clone [https://github.com/pavlushka-software/](https://github.com/pavlushka-software/)[PROJE-ADINIZ].git
cd [PROJE-ADINIZ]
```
*(Not: `[PROJE-ADINIZ]` kısmını GitHub'daki depo adınızla değiştirin.)*

### 2. Gerekli Kütüphaneleri Yükleyin

Projenin
