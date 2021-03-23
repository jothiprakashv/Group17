# -*- encoding: utf-8 -*-

import json

from django import template
from django.contrib.auth.decorators import login_required
from django.db.models.aggregates import Avg
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from scoresheet.models import ScoreSheet
from suggestedcourse.models import SuggestedCourse


def index(request):
    return redirect('/login/')


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def view_dashboard(request):
    context = {}
       
    try:
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
            html_template = loader.get_template('faculty/dashboard.html')
            return HttpResponse(html_template.render(context, request))
        else:
            score_sheets = ScoreSheet.objects.filter(candidate_id=request.user.last_name)
            suggested_courses = SuggestedCourse.objects.filter(candidate_id=request.user.last_name)
            programming_skills_avg = ScoreSheet.objects.filter(candidate_id = request.user.last_name, course_category='Programming\r\n').aggregate(Avg('mark'))['mark__avg']
            soft_skills_avg = ScoreSheet.objects.filter(candidate_id = request.user.last_name, course_category='Communication\r\n').aggregate(Avg('mark'))['mark__avg']
            analytical_skills_avg = ScoreSheet.objects.filter(candidate_id = request.user.last_name, course_category='Analytics\r\n').aggregate(Avg('mark'))['mark__avg']
            print(programming_skills_avg, soft_skills_avg, analytical_skills_avg)
            context = { 'score_sheets': score_sheets,
                        'suggested_courses': suggested_courses,
                        'chart':json.dumps([programming_skills_avg, soft_skills_avg, analytical_skills_avg]),
                        }
            html_template = loader.get_template('candidate/dashboard.html')
            return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    
@login_required(login_url="/login/")
def facultyDashboard(request):
    score_sheets = ScoreSheet.objects.all()
    suggested_courses = SuggestedCourse.objects.all()
    context = { 'score_sheets': score_sheets,
               'suggested_courses': suggested_courses
        }
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try: 
        
        html_template = loader.get_template('faculty/dashboard.html')
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def facultyScore(request):
    scores = ScoreSheet.objects.all()
    context = {
        'msg':'',
        'value': '',
        'scores': scores  }
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
              
        html_template = loader.get_template('faculty/faculty-upload-score.html')
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def facultySuggest(request):
    suggested_courses = SuggestedCourse.objects.all()
    context = {'value': '',
               'msg':'',
               'suggested_courses':suggested_courses}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
                
        html_template = loader.get_template('faculty/faculty-suggestion.html')
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

