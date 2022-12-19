from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill


@add_skill('/testbutton')
def get(message_request: MessageRequest):

    buttons_template_message = TemplateSendMessage(
        alt_text='Button',
        template=ButtonsTemplate(
            title='測試按鈕',
            text='敘述.................',
            actions=[
                PostbackAction(
                    label='按鈕',
                    data='/hello'
                )
            ]
        )
    )

    return [
        buttons_template_message
    ]


# @add_skill('/testbutton-hello')
# def get(message_request: MessageRequest):

#     return [
#         TextSendMessage(text=f'Hello!!!!!!!!')
#     ]
