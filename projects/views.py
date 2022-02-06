from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import project
from .tables import ProjectTable
from .forms import ProjectForm
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
    form = ProjectForm()
    if request.method=="POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form': form ,'title': 'Add Project'}
    return render(request, 'projects/add.html', context)

def view(request,id):
    proje = project.objects.get(id=id)
    context = {'project': proje}
    return render(request, 'projects/view.html', context)


def edit(request, id):
    pro = project.objects.get(id = id)
    form = ProjectForm(instance=pro)
    context = {'form': form, 'title': 'Edit Project'}
    if request.method=="POST":
        form = ProjectForm(request.POST, instance=pro)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'projects/add.html', context)
    

# Create your views here.
