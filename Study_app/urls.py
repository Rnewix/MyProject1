from django.urls import path
from Study_app import views


app_name= 'Study_app'

urlpatterns = [
    path('', views.greetings, name='greetings'),
    path('dinamic_response/', views.time_now, name='time_now'),
    path('dinamic_resp_parametURL/<a>/<b>/', views.your_age, name='your_age'),
    path('workers/', views.show_workers, name='show_workers'),
    path('jobs/', views.show_jobs, name='show_jobs'),  
    path('herencia_template/', views.herencia_template, name='herencia_template'),
    path('formulario/', views.formulario_trabajador, name='formulario_trabajador'),
    path('resultado_Query/', views.resultado_query, name='resultado_query'),
]    