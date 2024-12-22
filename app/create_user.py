import hashlib
import os
import django
from django.contrib.auth.models import User


# Django設定を読み込む
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "app.settings"
)  # プロジェクト名に合わせて変更
django.setup()


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
    username = "50M24146"
    password = "50M24146"
    create_user_with_md5(username, password)
