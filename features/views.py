from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Debug

def all_debug(request):
    debugs = Debug.objects.all()
    for debug in debugs:
        debug.views += 1
        debug.save()
    return render(request, 'debug_details.html', {"debugs": debugs})
    
def bug_details(request, pk):
    debug = get_object_or_404(Debug, pk=pk)
    debug.views += 1
    debug.save()
    return render(request, 'debug_view.html', {'debug': debug})  
    
def bug_like(request, pk):
    if pk:
        debug = Debug.objects.get(id=pk)
        count = debug.likes
        count += 1
        debug.likes = count
        debug.save()
    return redirect('all_debug')
    
def free_debug(request):
    debugs = Debug.objects.all()
    return render(request, 'free_debug.html', {"debugs": debugs})    
    
def form_view(request):
    return render(request, 'form.html')
    
def join_us(request):
    return render(request, 'join_us.html')    
    
    
