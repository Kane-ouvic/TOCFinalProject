# TOC Final Project

## 1. How to use

* start from local
```
pip install -r requurments
ngrok http 8000
uvicorn main:app --reload
```

## 2. 功能

### 生活小幫手
* 聊天 (OpenAI chatGPT)
* 隨機決定想買的選項
* 代辦事項清單 (資料庫: Microsoft Azure Table)
* 號碼對獎 (資料庫: Microsoft Azure Table)
* 尋找附近餐廳 (資料來源: GCP map)
* 天氣預報 (資料來源: 中央氣象局)



## 3. FSM
![](https://i.imgur.com/QNIQUDp.png)

## 4. 用到的相關技術

* 爬蟲 (匯率資訊抓取、chatGPT)
* API  (GCP map、openData)
* 資料庫 (Azure Table)

## 5. 指令

* /weather 縣市 -- 回傳該縣市天氣狀況
* /exchange 幣別 金額 -- 回傳當天的匯率
* /invoice -- 進入兌獎階段
* /choose 類別1,類別2, .....(用,分隔) -- 隨機選擇其中一個類別
* /todo-list -- 查看代辦事項清單
* /fsm -- 查看狀態圖
* 傳送位置資訊 -- 回傳附近的餐廳資訊
* 任意訊息 -- 交給chatGPT處理


## 6. Demo
![](https://i.imgur.com/Ab1NqmS.png)


