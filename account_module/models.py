from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='آواتار', null=True, blank=True)
    email_active_code = models.IntegerField(verbose_name='کد فعالسازی', null=True, blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.get_full_name() != '':
            return self.get_full_name()
        return self.email
