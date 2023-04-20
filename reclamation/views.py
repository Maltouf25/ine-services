from django.shortcuts import render,get_object_or_404, redirect
from .models import Reclamation,Suivi
from .form import Reclamationform
from .formSuivi import suiviform
from datetime import datetime
from django.urls import reverse


# Create your views here.
def view_form(request):
    #create an instance of the class From
    my_form=Reclamationform()
    
    
    if request.method=='POST':    
        my_form=Reclamationform(request.POST)# to save the data entered
        if my_form.is_valid(): 
            reclamtion_obj=Reclamation.objects.create(**my_form.cleaned_data,time=datetime.now())
              #to save in the database
              
            context= {
                'reclamtion': my_form,
                'id': reclamtion_obj.id
                }
            return render(request, 'reclamtion_created.html',context)
   
    else:
        my_form=Reclamationform() #to clean the form
        context={
            'form':my_form
        }
        return render(request,'index-form.html',context)

def view_form_suivi(request):
    #create an instance of the class From
    my_form=suiviform()
    
    
    if request.method=='POST':    
        my_form=suiviform(request.POST)# to save the data entered
        if my_form.is_valid(): 
            Suivi.objects.create(**my_form.cleaned_data)
              #to save in the database
            my_form=suiviform() #to clean the form
   
    context={
        'form':my_form
    }
    return render(request,'index-suivi1.html',context)

def update_database_traitement(request):
    if request.method == 'POST':
        id = request.POST['object_id']
        my_object = Reclamation.objects.get(id=id)
        if my_object.traitement ==True:
            my_object.traitement = False
        else:
            my_object.traitement =True
        my_object.save()
        reclamations=Reclamation.objects.all()
        context={
            'recl':reclamations,
                }
        return render(request, 'data.html',context)

def update_database_reparer(request):
    if request.method == 'POST':
        id = request.POST['object_id']
        my_object = Reclamation.objects.get(id=id)
        if my_object.reparer ==True:
            my_object.reparer = False
        else:
            my_object.reparer =True
        my_object.save()
        reclamations=Reclamation.objects.all()
        context={
            'recl':reclamations   }
        return render(request, 'data.html',context)

def update_database_fin(request):
    if request.method == 'POST':
        id = request.POST['object_id']
        my_object = Reclamation.objects.get(id=id)
        if my_object.terminer ==True:
            my_object.terminer = False
        else:
            my_object.terminer =True
        my_object.save()
        reclamations=Reclamation.objects.all()
        context={
            'recl':reclamations   }
        return render(request, 'data.html',context)




def view_reclamation(request):
    reclamations=Reclamation.objects.all()
    context={
        'recl':reclamations   }
    return render(request,'data.html',context)


def view_reclamation_suivi(request,id):
    reclamations= Reclamation.objects.get(id=id)
    context={
        'x':reclamations   }
    return render(request,'data-suivi.html',context)

def get_reclamation(request):
    if request.method == 'POST':
        object_id = request.POST['object_id']
        num = request.POST['Numéro_de_Téléphone']
        obj=get_object_or_404(Reclamation,id=object_id)
        obj_num=obj.Numéro_de_Téléphone
        if int(obj_num)==int(num):
            return render(request, 'data-suivi.html', {'x': obj})
        else:
            print('error')
            error_msg = "Le numéro de téléphone ne correspond pas à cet ID. Veuillez réessayer."
            return render(request, 'index-suivi1.html', {'error_msg': error_msg})
    return render(request,'index-suivi1.html')


def view_home(request):
    return render (request,'index-home.html')
