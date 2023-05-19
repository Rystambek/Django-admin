from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,JsonResponse
# Create your views here.
from .models import Smartphones
import json

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
    if request.method == "POST":
        data = request.body.decode()
        data_json = json.loads(data)

        phone = Smartphones(
            price = data_json['price'],
            img_url = data_json['img_url'],
            color = data_json['color'],
            ram = data_json['ram'],
            memory = data_json['memory'],
            name = data_json['name'],
            model = data_json['model']
        )

        phone.save()
    
    return JsonResponse({'Status':200})

def get_id(request:HttpRequest,id):
    smartphone = Smartphones.objects.all()

    result = []
    for phone in smartphone:
        if id == phone.pk:
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
    

def get_delete(request:HttpRequest,id):
    smartphone = Smartphones.objects.all()
    for phone in smartphone:
        if id == phone.pk:
            phone.delete()
    return JsonResponse({'status':200})

def get_update(request:HttpRequest,id):
    if request.method == "POST":
        data = request.body.decode()
        data_json = json.loads(data)

        smartphones = Smartphones.objects.all()
        for phone in smartphones:
            if id == phone.pk:
                phone.price = data_json['price']
                phone.img_url = data_json['img_url']
                phone.color = data_json['color']
                phone.ram = data_json['ram']
                phone.memory = data_json['memory']
                phone.name = data_json['name']
                phone.model = data_json['model']
                
            phone.save()    
    return JsonResponse({'Update':200})


