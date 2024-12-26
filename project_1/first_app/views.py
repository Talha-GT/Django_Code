from django.shortcuts import render
from django.http import HttpResponse

def AllCourses(r):
    return HttpResponse("Hello from first_app/AllCourses")

def AppHome(r):
    return HttpResponse("Hello from first_app/Home page")

def AllResource(r):
    return HttpResponse("Hello from first_app/AllResource")


# Create your views here.
