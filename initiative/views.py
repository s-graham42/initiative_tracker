from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Character, Campaign
from .forms import CharacterForm, CampaignForm
import random
import string

# functions
def generate_code(length):
    letters_and_numbers = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(letters_and_numbers) for i in range(length)))
    return result_str

# Create your views here.
def characters(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(dict(request.POST))
            form = CharacterForm(request.POST)
            if form.is_valid():
                print("form is valid")
                newCharacter = form.save(commit=False)
                newCharacter.user = request.user
                newCharacter.save()
                print("newCharacter saved")
                return HttpResponseRedirect('/initiative/characters')
        else:
            form = CharacterForm()
            return render(request, 'characters.html', {'form': form})
        return render(request, 'characters.html', {'form': form})
    return redirect('/')

def campaigns(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(dict(request.POST))
            form = CampaignForm(request.POST)
            print(form)
            if form.is_valid():
                print("form is valid")
                # save the name
                newCampaign = form.save(commit=False)
                # generate a code
                newCode = generate_code(4)
                print(f'New Code is: {newCode}')
                #assign code to newCampaign
                newCampaign.code = newCode
                newCampaign.user = request.user
                newCampaign.save()
                print("newCampaign saved")
                return redirect('/initiative/campaigns')
            else:
                print("Not Valid")
        else:
            form = CampaignForm()
            return render(request, 'campaigns.html', {'form': form})
        return render(request, 'campaigns.html', {'form': form})
    return redirect('/')

def show_character(request, char_id):
    if request.user.is_authenticated:
        one_char = Character.objects.filter(id=char_id)
        if len(one_char) > 0:
            one_char = one_char[0]
            form = CampaignForm()
            return render(request, 'one_character.html', {'one_char': one_char, 'form': form})
    return redirect('/')

def join_campaign(request, char_id):
    if request.user.is_authenticated: # is user logged in?
        if request.method == 'POST':
            one_char = Character.objects.filter(id=char_id) # does the character exist?
            if len(one_char) > 0:
                one_char = one_char[0] # if it does, select the first one in the list.
                if one_char.user == request.user: # does the logged in user own this character?
                    form = CampaignForm(request.POST) # fill in the form
                    if form.is_valid(): # if it's valid info:
                        campaign_to_join = Campaign.objects.filter(name=form.cleaned_data['name'])
                        if len(campaign_to_join) > 0:
                            campaign_to_join = campaign_to_join[0]
                            # print(form.cleaned_data)
                            # print(campaign_to_join.code)
                            # print(form.cleaned_data['code'])
                            # print(form.cleaned_data['code'].upper())
                            if campaign_to_join.code == form.cleaned_data['code'].upper():
                                one_char.campaigns_joined.add(campaign_to_join)
                                return redirect(f'/initiative/character/{char_id}')
                return redirect(f'/initiative/character/{char_id}')
        return redirect('/initiative/characters')
    return redirect('/')

def leave_campaign(request, char_id):
    if request.user.is_authenticated: # is user logged in?
        if request.method == 'POST':
            one_char = Character.objects.filter(id=char_id) # does the character exist?
            if len(one_char) > 0:
                one_char = one_char[0] # if it does, select the first one in the list.
                if one_char.user == request.user: # does the logged in user own this character?
                    campaign_to_leave = Campaign.objects.filter(id=request.POST['campaign'])
                    if len(campaign_to_leave) > 0:
                        campaign_to_leave = campaign_to_leave[0]
                        one_char.campaigns_joined.remove(campaign_to_leave)
                        return redirect(f'/initiative/character/{char_id}')
                return redirect(f'/initiative/character/{char_id}')
        return redirect('/initiative/characters')
    return redirect('/')

def delete_character(request, char_id):
    if request.user.is_authenticated: # is user logged in?
        if request.method == 'POST':
            one_char = Character.objects.filter(id=char_id) # does the character exist?
            if len(one_char) > 0:
                one_char = one_char[0] # if it does, select the first one in the list.
                if one_char.user == request.user: # does the logged in user own this character?
                    one_char.delete()
        return redirect('/initiative/characters')           
    return redirect('/')
    
def initiative_main(request, campaign_id):
    if request.user.is_authenticated: # is user logged in?
        one_campaign = Campaign.objects.filter(id=campaign_id)
        if len(one_campaign) > 0:
            one_campaign = one_campaign[0]
            context = {
                'campaign': one_campaign,
                'characters': Character.objects.filter(campaigns_joined=one_campaign).order_by('-current_init', '-dex', '-bonus'),
            }
            return render(request, 'initiative_main.html', context)
        return redirect('/initiative/campaigns')
    return redirect('/')

def enter_initiative(request, char_id):
    if request.method == "POST":
        if request.user.is_authenticated: # is user logged in?
            this_character = Character.objects.filter(id=char_id) # does the character exist?
            if len(this_character) > 0:
                this_character = this_character[0]
                if this_character.user.id == request.user.id:
                    this_character.current_init = request.POST['current_initiative']
                    this_character.save()
                    return redirect(f"/initiative/campaigns/{request.POST['current_campaign']}")
    return redirect('/')

def enter_init(request):
    if request.method == "POST":
        print(request.POST)
        if request.user.is_authenticated: # is user logged in?
            char_id = request.POST['current_character']
            this_character = Character.objects.filter(id=char_id) # does the character exist?
            if len(this_character) > 0:
                this_character = this_character[0]
                if this_character.user.id == request.user.id:
                    this_character.current_init = request.POST['current_initiative']
                    this_character.save()
                    one_campaign = Campaign.objects.get(id=request.POST['current_campaign'])
                    context = {
                        'campaign': one_campaign,
                        'characters': Character.objects.filter(campaigns_joined=one_campaign).order_by('-current_init', '-dex', '-bonus'),
                    }
                    return render(request, "main_init_table.html", context)
    return redirect('/')