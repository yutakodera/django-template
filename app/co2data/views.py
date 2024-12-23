import requests
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def fetch_data():
    # 送信先のURL
    url = "http://10.2.17.66/cgi-bin/cgi.py"

    try:
        # GETリクエストを送信
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # ステータスコードがエラーの場合例外を投げる

        # JSONデータを取得
        data = response.json()  # [{...}, {...}, ...]

        # 整形処理（例: datetimeを人間が読める形式に変換）
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

        # レスポンスに整形されたデータを含める
        response_data = {"status": "success", "formatted_json": formatted_data}

    except requests.exceptions.RequestException as e:
        # エラー時のレスポンス
        response_data = {"status": "error", "message": str(e)}

    return response_data


def render_json_response(request):
    data = fetch_data()
    return JsonResponse(data)


@login_required
def display_co2_data(request):
    data = fetch_data()
    if data["status"] == "error":
        # エラーページを表示
        return render(request, "error.html", {"message": data["message"]})
    # 正常時はデータをテンプレートに渡す
    return render(request, "co2_table.html", {"data": data["formatted_json"]})
