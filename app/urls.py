

from django.urls import path, re_path
from app import views
from django.urls.conf import include

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path('dashboard', views.view_dashboard, name="dashboard"),
    path('upload-scores', views.facultyScore, name='upload'),
    path('suggest-courses', views.facultySuggest, name='suggest'),
    path('team-formation', views.facultyTeam, name='team'),
    path('', include("scoresheet.urls")),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
