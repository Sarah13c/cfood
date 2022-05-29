
from django.urls import path

from . import views

urlpatterns = [

    path('login/',views.login2, name = 'login '),
    path('register/', views.register, name='register'),
    path('', views.inicio, name = "inicio"),

]