from django.db import models

# Create your models here.
class Team(models.Model):
    candidate_id = models.CharField(max_length=20, default="")
    candidate_name = models.CharField(max_length=30)
    mentor_id = models.CharField(max_length=20, default="")
    mentor_name = models.CharField(max_length=30)
    course_id = models.CharField(max_length=20,primary_key=True, default="")
    course_name = models.CharField(max_length=30)
    course_category = models.CharField(max_length=30)