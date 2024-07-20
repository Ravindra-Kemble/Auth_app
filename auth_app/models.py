import secrets
import hashlib
import hmac
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class Otp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    @staticmethod
    def generate_otp():
        return secrets.token_urlsafe(4)
    
    @staticmethod
    def hash_otp(otp_code):
        return hmac.new(settings.SECRET_KEY.encode(), otp_code.encode(), hashlib.sha256).hexdigest()
    
    def save(self, *args, **kwargs):
        self.otp_code = self.hash_otp(self.otp_code)
        super().save(*args, **kwargs)