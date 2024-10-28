import requests
from appconfig import CHAT_URL, OPENAI_API_KEY

def openaiChatMessage(chat_message):
    try:
        ai_headers = {'Content-Type': 'application/json',
                    'Authorization': OPENAI_API_KEY}
        ai_body = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "system",
                    "content": chat_message
                }
            ]
        }

        # json.loads(): deserialization json string to dict

        response = requests.post(url=CHAT_URL, headers=ai_headers, json=ai_body)
        result = response.json()
        openai_reply = result['choices'][0]['message']['content']

        return openai_reply
    
    except Exception as ex:
        print(f'!!! openaiChatMessage fuction error: {ex}')