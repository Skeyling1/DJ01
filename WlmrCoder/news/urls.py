from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="news_home"),
    path('create_news/', views.add_news, name="news_addition")
]
