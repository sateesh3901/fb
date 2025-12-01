from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PlayersSerializer
from .models import Players

# Create your views here.
def players(request):
    players = Players.objects.all()
    sr = PlayersSerializer(players, many = True)
    return JsonResponse({"players":sr.data},safe=False)

def player(request,i):
    try:
        player = Players.objects.get(id = i) 
    except:
        return JsonResponse({"status":"player not found or invalid player id"})
    
    sr = PlayersSerializer(player)
    return JsonResponse({"player":sr.data})