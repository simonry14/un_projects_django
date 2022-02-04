# tutorial/tables.py
import django_tables2 as tables
from .models import project

class ProjectTable(tables.Table):
    class Meta:
        model = project
        template_name = "django_tables2/bootstrap.html"
        fields = ("project_id","project_tile" )