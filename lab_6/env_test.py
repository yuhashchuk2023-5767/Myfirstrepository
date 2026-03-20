import os

value = os.environ.get('IT_TEST')

if value:
    print(f"Значення змінної IT_TEST = {value}")
else:
    print("Помилка: Змінну IT_TEST не знайдено у файлі .env!")