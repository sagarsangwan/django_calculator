from django import urls
from . import views
from django.urls import path

urlpatterns = [
    path('Sum/<number1>/<number2>', views.Sum, name="Sum"),
    path('Difference/<number1>/<number2>', views.Difference, name="Difference"),
    path('Multiplication/<number1>/<number2>',
         views.Multiplication, name="Multiplication"),
    path('Division/<number1>/<number2>', views.Division, name="Division"),
]
