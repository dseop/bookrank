from django.http import HttpResponse
from .models import bookcode, bookdata, bookrank

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def intro(request):
    bookcodes = bookcode.objects.all()
    context = {
        "bookcodes": bookcodes
    }
    return render(request, 'index.html', context)

