from abc import ABC, abstractmethod
from typing import List, Dict, Optional

# ======================
# OOP: ABSTRACTION
# ======================
class Transport(ABC):
    def __init__(self, route_number: str, departure: str):
        self.route_number = route_number
        self.departure = departure

    @abstractmethod
    def get_schedule(self) -> dict:
        pass


# ======================
# INHERITANCE + POLYMORPHISM
# ======================
class Bus(Transport):
    def __init__(self, route_number: str, departure: str, stops: List[str]):
        super().__init__(route_number, departure)
        self.stops = stops

    def get_schedule(self) -> dict:
        return {
            "type": "Bus",
            "route": self.route_number,
            "departure": self.departure,
            "stops": self.stops
        }


class Train(Transport):
    def __init__(self, route_number: str, departure: str, stations: List[str], travel_time_min: int):
        super().__init__(route_number, departure)
        self.stations = stations
        self.travel_time_min = travel_time_min

    def get_schedule(self) -> dict:
        return {
            "type": "Train",
            "route": self.route_number,
            "departure": self.departure,
            "stations": self.stations,
            "travel_time_min": self.travel_time_min
        }


# ======================
# ENCAPSULATION
# ======================
class Schedule:
    def __init__(self):
        self.__routes: Dict[str, Transport] = {}

    def add_route(self, transport: Transport):
        self.__routes[transport.route_number] = transport

    def find_route(self, route_number: str) -> Optional[Transport]:
        return self.__routes.get(route_number)


# ======================
# TOOL FUNCTION
# ======================
def get_transport_schedule(route_number: str) -> dict:
    schedule = Schedule()

    schedule.add_route(Bus("1", "08:00", ["A", "B", "C"]))
    schedule.add_route(Bus("2", "09:00", ["D", "E", "F"]))
    schedule.add_route(Train("10", "07:30", ["Lviv", "Kyiv"], 300))

    route = schedule.find_route(route_number)

    if route is None:
        return {"found": False}

    return route.get_schedule()


# ======================
# FORMAT OUTPUT (гарний текст)
# ======================
def format_schedule(data: dict) -> str:
    if not data or data.get("found") is False:
        return " Маршрут не знайдено."

    if data["type"] == "Bus":
        return (
            f" Тип: Автобус\n"
            f" Маршрут: {data['route']}\n"
            f" Відправлення: {data['departure']}\n"
            f" Зупинки: {' → '.join(data['stops'])}"
        )

    if data["type"] == "Train":
        return (
            f" Тип: Потяг\n"
            f" Маршрут: {data['route']}\n"
            f" Відправлення: {data['departure']}\n"
            f" Час у дорозі: {data['travel_time_min']} хв\n"
            f" Станції: {' → '.join(data['stations'])}"
        )

    return " Невідомий тип транспорту"


# ======================
# CHAT AGENT (FIXED LOGIC)
# ======================
def chat_with_agent(user_input: str) -> str:
    route_number = None

    # правильний парсинг номеру маршруту
    for r in ["1", "2", "10"]:
        if f"маршрут {r}" in user_input.lower():
            route_number = r

    if route_number:
        data = get_transport_schedule(route_number)
    else:
        data = {"found": False}

    return (
        " ТРАНСПОРТНИЙ ПОМІЧНИК\n"
        "──────────────────────\n"
        f" Запит: {user_input}\n\n"
        f"{format_schedule(data)}\n\n"
        " Поради:\n"
        "1) Який маршрут найшвидший?\n"
        "2) Які зупинки на маршруті 2?\n"
        "3) О котрій відправляється потяг 10?\n"
    )


# ======================
# RUN LOOP
# ======================
if __name__ == "__main__":
    print("🚍 Транспортний агент запущено (exit для виходу)")

    while True:
        user = input("Ти: ")

        if user.lower() == "exit":
            break

        print(chat_with_agent(user))