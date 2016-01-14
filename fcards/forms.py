from django import forms
from django.contrib.auth.models import User
from .models import Card, Subject

class CardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ('term', 'defin',)

class SetForm(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields = ('name',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')