
from django.urls import path

from . import views

urlpatterns = [


    path('', views.login,name='login'),
    path('<int:recipes_id>/', views.detail,name='detail'),
]