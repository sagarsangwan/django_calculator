from django.http import JsonResponse, HttpResponse


def home(request):
    number1 = 1
    number2 = 2
    return HttpResponse(
        '<a href="/api/sum/{}/{}">Sum</a><br>'
        '<a href="/api/difference/{}/{}">Difference</a><br>'
        '<a href="/api/multiplication/{}/{}">Multiplication</a><br>'
        '<a href="/api/division/{}/{}">Division</a>'.format(number1, number2, number1, number2, number1, number2, number1, number2))


def sum(request, number1, number2):
    try:
        result = float(number1) + float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input'})


def difference(request, number1, number2):
    try:
        result = float(number1) - float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input'})


def multiplication(request, number1, number2):
    try:
        result = float(number1) * float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input'})


def division(request, number1, number2):
    try:
        result = float(number1) / float(number2)
        return JsonResponse({'number1': number1, 'number2': number2, 'result': result})
    except:
        return JsonResponse({'error': 'Invalid Input or division by 0'})
