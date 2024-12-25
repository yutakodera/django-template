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
username，passwordは自分で決めてください
```
docker compose exec app bash
python create_user.py [username] [password]
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
- `get_test.py`
    - `http://10.2.17.66/cgi-bin/cgi.py`にGETリクエストを送る
- `create_user.py`
    - Usage: `python create_user.py [username] [password]`
    - MD5ハッシュ化されたパスワードを有するユーザを作成する


## MD5ハッシュ衝突実験
- HashClashというプロジェクトを使って実験する
- ハッシュが衝突する入力のペアを見つける

### コンテナに入る
```bash
cd workspace
docker compose up -d --build
docker compose exec ubuntu bash
```

### HashClashをクローンしてビルド
```bash
git clone https://github.com/cr-marcstevens/hashclash.git
cd hashclash
bash ./build.sh
```

### ハッシュ衝突ペアを見つける
```bash
mkdir textcoll_workdir
cd textcoll_workdir
bash ../scripts/textcoll.sh
```

<!-- 
### ハッシュ衝突ペアを見つける
```bash
cd hashclash-static-release-v1.2b/bin
echo -n "123123123" > prefix
./scripts/poc_no.sh prefix
```

### ハッシュ衝突ペアを確認
- バイナリファイルを16進数で見る
```bash
xxd collision1.bin
xxd collision1.bin
```

- バイナリファイルを文字列に変換して比較
```bash
xxd collision1.bin > collision1_hex.txt
xxd collision2.bin > collision2_hex.txt
diff collision1_hex.txt collision2_hex.txt
```

### ハッシュ衝突ペアを使ってユーザ登録
```bash
python create_user.py collision1 collision2
```
 -->
