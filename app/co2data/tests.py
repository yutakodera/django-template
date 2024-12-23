import requests
from django.test import TestCase, Client
from unittest.mock import patch
from datetime import datetime
from .views import fetch_data


class FetchDataTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("requests.get")
    def test_fetch_data_success(self, mock_get):
        # モックレスポンスを設定
        mock_response = {
            "status_code": 200,
            "json": lambda: [
                {"id": 1, "datetime": 1671430000, "co2_val": 1117.0},
                {"id": 2, "datetime": 1671430000, "co2_val": 1078.0},
            ],
        }
        mock_get.return_value = type("MockResponse", (), mock_response)

        # 関数の実行
        result = fetch_data()

        # 結果の確認
        self.assertEqual(result["status"], "success")
        self.assertEqual(len(result["formatted_json"]), 2)
        self.assertEqual(result["formatted_json"][0]["datetime"], "2023-01-01 12:00:00")
        self.assertEqual(result["formatted_json"][0]["co2_val"], 1117.0)

    @patch("requests.get")
    def test_fetch_data_error(self, mock_get):
        # モックレスポンスで例外を発生
        mock_get.side_effect = requests.exceptions.RequestException("APIエラー")

        # 関数の実行
        result = fetch_data()

        # 結果の確認
        self.assertEqual(result["status"], "error")
        self.assertIn("APIエラー", result["message"])

    def test_render_json_response(self):
        # APIエンドポイントのテスト
        response = self.client.get("/fetch-json/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("status", response.json())

    def test_display_co2_data_template(self):
        # テンプレートレンダリングのテスト
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "co2_table.html")
