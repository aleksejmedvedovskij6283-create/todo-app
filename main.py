from ui import ConsoleUI
from logic import TaskManager
from storage import Storage


def main():
    storage = Storage("tasks.json")
    manager = TaskManager(storage)
    try:
        manager.load()
    except ValueError as error:
        print(f"Предупреждение: {error}")
        print("Начинаем с пустого списка дел")

    ui = ConsoleUI(manager)
    try:
        ui.run()
    finally:
        manager.save()
        print("Данные сохранены")


if __name__ == "__main__":
    main()
