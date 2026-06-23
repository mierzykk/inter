import requests
import json

def pogoda(miasto,zmienne = False):
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": miasto, "count": 1}
    ).json()
    if "results" not in geo:
            if zmienne:
                return None, None, None, None, None, None, None
            else:
                return "Nie znaleziono miasta"
    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]
    weather = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "timezone": "Europe/Warsaw"
        }
    ).json()
    if zmienne:
        # czas (str): Data i godzina w formacie ISO 8601 (np. "2026-05-31T18:00")
        # interval (int): Częstotliwość aktualizacji danych w sekundach (np. 900 lub 3600)
        # temperature (float): Aktualna temperatura powietrza w stopniach Celsjusza (°C)
        # windspeed (float): Aktualna prędkość wiatru w kilometrach na godzinę (km/h)
        # winddirection (int): Kierunek wiatru w stopniach geograficznych (0°/360°=Północ, 90°=Wschód, 180°=Południe, 270°=Zachód)
        # is_day (bool): Status dnia (1 = dzień, 0 = noc)
        # weathercode (int): Kod stanu pogody WMO (np. 0=słonecznie, 3=pochmurnie, 61=deszcz, 95=burza)
        #czas, interval, temperature, windspeed, winddirection, is_day, weathercode = inter.pogoda(miasto)
        czas = weather["current_weather"]["time"]
        interval = weather["current_weather"]["interval"]
        temperature = weather["current_weather"]["temperature"]
        windspeed = weather["current_weather"]["windspeed"]
        winddirection = weather["current_weather"]["winddirection"]
        is_day = weather["current_weather"]["is_day"]
        weathercode = weather["current_weather"]["weathercode"]
        return str(czas), int(interval), float(temperature), float(windspeed), int(winddirection), bool(is_day), int(weathercode)
    else:return weather["current_weather"]
