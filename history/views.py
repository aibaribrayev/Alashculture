from django.shortcuts import render
from .models import History

def allhistory(request):
    history = History.objects
    return render(request, 'history/allhistory.html', {'history':history})
