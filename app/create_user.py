import django
import hashlib
import os
import sys


# Django設定を読み込む
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "app.settings"
)  # プロジェクト名に合わせて変更
django.setup()


from django.contrib.auth.models import User


def create_user_with_md5(username, password):
    # パスワードをMD5でハッシュ化（ソルトなし）
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # ユーザ作成
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.password = hashed_password
        user.is_active = True  # ユーザを有効化
        user.save()
        print(f"User '{username}' created successfully with MD5 hashed password.")
    else:
        print(f"User '{username}' already exists.")


# 実行
if __name__ == "__main__":
    args = sys.argv()
    if len(args) == 3:
        username = args[1]
        password = args[2]
        args = sys.argv()
        create_user_with_md5(username, password)
    else:
        print("Usage: python create_user.py <username> <password>")
        sys.exit(1)
