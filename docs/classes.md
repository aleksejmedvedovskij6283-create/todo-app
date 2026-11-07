# Классы приложения «Список дел»

| Класс | Атрибуты | Методы | Ответственность |
|---|---|---|---|
| Task | +title: str, +deadline: str, +done: bool | +mark_done(), +__str__(): str | Одно дело |
| TaskManager | -tasks: list | +add_task(task), +remove_task(title), +get_all(), +find_by_title(title) | Логика работы со списком дел |
| TaskStorage | -filename: str | +load(), +save(tasks) | Чтение и запись дел в файл |
| ConsoleUI | -manager: TaskManager | +run(), +print_menu(), +print_tasks() | Консольный интерфейс |

## Связи
- **ConsoleUI → TaskManager** — ассоциация: интерфейс хранит менеджер и вызывает его методы.
- **TaskManager o-- Task** — агрегация: менеджер содержит список дел, но дело может существовать и отдельно.
- **TaskManager ..> TaskStorage** — зависимость: менеджер использует хранилище только при загрузке и сохранении.
- **TaskStorage и ConsoleUI не связаны** — зависимости идут только вниз: UI → логика → хранение.

## Расширение (задание 2.5)
Базовый класс `Storage` с методами `load()` и `save()` и наследники `FileStorage` (файл) и `MemoryStorage` (оперативная память). `TaskManager` зависит от `Storage`, поэтому способ хранения можно менять без правки логики. Диаграмма: `class_diagram_storage.puml`.
