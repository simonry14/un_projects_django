import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import project, country, approval_status
from .tables import ProjectTable
from .forms import ProjectForm
from django_tables2 import SingleTableView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import projectSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

class PersonListView(SingleTableView):
    model = project
    table_class = ProjectTable
    template_name = 'projects/home.html'
    
def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username = username)
            
        except:
            messages.error(request, 'User Doesnt Exist')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Username OR Password Doesnt Exist')
            
        
    context = {'page': page}
    return render(request, 'projects/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurd during registration')
            
          
    form = UserCreationForm()
    context = {'form': form}
    
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
    
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))    
def all(request):
    projects = project.objects.all()
    serializer = projectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))    
def by_country(request, countr):
    country_id = country.objects.get(name = countr)
    projects = project.objects.filter(country__exact = country_id)
    serializer = projectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))    
def by_status(request, statu):
    status_id = approval_status.objects.get(name = statu)
    projects = project.objects.filter(approval_status__exact = status_id)
    serializer = projectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))    
def add_project(request):
    serializer = projectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    

# Create your views here.
