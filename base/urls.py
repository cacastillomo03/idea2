from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('transaction/', views.new_transaction, name='new_transaction'),
    path('historial/', views.transaction, name='transaction'),
    path('saldo/', views.versaldo, name='versaldo')

]


