from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'zoo/home.html')