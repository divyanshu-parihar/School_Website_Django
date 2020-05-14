from django.shortcuts import render
from .models import twelveclass,elevenclass
# Create your views here.
def index(request):
    return render(request,'index.html')
def Class12(request):
    files =twelveclass.objects.all()
    return render(request,'class12.html',{"files":files})
def Class11(request):
    files=elevenclass.objects.all()
    return render(request,'class11.html',{"files":files})
def PLayer(request):
    return render(request,'player.html')