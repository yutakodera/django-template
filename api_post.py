import requests
import random
import datetime

# APIエンドポイントURL
API_URL = "http://127.0.0.1:8002/co2data/api/"


# ダミーデータを生成してAPIにPOSTする関数
def post_dummy_data():
    for _ in range(100):  # ダミーデータ100件を生成
        # ダミーデータの生成
        timestamp = datetime.datetime.now().isoformat()
        data = {
            "timestamp": timestamp,
            "co2_level": round(random.uniform(300, 800), 2),
            "temperature": round(random.uniform(15, 30), 1),
            "humidity": round(random.uniform(30, 70), 1),
        }

        # POSTリクエストの送信
        response = requests.post(API_URL, json=data)

        if response.status_code == 201:
            print(f"Success: {response.json()}")
        else:
            print(f"Failed: {response.status_code}, {response.text}")


# 実行
if __name__ == "__main__":
    post_dummy_data()
