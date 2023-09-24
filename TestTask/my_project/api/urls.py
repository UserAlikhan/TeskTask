from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addLesson),
    path('s/<str:person_name>/', views.LessonViewListAPIView.as_view(), name='lesson-list-api')
]