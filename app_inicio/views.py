from django.shortcuts import render
import datetime as dt

# Create your views here.
def index(request):
    fecha = dt.datetime.date(dt.datetime.now())
    ctx = {
        'fecha':fecha
    }
    return render(request, 'index/index.html', ctx)