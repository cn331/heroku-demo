from django.shortcuts import render

from .models import Task

# Create your views here.

def index(request):
    return render(request,'tasks/index.html',{
        'tasks': Task.objects.all()
    })