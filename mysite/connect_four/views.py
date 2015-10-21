from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import json

from connect_four.models import Board

def index(request):
    return HttpResponse("Hello, world. You're at the games index.")

def my_turn(request):
    b = Board.objects.get(Q(user1=request.user) | Q(user2=request.user))
    context = {'your_turn': b.next_turn == request.user}
    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')

def play(request, user_id):
    move = None
    if int(user_id) != request.user.id:
        return render(request, '403.html')
    if request.method == "GET":
        return render(request, 'connect_four/play.html')
    elif request.method == "POST":
        if "selected" in request.POST:
            move = request.POST["selected"]

    try:
        u = request.user
        b = Board.objects.get(Q(user1=u) | Q(user2=u))
        if move:
            column = int(move.split(".")[1])
            r = b.move(u, column)
        context = {'rows': b.get_rows(), 'your_turn': b.next_turn == u}
        data = json.dumps(context)
        return HttpResponse(data, content_type='application/json')

    except ObjectDoesNotExist:
        return render(request, '404.html')
