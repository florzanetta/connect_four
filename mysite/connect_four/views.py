from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import json

from connect_four.models import Board

def index(request):
    return HttpResponse("Hello, world. You're at the games index.")

def play(request, user_id):
    # check if user_id matches the logged user_id
    move = None
    if request.method == "GET":
        return render(request, 'connect_four/play.html')
    elif request.method == "POST":
        move = request.POST["selected"]

    try:
        u = User.objects.get(id=user_id)
        b = Board.objects.get(Q(user1=u) | Q(user2=u))
        if move:
            column = int(move.split(".")[1])
            r = b.move(u, column)
            # print(r)
        context = {'rows': b.get_rows()}
        data = json.dumps(context)
        return HttpResponse(data, content_type='application/json')
        #

    except ObjectDoesNotExist:
        return render(request, '404.html')
