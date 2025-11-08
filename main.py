# Hava Durumu Bilgisi Çekme Uygulaması / Weather Information Fetching Application
# Bu uygulama, kullanıcıdan bir şehir adı alır ve WeatherAPI'den o şehre ait güncel hava durumu bilgilerini çeker.
# www.github.com/pavlushka-software

# Gerekli Kütüphaneler / Required Libraries
import requests
import json
import os
from dotenv import load_dotenv, dotenv_values

# .env.example dosyasındaki çevre değişkenlerini yükle
# .env.example dosyasının adını değiştiriseniz burayı da değiştirin. / If you change the name of the .env.example file, change it here as well.
load_dotenv(dotenv_path=".env.example")

# Hava Durumu API Anahtarı / Weather API Key
api_key = os.getenv("WEATHER_API_KEY")

# Kullanıcıdan Şehir Bilgisini Alma / Getting City Information from User
sehir = input("Lütfen hava durumu bilgisini almak istediğiniz şehri giriniz: ") 
url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={sehir}&aqi=no"

try:
    response = requests.get(url)
    # Başarılı Yanıt Durumu / Successful Response Handling
    if response.status_code == 200:
        data = response.json()
        
        # Çekilen Verileri Değişkenlere Atama / Assigning Retrieved Data to Variables
        konum = data['location']['name']
        sicaklik_c = data['current']['temp_c']
        durum = data['current']['condition']['text']
        saat = data['location']['localtime']
        son = data['current']['last_updated']
        ruzgar_hizi = data['current']['wind_kph']
        uv_index = data['current']['uv']
        hisse_edilen_sicaklik = data['current']['feelslike_c']
        gg = data['current']['is_day']
        if gg == 1:
            gg = "Gündüz"
        else:
            gg = "Gece"

        # Sonuçları Yazdırma / Printing Results

        print(f"API Yanıtı Başarılı:")
        print(f"Tarih / Saat: {saat}")
        print(f"Konum: {konum}")
        print(f"Sıcaklık: {sicaklik_c}°C")
        print(f"Durum: {durum}")
        print(f"Gündüz mü? - Gece mi?: {gg}")
        print(f"Rüzgar Hızı: {ruzgar_hizi} kph")
        print(f"UV İndeksi: {uv_index}")
        print(f"Hissedilen Sıcaklık: {hisse_edilen_sicaklik}°C")
        print(f"Son Güncelleme: {son}")
    
    # Hata Durumu / Error Handling
    else:
        print(f"Hata: API isteği başarısız oldu. Durum Kodu: {response.status_code}")
        print("Dönen Yanıt:", response.text)

# İstek Hatası Durumu / Request Exception Handling
except requests.exceptions.RequestException as e:
    print(f"İstek sırasında bir hata oluştu: {e}")


