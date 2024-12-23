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

## コンテナに入る
```bash
docker compose exec app bash
```

## 変更を反映
```bash
make rebuild
```

## URL
- `http://localhost:8002/admin`
- `http://localhost:8002/co2data/api`
- `http://localhost:8002/co2data/table`

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
