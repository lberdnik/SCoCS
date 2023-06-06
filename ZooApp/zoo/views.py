import logging
from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
from django.contrib.auth import authenticate, login
from .models import Animal, Client, Employee, Placement, User
from transliterate import translit
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Создаем логгер
logger = logging.getLogger(__name__)

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
            
            # Логируем запрос к внешнему API
            url = 'https://api.genderize.io/?name=' + translit(employee.firstname, language_code='ru', reversed=True)
            logger.info(f"Отправка запроса к API: {url}")
            response = requests.get(url)
            data = response.json()
            if data['gender'] == 'male':  
                employee.gender = 'Мужской'
            else:
                employee.gender = 'Женский'

            # Логируем запрос к внешнему API
            url = 'https://api.nationalize.io/?name=' + translit(employee.firstname, language_code='ru', reversed=True)
            logger.info(f"Отправка запроса к API: {url}")
            response = requests.get(url)
            data = response.json()
            employee.nationality = data['country'][0]['country_id']

    animals = Animal.objects.all()
    placements = Placement.objects.all()
    return render(request, 'home.html', {'placements': placements, 'employee': employee, 'animals': animals, 'is_authorized': is_authorized, 'is_superuser': is_superuser})

class RegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
                message='Invalid phone number.'
            )
        ],
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            logger.info(f'New user {request.POST.get("username")} was added.')
            client = Client.objects.create(username=request.POST.get('username'),
                                           first_name=request.POST.get('first_name'),
                                           last_name=request.POST.get('last_name'),
                                           address=request.POST.get('address'),
                                           phone_number=request.POST.get('phone_number'))
            client.save()

            return redirect('home')
    else:
        logger.info(f'Invalid data in the registration form.')
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


class AnimalDetailView(generic.DetailView):
    template_name = 'animal_detail.html'
    model = Animal


class PlacementsIndexView(generic.ListView): # лист
    template_name = 'placements.html'
    context_object_name = 'placements'

    def get_queryset(self):
        return Placement.objects.order_by('name')

class PlacementsDetailView(generic.DetailView): # объект
    template_name = 'animals_in_placements.html'
    model = Placement

class StatisticsView(LoginRequiredMixin, generic.TemplateView): # страничка
    template_name = 'statistics'
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)