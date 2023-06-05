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

    if request.user.is_authenticated:
        user = request.user
        is_authorized = True

        if user.is_superuser:
            employee = Employee.objects.all()            
            is_superuser = True

        elif user.employee:
            employee = user.employee
            
            response = requests.get('https://api.genderize.io/?name=' + translit(employee.firstname, language_code='ru', reversed=True)) #Внешнее api
            data = response.json()
            if data['gender'] == 'male':  
                employee.gender = 'Мужской'
            else:
                employee.gender = 'Женский'

            response = requests.get('https://api.nationalize.io/?name=' + translit(employee.firstname, language_code='ru', reversed=True)) #Внешнее api
            data = response.json()
            employee.nationality = data['country'][0]['country_id']; 

    animals = Animal.objects.all()
    placements = Placement.objects.all()
    return render(request, 'home.html', {'placements': placements, 'employee': employee, 'animals': animals, 'is_authorized': is_authorized, 'is_superuser': is_superuser})   
