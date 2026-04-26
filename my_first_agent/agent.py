import logging
import datetime
from google.adk.agents.llm_agent import Agent

logging.basicConfig(level=logging.INFO)

def get_current_time(city: str) -> dict:
    """Повертає поточний час у вказаному місті."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return {"status": "success", "city": city, "time": current_time}

def calculate_triangle_area(base: float, height: float) -> float:
    """Обчислює площу трикутника за основою та висотою."""
    return 0.5 * base * height

root_agent = Agent(
    model='gemini-2.5-flash',
    name='time_agent',
    description="Агент для часу та математики",
    instruction="Відповідай українською мовою. Використовуй інструменти для запитів про час або площу.",
    tools=[get_current_time, calculate_triangle_area],
)