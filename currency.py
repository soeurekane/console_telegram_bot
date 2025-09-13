import requests
from config import CURRENCY_API_KEY

def convert_currency(amount, from_currency, to_currency):
    """
    Конвертирует валюту через FreeCurrencyAPI
    """
    # Валидация входных данных
    if not amount or not from_currency or not to_currency:
        return "❌ Ошибка: Все поля обязательны для заполнения"
    
    if not CURRENCY_API_KEY or CURRENCY_API_KEY == "your_currencyapi_key_here":
        return "❌ Ошибка: Не установлен API ключ для валют. Проверьте config.py"
    
    # Валидация суммы
    try:
        amount_float = float(amount)
        if amount_float <= 0:
            return "❌ Ошибка: Сумма должна быть положительным числом"
    except ValueError:
        return "❌ Ошибка: Сумма должна быть числом"
    
    # Валидация валют
    from_currency = from_currency.upper().strip()
    to_currency = to_currency.upper().strip()
    
    if len(from_currency) != 3 or len(to_currency) != 3:
        return "❌ Ошибка: Код валюты должен состоять из 3 букв (например: USD, EUR, RUB)"
    
    if from_currency == to_currency:
        return f"✅ {amount} {from_currency} = {amount} {to_currency} (одинаковые валюты)"
    
    try:
        url = f"https://api.freecurrencyapi.com/v1/latest?apikey={CURRENCY_API_KEY}&base_currency={from_currency}"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if response.status_code == 200 and 'data' in data:
            if to_currency in data['data']:
                rate = data['data'][to_currency]
                converted_amount = amount_float * rate
                return f"💱 {amount} {from_currency} = {converted_amount:.2f} {to_currency}\n📊 Курс: 1 {from_currency} = {rate:.4f} {to_currency}"
            else:
                return f"❌ Ошибка: Валюта {to_currency} не найдена в базе данных"
        else:
            error_msg = data.get('message', 'Unknown error') if isinstance(data, dict) else 'API error'
            return f"❌ Ошибка API: {error_msg}"
            
    except requests.exceptions.Timeout:
        return "❌ Ошибка: Превышено время ожидания ответа от сервиса валют"
    except requests.exceptions.RequestException as e:
        return f"❌ Ошибка подключения к сервису валют: {str(e)}"
    except ValueError:
        return "❌ Ошибка: Сумма должна быть числом"
    except Exception as e:
        return f"❌ Неожиданная ошибка: {str(e)}"