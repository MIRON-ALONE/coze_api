"""Endpoints for getting version information."""
from typing import Any
from fastapi import APIRouter, Body
from ..schemas.base import VersionResponse, CreateMessageDto
from ..version import __version__
from ..services.messages import create_message

base_router = APIRouter()


@base_router.get("/version", response_model=VersionResponse)
async def version() -> Any:
    """Provide version information about the web service.

    \f
    Returns:
        VersionResponse: A json response containing the version number.
    """
    return VersionResponse(version=__version__)



@base_router.post('/create_meassge')
async def create_message_request(create_message_dto: CreateMessageDto = Body(...)):
    result = await create_message(create_message_dto)
    return result
