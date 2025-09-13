import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    """
    Загружает задачи из файла
    """
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️ Ошибка чтения файла задач: {e}")
            return []
    return []

def save_tasks(tasks):
    """
    Сохраняет задачи в файл
    """
    try:
        with open(TODO_FILE, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"⚠️ Ошибка сохранения файла задач: {e}")
        raise

def add_task(task_text):
    """
    Добавляет новую задачу
    """
    if not task_text or not task_text.strip():
        return "❌ Ошибка: Текст задачи не может быть пустым"
    
    task_text = task_text.strip()
    
    try:
        tasks = load_tasks()
        task_id = len(tasks) + 1
        tasks.append({"id": task_id, "task": task_text, "completed": False})
        save_tasks(tasks)
        return f"✅ Задача добавлена: {task_text}"
    except Exception as e:
        return f"❌ Ошибка при добавлении задачи: {str(e)}"

def show_tasks():
    """
    Показывает все задачи
    """
    tasks = load_tasks()
    if not tasks:
        return "Список дел пуст!"
    
    result = "📋 Ваш список дел:\n"
    for task in tasks:
        status = "✅" if task["completed"] else "⭕"
        result += f"{task['id']}. {status} {task['task']}\n"
    return result

def complete_task(task_id):
    """
    Отмечает задачу как выполненную
    """
    try:
        task_id = int(task_id)
        tasks = load_tasks()
        
        if not tasks:
            return "❌ Список дел пуст!"
        
        if 1 <= task_id <= len(tasks):
            if tasks[task_id-1]["completed"]:
                return f"ℹ️ Задача {task_id} уже была выполнена"
            tasks[task_id-1]["completed"] = True
            save_tasks(tasks)
            return f"✅ Задача {task_id} отмечена как выполненная!"
        else:
            return f"❌ Ошибка: Неверный номер задачи. Доступны номера от 1 до {len(tasks)}"
    except ValueError:
        return "❌ Ошибка: Номер задачи должен быть числом"
    except Exception as e:
        return f"❌ Ошибка при выполнении задачи: {str(e)}"

def delete_task(task_id):
    """
    Удаляет задачу
    """
    try:
        task_id = int(task_id)
        tasks = load_tasks()
        
        if not tasks:
            return "❌ Список дел пуст!"
        
        if 1 <= task_id <= len(tasks):
            deleted_task = tasks.pop(task_id-1)
            # Пересчитываем ID оставшихся задач
            for i, task in enumerate(tasks, 1):
                task["id"] = i
            save_tasks(tasks)
            return f"🗑️ Задача удалена: {deleted_task['task']}"
        else:
            return f"❌ Ошибка: Неверный номер задачи. Доступны номера от 1 до {len(tasks)}"
    except ValueError:
        return "❌ Ошибка: Номер задачи должен быть числом"
    except Exception as e:
        return f"❌ Ошибка при удалении задачи: {str(e)}"

def get_todo_stats():
    """
    Возвращает статистику по задачам
    """
    try:
        tasks = load_tasks()
        
        if not tasks:
            return "📊 Статистика: Список дел пуст!"
        
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task["completed"])
        pending_tasks = total_tasks - completed_tasks
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        
        return (f"📊 Статистика списка дел:\n"
                f"📝 Всего задач: {total_tasks}\n"
                f"✅ Выполнено: {completed_tasks}\n"
                f"⭕ Осталось: {pending_tasks}\n"
                f"📈 Прогресс: {completion_rate:.1f}%")
    except Exception as e:
        return f"❌ Ошибка при получении статистики: {str(e)}"