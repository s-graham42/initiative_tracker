from django.urls import path
from . import views

urlpatterns = [
    path('characters', views.characters),
    # path('create_character', views.create_character),
    path('campaigns', views.campaigns),
    path('character/<int:char_id>', views.show_character),
    path('character/<int:char_id>/join_campaign', views.join_campaign),
]