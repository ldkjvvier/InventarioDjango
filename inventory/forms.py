from django import forms

class UserRegistrationForm(forms.Form):
    nombre = forms.CharField()
    fono = forms.CharField()
    email = forms.CharField()