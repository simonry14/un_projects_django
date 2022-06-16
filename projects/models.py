from django.db import models

# Create your models here.

class paas_code(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name

class approval_status(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name
    
class country(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name
    
class theme(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name
    
class donor(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name
    
class lead_org_unit(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name
    
class fund(models.Model):
    name = models.CharField(max_length=201)
    def __str__(self):
        return self.name
    

class project(models.Model):
    project_id = models.IntegerField()
    project_title = models.CharField(max_length=201)
    start_date = models.DateField()
    end_date = models.DateField()
    total_expenditure = models.IntegerField()
    total_contribution = models.IntegerField()
    pag_value = models.IntegerField()
    total_psc = models.IntegerField(default=0)
    approval_status = models.ForeignKey(approval_status, on_delete=models.CASCADE,default=1)
    paas_code = models.ForeignKey(paas_code, on_delete=models.CASCADE,default=1)
    country = models.ForeignKey(country, on_delete=models.CASCADE,default=1)
    theme = models.ForeignKey(theme, on_delete=models.CASCADE,default=1)
    donor = models.ForeignKey(donor, on_delete=models.CASCADE,default=1)
    lead_org_unit = models.ForeignKey(lead_org_unit, on_delete=models.CASCADE,default=1)
    fund = models.ForeignKey(fund, on_delete=models.CASCADE,default=1)
    
    
    def __str__(self) -> str :
        return str(self.project_id)
    
