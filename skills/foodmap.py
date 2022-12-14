import json
import os
from typing import Text
from linebot.models import FlexSendMessage
from models.message_request import MessageRequest
from skills import add_skill
from helpers import google_map_estimation, google_map_search


@add_skill('/foodmap')
def get(message_request: MessageRequest):

    msg_array = message_request.message.split()
    lat, lon = msg_array[1], msg_array[2]
    location = (lat, lon)

    radius = 1000  # meter
    A = google_map_search.GoogleMapSearch(location, radius)
    A.get_info()
    print(A.result)

    items = json.load(
        open(os.getcwd() + '\\skills\\' 'flex_carousel.json', 'r', encoding='utf-8'))

    for i, row in A.result.head(12).iterrows():
        destination = row['name']
        destination_id = row['place_id']
        destination_location = row['geometry']
        des_geo = (destination_location['location']['lat'],
                   destination_location['location']['lng'])
        estimation = google_map_estimation.Estimation()
        cost_time, guide_url = estimation.evaluate(
            location, des_geo, destination_id)

        item = json.load(
            open(os.getcwd() + '\\skills\\' 'foodmap-item.json', 'r', encoding='utf-8'))

        item['body']['contents'][0]['text'] = destination
        item['body']['contents'][2]['contents'][0]['contents'][0]['text'] = cost_time
        rate = round(row['rating'])

        for k in range(1, 6):
            if (rate >= k):
                url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            else:
                url = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
            icon = {
                "type": "icon",
                "size": "xs",
                "url": url
            }
            item['body']['contents'][1]["contents"].append(icon)

        icon_text = {
            "type": "text",
            "text": str(rate),
            "size": "xs",
            "color": "#8c8c8c",
            "margin": "md",
            "flex": 0
        }
        item['body']['contents'][1]["contents"].append(icon_text)

        items['contents'].append(item)
        item['footer']['contents'][0]['action']['uri'] = guide_url

    return [
        FlexSendMessage(alt_text='美食地圖', contents=items)
    ]
