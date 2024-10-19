from ..schemas.base import CreateMessageDto
import httpx #если чо добавить в реквайрементс 
import json 
from ..utils.coze_data_parser import parse_coze_data
from fastapi import HTTPException
import os

URL = "https://api.coze.com/v3/chat"

async def create_message(create_message_dto: CreateMessageDto):
    user_id = create_message_dto.user_id
    text = create_message_dto.text
    conversation_id = create_message_dto.conversation_id
    
    bot_id = os.getenv("COZE_BOT_ID")
    coze_api_token = os.getenv("COZE_API_TOKEN")
    print(bot_id)
    print(coze_api_token)

    request_data = {
        "stream": True,
        "bot_id": bot_id,
        "user_id": user_id,
        "additional_messages": [{
            "role": "user",
            "content_type": "text",
            "content": text
        }] 
    }
    params = {
        "conversation_id": conversation_id
    }
    headers = {
        "Authorization": "Bearer " + coze_api_token,
        "Content-Type": "application/json"
    }
   
    async with httpx.AsyncClient() as client:
        response = await client.post(URL, json=request_data, headers=headers, params=params)
    print(response)

    parsed_events = parse_coze_data(response.text)
    completed_message = next((event['data'] for event in parsed_events if event['event'] == "conversation.message.completed"), None)
    failed_message = next((event['data'] for event in parsed_events if event['event'] == "conversation.chat.failed"), None)

    if completed_message:
        return completed_message

    if failed_message:
        raise HTTPException(status_code=400, detail=failed_message)
    