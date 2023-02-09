from django.shortcuts import render, redirect
from .models import Student
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        language = request.POST['language']
        country = request.POST['country']
        image = request.POST['image']
        if Student.objects.create(name=name, email=email, gender=gender, language=language, country=country, image=image):
            data = {
                'studentsData': Student.objects.all()
            }
            return render(request, 'index.html', data)
        else:
            redirect("/")
    else:
        data = {
            'studentsData': Student.objects.all()
        }
        return render(request, 'index.html', data)
