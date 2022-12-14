from linebot.models import *
from linebot.models.template import *
from linebot.models.actions import *
from models.message_request import MessageRequest
from skills import add_skill
from dal.azure_table_repository import AzureTableRepository
import json
import os


@add_skill('/todo-list')
def get(message_request: MessageRequest):

    # 取得所有資訊
    repo = AzureTableRepository('todos')
    entities = repo.get('')

    flex = json.load(
        open(os.getcwd() + '\\skills\\' 'flex_carousel.json', 'r', encoding='utf-8'))

    for entity in entities:
        print(entity)
        item = json.load(
            open(os.getcwd() + '\\skills\\' 'todo-item.json', 'r', encoding='utf-8'))

        # 待辦事項名稱
        item['body']['contents'][0]['contents'][0]['text'] = entity['Name']
        # 狀態
        item['header']['contents'][0]['text'] = getStatusName(entity['Status'])
        # 完成度
        item['header']['contents'][1]['text'] = str(entity['Progress']) + '%'
        item['header']['contents'][2]['contents'][0]['width'] = str(
            entity['Progress']) + '%'
        # 到期日期
        if entity["ExpireDate"] == '':
            item['body']['contents'][1]['contents'][0]['text'] = '未設定日期'
        else:
            item['body']['contents'][1]['contents'][0]['text'] = entity["ExpireDate"]

        flex['contents'].append(item)

        item['footer']['contents'][0]['action'][
            'data'] = f'/todo-status {entity["RowKey"]}'
        item['footer']['contents'][1]['action'][
            'data'] = f'/todo-progress {entity["RowKey"]}'
        item['footer']['contents'][2]['action']['data'] = f'/todo-date {entity["RowKey"]}'

    # 針對這些待辦事項處理訊息
    msg = FlexSendMessage(alt_text='待辦事項', contents=flex)

    return [
        msg
    ]


def getStatusName(status: int):
    if status == 0:
        return '待處理'
    elif status == 1:
        return '進行中'
    elif status == 2:
        return '已完成'
    elif status == 3:
        return '已封存'
