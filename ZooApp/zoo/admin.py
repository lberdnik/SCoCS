from django.contrib import admin

from .models import Animal, Class, Complex, Country, Employee, Food, Job, Kind, Placement, User

admin.site.register(Animal)
admin.site.register(Food)
admin.site.register(Complex)
admin.site.register(Placement)
admin.site.register(Employee)
admin.site.register(Country)
admin.site.register(Class)
admin.site.register(Kind)
admin.site.register(Job)
admin.site.register(User)