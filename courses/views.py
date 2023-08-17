from django.shortcuts import render
from .models import Courses

def index(request):
    return render(request, 'courses/index.html')

def courses(request):
    courses_list = Courses.objects.all()
    return render(request, 'courses/courses.html',{'courses_list':courses_list})

def about(request):
    return render(request,"courses/about.html")

def benefits(request):
    return render(request,"courses/benefits.html")

