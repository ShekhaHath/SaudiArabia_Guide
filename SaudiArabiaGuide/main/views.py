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

def riyadh_page(request:HttpRequest):
    return render(request,'main/Riyadh.html')

def jeddah_page(request:HttpRequest):
    return render(request,'main/Jeddah.html')

def alula_page(request:HttpRequest):
    return render(request,'main/Al-ula.html')

def abha_page(request:HttpRequest):
    return render (request, 'main/Abha.html')