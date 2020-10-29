from django.urls import path
from . import views

urlpatterns = [
    path('characters', views.characters),
]