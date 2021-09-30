from django.db import models

# Create your models here.
class Trainer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)
    #updated = models.DateTimeField(auto_now = True)
    #created = models.DateTimeField(auto_now_add = True)

#   class Meta:
#       ordering = ["-updated"]

class Del_Trainer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)