from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()

    ctx={
        'form' : form,
    }
    return render(request, 'accounts/signup_form.html',ctx)


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
