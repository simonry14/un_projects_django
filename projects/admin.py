from django.contrib import admin
from .models import project, approval_status, paas_code, country, theme, donor, fund, lead_org_unit

# Register your models here.
admin.site.register([ project, approval_status, paas_code, country, theme, donor, fund, lead_org_unit])
