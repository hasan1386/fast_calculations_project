from django.views.generic import TemplateView

from site_module.models import SiteSettings


class AboutUs(TemplateView):
    template_name = 'site_module/about_us_page.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs, self).get_context_data(**kwargs)
        site_setting = SiteSettings.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting

        return context
