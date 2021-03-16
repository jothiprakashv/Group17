from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=20,primary_key=True, default="")
    course_name = models.CharField(max_length=30)
    course_type = models.CharField(max_length=30) 
    course_duration = models.CharField(max_length=30)
    course_instructor = models.CharField(max_length=30)
    course_category = models.CharField(max_length=30)
    course_url = models.URLField();