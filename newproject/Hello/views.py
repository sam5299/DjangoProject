from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse('Hello newproject-Hello app')
    return render(request,'hello/home.html')