from django.db import models
from account_module.models import User
from lessons_module.models import Lessons


class Exercises(models.Model):
    calculations = models.CharField(max_length=500, verbose_name='سؤال')
    result = models.IntegerField(verbose_name='جواب', null=True)
    lesson = models.ForeignKey(Lessons, on_delete=models.PROTECT, verbose_name='درس مربوطه')

    def __str__(self):
        return self.lesson.title

    class Meta:
        verbose_name = 'تمرین'
        verbose_name_plural = 'تمرینات'


class IsSolve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', editable=False)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, verbose_name='تمرین', editable=False)

    def __str__(self):
        return f'{self.user} - {self.exercise}'

    class Meta:
        verbose_name = 'تمرین انجام شدۀ کاربر'
        verbose_name_plural = 'تمرینات انجام شدۀ کاربران'