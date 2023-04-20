from django.contrib import admin
from django.urls import path,include
from .views import view_form,view_reclamation ,view_reclamation_suivi,view_form_suivi,view_home

urlpatterns = [
    path("form",view_form),
    path('data/',view_reclamation),
    path('',view_home)
     
     
]