from django.http.response import HttpResponse
from django.shortcuts import render
import pywhatkit

# Create your views here.
def home_whatsapp(request):
    pywhatkit.sendwhatmsg('+919313152973', 'test message', 13, 16)
    return HttpResponse("home_whatsapp")

def result_whatsapp(request):
    pywhatkit.sendwhatmsg('+919313152973', 'test message', 16, 44)
    return HttpResponse("result_whatsapp")