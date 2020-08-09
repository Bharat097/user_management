from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.contrib.auth.hashers import check_password
from .models import User


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
