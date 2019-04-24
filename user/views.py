from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User
from .forms import UserForm

def get_user(request):
    profos = User.objects.all()
    return render(request, "user_details.html", {"profos": profos})

def create_or_edit_user(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    profo = get_object_or_404(User, pk=pk) if pk else None
    if request.method == "POST":
        profo = UserForm(request.POST, request.FILES, instance=profo)
        if profo.is_valid():
            profo = profo.save()
            return render(request, "user_details.html", {'profo':profo})
    else:
        profo = UserForm(instance=profo)
    return render(request, 'user.html', {'profo': profo})  