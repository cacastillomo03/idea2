from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('new_transaction/', views.new_transaction, name='new_transaction'),
    path('transactions/', views.transactions, name='transactions'),
    path('see_balance', views.see_balance, name='see_balance')

]


