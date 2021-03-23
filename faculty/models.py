from django.db import models

# Create your models here.



class Faculty(models.Model):
    faculty_id = models.CharField(max_length=20,primary_key=True, default="")
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=30) 
    gender = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    role = models.CharField(max_length=30, blank=True)