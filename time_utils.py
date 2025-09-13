from datetime import datetime
import pytz

def get_current_time(timezone="UTC"):
    """
    Получает текущее время в указанной временной зоне
    """
    try:
        # Попытка получить указанную временную зону
        tz = pytz.timezone(timezone)
        current_time = datetime.now(tz)
        
        # Форматируем время
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
        
        return f"🕐 Текущее время в {timezone}: {formatted_time}"
        
    except pytz.exceptions.UnknownTimeZoneError:
        # Если временная зона не найдена, возвращаем список популярных
        popular_timezones = [
            "UTC", "Europe/Moscow", "Europe/London", "America/New_York", 
            "America/Los_Angeles", "Asia/Tokyo", "Asia/Shanghai", "Australia/Sydney"
        ]
        
        return (f"❌ Неизвестная временная зона: {timezone}\n"
                f"📋 Популярные временные зоны:\n" + 
                "\n".join(f"  • {tz}" for tz in popular_timezones))
    except Exception as e:
        return f"❌ Ошибка получения времени: {str(e)}"

def get_time_in_major_cities():
    """
    Получает время в основных городах мира
    """
    cities = {
        "Москва": "Europe/Moscow",
        "Лондон": "Europe/London", 
        "Нью-Йорк": "America/New_York",
        "Лос-Анджелес": "America/Los_Angeles",
        "Токио": "Asia/Tokyo",
        "Шанхай": "Asia/Shanghai",
        "Сидней": "Australia/Sydney"
    }
    
    result = "🌍 Время в основных городах мира:\n"
    
    for city, timezone in cities.items():
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            formatted_time = current_time.strftime("%H:%M:%S")
            result += f"  {city}: {formatted_time}\n"
        except Exception:
            result += f"  {city}: Ошибка получения времени\n"
    
    return result
