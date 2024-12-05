from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]

#Создайте новое Django приложение, зарегистрируйте его и
# сделайте так чтоб при переходе на страницу data и test открывались страницы с разным содержимым.