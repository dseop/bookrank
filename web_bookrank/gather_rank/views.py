from django.http import HttpResponse
from django.shortcuts import render
from .models import bookcode, bookdata, bookrank

def intro(request):
    bookcodes = bookcode.objects.all()
    context = {
        "bookcodes": bookcodes
    }
    return render(request, 'index.html', context)

