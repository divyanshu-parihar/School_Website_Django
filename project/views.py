from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request,'index.html')
def Class12(request):
    return render(request,'class12.html')
def Class11(request):
    return render(request,'class11.html')
def PLayer(request):
    return render(request,'class11.html')