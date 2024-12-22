import hashlib
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class MD5Backend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        # パスワードをMD5でハッシュ化して比較
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if user.password == hashed_password:
            return user

        return None
