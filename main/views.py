from django.shortcuts import render
from .models import (
    Academy,
    Manager,
    Mentor,
    Student,
)


def index(request):
    academys = Academy.objects.all()
    context = {
        'academys':academys
    }
    return render(request, 'main/index.html', context)

def academy(request, pk):
    academys = Academy.objects.all()
    academy = Academy.objects.get(id=pk)

    mentors = Mentor.objects.filter(academy=academy)

    managers = Manager.objects.filter(academy=academy)

    students = Student.objects.filter(academy=academy)
   

    context = {
        'academys': academys,
        'managers': managers,
        'mentors': mentors,
        'students': students,

    }
    return render(request, 'main/academy.html',context)
