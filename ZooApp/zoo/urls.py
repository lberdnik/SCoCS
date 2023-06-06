from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('placements/', views.PlacementsIndexView.as_view(), name='placements'),
    path('registration/', views.registration, name='registration'),
    path('animals/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail'),
    path('placements/<int:pk>/', views.PlacementsDetailView.as_view(), name='placement_detail')
]