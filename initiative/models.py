from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    # characters = list of characters who have joined this campaign.

class Character(models.Model):
    name = models.CharField(max_length=128)
    dex = models.IntegerField()
    bonus = models.IntegerField()
    user = models.ForeignKey(User, related_name="characters_created", on_delete=models.CASCADE)
    campaign_joined = models.ForeignKey(Campaign, related_name="characters", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_add_now=True)
    updated_at = models.DateTimeField(auto_now=True)

