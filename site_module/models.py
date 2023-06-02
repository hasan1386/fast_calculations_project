from django.db import models


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=300, verbose_name='نام سایت')
    email = models.EmailField(max_length=350, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='دربارۀ ما')
    copyright = models.TextField(max_length=600, verbose_name='متن کپی رایت')
    logo = models.ImageField(upload_to='images/logo', verbose_name='لوگوی سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی سایت')

    def __str__(self):
        if self.is_main_setting:
            return f'{self.site_title} - تنظیمات اصلی'
        else:
            return self.site_title

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات سایت'


class FooterLinkItems(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.CharField(max_length=600, verbose_name='آدرس (اگر آدرس از همین سایت است نیازی به نوشتن دامنه نیست)')

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title
