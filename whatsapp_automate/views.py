from django.http.response import HttpResponse
from django.shortcuts import render
import time
import pywhatkit

# Create your views here.
def home_whatsapp(request):
    #pywhatkit.sendwhatmsg('+919313152973', 'test message', 13, 16)
    timestamp = time.strftime('%H:%M:%S')
    
    return render(request, "whatsapp.html")

def result(request):
    msg = request.POST.get('txt')
    num = '+91'
    num += str(request.POST.get('num'))
    hours = time.strftime('%H')
    minutes = time.strftime('%M')
    print(hours, minutes, num, msg)
    pywhatkit.sendwhatmsg(num, msg, int(hours), int(minutes)+1)
    return render(request, "result.html", {'msg':msg, 'num':num})

