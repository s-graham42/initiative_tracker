from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from initiative.models import Character, Campaign


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/accounts/profile')
    else:
        return render(request, 'index.html')

def profile(request):
    context = {
        'all_users': User.objects.all(),
    }
    return render(request, 'profile.html', context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/profile')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
