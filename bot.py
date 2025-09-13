from weather import get_weather
from currency import convert_currency
from facts_quotes import get_fact, get_quote
from todo_list import add_task, show_tasks, complete_task, delete_task, get_todo_stats
from time_utils import get_current_time, get_time_in_major_cities

def print_help():
    """
    Выводит справку по командам
    """
    help_text = """
🤖 Консольный Телеграм-Бот
Доступные команды:

🌤  Погода:
  /weather [город]  - Узнать погоду в указанном городе

💱 Валюта:
  /convert [сумма] [из_валюты] [в_валюту] - Конвертировать валюту
  Пример: /convert 100 USD RUB

📚 Факты и цитаты:
  /fact - Случайный интересный факт
  /quote - Случайная цитата

🕐 Время:
  /time [временная_зона] - Текущее время в указанной зоне
  /timezones - Время в основных городах мира

📝 Список дел:
  /todo add [задача] - Добавить задачу
  /todo list - Показать все задачи
  /todo complete [номер] - Отметить задачу выполненной
  /todo delete [номер] - Удалить задачу
  /todo stats - Показать статистику задач

❓ Прочее:
  /help - Показать эту справку
  /exit - Выйти из бота
"""
    print(help_text)

def main():
    """
    Главная функция бота
    """
    print("🤖 Консольный Телеграм-Бот запущен!")
    print("📝 Введите /help для списка команд")
    print("=" * 50)
    
    while True:
        try:
            command = input("\nВведите команду: ").strip()
            
            if not command:
                continue
                
            if command.startswith('/'):
                parts = command.split()
                cmd = parts[0].lower()
                
                if cmd == '/exit':
                    print("👋 До свидания!")
                    break
                    
                elif cmd == '/help':
                    print_help()
                    
                elif cmd == '/weather':
                    if len(parts) > 1:
                        city = ' '.join(parts[1:])
                        print(get_weather(city))
                    else:
                        print("❌ Укажите город: /weather Москва")
                        
                elif cmd == '/convert':
                    if len(parts) == 4:
                        try:
                            amount = parts[1]
                            from_curr = parts[2]
                            to_curr = parts[3]
                            print(convert_currency(amount, from_curr, to_curr))
                        except Exception as e:
                            print(f"❌ Ошибка: {e}")
                    else:
                        print("❌ Используйте: /convert [сумма] [из] [в]")
                        print("Пример: /convert 100 USD RUB")
                        
                elif cmd == '/fact':
                    print("📚 Интересный факт:")
                    print(get_fact())
                    
                elif cmd == '/quote':
                    print("💬 Цитата дня:")
                    print(get_quote())
                    
                elif cmd == '/time':
                    if len(parts) > 1:
                        timezone = ' '.join(parts[1:])
                        print(get_current_time(timezone))
                    else:
                        print(get_current_time("UTC"))
                        
                elif cmd == '/timezones':
                    print(get_time_in_major_cities())
                    
                elif cmd == '/todo':
                    if len(parts) > 1:
                        subcmd = parts[1].lower()
                        
                        if subcmd == 'add' and len(parts) > 2:
                            task = ' '.join(parts[2:])
                            print(add_task(task))
                            
                        elif subcmd == 'list':
                            print(show_tasks())
                            
                        elif subcmd == 'complete' and len(parts) > 2:
                            print(complete_task(parts[2]))
                            
                        elif subcmd == 'delete' and len(parts) > 2:
                            print(delete_task(parts[2]))
                            
                        elif subcmd == 'stats':
                            print(get_todo_stats())
                            
                        else:
                            print("❌ Неверная подкоманда todo. Используйте: add, list, complete, delete, stats")
                    else:
                        print("❌ Используйте: /todo [add|list|complete|delete|stats]")
                        
                else:
                    print("❌ Неизвестная команда. Введите /help для справки")
                    
            else:
                print("❌ Команды должны начинаться с /. Введите /help для справки")
                
        except KeyboardInterrupt:
            print("\n👋 До свидания!")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")

if __name__ == "__main__":
    main()