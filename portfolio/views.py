from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
import requests, json

# Create your views here.

def index(request):
    return render(request, "portfolio/index.html")

def portfolio(request):
    return render(request, "portfolio/portfolio.html")

def projects(request):
    return render(request, "portfolio/projects.html")

def contact(request):
    print(request.method)
    if request.method == 'POST':
        email  =request.POST.get('email')
        subject  =request.POST.get('subject')
        message  =request.POST.get('message')
        c=Contact(email=email, subject=subject, message=message)
        c.save()
        return render(request, "portfolio/thank.html")
    else:
        return render(request, "portfolio/contact.html")

def wordCounter(request):
    return render(request, "portfolio/word-counter.html")
