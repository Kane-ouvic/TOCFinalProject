import os
import re
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.params import Header
from starlette.requests import Request
from models.message_request import MessageRequest
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from skills import *
from skills import skills
from dal.azure_table_repository import AzureTableRepository

app = FastAPI()

load_dotenv()

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))


def get_message(request: MessageRequest):
    for pattern, skill in skills.items():
        if re.match(pattern, request.intent):
            return skill(request)
    request.intent = '{not_match}'
    return skills['{not_match}'](request)


@app.post("/api/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(
            status_code=400, detail="Invalid signature. Please check your channel access token/channel secret.")
    return 'OK'


@handler.add(event=MessageEvent, message=TextMessage)
def handle_message(event):
    msg_request = MessageRequest()
    msg_request.intent = event.message.text
    msg_request.message = event.message.text
    msg_request.user_id = event.source.user_id

    # 處理當前使用者對話場景
    current_intent = log_user(msg_request.user_id)
    if current_intent != '':
        msg_request.intent = f'{current_intent} {msg_request.message}'

    func = get_message(msg_request)
    line_bot_api.reply_message(event.reply_token, func)


@handler.add(event=UnfollowEvent)
def handle_message(event):
    print('unfollow', event)


@handler.add(event=FollowEvent)
def handle_message(event):
    print('follow', event)

    # 取得使用者個人資訊
    profile = line_bot_api.get_profile(event.source.user_id)
    print(profile.display_name)
    print(profile.user_id)
    print(profile.picture_url)
    print(profile.status_message)

    # 回傳歡迎訊息
    line_bot_api.reply_message(event.reply_token, TextSendMessage(f'Hi, 蔥'))


# @handler.add(event=MessageEvent, message=LocationMessage)
# def handle_message(event):
#     print('location', event)
#     print('-----')
#     print(event.message.latitude)
#     print(event.message.longitude)


@handler.add(event=MessageEvent, message=LocationMessage)
def handle_message(event):
    msg_request = MessageRequest()
    msg_request.intent = f"/foodmap {event.message.latitude} {event.message.longitude}"
    msg_request.message = f"/foodmap {event.message.latitude} {event.message.longitude}"
    msg_request.user_id = event.source.user_id
    func = get_message(msg_request)
    line_bot_api.reply_message(event.reply_token, func)


@handler.add(event=PostbackEvent)
def handle_message(event):
    print('postback', event.postback)
    msg_request = MessageRequest()
    msg_request.intent = event.postback.data
    msg_request.message = event.postback.data
    msg_request.user_id = event.source.user_id

    if event.postback.params != None:
        msg_request.intent = msg_request.intent + \
            ' ' + event.postback.params['date']
        msg_request.message = msg_request.message + \
            ' ' + event.postback.params['date']

    func = get_message(msg_request)
    line_bot_api.reply_message(event.reply_token, func)


def log_user(user_id):
    print(user_id)
    # 使用者資訊儲存到Azure Table
    profile = line_bot_api.get_profile(user_id)
    repo = AzureTableRepository('users')
    entities = repo.get(f"RowKey eq '{user_id}'")
    item = list(entities)
    if len(item) == 0:
        create = {
            u'PartitionKey': 'users',
            u'RowKey': user_id,
            u'DisplayName': profile.display_name,
            u'CurrentIntent': ''
        }
        repo.create(create)
        return ''
    else:
        update = {
            u'PartitionKey': 'users',
            u'RowKey': user_id,
            u'DisplayName': profile.display_name
        }
        repo.update(update)
        return item[0]['CurrentIntent']
