from django.urls import path
from . import views

urlpatterns = [
    path('characters', views.characters),
    path('create_character', views.create_character),
    path('campaigns', views.campaigns),
]