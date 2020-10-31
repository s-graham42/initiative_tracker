from django.forms import ModelForm
from .models import Character, Campaign

class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'dex', 'bonus']

class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['name', 'code']