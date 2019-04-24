from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Form
from .forms import BugForm

def get_form(request):
    forms= Form.objects.all()
    return render(request, "bugform.html", {"forms":forms})

def create_or_edit_form(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    form = get_object_or_404(Form, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form = form.save()
            return render(request, "form_details.html")
    else:
        form = BugForm(instance=form)
    return render(request, 'bugform.html', {'form': form})  