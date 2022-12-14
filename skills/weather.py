import json
import os
from linebot.models import FlexSendMessage
from models.message_request import MessageRequest
from skills import add_skill
import requests


@add_skill('/天氣預報')
def get(message_request: MessageRequest):

    # /天氣預報 臺北市
    city = message_request.message.split()[1]

    # 串接 openAPI
    code = 'CWB-F614421C-F59C-42D3-B1F9-6F0E327D2DE7'
    url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={code}&format=JSON&locationName={city}"
    payload = {}
    headers = {
        'accept': 'application/json',
        'Cookie': 'TS01dbf791=0107dddfefba206e5b7f0c1ed580514ff49ac420ad0102f08071800ff1e5302948e45793cd45931b688552680395d734c467db30fe'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()

    # 處理回傳的JSON
    location = list(data['records']['location'])
    print(location)
    elements = location[0]['weatherElement']

    # 舒適度
    ci = list(filter(lambda c: c['elementName'] == 'CI', elements))[0]
    # 降雨機率
    pop = list(filter(lambda c: c['elementName'] == 'PoP', elements))[0]
    # 最低溫度
    minT = list(filter(lambda c: c['elementName'] == 'MinT', elements))[0]
    # 最高溫度
    maxT = list(filter(lambda c: c['elementName'] == 'MaxT', elements))[0]

    # 美化回傳字串
    flex = json.load(
        open(os.getcwd() + '\\skills\\' 'weather.json', 'r', encoding='utf-8'))

    for i in range(3):
        item = json.load(
            open(os.getcwd() + '\\skills\\' 'weather-item.json', 'r', encoding='utf-8'))

        item['body']['contents'][0]['text'] = f"{city} - {ci['time'][i]['parameter']['parameterName']}"
        item['body']['contents'][1]['text'] = f"{ci['time'][i]['startTime']} ~ {ci['time'][i]['endTime']}"
        item['body']['contents'][2]['contents'][0][
            'text'] = f"降雨機率 {pop['time'][i]['parameter']['parameterName']}%"
        min = minT['time'][i]['parameter']['parameterName'] + '°C'
        max = maxT['time'][i]['parameter']['parameterName'] + '°C'
        item['body']['contents'][3]['contents'][0][
            'contents'][0]['text'] = f"{min} ~ {max}"
        flex['contents'].append(item)

    msg = FlexSendMessage(alt_text='天氣預報', contents=flex)

    return [
        msg
    ]
