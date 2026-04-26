from google.adk.agents.llm_agent import Agent

def explain_concept(concept: str, level: str = "beginner") -> dict:
    explanations = {
        "beginner": f"Базове пояснення: {concept}",
        "intermediate": f"Середній рівень: {concept}",
        "advanced": f"Поглиблене пояснення: {concept}"
    }
    return {
        "concept": concept,
        "level": level,
        "explanation": explanations.get(level, "Невідомий рівень")
    }

def check_syntax(code: str, language: str = "python") -> dict:
    if not code.strip():
        return {"status": "error", "message": "Код порожній"}
    return {"status": "success", "message": "Синтаксис виглядає нормально"}

root_agent = Agent(
    model="gemini-2.5-flash",
    name="student_helper",
    description="Помічник для студентів",
    instruction="""
Ти викладач програмування.
Пояснюй просто, давай приклади Python.
Відповідай українською.
""",
    tools=[explain_concept, check_syntax],
)
