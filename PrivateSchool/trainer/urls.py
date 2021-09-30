from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('update_trainer/<int:pk>/', views.update_trainer, name='update_trainer'),
    path('delete_trainer/<int:pk>/', views.delete_trainer, name='delete_trainer'),
    path('show_trainers/', views.show_trainers, name='show_trainers'),
    path('deleted_trainers/', views.deleted_trainers, name='deleted_trainers'),
]