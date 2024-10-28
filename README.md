
# Ubike 即時車輛查詢服務（LineBot）

此專案包含一個 LineBot，用戶可以透過它查詢最近車站的 Ubike 即時可用車輛。該服務支持文字、位置以及自然語言的輸入查詢。

## 功能
- **即時車輛狀態查詢**：用戶可以請求查詢最近的 Ubike 車站車輛狀態。
- **自然語言輸入**：使用者可以使用簡單的語句來查詢車輛可用情況。
- **基於位置的服務**：使用 Line 的位置共享功能來尋找最近的 Ubike 車站。
- **SQL Server 資料庫整合**：用戶資料與查詢記錄將被存儲於資料庫中，供未來分析與改進。

## 安裝
1. 克隆此儲存庫。
2. 安裝所需套件：
   ```bash
   pip install -r requirements.txt
   ```
3. 設置 Microsoft SQL Server 資料庫並配置連接設定。
4. 將 LineBot 部署到您的 Line 開發者帳戶中。

## LineBot Webhook 設定
- **Webhook 事件**：處理收到的訊息時的示例事件 JSON 資料。
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
                "mode": "active"
            }
        ]
    }
    ```

- **回覆訊息 API 請求**：
    ```bash
    curl -v -X POST https://api.line.me/v2/bot/message/reply     -H "Content-Type: application/json"     -H "Authorization: Bearer {LINE_CHANNEL_ACCESS_TOKEN}"     -d '{
      "replyToken": "{replyToken}",
      "messages":[
        {
          "type":"text",
          "text":"這是最近的 Ubike 車站資訊..."
        }
      ]
    }'
    ```

## SQL 資料庫設置
- **Microsoft SQL Server 的 DB-API 介面**：
    ```python
    import pymssql
    connection = pymssql.connect(
      host="localhost",
      user="yourusername",
      password="yourpassword",
      database="mydatabase"
    )
    ```

- **資料插入範例**：
    ```python
    try:
        cursor = connection.cursor()
        insert = "INSERT INTO customers (name, address) VALUES (%s, %s)"
        cursor.execute(insert, ('John Doe', '123 Elm St'))
        connection.commit()
    except Exception as ex:
        connection.rollback()
    finally:
        connection.close()
    ```

## 未來功能
- **特定時間點查詢**：查詢未來或過去時間點的車輛狀態。
- **語音輸入支持**：使用語音指令與 LineBot 互動。
- **會員管理系統**：管理用戶資料和個人偏好設定。
- **支付整合**：處理預訂 Ubike 或其他服務的交易。

## 除錯
確保已啟用日誌記錄，以捕捉 Webhook 事件、SQL 查詢以及錯誤訊息。
