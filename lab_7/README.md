##ЗВІТ ДО ЛАБОРАТОРНОЇ РОБОТИ
#Тема:

Створення AI агентів з використанням Google ADK та Poetry

#Мета роботи:

Навчитись створювати AI агентів з використанням Google ADK (Python) та Poetry для управління залежностями проекту.

Виконання роботи
🔹 Перевірка середовища

Було перевірено встановлення Python та Poetry:

python --version
poetry --version

Встановлені версії:

Python: 3.13

Poetry: 2.3.2
🔹 Встановлення залежностей

Було виконано:

poetry init

poetry add google-adk python-dotenv

Було створено файл poetry.lock.

📌 Пояснення:

Файл poetry.lock зберігає точні версії залежностей для забезпечення стабільності роботи проєкту.

🔹 Основні команди ADK

create — створення агента

run — запуск у консолі

web — запуск веб-інтерфейсу

🎓 #Агент 1: my_first_agent

Було створено першого агента.

📌 Код:

from google.adk.agents.llm_agent import Agent

def get_current_time(city: str) -> dict:

    import datetime

    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    return {"city": city, "time": current_time}

root_agent = Agent(

    model='gemini-2.5-flash',

    name='time_agent',

    instruction="Повідомляє час",

    tools=[get_current_time],

)

![Скріншот 1](pictures/screen1.jng)

![Скріншот 2](pictures/screen2.jng)

🎓 #Агент 2: math_agent

Було створено математичного агента.

📌 Код:

def calculate_rectangle_area(width, height):

    return width * height

![Скріншот 3](pictures/screen3.jng)

📌 Додано власний інструмент:

обчислення площі трикутника

🎓 #Агент 3: student_helper

📌 Призначення:

допомога студентам

![Скріншот 4](pictures/screen4.jng)

🎓 #Агент 4: creative_writer

📌 Особливість:

параметр temperature = 1.3 (креативність)

![Скріншот 5](pictures/screen5.jng)

Під час тестування агента creative_writer спостерігалось зависання без отримання відповіді.
Імовірною причиною є перевищення квоти Google Gemini API (помилка 429 RESOURCE_EXHAUSTED), оскільки інші агенти з меншою складністю запитів продовжували працювати.

Агент 5: conversation_agent

📌 Має пам’ять

![Скріншот 6](pictures/screen6.jng)

📌 Результати
Розроблено кілька AI агентів
Отримано результати роботи агентів
Навчились працювати з Google ADK
Навчились створювати tools
🧾 ## Висновок

❓ Що зроблено:

Створено та протестовано AI агентів.

❓ Чи досягнуто мети:

Так, повністю.

❓ Нові знання:

Робота з AI агентами, tools, API.

❓ Чи виконані всі завдання:

Так.

❓ Складності:

Проблеми з квотою API та Poetry.

❓ Feedback:

Формат цікавий та сучасний.

❓ Suggestions:

Збільшити безкоштовні квоти API.
