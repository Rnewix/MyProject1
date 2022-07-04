from django.contrib import admin
from Study_app.models import Job, Worker

# Register your models here.

class WorkerAdminDisplay(admin.ModelAdmin):
    list_display = ('name', 'age', 'job')                        #Clase overdrive
    search_fields = ('name', 'age', 'job__job_name')   


admin.site.register(Job)
admin.site.register(Worker, 
                    WorkerAdminDisplay)