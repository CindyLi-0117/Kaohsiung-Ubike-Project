# Ubike 服務

### 即時車輛查詢（LineBot）
#### 模組
- LineBot
    * **Webhook Event**
    ```json
    {
        "destination": "xxxxxxxxxx",
        "events": [
            {
                "type": "message",
                "message": {
                    "type": "text",
                    "id": "14353798921116",
                    "text": "Hello, world"
                },
                "timestamp": 1625665242211,
                "source": {
                    "type": "user",
                    "userId": "U80696558e1aa831..."
                },
                "replyToken": "757913772c4646b784d4b7ce46d12671",
                "mode": "active",
                "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
                "deliveryContext": {
                    "isRedelivery": false
                }
            },
            {
                "type": "follow",
                "timestamp": 1625665242214,
                "source": {
                    "type": "user",
                    "userId": "Ufc729a925b3abef..."
                },
                "replyToken": "bb173f4d9cf64aed9d408ab4e36339ad",
                "mode": "active",
                "webhookEventId": "01FZ74ASS536FW97EX38NKCZQK",
                "deliveryContext": {
                    "isRedelivery": false
                }
            },
            {
                "type": "unfollow",
                "timestamp": 1625665242215,
                "source": {
                    "type": "user",
                    "userId": "Ubbd4f124aee5113..."
                },
                "mode": "active",
                "webhookEventId": "01FZ74B5Y0F4TNKA5SCAVKPEDM",
                "deliveryContext": {
                    "isRedelivery": false
                }
            }
        ]
    }
    ```
    * **Reply Message**
    * `POST https://api.line.me/v2/bot/message/reply`
    ```shell
      curl -v -X POST https://api.line.me/v2/bot/message/reply \
      -H 'Content-Type: application/json' \
      -H 'Authorization: Bearer {channel access token}' \
      -d '{
          "replyToken":"nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
          "messages":[
              {
                  "type":"text",
                  "text":"Hello, user"
              },
              {
                  "type":"text",
                  "text":"May I help you?"
              }
          ]
      }'
    ```
    * **Get User Profile**
    * `GET https://api.line.me/v2/bot/profile/{userId}`
    ```shell
      curl -v -X GET https://api.line.me/v2/bot/profile/{userId} \
      -H 'Authorization: Bearer {channel access token}'
    ```

    * Flask  
    * ngrok
- AI  
    * OpenAI (自然語言)
    * **Create Chat Completion**
    * `POST https://api.openai.com/v1/chat/completions`
    ```shell
    curl https://api.openai.com/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $OPENAI_API_KEY" \
    -d '{
        "model": "gpt-4o",
        "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Hello!"
        }
        ]
    }'
    ``` 
    * **Response Body**
    ```json
    {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": "gpt-4o-mini",
        "system_fingerprint": "fp_44709d6fcb",
        "choices": [
            {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "\n\nHello there, how may I assist you today?"
            },
            "logprobs": null,
            "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 9,
            "completion_tokens": 12,
            "total_tokens": 21,
            "completion_tokens_details": {
                "reasoning_tokens": 0
            }
        }
    }
    ```
    * GPS  
- SQL  
    * **DB-API interface to Microsoft SQL Server**
    ```python 
    import pymssql
    ```
    * **Create Connection**
    ```python
    connection = pymssql.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
    )
    ```
    * **Insert Into Table**
    ```python
    try:
        print('into insertProfileInfo function...')

        cursor = connection.cursor()
        insert = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        cursor.execute(insert, ())
        connection.commit()
    except Exception as ex:
        connection.rollback()
    finally:
        connection.close()
    ```

- Debug  
         
- **功能**  
    * 即時車輛狀態查詢
    * 自然語言輸入查詢  

- **可延伸功能**  
    * 查詢特定時間點車輛需求量  
    * 語音查詢  
    * 會員管理系統  
    * 金流 