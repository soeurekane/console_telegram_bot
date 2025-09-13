import requests
import random

def get_fact():
    """
    Получает случайный интересный факт
    """
    facts = [
        "Осьминог имеет три сердца.",
        "Сердце кита бьется всего 9 раз в минуту.",
        "Мед никогда не портится. Археологи находили мед в древнеегипетских гробницах, и он был съедобен.",
        "Банан - это ягода, а клубника - нет.",
        "В Японии есть более 50 000 человек, которым больше 100 лет.",
        "Крокодилы не могут высовывать язык.",
        "Сумчатые медведи коала имеют отпечатки пальцев, почти идентичные человеческим."
    ]
    return random.choice(facts)

def get_quote():
    """
    Получает случайную цитату
    """
    # Fallback цитаты если API не работает
    fallback_quotes = [
        "Лучше быть уверенным в хорошем результате, чем надеяться на отличный. — Билл Гейтс",
        "Настойчивость — это не длинный забег, это много коротких забегов один за другим. — Уолтер Эллиот",
        "Единственный способ делать великие дела — любить то, что ты делаешь. — Стив Джобс",
        "Успех — это способность переходить от одной неудачи к другой, не теряя энтузиазма. — Уинстон Черчилль",
        "Будущее принадлежит тем, кто верит в красоту своих мечтаний. — Элеонора Рузвельт",
        "Единственный способ делать великие дела — любить то, что ты делаешь. — Стив Джобс"
    ]
    
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if 'content' in data and 'author' in data:
            return f"💬 \"{data['content']}\" — {data['author']}"
        else:
            return f"💬 {random.choice(fallback_quotes)}"
            
    except requests.exceptions.Timeout:
        return f"💬 {random.choice(fallback_quotes)}\n(Использована локальная цитата из-за таймаута)"
    except requests.exceptions.RequestException:
        return f"💬 {random.choice(fallback_quotes)}\n(Использована локальная цитата из-за проблем с сетью)"
    except (KeyError, ValueError):
        return f"💬 {random.choice(fallback_quotes)}\n(Использована локальная цитата из-за ошибки API)"
    except Exception:
        return f"💬 {random.choice(fallback_quotes)}\n(Использована локальная цитата)"