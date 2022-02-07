from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import project
from .tables import ProjectTable
from .forms import ProjectForm
from django_tables2 import SingleTableView

class PersonListView(SingleTableView):
    model = project
    table_class = ProjectTable
    template_name = 'projects/home.html'
    
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
            
        except:
            messages.error(request, 'User Doesnt Exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return render('projects/home.html')
        else:
             messages.error(request, 'Username OR Password Doesnt Exist')
            
        
    context = {}
    return render(request, 'projects/login_register.html', context)

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
    context = {'project': proje, 'title': 'View Project'}
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

def delete(request, id):
    obj = project.objects.get(id=id)
    
    if request.method == 'POST':
        obj.delete()
        return redirect('home')
        
    
    return render(request, 'delete.html', {'project': obj})
    
    
    

# Create your views here.
