from django.shortcuts import render
from .models import *
# Create your views here.

def lessons(request):
    if "search" in request.GET:
        lessons = LessonsModel.objects.filter(title__icontains = request.GET['search'])
    else:
        lessons = LessonsModel.objects.all()
    return render(request, 'lessons.html', {"lessons": lessons})


