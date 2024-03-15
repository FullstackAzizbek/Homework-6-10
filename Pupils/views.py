from django.shortcuts import render
from .models import *
# Create your views here.

def pupils(request):
    if "search" in request.GET:
        students = PupilsModels.objects.filter(name__icontains=request.GET['search'])
    else:
        students = PupilsModels.objects.all()
    return render(request, 'pupils.html', {"students" : students})

def pupil_list(request, id):
    student = PupilsModels.objects.get(id=id)
    return render(request, 'pupils_list.html', {"student": student})