from django.shortcuts import render, redirect, get_object_or_404
from .models import Service

def homepage(request):
    services = Service.objects.all()
    return render(request, 'services.html', {"services": services})
    
def all_services(request):
    services = Service.objects.all()
    return render(request, 'homepage.html', {"services": services})    
    
    