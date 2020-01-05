# coding:utf-8

from django.urls import path

from . import views

urlpatterns = [
    path('', views.recv_data, name='recv_data'),
]
