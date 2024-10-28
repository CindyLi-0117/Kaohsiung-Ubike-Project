# app system config

from flask import Flask
app = Flask('__main__')

# ubike api url

KAOHSIUNG_UBIKE_API_URL = 'https://api.kcg.gov.tw/api/service/Get/b4dd9c40-9027-4125-8666-06bef1756092'
UBIKE_GOOGLE_MAP_URL = 'https://www.google.com/maps/search/?api=1&query={lat},{lng}'

# openai api

CHAT_URL = 'https://api.openai.com/v1/chat/completions'
OPENAI_API_KEY = 'Bearer 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'
CHAT_PROMPT = ('你現在是一位高雄市 ubike 客服，客戶的目的是要找出離他位置最近的站點，我們需要位置資訊才可以提供服務，'
               '請你根據客戶的訊息，使用Line位置分享功能，引導他傳送他的位置資訊。下列是客戶的訊息：%s')

# sql

SERVERNAME = 'localhost'
DATABASENAME = 'UbikeDB'
USERNAME = 'sa'
PASSWORD = '910117'

# use ryan's line bot setting
# line config

LINE_BOT_TOKEN = 'Bearer qVhlFDXJr8OhV1Qj2jWaZxIddC3mXnifc2aiMXCmsymAJvx5klgsC7nUIEAEWFMo7/FA/1Xk2AmbHN91VaAoz7XvQkccRoJQnx7n3cGonMa5DneM67pjX8RTEr8Fd/C6fAAYIPVPLqQMnXkeFQhR7AdB04t89/1O/w1cDnyilFU='
SEND_REPLY_MESSAGE_URL = 'https://api.line.me/v2/bot/message/reply'
GET_USER_PROFILE_URL = 'https://api.line.me/v2/bot/profile/%s'

# deploy modules

import appconfig.app_normal
import appconfig.line_service
import appconfig.line_utility
import appconfig.db_utility
import appconfig.flex_message_utility
