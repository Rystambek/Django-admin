from django.shortcuts import render
from django.http import HttpRequest, HttpResponse,JsonResponse
# Create your views here.

def home(request:HttpRequest):
    return HttpResponse("<h1>Hello Tashkent</h1>")