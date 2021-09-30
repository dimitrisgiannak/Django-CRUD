**NOT UP TO DATE READ TILL THE END
    Assignment : produce a solution that implements a CRUD using MVC methodologies for model Trainer

 In this assignment we where asked to create a Model Trainer and be able to create , read details ,
update and delete using technologies like Flask or Django.
 
 Details about the changes inside the Django framework are listed in -Django descr- file inside this 
folder.

 In order to run , see it on localhost and perform CRUD you need to do the following commands first :
 
 - You need to activate the venv first which is located on myenv file.

 Windows: myenv\Scripts\activate
 
 Unix or MacOS: myenv/bin/activate
 
 Activating the virtual environment will change your shell's prompt to show what virtual environment 
you are using and it will start with (myenv).

 - Then you need to go inside the project's folder named PrivateSchool and find the manage.py file.

 Once you are there type the next command: python manage.py runserver 
                                        or python3 manage.py runserver
                                           (you need to have python 3 or above)

 - Finally open your browser at localhost:8000.

 In this project we will be using the default database that Django provides(SQLite).

 
 **ADDED : new model for all deleted trainers
           new view , html , url so we can see a list with all deleted trainers as well
           two cards in home html informing us how many active trainers and how many deleted
           trainers there are!
 