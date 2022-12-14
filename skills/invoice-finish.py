from linebot.models import TextSendMessage
from models.message_request import MessageRequest
from skills import add_skill
from dal.azure_table_repository import AzureTableRepository
from datetime import date

@add_skill('/invoice-finish')
def get(message_request: MessageRequest):
    
    # 使用者當前兌獎紀錄撈出來
    repo = AzureTableRepository('invoices')
    entities = repo.get(f"PartitionKey eq '{message_request.user_id}' and CalcDate eq ''")
    results = list(entities)
    results_wins = list(filter(lambda c: c['Result'] == True, results))
    
    # 批次更新 (結算)
    for item in results:
        item['CalcDate'] = date.today().strftime('%Y-%m-%d')
    repo.batch_update(results)
    
    # 更新意圖
    repo = AzureTableRepository("users")
    user = list(repo.get(f"RowKey eq '{message_request.user_id}'"))
    user[0]['CurrentIntent'] = ''
    repo.update(user[0])
    
    text = TextSendMessage(text=f'本次發票兌獎結果: {len(results_wins)}/{len(results)}')
    
    return [
        text
    ]
