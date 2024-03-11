from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


# Create your views here.

def home_page(request:HttpRequest):
    return render(request,'main/home_page.html')


def distance_page(request:HttpRequest):
    return render(request,'main/distance.html')

def currency_exchange(request:HttpRequest):
    return render(request,'main/currency.html')

def weather_informations(request:HttpRequest):
    return render(request,'main/weather.html')