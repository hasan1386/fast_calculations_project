from django.db import models
from django_summernote.fields import SummernoteTextField

from account_module.models import User


class Lessons(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/lessons/', verbose_name='عکس کاور')
    id_lesson = models.IntegerField(verbose_name='شماره درس', primary_key=True)
    description = SummernoteTextField(verbose_name='توضیحات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'درس‌ها'


class IsRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کابر', editable=False)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, verbose_name='درس', editable=False)

    def __str__(self):
        return f'{self.user} - {self.lesson}'

    class Meta:
        verbose_name = 'درس خوانده شده کاربر'
        verbose_name_plural = 'درس های خوانده شده کاربران'