from django.db import models

# Create your models here.
class ScoreSheet(models.Model):
    course_id = models.CharField(max_length=20, default="")
    course_name = models.CharField(max_length=30)
    course_category = models.CharField(max_length=30,default="")
    attempt_id = models.CharField(max_length=30) 
    candidate_id = models.CharField(max_length=30)
    candidate_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    candidate_email = models.EmailField(blank=True)
    mark = models.IntegerField()
    grade = models.CharField(max_length=30)

class FileStoreage(models.Model):
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)