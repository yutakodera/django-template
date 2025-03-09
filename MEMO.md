# ネットワークプログラミング実験

## 全体の流れ
1. Dockerfile, docker-compose.ymlを作成
    - Python (Django, gunicorn)
    - PostgreSQL
    - Nginx
2. コンテナをビルドし起動
3. Pythonコンテナの中でDjangoアプリケーションを作成
    - `python manage.py startapp co2data`
4. APIを作成
    - `app/co2data/views.py`にCO2データを取得するAPIを追加
    - `app/co2data/urls.py`にAPIのURLを追加
    - `app/co2data/apps.py`
5. CO2データを表示するページを作成
    - `/app/templates/co2_table.html`にCO2データを表示するページを追加
    - `app/app/settings.py`の`LOCAL_APPS`に`co2data`を追加
6. ユーザ認証を追加
    - `/app/templates/login.html`にユーザ名とパスワードを入力するログインフォームを追加
    - `/app/views.py`にログイン処理を追加（`@login_required`を追加）
    - `/app/co2data/urls.py`にログインページのURLを追加
    - `/app/co2data/urls.py`にログアウトの処理を追加
    - `/app/app/settings.py`に`LOGIN_URL`，`LOGIN_REDIRECT_URL`，`LOGOUT_REDIRECT_URL`
7. ハッシュ衝突実験のためにパスワードハッシュの方式をMD5に変更
    - `/app/app/backends.py`にユーザ認証バックエンドを追加
    - `/app/app/settings.py`の`PASSWORD_HASHERS`を設定し，MD5ハッシュ化を追加
    - `/app/app/settings.py`の`AUTH_PASSWORD_VALIDATORS`をコメントアウトし，パスワードポリシーを削除
    - `/app/app/settings.py`の`AUTHENTICATION_BACKENDS`にユーザ認証バックエンド（`/app/app/backends.py`で追加したもの）を設定
    - DBに保存されるパスワードがMD5ハッシュであるユーザを作成する（`create_user.py`）
    - ユーザ名：user（なんでもいい）
    - パスワード：TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak（[文字列A](#文字列A)）
8. ハッシュ衝突実験の詳細は[MD5ハッシュ衝突実験](#MD5ハッシュ衝突実験)に記載


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

## MD5ハッシュ衝突実験<a id="MD5ハッシュ衝突実験"></a>
- [HashClash](https://github.com/cr-marcstevens/hashclash)を用いて，ハッシュが衝突する入力のペアを見つける
- 参考：[https://burion.net/entry/2024/01/12/012723](https://burion.net/entry/2024/01/12/012723)

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
- 文字列A<a id="文字列A"></a>
    - TEXTCOLLBYfGiJUETHQ4h<span style="color: red;">A</span>cKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak
- 文字列B
    - TEXTCOLLBYfGiJUETHQ4h<span style="color: red;">E</span>cKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak
- 文字列AのMD5ハッシュ値
    - faad49866e9498fc1719f5289e7a0269
- 文字列BのMD5ハッシュ値
    - faad49866e9498fc1719f5289e7a0269
- 異なる文字列でもハッシュ値が一致する場合があることを確認

### 文字列Bを使ってログイン
- 以下のユーザでログインできることを確認
    - ユーザ名：user
    - パスワード：TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak（文字列B）
- 本来のパスワード（文字列A）と異なるのにもかかわらずログインできる

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
