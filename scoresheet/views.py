import os

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from datetime import date

import pandas as pd
from scoresheet.forms import DocumentForm
from scoresheet.models import ScoreSheet
from scoresheet.recommender import prep_for_cbr
from suggestedcourse.models import SuggestedCourse


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
                    temp_data = ScoreSheet.objects.filter(candidate_id=data[1],course_id=data[6])
                    if len(temp_data)!=0:
                        temp_data.update(attempt_id=data[7],mark=data[8],grade=data[9])
                    else:
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

        score_sheets = ScoreSheet.objects.all()
        data = pd.read_csv(STATIC_ROOT+'/assets/datasets/coursera-courses.csv',encoding='utf8')
        for score_sheet in score_sheets:
            if score_sheet.mark < 70.0:
                selected_mentors = [ score for score in ScoreSheet.objects.all() if score.mark >= 70.0 and score.course_name ==  score_sheet.course_name]
                
                course_status_update = SuggestedCourse.objects.filter(candidate_id = score_sheet.candidate_id, 
                                                                    suggested_course_name = score_sheet.course_name)
                course_status_update.update(status = 'Completed')
    
                
                suggestions = prep_for_cbr(data, score_sheet.course_name, score_sheet.course_category )
                if len(suggestions) == 0:
                    suggested_course = SuggestedCourse(course_id=score_sheet.course_id, 
                                                       course_name = score_sheet.course_name,
                                                       course_category = score_sheet.course_category,
                                                       suggested_course_id= '-NA-',
                                                       suggested_course_name=str(suggestions),
                                                       suggested_course_duration='-NA-',
                                                       suggested_course_instructor='-NA-',
                                                       suggested_course_category='-NA-',
                                                       suggested_course_url='-NA-',
                                                       candidate_id = score_sheet.candidate_id,
                                                       candidate_name = score_sheet.candidate_name,
                                                       suggested_mentor_id ='-NA-',
                                                       suggested_mentor_name ='-NA-',
                                                       suggested_mentee_id ='-NA-',
                                                       suggested_mentee_name='-NA-'
                                                        )
                    suggested_course.save()
                    
                    
                else:
                    candidate = SuggestedCourse.objects.all().filter(candidate_id=score_sheet.candidate_id,course_name = score_sheet.course_name  )
                    if len(candidate)==0:
                        
                        for i in range(len(suggestions)):
                            mentor_id=''
                            mentor_name=''
                            if len(selected_mentors)==0:
                                mentor_id = '-NA-'
                                mentor_name = '-NA-'
                            else:
                                mentor_id = selected_mentors[i].candidate_id
                                mentor_name = selected_mentors[i].candidate_name
                        #Assigning the mentors
                            suggested_course = SuggestedCourse(course_id=score_sheet.course_id, 
                                                       course_name = score_sheet.course_name,
                                                       course_category = score_sheet.course_category,
                                                       suggested_course_id= 'CPRTS'+ str(date.today()),
                                                       suggested_course_name=suggestions.iloc[i]['course_name'],
                                                       suggested_course_duration=suggestions.iloc[i]['estimated_time_to_complete'],
                                                       suggested_course_instructor=str(suggestions.iloc[i]['instructors']),
                                                       suggested_course_category=suggestions.iloc[i]['learning_product_type'],
                                                       suggested_course_url=suggestions.iloc[i]['course_url'],
                                                       candidate_id = score_sheet.candidate_id,
                                                       candidate_name = score_sheet.candidate_name,
                                                       suggested_mentor_id = mentor_id,
                                                       suggested_mentor_name = mentor_name,
                                                       suggested_mentee_id ='-NA-',
                                                       suggested_mentee_name='-NA-'
                                                        )
                            suggested_course.save()
                            
            else:
                course_status_update = SuggestedCourse.objects.filter(candidate_id = score_sheet.candidate_id, 
                                                                    suggested_course_name = score_sheet.course_name)
                course_status_update.update(status = 'Completed')  
            
         
                
        return redirect('suggest')

        
        
        
        