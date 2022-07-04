from django.shortcuts import render
from django.http import HttpResponse
import datetime
from Study_app.models import Worker
# Create your views here.

#Statict Response
def greetings(request):
    return HttpResponse('Hello there')

#Dinamic Response
def time_now(request):
    actual_time= datetime.datetime.now()
    text='now is: %s' % actual_time
    return HttpResponse(text)

#Dinamic Response with parameters from URL
def your_age(request, a, b):
    your_age= int(a)
    actual_year= 2022
    desired_year= int(b)
    future_age= (desired_year - actual_year) + your_age
    text= '''<html>
    <body> 
    Your age is: %s and in the year %s your age is going to be: %s 
    </body>
    </html>''' %(your_age, desired_year, future_age)
    return HttpResponse(text)



def show_workers(request):
    return HttpResponse('show_workers')
 
def show_jobs(request):
    return HttpResponse ('show_jobs')



#Herencia de Templates
def herencia_template(request):
    return render(request, 'Study_app/My_web/1Template_hija.html')


#Formulario Query
def formulario_trabajador(request):
    return render(request, 'Study_app/My_web/formulario_Query.html')

def resultado_query(request):
    if request.GET["query_trabajador"]:
        query= request.GET["query_trabajador"]
        if len(query)>20:
            msj="Reduce la cantidad de caracteres de tu busqueda"
        else:
            result= Worker.objects.filter(name__icontains= query)  
            if result:
                return render(request, 'Study_app/My_web/result_Query.html', {"query":query, "result":result})
            else:
                msj="No se encontro ningun resultado"
    return HttpResponse(msj)
