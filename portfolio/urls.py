from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('', views.portfolio, name="portfolio"),
    path('', views.projects, name="projects"),
    path('contact', views.contact, name="home"),
]