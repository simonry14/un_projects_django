from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("All Projects")

def add(request):
    return HttpResponse("Add Project")


def edit(request):
    return HttpResponse("Edit Project")

# Create your views here.
