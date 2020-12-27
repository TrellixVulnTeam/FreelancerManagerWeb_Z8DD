from django.shortcuts import render, Http404

# Create your views here.
from django.urls import path


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def login(request):
    return render(request, 'pages/login.html')