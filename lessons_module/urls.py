from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListLessons.as_view(), name='lessons-list'),
    path('<int:pk>/', views.DetailLesson.as_view(), name='detail-lesson'),
]
