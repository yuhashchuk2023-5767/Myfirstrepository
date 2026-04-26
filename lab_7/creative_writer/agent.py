from google.adk.agents.llm_agent import Agent
from google.genai.types import GenerateContentConfig

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    return f"Напиши історію про '{theme}' з {characters} персонажами"

root_agent = Agent(
    model="gemini-1.5-flash",
    name="creative_writer",
    description="Пише історії",
    instruction="""
Ти письменник.
Пиши цікаві історії українською.
Додавай емоції та сюжетні повороти.
""",
    tools=[generate_story_prompt],
    config=GenerateContentConfig(
        temperature=1.3,
        top_p=0.95,
        top_k=40
    )
)