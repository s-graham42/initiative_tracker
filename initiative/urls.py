from django.urls import path
from . import views

urlpatterns = [
    path('characters', views.characters),
    path('campaigns', views.campaigns),
    path('campaigns/<int:campaign_id>', views.initiative_main),
    path('character/<int:char_id>', views.show_character),
    path('character/<int:char_id>/join_campaign', views.join_campaign),
    path('character/<int:char_id>/leave_campaign', views.leave_campaign),
    path('enter_initiative/<int:char_id>', views.enter_initiative),
]