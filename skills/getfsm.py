from typing import Text
from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from linebot.models import ImageSendMessage
from skills import add_skill


@add_skill('/fsm')
def get(message_request: MessageRequest):
    return [
        ImageSendMessage(original_content_url='https://i.imgur.com/QNIQUDp.png',
    preview_image_url='https://i.imgur.com/QNIQUDp.png')
    ]
