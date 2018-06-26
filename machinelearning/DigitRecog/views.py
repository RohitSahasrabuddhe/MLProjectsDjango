from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, This is my first View!")

def hello(request):
   return render(request,'./DigitRecog/html/hello.html')

def drawer(request):
   return render(request,'./DigitRecog/html/drawer.html')