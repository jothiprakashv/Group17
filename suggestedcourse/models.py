from django.db import models
from datetime import date

# Create your models here.
class SuggestedCourse(models.Model):
    course_id = models.CharField(max_length=20, default="")
    course_name = models.CharField(max_length=150)
    course_category = models.CharField(max_length=150) 
    suggested_course_id = models.CharField(max_length=150) 
    suggested_course_name = models.CharField(max_length=150) 
    suggested_course_duration = models.CharField(max_length=30)
    suggested_course_instructor = models.CharField(max_length=200)
    suggested_course_category = models.CharField(max_length=50)
    suggested_course_url = models.URLField();
    candidate_id = models.CharField(max_length=30)
    candidate_name =  models.CharField(max_length=30)
    suggested_mentor_id =  models.CharField(max_length=50)
    suggested_mentor_name =  models.CharField(max_length=50)
    suggested_mentee_id =  models.CharField(max_length=50)
    suggested_mentee_name =  models.CharField(max_length=50)
    assigned_on = models.DateField(default=date.today())
    status = models.CharField(max_length=30,default="Assigned")