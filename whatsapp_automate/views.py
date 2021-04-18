from django.http.response import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def home_whatsapp(request):
    return HttpResponse("home_whatsapp")