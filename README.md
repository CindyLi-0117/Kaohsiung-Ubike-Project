
# 高雄 Ubike 即時資訊 LineBot

本專案提供使用者在 Line 上查詢離自己或指定位置最近的高雄 Ubike 站點的即時資訊，整合了多項工具與 API，實現即時站點查詢和使用者引導互動。

## 目錄
- [專案概述](#專案概述)
- [功能特色](#功能特色)
- [使用技術](#使用技術)
- [系統架構](#系統架構)
- [檔案結構](#檔案結構)
- [使用說明](#使用說明)
- [LineBot Webhook 設定](#linebot-webhook-設定)
- [SQL 資料庫設置](#sql-資料庫設置)
- [未來擴充](#未來擴充)

## 專案概述
此 LineBot 專案可接收使用者的定位，並查詢距離最近的 3 個高雄 Ubike 站點的即時資訊。系統使用高雄 Ubike API 獲取站點資料，並結合 OpenAI 的 API 來增強使用者互動體驗，支持地圖顯示、訊息引導等功能。

## 功能特色
- **基於位置的搜尋**：使用者可傳送位置並獲得最近 Ubike 站點資訊。
- **即時站點資訊查詢**：包括車輛及空位數量、站點名稱與地址等。
- **使用者引導**：直覺的 Line 互動式操作。
- **數據儲存**：儲存使用者資訊以提升體驗。
- **地圖顯示**：支援地圖連結以便導航至站點。

## 使用技術
- **Python 3.12**：核心程式語言
- **Flask**：用於架設 Web API 服務
- **Microsoft SQL Server 2022 與管理工作室**：數據儲存和管理
- **Line Messaging API**：Line Bot 互動與訊息處理
- **OpenAI API**：用於增強使用者互動的自然語言處理
- **Pandas、NumPy**：用於數據處理和距離計算
- **JSON、Postman**：JSON 編輯和 API 測試工具

## 系統架構
1. **使用者輸入**：使用者在 Line 上傳送位置。
2. **資料處理**：系統使用 Ubike API 計算距離最近的站點，並使用 Pandas 資料框架進行處理。
3. **資料回傳**：提供即時站點資料及地圖連結至使用者。

## 檔案結構
- `app.py`：啟動 Flask 應用的主要程式。
- `__init__.py`：Flask 應用的配置，包含 API 金鑰和主要 API URL。
- `app_normal.py`：Flask 應用的基本路由配置。
- `db_utility.py`：包含連接 SQL Server 的方法，用於儲存和管理使用者資料。
- `flex_message_utility.py`：用於建立和處理 Line Flex Message 的格式與樣板。
- `line_service.py`：處理 Line Bot 的服務路由，包括 webhook 事件處理。
- `line_utility.py`：包含 Line Bot 互動功能，例如使用者追蹤與訊息回覆。
- `openai_utility.py`：負責與 OpenAI API 的連接，用於生成回覆訊息。
- `ubike_utility.py`：處理 Ubike API 的請求與資料計算，包括距離計算和位置資訊獲取。

## 使用說明
1. 將 Bot 部署至支援的伺服器或本機環境。
2. 連接 Line App，與 Bot 互動以查詢站點資訊。
3. 傳送定位以獲得附近的 Ubike 站點資訊及導航地圖。

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

## 未來擴充
- **多媒體查詢**：擴充支援文字、圖片及語音查詢。
- **會員系統整合**：支援 Ubike 會員管理系統。
- **需求預測**：利用數據分析來預測車輛需求與可用性。
