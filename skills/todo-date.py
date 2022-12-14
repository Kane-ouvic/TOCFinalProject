from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill
from dal.azure_table_repository import AzureTableRepository
@add_skill('/todo-date')
def get(message_request: MessageRequest):

    # /todo-date <row_key> <date>
    msg_array = message_request.message.split()
    row_key = msg_array[1]
    date = msg_array[2]

    repo = AzureTableRepository('todos')
    
    update_event = {
        u'PartitionKey': 'todo-items',
        u'RowKey': row_key,
        u'ExpireDate': date,
    }
    repo.update(model=update_event)

    return [
        TextSendMessage(text=f'已更新到期日期')
    ]
