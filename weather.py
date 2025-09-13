import requests

def get_weather(city):
    """
    Получает погоду через Open-Meteo API (не требует ключа!)
    """
    if not city or not city.strip():
        return "❌ Ошибка: Укажите название города"
    
    city = city.strip()
    
    try:
        # Сначала получаем координаты города
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=ru"
        geo_response = requests.get(geo_url, timeout=10)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if not geo_data.get('results'):
            return f"❌ Город '{city}' не найден. Проверьте правильность написания."
        
        location = geo_data['results'][0]
        lat = location['latitude']
        lon = location['longitude']
        city_name = location.get('name', city)
        country = location.get('country', '')
        
        # Получаем погоду по координатам
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
        weather_response = requests.get(weather_url, timeout=10)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        if 'current' not in weather_data:
            return "❌ Ошибка получения данных о погоде"
        
        current = weather_data['current']
        temp = current['temperature_2m']
        humidity = current['relative_humidity_2m']
        wind_speed = current['wind_speed_10m']
        weather_code = current['weather_code']
        
        # Преобразуем код погоды в текст
        weather_desc = get_weather_description(weather_code)
        
        # Определяем эмодзи для температуры
        temp_emoji = "🥶" if temp < 0 else "❄️" if temp < 10 else "🌤️" if temp < 20 else "☀️" if temp < 30 else "🔥"
        
        location_str = f"{city_name}, {country}" if country else city_name
        
        return (f"🌍 Погода в {location_str}:\n"
                f"{temp_emoji} Температура: {temp}°C\n"
                f"📝 Описание: {weather_desc}\n"
                f"💧 Влажность: {humidity}%\n"
                f"💨 Скорость ветра: {wind_speed} км/ч")
            
    except requests.exceptions.Timeout:
        return "❌ Ошибка: Превышено время ожидания ответа от сервиса погоды"
    except requests.exceptions.RequestException as e:
        return f"❌ Ошибка подключения к сервису погоды: {str(e)}"
    except KeyError as e:
        return f"❌ Ошибка: Неожиданный формат данных от API: {str(e)}"
    except Exception as e:
        return f"❌ Неожиданная ошибка: {str(e)}"

def get_weather_description(code):
    """Преобразует код погоды в текст"""
    weather_codes = {
        0: "ясно", 1: "преимущественно ясно", 2: "переменная облачность",
        3: "пасмурно", 45: "туман", 48: "туман", 51: "легкая морось",
        53: "умеренная морось", 55: "сильная морось", 56: "легкая ледяная морось",
        57: "сильная ледяная морось", 61: "небольшой дождь", 63: "умеренный дождь",
        65: "сильный дождь", 66: "ледяной дождь", 67: "сильный ледяной дождь",
        71: "небольшой снег", 73: "умеренный снег", 75: "сильный снег",
        77: "снежные зерна", 80: "небольшие ливни", 81: "умеренные ливни",
        82: "сильные ливни", 85: "снежные ливни", 86: "сильные снежные ливни",
        95: "гроза", 96: "гроза с градом", 99: "сильная гроза с градом"
    }
    return weather_codes.get(code, "неизвестно")