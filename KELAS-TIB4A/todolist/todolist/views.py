from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    return render(request,'base.html')

def profil(request):
    return render(request,'profil.html')
