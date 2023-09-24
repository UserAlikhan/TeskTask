from django.urls import path, include, re_path
from . import views

urlpatterns = [
    # /
    path('', views.home, name='task-home'),

    # /lessons/1
    #re_path(r'(?P<user_id>[0-9]+)', views.user_request, name='user-page'),
    # path('<str:name>/', views.user_request, name='user-page'),
    path('status/', views.ProductStatisticsAPIView.as_view(), name='statistic'),
    path('<str:person_name>/', views.LessonViewListAPIView.as_view(), name='lesson-list-api'),
    path('<str:person_name>/<str:product_name>/', views.ProductLessonsAPIVIEW.as_view(), name='product-lesson-api'),
]