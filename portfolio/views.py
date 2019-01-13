from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "portfolio/index.html")

def portfolio(request):
    return render(request, "portfolio/portfolio.html")

def projects(request):
    return render(request, "portfolio/projects.html")

def contact(request):
    return render(request, "portfolio/portfolio.html")
