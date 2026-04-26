from google.adk.agents.llm_agent import Agent

def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Обчислює площу прямокутника.
    """
    return width * height

def calculate_circle_area(radius: float) -> float:
    """
    Обчислює площу кола.
    """
    import math
    return math.pi * radius ** 2

def calculate_cube_volume(side: float) -> float:
    """
    Обчислює об'єм куба.
    """
    return side ** 3

def calculate_triangle_area(base: float, height: float) -> float:
    """
    Обчислює площу трикутника.
    """
    return 0.5 * base * height


root_agent = Agent(
    model='gemini-2.5-flash',
    name='math_agent',
    description="Виконує математичні обчислення.",
    instruction="""
    Ти математичний асистент.
    Використовуй інструменти для обчислень.
    Пояснюй хід розв'язання.
    Відповідай українською мовою.
    """,
    tools=[
        calculate_rectangle_area,
        calculate_circle_area,
        calculate_cube_volume,
        calculate_triangle_area  
    ],
)
