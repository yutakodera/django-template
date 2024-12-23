# ネットワークプログラミング実験

## インストール
- WSL2
- Docker Desktop
- Visual Studio Code

## 初回ビルド
```
cp .env.example .env
make init
```

## ユーザ登録
デフォルトでは`Username=123123123, Password=123123123`が登録される
`create_user.py`を編集することで登録ユーザを変更可能
```
docker compose exec app bash
python create_user.py
```

## コンテナに入る
```bash
docker compose exec app bash
```

## 変更を反映
```bash
make rebuild
```

## URL
- `http://localhost:8002`
- `http://localhost:8002/admin`
- `http://localhost:8002/co2data`
- `http://localhost:8002/co2data/fetch-json`
- `http://localhost:8002/login`
- `http://localhost:8002/logout`

## リセット
```bash
make rmall
```

## Pythonスクリプト
コンテナ内で実行する
```bash
docker compose exec app bash
```
- `api_post.py`
    - APIにPOSTリクエストを送信する．
- `md5_hash.py`
    - パスワードのMD5ハッシュを生成する．
- `create_user.py`
    - MD5ハッシュ化されたパスワードを有するユーザを作成する．
