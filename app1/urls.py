from django.urls import path
from django.conf import settings
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('result', views.result, name='result')
]
