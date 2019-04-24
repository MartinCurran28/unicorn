from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Join
from .forms import JoinForm

def get_app(request):
    return render(request, "app_details.html")

def create_or_edit_app(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    app = get_object_or_404(Join, pk=pk) if pk else None
    if request.method == "POST":
        app = JoinForm(request.POST, request.FILES, instance=app)
        if app.is_valid():
            app = app.save()
            return render(request, "app_details.html", {'app':app})
    else:
        app = JoinForm(instance=app)
    return render(request, 'application.html', {'app': app})  