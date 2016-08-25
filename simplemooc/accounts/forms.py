form django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    emial = forms.EmailField(label='E-mail')
