from django.contrib import admin
from .models import Lessons, IsRead

admin.site.register(Lessons)

admin.site.register(IsRead)