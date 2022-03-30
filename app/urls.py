from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('sum/<number1>/<number2>', views.sum, name="sum"),
    path('difference/<number1>/<number2>', views.difference, name="difference"),
    path('multiplication/<number1>/<number2>',
         views.multiplication, name="multiplication"),
    path('division/<number1>/<number2>', views.division, name="division"),
]
