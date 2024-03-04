from django.shortcuts import render
from .models import Pin


def board(request):
    board = Pin.objects.all
    return render(request, 'pins/board.html', {'board': board})
