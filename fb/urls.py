from django.urls import path
from .views import players,player

urlpatterns = [
    path('players/',players),
    path('player/<int:i>/',player)
]