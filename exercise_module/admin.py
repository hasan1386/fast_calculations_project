from django.contrib import admin
from .models import Exercises, IsSolve
from .form import LessonsModelForm


@admin.register(Exercises)
class LessonsAdmin(admin.ModelAdmin):
    form = LessonsModelForm

admin.site.register(IsSolve)