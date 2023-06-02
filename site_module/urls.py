from django.urls import path
from . import views

urlpatterns = [
    path('about-us', views.AboutUs.as_view(), name='about-us-page')
]