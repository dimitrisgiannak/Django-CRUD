from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import TrainerForm
from .models import Trainer , Del_Trainer
from django.contrib import messages






def home(request):
    add_count = Trainer.objects.filter().count
    if not add_count:
        add_count = 0
        
    del_count = Del_Trainer.objects.filter().count
    if not del_count:
        del_count = 0
    return render(request , "trainer/home.html" , {"add_count" : add_count , 
                                                   "del_count" : del_count ,
                                                   })


def add_trainer(request):
    if request.method == "POST":
        trainer_form = TrainerForm(request.POST)
        if trainer_form.is_valid():
            trainer_form.save()
            

            return HttpResponseRedirect("/")
    
    else:
        trainer_form = TrainerForm()

    return render(request , "trainer/add_trainer.html" , {"form" : trainer_form})


"""

def update_trainer(request , pk):
    trainer = Trainer.objects.get(pk = pk)
    if request.method == "POST":
        messages.success(request , "Successfully updated")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        subject = request.POST.get("subject")
        trainer.first_name = first_name
        trainer.last_name = last_name
        trainer.subject = subject
        trainer.save()

        return HttpResponseRedirect("/show_trainers/")
    
    else:
        first_name = trainer.first_name
        last_name = trainer.last_name
        subject = trainer.subject
    
    return render(request , "trainer/update_trainer.html" , 
                  {"first_name" : first_name ,
                   "last_name"  : last_name ,
                    "subject"   : subject
                  })

"""
def update_trainer(request , pk):
    trainer = Trainer.objects.get(pk = pk)
    form = TrainerForm(instance = trainer)
    if request.method == 'POST':
        form = TrainerForm(request.POST , instance = trainer)
        
        if form.is_valid():
            form.save()
            messages.success(request , "Successfully updated")
            return HttpResponseRedirect("/show_trainers/")
        
    else:
        form = TrainerForm(instance = trainer)

    return render(request ,
                  "trainer/update_trainer.html" ,
                  {"form" : form } ,
                  )


def delete_trainer(request , pk):
    delete_trainer = Trainer.objects.get(pk = pk)
    add_to_bin = Del_Trainer(delete_trainer.pk , delete_trainer.first_name , delete_trainer.last_name , delete_trainer.subject)
    add_to_bin.save()
    delete_trainer.delete()
    messages.success(request , "Successfully deleted")
    
    return HttpResponseRedirect("/show_trainers/")




def show_trainers(request):
    trainers_list = Trainer.objects.all()
    return render (request , "trainer/all_trainers.html" , 
                   {"tr_list" : trainers_list} 
                  )


def deleted_trainers(request):
    del_trainers = Del_Trainer.objects.all()
    return render (request , "trainer/del_trainers.html" , 
                    {"del_list" : del_trainers})