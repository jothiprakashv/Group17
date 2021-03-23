# -*- encoding: utf-8 -*-

import json

from django.contrib.auth import authenticate, login
from django.db.models.aggregates import Avg
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template import loader

from scoresheet.models import ScoreSheet
from suggestedcourse.models import SuggestedCourse

from .admin import User
from .forms import LoginForm, SignUpForm


# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    context = { 
        }
       
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_staff:
                        score_sheets = ScoreSheet.objects.all()
                        suggested_courses = SuggestedCourse.objects.all()
                        programming_skills_avg = ScoreSheet.objects.filter(course_category='Programming\r\n').aggregate(Avg('mark'))['mark__avg']
                        soft_skills_avg = ScoreSheet.objects.filter(course_category='Communication\r\n').aggregate(Avg('mark'))['mark__avg']
                        analytical_skills_avg = ScoreSheet.objects.filter(course_category='Analytics\r\n').aggregate(Avg('mark'))['mark__avg']
                        context = { 'score_sheets': score_sheets,
                                           'suggested_courses': suggested_courses,
                                           'chart':json.dumps([programming_skills_avg, soft_skills_avg, analytical_skills_avg]),
                                           
                                    }
                        html_template = loader.get_template( 'faculty/dashboard.html' )
                        return HttpResponse(html_template.render(context, request))
                else:
                    score_sheets = ScoreSheet.objects.filter(candidate_id = user.last_name)
                    suggested_courses = SuggestedCourse.objects.filter(candidate_id = user.last_name)
                    programming_skills_avg = ScoreSheet.objects.filter(candidate_id = user.last_name, course_category='Programming\r\n').aggregate(Avg('mark'))['mark__avg']
                    soft_skills_avg = ScoreSheet.objects.filter(candidate_id = user.last_name, course_category='Communication\r\n').aggregate(Avg('mark'))['mark__avg']
                    analytical_skills_avg = ScoreSheet.objects.filter(candidate_id = user.last_name, course_category='Analytics\r\n').aggregate(Avg('mark'))['mark__avg']
                    print(programming_skills_avg, soft_skills_avg, analytical_skills_avg)
                    context = { 'score_sheets': score_sheets,
                                'suggested_courses': suggested_courses,
                                'chart':json.dumps([programming_skills_avg, soft_skills_avg, analytical_skills_avg]),
                                      
                                }
                    html_template = loader.get_template( 'candidate/dashboard.html' )
                    return HttpResponse(html_template.render(context, request))
                
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })
