from django.shortcuts import render, redirect
from .models import Registration, Courses

# Create your views here.

def index(request):
    return render(request,'index.html')

def courses(request):
    data = Courses.data.all()
    return render(request, 'courses.html',{"data":data})


    