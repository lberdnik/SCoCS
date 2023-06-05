from django.db import models
from django.contrib.auth.models import AbstractUser

class Food(models.Model):

    food = models.CharField("food", max_length=256)

class Complex(models.Model):

    complex_name = models.CharField("complex_name", max_length=128)
    
class Placement(models.Model):
    
    name = models.CharField("name", max_length=128, default="")
    number = models.IntegerField("number")
    reservoir = models.BooleanField("reservoir")    # наличие водоема
    heating = models.BooleanField("heating")        # наличие отопления
    complex_area = models.ForeignKey(Complex, on_delete=models.CASCADE)

class Country(models.Model):

    country = models.CharField("country", max_length=64, unique=True)

class Class(models.Model):

    class_name = models.CharField("class_name", max_length=128, unique=True)

class Kind(models.Model):

    kind = models.CharField("kind", max_length=128, unique=True)    
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE) 

class Animal(models.Model):

    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    age = models.IntegerField("age", null=True)
    description = models.TextField("description", null=True)
    gender = models.CharField("gender", choices=GENDER, max_length=1)
    arrival_date = models.DateField("arrival_date")         # дата поступления в зоопарк
    food = models.ManyToManyField(Food)                     # потребление корма
    img = models.URLField("url", null=True)
    placement = models.ForeignKey(Placement, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    kind = models.ForeignKey(Kind, on_delete=models.SET_NULL, null=True)    # семейство

class Job(models.Model):

    job_title = models.CharField("job_title", max_length=128)

class Employee(models.Model):

    firstname = models.CharField("firstname", max_length=128)
    lastname = models.CharField("lastname", max_length=128)
    patronymic = models.CharField("patronymic", max_length=128)
    phone = models.CharField("phone", max_length=32, unique=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)
    animals = models.ManyToManyField(Animal)

class User(AbstractUser):

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True)
