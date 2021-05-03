from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers', views.customers, name='customers'),
    path('user', views.user, name='user'),
    path('send_money', views.send_money, name='send_money'),
    path('transaction_history', views.transaction_history, name='transaction_history'),
    path('transaction_done', views.transaction_done, name='transaction_done')
]