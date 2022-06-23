from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Kullanici'
        verbose_name_plural = 'Kullanicilar'

    def __str__(self):
        return self.username
