from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Character
from .forms import CharacterForm, CampaignForm

# Create your views here.
def characters(request):
    form = CharacterForm
    context = {
        'form': form,
    }
    return render(request, 'characters.html', context)

def create_character(request):
    if request.method == "POST":
        # print(dict(request.POST))
        form = CharacterForm(request.POST)
        if form.is_valid():
            newCharacter = form.save(commit=False)
            newCharacter.user = request.user
            newCharacter.save()
            return redirect('/initiative/characters')
    return redirect('/initiative/characters')

def campaigns(request):
    return render(request, 'campaigns.html')