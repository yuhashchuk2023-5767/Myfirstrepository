from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext

def save_user_preference(tool_context: ToolContext, key: str, value: str):
    state = tool_context.state.get(key, [])
    tool_context.state[key] = state + [value]
    return {"saved": True}

def recall_preference(tool_context: ToolContext, key: str):
    return {"value": tool_context.state.get(key, [])}

root_agent = Agent(
    model="gemini-2.5-flash",
    name="conversation_agent",
    description="Пам’ятає користувача",
    instruction="""
Запам’ятовуй ім’я, хобі, колір користувача.
Використовуй інструменти пам’яті.
""",
    tools=[save_user_preference, recall_preference],
)