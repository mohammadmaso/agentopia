from langgraph.graph.state import CompiledStateGraph

from agents.chatbot import chatbot
from agents.research_assistant import research_assistant
from agents.text2sql import text2sql

DEFAULT_AGENT = "research-assistant"


agents: dict[str, CompiledStateGraph] = {
    "chatbot": chatbot,
    "research-assistant": research_assistant,
    "text2sql": text2sql,
}
