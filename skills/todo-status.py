from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill

@add_skill('/todo-status')
def get(message_request: MessageRequest):
    
    # /todo-status {row_key}
    msg_array = message_request.message.split()
    row_key = msg_array[1]
    
    next_flow = '/todo-status-update'
    buttons_template_message = TemplateSendMessage(
        alt_text='更新代辦事項狀態',
        template=ButtonsTemplate(
            text='請選擇更新狀態',
            actions=[
                PostbackAction(
                    label='待處理',
                    data=f'{next_flow} { row_key} 0'
                ),
                PostbackAction(
                    label='進行中',
                    data=f'{next_flow} { row_key} 1'
                ),
                PostbackAction(
                    label='已完成',
                    data=f'{next_flow} { row_key} 2'
                ),
                PostbackAction(
                    label='封存',
                    data=f'{next_flow} { row_key} 3'
                )
            ]
        )
    )

    return [
        buttons_template_message
    ]
