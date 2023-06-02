from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render
from django.views.generic import TemplateView
from site_module.models import SiteSettings, FooterLinkItems


class HomeView(TemplateView):
    template_name = 'home_module/index.html'


def site_header(request: HttpRequest):
    context = {}
    return render(request, 'layout/site_header.html', context)


def site_footer(request: HttpRequest):
    site_setting = SiteSettings.objects.filter(is_main_setting=True).first()
    footer_link = FooterLinkItems.objects.all()
    context = {
        'site_setting': site_setting,
        'footer_link': footer_link,
    }
    return render(request, 'layout/site_footer.html', context)


def change_theme(request: HttpRequest):
    theme = request.GET.get('theme')
    if theme == 'light':
        request.session['theme'] = 'light'
    elif theme == 'dark':
        request.session['theme'] = 'dark'
    else:
        return Http404()
    return JsonResponse({'status': 'success'})