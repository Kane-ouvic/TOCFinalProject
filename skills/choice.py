from linebot.models import TextSendMessage
from linebot.models.template import ButtonsTemplate, TemplateSendMessage
from linebot.models.actions import MessageAction
from models.message_request import MessageRequest
from skills import add_skill
import random


@add_skill('/買什麼')
def get(message_request: MessageRequest):

    # /吃什麼 烤雞.炸雞.鹹酥雞

    # 處理字串
    choices_str = message_request.message.replace("/買什麼 ", "")
    choices = choices_str.split(',')
    print(choices)

    # 隨機挑選一個項目
    result = random.choice(choices)
    print(result)

    # 處理回傳訊息
    message = TemplateSendMessage(
        alt_text='買什麼會贏',
        template=ButtonsTemplate(
            title='買什麼會贏?',
            text=f'就決定買 {result} 來贏錢吧!',
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
