from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,JsonResponse
# Create your views here.
from .models import Smartphones

def home(request:HttpRequest):
    return HttpResponse("<h1>Hello Tashkent</h1>")


def smartphones(request:HttpRequest):
    smartphone = Smartphones.objects.all()

    results = []
    for phone in smartphone:
        results.append({
            'id':phone.pk,
            'price':phone.price,
            'img_url':phone.img_url,
            'color':phone.color,
            'ram':phone.ram,
            'memory':phone.memory,
            'name':phone.name,
            'model':phone.model
        })

    return JsonResponse({'results':results})

def add_smartphone(request:HttpRequest):
    phone = Smartphones(
        price = "1500000",
        img_url = 'dfewfafw',
        color = 'while',
        ram = '16 GB',
        memory = '256 GB',
        name = 'Samsung A22',
        model = 'Samsung'
    )
    phone.save()

    return JsonResponse({'Status':200})

def get_id(request:HttpRequest,id:int):
    smartphones = Smartphones.objects.all()

    result = []
    for phone in smartphones:
        if int(id) == phone.pk:
            result.append({
            'id':phone.pk,
            'price':phone.price,
            'img_url':phone.img_url,
            'color':phone.color,
            'ram':phone.ram,
            'memory':phone.memory,
            'name':phone.name,
            'model':phone.model
            })
            return JsonResponse({'result':result})
    else:
        return HttpResponse('Bunday IDdagi maxsulot yo\'q')
