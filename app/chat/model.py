from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    """Final structured response returned by the assistant."""
    intent: str = Field(description="Intention of the assistant")
    tool_called: str = Field(description="Used tool name")
    ui_type: str = Field(description="Page type is the name of the page user is being redirected. Tool name = Page name but with page, example hotel_search_page")
    message: str = Field(description="Summarize the description what the tool has done")
    data: dict = Field(description="The data of the response of the llm")


class UserInput(BaseModel):
    message: str
    thread_id: str