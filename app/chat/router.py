from fastapi import APIRouter
import os

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import InMemorySaver

from .tools import (
    tracking_tool,
    refund,
    complaint,
    escalation,
    hotel_search,
    flight_search
)

from .model import ChatResponse, UserInput

chat_router = APIRouter()

checkpointer = InMemorySaver()


@chat_router.post("/chat")
def chat(user_input: UserInput):

    model = ChatOllama(
        model=os.environ["MODEL"],
        base_url=os.environ["OLLAMA_URL"],
        temperature=0
    )

    agent = create_agent(
        model=model,
        tools=[
            tracking_tool,
            refund,
            complaint,
            escalation,
            hotel_search,
            flight_search
        ],
        checkpointer=checkpointer,

        # IMPORTANT
        response_format=ToolStrategy(ChatResponse)
    )

    system_message = """
    You are an AI Powered Customer Support Assistant.

    Always respond using the structured output schema.
    """

    response = agent.invoke(
        {
            "messages": [
                SystemMessage(content=system_message),
                HumanMessage(content=user_input.message)
            ]
        },
        config={
            "configurable": {
                "thread_id": user_input.thread_id
            }
        }
    )

    print(response)

    structured = response.get("structured_response")

    if structured is None:
        return {
            "error": "No structured response returned",
            "raw_response": str(response)
        }

    return (
        structured.model_dump()
        if hasattr(structured, "model_dump")
        else structured
    )