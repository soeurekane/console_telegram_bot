import os
from typing import Optional

# Конфигурационные переменные
# Безопасное получение API ключей из переменных окружения
WEATHER_API_KEY: Optional[str] = os.getenv('WEATHER_API_KEY')
CURRENCY_API_KEY: Optional[str] = os.getenv('CURRENCY_API_KEY')

# Fallback значения (не рекомендуется для продакшена)
if not WEATHER_API_KEY:
    WEATHER_API_KEY = "517b4caa8578564c1b2314c832ce16d0"  # OpenWeatherMap (не используется в текущей реализации)
    
if not CURRENCY_API_KEY:
    CURRENCY_API_KEY = "cur_live_ijmAE9LIwWHmjCncur_live_ijmAE9LIwWHmjCnHqGoqlLtbmr1Fr7WAOVX6mKF6HqGoqlLtbmr1Fr7WAOVX6mKF6" 
