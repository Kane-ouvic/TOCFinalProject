from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill
from dal.azure_table_repository import AzureTableRepository

@add_skill('/invoice-start')
def get(message_request: MessageRequest):
    
    repo = AzureTableRepository("users")
    
    user = list(repo.get(f"RowKey eq '{message_request.user_id}'"))
    
    # 更新使用者當前對話場景為核對發票
    user[0]['CurrentIntent'] = '/invoice-compare'
    repo.update(user[0])
    
    text = TextSendMessage(text="請開始輸入三碼數字")
    
    return [
        text
    ]
