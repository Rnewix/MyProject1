from django.db import models
from django.forms import EmailField

# Create your models here.
class Job (models.Model):
    job_name = models.CharField(max_length=20)
    salary_month = models.CharField(max_length=8)
    workers_needed = models.CharField(max_length=8)
    
    def __str__(self):
        return self.job_name
    

class Worker (models.Model):
    name=models.CharField(max_length=30, verbose_name= "El Nombre")
    age=models.CharField(max_length=3)
    sex=models.CharField(max_length=3)
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    year_start=models.CharField(max_length=4)
    month_start=models.CharField(max_length=2)
    day_start=models.CharField(max_length=2)

    def __str__(self):
        return self.name
    
    
