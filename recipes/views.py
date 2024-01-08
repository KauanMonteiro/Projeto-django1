from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')