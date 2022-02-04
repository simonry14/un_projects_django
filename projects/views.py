from django.shortcuts import render
from django.http import HttpResponse
from .models import project
from .tables import ProjectTable
from django_tables2 import SingleTableView

class PersonListView(SingleTableView):
    model = project
    table_class = ProjectTable
    template_name = 'projects/home.html'

#def home(request):
#    projects = project.objects.all()
#    context = {'projects', projects}
#    return render(request, 'projects/home.html', context)

def add(request):
    
    return render(request, 'projects/add.html')

def view(request):
    
    return render(request, 'projects/view.html')


def edit(request, id):
    
    return render(request, 'projects/edit.html',)
    #return HttpResponse("Edit Project")

# Create your views here.
