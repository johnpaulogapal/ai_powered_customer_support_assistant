import os
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from fastapi import Depends

from .tools import (
    tracking_tool,
    refund,
    complaint,
    escalation,
    hotel_search,
    flight_search,
)
from .model import ChatResponse
from typing import Annotated


TOOL_UI_MAP = {
    "hotel_search": {"intent": "hotel_search", "ui_type": "hotel_search_page"},
    "flight_search": {"intent": "flight_search", "ui_type": "flight_search_page"},
    "refund": {"intent": "refund", "ui_type": "refund_page"},
    "complaint": {"intent": "complaint", "ui_type": "complaint_page"},
    "tracking_tool": {"intent": "tracking", "ui_type": "tracking_page"},
    "escalation": {"intent": "escalation", "ui_type": "escalation_page"},
}


class ChatService:
    def __init__(self):
        self.llm = ChatOllama(
            model=os.environ["MODEL"],
            base_url=os.environ["OLLAMA_URL"],
            temperature=0,
        )

        self.agent = create_agent(
            model=self.llm,
            tools=[
                tracking_tool,
                refund,
                complaint,
                escalation,
                hotel_search,
                flight_search,
            ],
        )

        self.structured_llm = self.llm.with_structured_output(ChatResponse)

    def run(self, message: str, thread_id: str):

        system_message = SystemMessage(content="You are a customer support assistant.")

        result = self.agent.invoke(
            {"messages": [system_message, HumanMessage(content=message)]},
            config={"configurable": {"thread_id": thread_id}},
        )

        tool_name = None
        for m in result["messages"]:
            if hasattr(m, "tool_calls") and m.tool_calls:
                tool_name = m.tool_calls[0]["name"]

        final_text = result["messages"][-1].content

        structured = self.structured_llm.invoke(f"""
        Convert into schema:

        {final_text}
        """)

        mapping = TOOL_UI_MAP.get(
            tool_name or "", {"intent": "general", "ui_type": "general_page"}
        )

        return {
            "intent": mapping["intent"],
            "tool_called": tool_name,
            "ui_type": mapping["ui_type"],
            "message": structured.message,
            "data": structured.data,
        }


def get_chat_service():
    return ChatService()


ChatServiceDep = Annotated[ChatService, Depends(get_chat_service)]
