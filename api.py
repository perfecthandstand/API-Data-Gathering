import requests
import json

# 抓取資料 (以 JSONPlaceholder 為例)
url = "message":"https:\/\/images.dog.ceo\/breeds\/pomeranian\/n02112018_5089.jpg","status":"success"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # 儲存成 output.json
    with open('output.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("檔案已產出")
