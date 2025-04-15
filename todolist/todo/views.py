from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.

def todo_home(request, *args, **kwargs):
    return render(request, 'partials/base.html')