from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Campaign(models.Model):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=10, null=True, blank=True)
    user = models.ForeignKey(User, related_name="campaigns_created", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # characters = list of characters who have joined this campaign.

class Character(models.Model):
    name = models.CharField(max_length=128)
    dex = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    bonus = models.IntegerField(validators=[MinValueValidator(-10), MaxValueValidator(30)])
    current_init = models.IntegerField(default=0, validators=[MinValueValidator(-10), MaxValueValidator(30)])
    user = models.ForeignKey(User, related_name="characters_created", on_delete=models.CASCADE)
    campaigns_joined = models.ManyToManyField(Campaign, related_name="characters")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

