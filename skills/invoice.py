from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('/invoice')
def get(message_request: MessageRequest):
    
    buttons_template_message = TemplateSendMessage(
        alt_text='是否要開始發票對獎?',
        template=ButtonsTemplate(
            title='您確定要開始兌獎嗎?',
            text='點選開始兌獎後請開始輸入3碼數字',
            actions=[
                PostbackAction(
                    label='開始兌獎',
                    data='/invoice-start'
                )
            ]
        )
    )
    
    return [
        buttons_template_message
    ]
