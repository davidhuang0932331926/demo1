from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bweb(request):
    return HttpResponse("Hello, world i am here!")

def aweb(request):
    return HttpResponse("Hello, this is the aweb view.")

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')          
