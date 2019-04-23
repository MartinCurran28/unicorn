from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Form

class BugForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ('name', 'email', 'title', 'content', 'image')