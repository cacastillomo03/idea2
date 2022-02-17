from cgitb import html
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index( request ):
    return render (request, 'base/index.html')

def login (request):
    return render (request,'base/login.html')

def inicio (request):
    return render (request,'base/inicio.html')

def new_transaction(request):
    return  render (request, 'base/new_transaction.html')

def transaction(request):
    return render (request, 'base/transaction.html')

def versaldo(request):
    return render(request,'base/versaldo.html')