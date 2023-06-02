from django.contrib import admin
from . import models

admin.site.register(models.SiteSettings)
admin.site.register(models.FooterLinkItems)