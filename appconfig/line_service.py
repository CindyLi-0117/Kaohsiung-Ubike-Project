from flask import request
from appconfig import app
from appconfig.line_utility import followEvent, unfollowEvent, messageEvent

# because line reply message use POST-method

@app.route('/api/v1/linebot/service', methods=['POST'])
def lineBot():
    try:
        webhook_data = request.get_json()
        events = webhook_data['events']

        if len(events) == 0:
            print('events now are null~')
        else:
            event_data = events[0]
            event_type = event_data['type']

            match event_type:
                case 'follow':
                    source = event_data['source']
                    reply_token = event_data['replyToken']
                    followEvent(event_data, source, reply_token)

                case 'unfollow':
                    source = event_data['source']
                    unfollowEvent(source)

                case 'message':
                    reply_token = event_data['replyToken']
                    messageEvent(event_data, reply_token)

    except Exception as ex:
        print(f'!!! lineBot function request error: {ex}')
        
    return 'OK'
