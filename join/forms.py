from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Join

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ('name', 'surname', 'email', 'phone', 'town', 'street_address1', 'street_address2', 'county', 'date', 'cover_letter', 'cv')