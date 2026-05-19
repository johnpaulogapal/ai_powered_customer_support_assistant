from pydantic import BaseModel, Field
from typing import Optional, Any


class ChatResponse(BaseModel):
    """Final structured response returned by the assistant."""

    intent: str = Field(default="general", description="Intent of the assistant")

    tool_called: Optional[str] = Field(default=None, description="Used tool name")

    ui_type: Optional[str] = Field(default=None, description="Frontend page type")

    message: str = Field(description="Assistant response summary")

    data: Optional[dict[str, Any]] = Field(
        default=None, description="Structured tool response data"
    )


class UserInput(BaseModel):
    message: str
    thread_id: str
