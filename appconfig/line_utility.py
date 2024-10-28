import requests
import json
from pprint import pprint
from appconfig import LINE_BOT_TOKEN, SEND_REPLY_MESSAGE_URL,GET_USER_PROFILE_URL, CHAT_PROMPT, UBIKE_GOOGLE_MAP_URL
from appconfig.db_utility import insertProfileInfo, updateLocked
from appconfig.openai_utility import openaiChatMessage
from appconfig.ubike_utility import ubikeDataframe, ubikeLocation
from appconfig.flex_message_utility import BubbleBuilder

def followEvent(event_data, source, reply_token):
    try:
        # print('into followEvent function...')

        match event_data['follow']['isUnblocked']:
            case False: # new friends, need insert into database
                # print('into followEvent new friends case...')

                # we need four items(user_type, user_id, display_name, picture_url)

                user_type = source['type']
                user_id = source['userId']

                # get user profile (display_name and picture_url)

                url_string = GET_USER_PROFILE_URL % (user_id)
                my_header = {'Authorization': LINE_BOT_TOKEN}
                response = requests.get(url=url_string,
                                        headers=my_header)
                profile_data = response.json()
                display_name = profile_data['displayName']
                picture_url = profile_data['pictureUrl']

                # database connection and insert profile information

                insertProfileInfo(user_id, user_type, display_name, picture_url)
                    
                # send reply_message to user

                message = '歡迎您加入好友 ~'
                sendTextReplyMessage(message, reply_token)

                # print('New friends event complete!!!')

            case True: # Unblocked
                # print('into followEvent unblocked case...')

                user_id = source['userId']

                # database connection and update Locked

                updateLocked('0', user_id)

                message = '歡迎您回來 ~'
                sendTextReplyMessage(message, reply_token)

                # print('Unblocked event complete!!!')

        # print('followEvent function complete!!!')

    except Exception as ex:
        print(f'!!! followEvent function error: {ex}')

def unfollowEvent(source):
    try:
        # print('into unfollowEvent function...')

        user_id = source['userId']
        # database connection and update Locked

        updateLocked('1', user_id)

        # print('unfollowEvent function complete!!!')
    except Exception as ex:
        print(f'!!! unfollowEvent function error: {ex}')

def messageEvent(event_data, reply_token):
    try:
        # print('into messageEvent function...')

        message_data = event_data['message']

        match message_data['type']:
            case 'text':
                # print('into messageEvent function text case...')
                # content = '請傳送位置資訊'
                
                content = message_data['text']
                chat_message = CHAT_PROMPT % (content)
                answer = openaiChatMessage(chat_message)
                sendTextReplyMessage(answer, reply_token)

            case 'location':
                # get longitude and latitude

                longitude = message_data['longitude'] # 經度
                latitude = message_data['latitude'] # 緯度

                # calculate distance and return json

                df = ubikeDataframe()
                json_file = ubikeLocation(df, longitude, latitude)
                data = json.loads(json_file)

                bubbles = []
                for station in data:
                    bubble = BubbleBuilder(
                            'Ubilk即時資料',
                            station['sna'],
                            f'{station['scity']}{station['sarea']}{station['ar']}',
                            str(station['sbi']),
                            str(station['bemp']),
                            station['mday'],
                            '查看地圖',
                            f'{UBIKE_GOOGLE_MAP_URL.format(lat = station['lat'], lng = station['lng'])}'
                        )
                    bubbles.append(bubble.createBubble())
                carousel = {
                    "type": "carousel",
                    "contents": bubbles
                }

                carousel_2 = json.dumps(carousel)
                result = json.loads(carousel_2)

                sendFlexMessage(result, reply_token)
            
            case 'sticker':
                package_id = '789'
                sticker_id = '10855'

                sendStickerReplyMessage(sticker_id, package_id, reply_token)

            case _:
                answer = '我們不接受此格式！！'

                sendTextReplyMessage(answer, reply_token)

        # print('messageEvent function complete!!!')

    except Exception as ex:
        print(f'!!! messageEvent function error: {ex}')

def sendTextReplyMessage(message, reply_token):
    try:
        # print('into sendTextReplyMessage function...')
        my_header = {
            'Content-Type': 'application/json',
            'Authorization': LINE_BOT_TOKEN
        }
        my_body = {
            'replyToken': reply_token,
            'messages' :[
                {
                    "type": "text",
                    "text": message
                }
            ]
        }

        requests.post(url=SEND_REPLY_MESSAGE_URL,
                      headers=my_header,
                      json=my_body)
        
        # print('sendTextReplyMessage function complete!!!')
    except Exception as ex:
        print(f'!!! sendTextReplyMessage function error: {ex}')

def sendStickerReplyMessage(sticker_id, package_id, reply_token):
    try:
        my_header = {
            'Content-Type': 'application/json',
            'Authorization': LINE_BOT_TOKEN
        }
        my_body = {
            'replyToken': reply_token,
            'messages' :[
                {
                    "type": "sticker",
                    "stickerId": sticker_id,
                    "packageId": package_id
                }
            ]
        }

        requests.post(url=SEND_REPLY_MESSAGE_URL,
                      headers=my_header,
                      json=my_body)
        
        # print('sendStickerReplyMessage function complete!!!')
    except Exception as ex:
        print(f'!!! sendStickerReplyMessage function error: {ex}')

def sendFlexMessage(flex_message, reply_token):
    try:
        my_header = {
            'Content-Type': 'application/json',
            'Authorization': LINE_BOT_TOKEN
        }
        my_body = {
            'replyToken': reply_token,
            'messages': [
                {
                    "type": "flex",
                    "altText": "Ubike查詢結果",
                    "contents": flex_message
                }
            ]
        }

        requests.post(url=SEND_REPLY_MESSAGE_URL,
                      headers=my_header,
                      json=my_body)
        
        # print('sendFlexMessage function complete!!!')
    except Exception as ex:
        print(f'!!! sendFlexMessage function error: {ex}')

# result ="您附近的站場：\n---------------------------------------\n"
# for station in data:
#     result += f'地址：{station['scity']}{station['sarea']}{station['ar']} \n'
#     result += f'google map 連結：{UBIKE_GOOGLE_MAP_URL.format(lat = station['lat'], lng = station['lng'])} \n'
#     result += f'站場名稱：{station['sna']} \n'
#     result += f'目前車輛數：{station['sbi']} \n'
#     result += f'空位數量：{station['bemp']} \n'
#     result += f'資料更新時間：{station['mday']} \n---------------------------------------\n'

# sendTextReplyMessage(result, reply_token)