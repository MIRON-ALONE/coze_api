"""Define response model for the endpoint version."""
from pydantic import BaseModel, Field  # type: ignore
from typing import Optional

class VersionResponse(BaseModel):
    """Response for version endpoint."""
    version: str = Field(..., example="1.0.0")

class CreateMessageDto(BaseModel):
    user_id: str
    text: str
    conversation_id: Optional[str] = None

