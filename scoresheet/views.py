from django.shortcuts import render, redirect
import numpy as np
import pandas as pd
from scoresheet.forms import DocumentForm
from scoresheet.models import ScoreSheet
import os
from sklearn.ensemble import RandomForestClassifier
from scoresheet.recommender import prep_for_cbr
from django.http.response import HttpResponse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Create your views here.
def upload_data(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            is_header=True
            csvfile = request.FILES['document'];
            for row in csvfile:
                if is_header:
                    is_header=False
                else:
                    data=row.decode('utf-8').split(",")
                    score_sheet = ScoreSheet(candidate_id=data[1], candidate_name=data[2],gender=data[3],
                                             candidate_email=data[4],course_name=data[5], course_id=data[6],
                                             attempt_id=data[7],mark=data[8],grade=data[9], course_category=data[10])
                    score_sheet.save()
                      
            form.save()
            return render(request,'faculty/faculty-upload-score.html',{'msg':'Score Sheet uploaded successfully!',"value":"success", 'scores' : ScoreSheet.objects.all()})
        else:
            return render(request,'faculty/faculty-upload-score.html',{'msg':'Error uploading Score Sheet!',"value":"danger"})


# Create your views here.
def fetch_data(request):
    if request.method == 'POST':
        score_sheets = [ score.course_category for score in ScoreSheet.objects.all() ]
        prediction_data=np.asarray(list(set(score_sheets)))
        data = pd.read_csv(STATIC_ROOT+'/assets/datasets/courses-details.csv')
        prep_for_cbr(data, "IBM Applied AI")
        return HttpResponse("<h1>OK</h1>")
       

        
        
        
        