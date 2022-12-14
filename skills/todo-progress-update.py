from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill
from dal.azure_table_repository import AzureTableRepository


@add_skill('/todo-progress-update')
def get(message_request: MessageRequest):

    # /todo-progress-update <row_key> <prgress>
    msg_array = message_request.message.split()
    row_key = msg_array[1]
    progress = msg_array[2]

    repo = AzureTableRepository('todos')
    update_event = {
        u'PartitionKey': 'todo-items',
        u'RowKey': row_key,
        u'Progress': progress,
    }
    repo.update(model=update_event)

    return [
        TextSendMessage(text=f'已更新完成度')
    ]
