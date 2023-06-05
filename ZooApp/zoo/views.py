from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login
from .models import Animal, Employee, Placement
from transliterate import translit

def index(request):
    is_authorized = False
    is_superuser = False
    employee = 0

    return render(request, 'zoo/home.html')