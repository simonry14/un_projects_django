from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import project
from .tables import ProjectTable
from django_tables2 import SingleTableView

class PersonListView(SingleTableView):
    model = project
    table_class = ProjectTable
    template_name = 'projects/home.html'

def home(request):
    projects = project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/home.html', context)

def add(request):
    
    return render(request, 'projects/add.html')

def view(request,id):
    proje = project.objects.get(id=id)
    context = {'proje': proje}
    return render(request, 'projects/view.html', context)


def edit(request, id):
    
    return render(request, 'projects/edit.html',)
    #return HttpResponse("Edit Project")

# Create your views here.
