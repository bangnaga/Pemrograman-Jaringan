# Credit: Fikom UIT
import requests
import json

def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }
    
    print(f"Mengambil data cuaca untuk koordinat {lat}, {lon}...")
    
    try:
        response = requests.get(url, params=params)
        
        # Cek status code (200 = Success)
        if response.status_code == 200:
            data = response.json()
            cuaca = data['current_weather']
            
            print("\n--- LAPORAN CUACA TERKINI ---")
            print(f"Suhu        : {cuaca['temperature']} {data['current_weather_units']['temperature']}")
            print(f"Kecepatan Angin: {cuaca['windspeed']} km/h")
            print(f"Waktu Data  : {cuaca['time']}")
        else:
            print(f"Gagal mengambil data. Status: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Tidak ada koneksi internet.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    # Koordinat Jakarta
    jkt_lat = -6.2088
    jkt_lon = 106.8456
    
    get_weather(jkt_lat, jkt_lon)
