class MyName:
    """Опис класу / Документація"""
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        # якщо name == None -> беремо Anonymous
        if name is None:
            name = self.anonymous_user().name

        # приводимо до рядка та прибираємо зайві пробіли
        name = str(name).strip()

        # перевірка — ім'я повинно містити лише літери
        if not name.isalpha():
            raise ValueError("Ім'я може містити лише літери!")

        # робимо першу букву великою
        self.name = name.capitalize()

        # збільшуємо лічильник класу і даємо id
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        """Class property — повертаємо ім'я"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property — повертаємо емейл (за замовчуванням домен)"""
        return self.create_email()

    def create_email(self, domain: str = "itcollege.lviv.ua") -> str:
        """Instance method — формує email з можливістю змінити домен"""
        return f"{self.name}@{domain}"

    @classmethod
    def anonymous_user(cls):
        """Class method — повертає об'єкт з ім'ям Anonymous"""
        return cls("Anonymous") if cls.total_names == 0 else cls("Anonymous")

    @staticmethod
    def say_hello(message: str = "Hello to everyone!") -> str:
        """Static method"""
        return f"You say: {message}"

    def name_length(self) -> int:
        """Повертає кількість букв в імені"""
        return len(self.name)

    @property
    def full_name(self) -> str:
        """Новa властивість: User #<id>: <name> (<email>)"""
        return f"User #{self.my_id}: {self.name} ({self.my_email})"

    def save_to_file(self, filename: str = "users.txt"):
        """Додає запис у файл (додаємо новий рядок)"""
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{self.full_name}\n")


if __name__ == "__main__":
    print("Розпочинаємо створювати обєкти!")

    names = ("Bohdan", "Marta", None, "Юлія")  # додала своє ім'я приклад
    all_names = {}
    for name in names:
        try:
            obj = MyName(name)
            all_names[name] = obj
        except ValueError as e:
            print(f"Помилка при створенні об'єкта для '{name}': {e}")

    for orig_name, me in all_names.items():
        print(f"""{">*<"*8}
Об'єкт: {me}
Ім'я: {me.name} / id: {me.my_id}
whoami (property): {me.whoami}
email (property): {me.my_email}
create_email() з доменом example.com: {me.create_email('example.com')}
Static say_hello(): {MyName.say_hello('Привіт від студента!')}
Кількість букв в імені: {me.name_length()}
full_name: {me.full_name}
{"<*>"*8}""")

    print(f"Ми створили {MyName.total_names} об'єкт(ів) загалом.")
    # приклад збереження першого користувача у файл
    first = next(iter(all_names.values()))
    first.save_to_file("users.txt")
    print("Перший користувач збережений у users.txt")
    if __name__ == "__main__":
       print("Розпочинаємо створювати об'єкти!")

    names = ("Bohdan", "Marta", None, "Юлія")  # додала своє ім'я приклад
    all_names = {}
    for name in names:
        try:
            obj = MyName(name)
            all_names[name] = obj
        except ValueError as e:
            print(f"Помилка при створенні об'єкта для '{name}': {e}")

    for orig_name, me in all_names.items():
        print(f"""{">*<"*8}
Об'єкт: {me}
Ім'я: {me.name} / id: {me.my_id}
whoami (property): {me.whoami}
email (property): {me.my_email}
create_email() з доменом example.com: {me.create_email('example.com')}
Static say_hello(): {MyName.say_hello('Привіт від студента!')}
Кількість букв в імені: {me.name_length()}
full_name: {me.full_name}
{"<*>"*8}""")

    print(f"Ми створили {MyName.total_names} об'єкт(ів) загалом.")
    first = next(iter(all_names.values()))
    first.save_to_file("users.txt")
    print("Перший користувач збережений у users.txt")