from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill
from dal.azure_table_repository import AzureTableRepository
import uuid

@add_skill('/todo-create')
def get(message_request: MessageRequest):
    
    # 使用 Azure Table Repo
    repo = AzureTableRepository('todos')
    
    # 取得使用者傳入的待辦事項名稱
    # /todo-create 讀一本書
    msg_array = message_request.message.split()
    event_name = msg_array[1]
    
    # 寫入資料庫
    create_event = {
            u'PartitionKey': 'todo-items',
            u'RowKey': str(uuid.uuid1()),
            u'Name': event_name, #待辦事項名稱
            u'Progress': 0, #完成度
            u'Status': 0, #0待處理,1進行中,2已完成,3封存
            u'ExpireDate': '', #到期日期
    }
    repo.create(create_event)
    
    return [
        TextSendMessage(text='已新增待辦事項')
    ]
