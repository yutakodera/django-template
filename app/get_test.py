import requests
from datetime import datetime


url = "http://10.2.17.66/cgi-bin/cgi.py"

response = requests.get(url, timeout=20)
response.raise_for_status()  # ステータスコードがエラーの場合例外を投げる
data = response.json()
print(data)

formatted_data = []
for entry in data:
    formatted_entry = {
        "id": entry.get("id"),
        "datetime": datetime.fromtimestamp(entry.get("datetime")).strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "co2_val": entry.get("co2_val"),
    }
    formatted_data.append(formatted_entry)
print(formatted_data)
