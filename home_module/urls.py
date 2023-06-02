from django.urls import path

from . import views

urlpatterns = [
    path('change-theme/', views.change_theme, name='home-page'),
    path('', views.HomeView.as_view(), name='home-page'),
]