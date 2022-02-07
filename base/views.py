from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index( request ):
    return render (request, 'base/index.html')

def login(request):
    return HttpResponse('You are in login page')

def new_transaction(request):
    return HttpResponse('You are in new transaction')

def transactions(request):
    return HttpResponse('You are in TRANSACTION')

def see_balance(request):
    return HttpResponse('You are in BALANCE')