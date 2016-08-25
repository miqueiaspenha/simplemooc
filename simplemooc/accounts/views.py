from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from simplemooc.accounts import forms

# Create your views here.

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = forms.RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
