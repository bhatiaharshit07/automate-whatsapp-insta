from django.http.response import HttpResponse
from django.shortcuts import render
import pywhatkit

# Create your views here.
def home_whatsapp(request):
    #pywhatkit.sendwhatmsg('+919313152973', 'test message', 13, 16)
    return render(request, "whatsapp.html")

def result(request):
    input_sentence = request.POST.get('txt')
    return render(request, "result.html", {'content':input_sentence})

