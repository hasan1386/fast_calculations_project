from django.urls import path
from .views import UserPanelModule, UserEditProfileView, ChangePasswordView

urlpatterns = [
    path('', UserPanelModule.as_view(), name="user-panel-page"),
    path('information/', UserEditProfileView.as_view(), name='user-edit-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='user-edit-password'),
]
