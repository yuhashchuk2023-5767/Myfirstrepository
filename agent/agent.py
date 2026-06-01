from abc import ABC, abstractmethod
from google.adk.agents import Agent


# =====================================================
# OOP ЧАСТИНА
# =====================================================

class Transport(ABC):
    def __init__(self, route_number: str, departure: str):
        self.route_number = route_number
        self.departure = departure

    @abstractmethod
    def get_schedule(self) -> dict:
        pass


class Bus(Transport):
    def __init__(self, route_number: str, departure: str, stops: list[str]):
        super().__init__(route_number, departure)
        self.stops = stops

    def get_schedule(self) -> dict:
        return {
            "type": "Bus",
            "route_number": self.route_number,
            "departure": self.departure,
            "stops": self.stops
        }


class Train(Transport):
    def __init__(self, route_number: str, departure: str, stations: list[str], travel_time_min: int):
        super().__init__(route_number, departure)
        self.stations = stations
        self.travel_time_min = travel_time_min

    def get_schedule(self) -> dict:
        return {
            "type": "Train",
            "route_number": self.route_number,
            "departure": self.departure,
            "stations": self.stations,
            "travel_time_min": self.travel_time_min
        }


class Schedule:
    def __init__(self):
        self.__routes: dict[str, Transport] = {}  # інкапсуляція

    def add_route(self, transport: Transport):
        self.__routes[transport.route_number] = transport

    def find_route(self, route_number: str) -> Transport | None:
        return self.__routes.get(route_number)

    def list_routes(self) -> list[dict]:
        return [t.get_schedule() for t in self.__routes.values()]


# =====================================================
# TOOL (AI ФУНКЦІЯ ДЛЯ АГЕНТА)
# =====================================================

def get_transport_schedule(route_number: str) -> dict:
    schedule = Schedule()

    # наповнення даними
    schedule.add_route(Bus("11", "08:30", ["Вокзал", "Центр", "Університет"]))
    schedule.add_route(Bus("4A", "07:15", ["Сихів", "Ринок", "Оперний"]))
    schedule.add_route(Train("705", "06:00", ["Львів", "Перемишль"], 150))
    schedule.add_route(Train("12", "21:40", ["Львів", "Київ"], 520))

    route = schedule.find_route(str(route_number))

    if route:
        result = route.get_schedule()
        result["found"] = True
        return result

    return {"found": False}


# =====================================================
# ROOT AGENT (ГОЛОВНЕ ДЛЯ ADK)
# =====================================================

root_agent = Agent(
    name="transport_agent",
    description="Агент розкладу громадського транспорту",
    instruction=(
        "Ти є помічником з громадського транспорту. "
        "Надавай інформацію про маршрути, зупинки та час у дорозі. "
        "Відповідай виключно українською мовою."
    ),
    tools=[get_transport_schedule]
)