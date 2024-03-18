from django.shortcuts import render, redirect, get_object_or_404
from .models import *
# Create your views here.

def pupils(request):
    if "search" in request.GET:
        students = PupilsModels.objects.filter(name__icontains=request.GET['search'])
    else:
        students = PupilsModels.objects.all().order_by('-id')
    return render(request, 'pupils.html', {"students" : students})

def pupil_list(request, id):
    student = PupilsModels.objects.get(id=id)
    return render(request, 'pupils_list.html', {"student": student})




def add_pupil(request):
    if request.method == "POST":
        name = request.POST['name']
        spec = request.POST['spec']
        pupil_img = request.FILES.get('img')
        res_1 = request.POST['res_1']
        res_2 = request.POST['res_2']
        res_3 = request.POST['res_3']
        res_4 = request.POST['res_4']
        res_5 = request.POST['res_5']

        users = PupilsModels(name=name, spec=spec, pupil_img=pupil_img, res_1=res_1, res_2=res_2, res_3=res_3, res_4=res_4, res_5=res_5)
        users.save()

        return redirect('/pupils')
    else:
        return render(request, 'add_pupil.html')

def delete_user(request, id):
    PupilsModels.objects.filter(pk=id).delete()
    return redirect('/pupils')


def edit_user(request, id):
    pupil = PupilsModels.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        spec = request.POST['spec']
        pupil_img = request.FILES.get('image')
        res_1 = request.POST['res_1']
        res_2 = request.POST['res_2']
        res_3 = request.POST['res_3']
        res_4 = request.POST['res_4']
        res_5 = request.POST['res_5']

        pupil.name = name
        pupil.spec = spec
        pupil.pupil_img = pupil_img
        pupil.res_1 = res_1
        pupil.res_2 = res_2
        pupil.res_3 = res_3
        pupil.res_4 = res_4
        pupil.res_5 = res_5
        
        pupil.save()
        return redirect('/pupils')
    else:
        return render(request, 'edit_pupil.html', {'pupil': pupil})
