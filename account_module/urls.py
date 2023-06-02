from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login-page'),
    path('logout/', LogoutView.as_view(), name="log-out-page"),
    path('register/', views.RegisterUserView.as_view(), name='register-page'),
    path('active-account/', views.ActiveAccountView.as_view(), name='active-account'),
    path('forget-paassword/', views.ForgetPasswordView.as_view(), name='forget-password-page'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'),
]
