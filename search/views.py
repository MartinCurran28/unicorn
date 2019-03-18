from django.shortcuts import render
from services.models import Service

def do_search(request):
    services = Service.objects.filter(name__icontains=request.GET['q'])
    return render(request, "services.html", {"services":services})