from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import *

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email','mobile','password1','password2','branch']


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

class PatientForm(forms.ModelForm):
    class Meta:
        model = Paitent
        fields = ['name','mobile','age']