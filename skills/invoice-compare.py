from linebot.models import TextSendMessage
from linebot.models.flex_message import FlexSendMessage
from dal.azure_table_repository import AzureTableRepository
from models.message_request import MessageRequest
from skills import add_skill
import uuid
import json
import os

@add_skill('/invoice-compare')
def get(message_request: MessageRequest):
        
    # /invoice-compare 123
    msg_array = message_request.intent.split()
    number = msg_array[1]
    
    if len(number) != 3 :
        return [ TextSendMessage(text=f'您輸入的非三碼數字')]
    
    if number.isnumeric() == False:
        return [ TextSendMessage(text=f'{number} 非數字')]
    
    # 當期中獎發票
    answer = [555, 666, 777]
    
    result = int(number) in answer
    
    # 寫入資料庫
    create_event = {
            u'PartitionKey': message_request.user_id,
            u'RowKey': str(uuid.uuid1()),
            u'Result': result,
            u'CalcDate': ''
    }
    repo = AzureTableRepository('invoices')
    repo.create(create_event)
    
    entities = repo.get(f"PartitionKey eq '{message_request.user_id}' and CalcDate eq ''")
    results = list(entities)
    results_wins = list(filter(lambda c: c['Result'] == True, results))
    
    # Flex Message (含兌獎結束的按鈕)
    
    flex = json.load(
        open(os.getcwd() + '\\skills\\' 'invoice-compare.json', 'r', encoding='utf-8'))
    
    if result == True:
        flex['body']['contents'][2]['text'] = f'中獎 !!! 累積中獎數: {len(results_wins)}/{len(results)}'
        msg = FlexSendMessage(alt_text='兌獎結果', contents=flex)
    else:
        flex['body']['contents'][2]['text'] = f'未中獎 ... 累積中獎數: {len(results_wins)}/{len(results)}'
        msg = FlexSendMessage(alt_text='兌獎結果', contents=flex)
    
    return[
        msg
    ]
    