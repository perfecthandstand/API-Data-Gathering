import requests
import json

# 正確的網址應該是字串格式，指向 API 的進入點
url = "https://dog.ceo/api/breeds/image/random"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # 儲存成 output.json
        with open('output.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("檔案已產出")
    else:
        print(f"抓取失敗，錯誤代碼：{response.status_code}")
except Exception as e:
    print(f"發生錯誤：{e}")
