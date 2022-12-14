from linebot.models import TextSendMessage
from linebot.models.template import ButtonsTemplate, TemplateSendMessage
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill
import random


@add_skill('/吃什麼')
def get(message_request: MessageRequest):

    # /吃什麼 烤雞.炸雞.鹹酥雞

    # 處理字串
    foods_str = message_request.message.replace("/吃什麼 ", "")
    foods = foods_str.split('.')
    print(foods)

    # 隨機挑選一個項目
    result = random.choice(foods)
    print(result)

    # 處理回傳訊息
    message = TemplateSendMessage(
        alt_text='今天吃什麼',
        template=ButtonsTemplate(
            title='今天吃什麼?',
            text=f'就決定吃 {result} 吧!',
            actions=[
                MessageAction(
                    label='我不要，換一個',
                    text=message_request.message
                )
            ]
        )
    )

    return [
        message
    ]
