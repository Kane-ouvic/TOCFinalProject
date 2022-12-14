from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('/todo-progress')
def get(message_request: MessageRequest):
    
    # /todo-progress {row_key}
    msg_array = message_request.message.split()
    row_key = msg_array[1]
    
    next_flow = '/todo-progress-update'
    low = CarouselColumn(
        title='完事起步難，一步一腳印',
        text='請選擇完成度',
        actions=[
            PostbackAction(
                label='0%',
                data=f'{next_flow} {row_key} 0'
            ),
            PostbackAction(
                label='25%',
                data=f'{next_flow} {row_key} 25'
            ),
        ]
    )
    
    mid = CarouselColumn(
        title='再接再厲，超過一半了',
        text='請選擇完成度',
        actions=[
            PostbackAction(
                label='50%',
                data=f'{next_flow} {row_key} 50'
            ),
            PostbackAction(
                label='75%',
                data=f'{next_flow} {row_key} 75'
            ),
        ]
    )
    
    high = CarouselColumn(
        title='最後一口氣，把他搞定',
        text='請選擇完成度',
        actions=[
            PostbackAction(
                label='95%',
                data=f'{next_flow} {row_key} 95'
            ),
            PostbackAction(
                label='100%',
                data=f'{next_flow} {row_key} 100'
            ),
        ]
    )
    
    carousel_template_message = TemplateSendMessage(
        alt_text='更新待辦事項完成度',
        template=CarouselTemplate(
            columns=[
                low,
                mid,
                high
            ]
        )
    )

    return [
        carousel_template_message
    ]
