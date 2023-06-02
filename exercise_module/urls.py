from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.ExerciseView.as_view(), name='exercise')
]