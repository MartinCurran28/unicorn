from django.shortcuts import render, redirect, get_object_or_404
from .models import Service

def homepage(request):
    services = Service.objects.all()
    for service in services:
        service.views += 1
        service.save()
    return render(request, 'services.html', {"services": services})
    
def service_like(request, pk):
    if pk:
        service = Service.objects.get(id=pk)
        count = service.likes
        count += 1
        service.likes = count
        service.save()
    return redirect('homepage')    
    
def all_services(request):
    services = Service.objects.all()
    return render(request, 'homepage.html', {"services": services})    
    
    