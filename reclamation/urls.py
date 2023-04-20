from django.contrib import admin
from django.urls import path,include
from .views import view_form,view_reclamation ,view_reclamation_suivi,view_form_suivi

urlpatterns = [
    path("",view_form),
     path('data/',view_reclamation),
     
     
]