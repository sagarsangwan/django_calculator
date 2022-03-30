import json
from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse


# Create your views here.

def Sum(request, number1, number2):
    try:
        result = float(number1) + float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input'})


def Difference(request, number1, number2):
    try:
        result = float(number1) - float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input'})


def Multiplication(request, number1, number2):
    try:
        result = float(number1) * float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input'})


def Division(request, number1, number2):
    try:
        result = float(number1) / float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input or division by 0'})
