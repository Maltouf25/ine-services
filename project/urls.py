"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from reclamation.views import update_database_traitement, update_database_fin,view_form_suivi,get_reclamation,update_database_reparer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include('reclamation.urls')),
    path('data/traitement/', update_database_traitement, name='update_database_traitement'),
    path('data/terminer/', update_database_fin, name='update_database_fin'),
    path('data/reparer/', update_database_reparer, name='update_database_reparer'),
    path('suivi/details/', get_reclamation, name='get_reclamation'),
    path("suivi/",view_form_suivi, name='view_form_suivi'),
   

]
