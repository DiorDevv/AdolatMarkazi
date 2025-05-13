from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from shared.models import BaseModel


class OTPCode(models.Model):
    chat_id = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
    expiration_time = models.DateTimeField()

    def is_expired(self):
        return timezone.now() > self.expiration_time


class User(BaseModel):
    user_chat = models.CharField(max_length=100, unique=True)  # ForeignKey o‘rniga oddiy chat_id

