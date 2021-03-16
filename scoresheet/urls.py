# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import upload_data, fetch_data
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('upload-data/', upload_data, name="upload-file"),
    path('fetch-report/', fetch_data, name="fetch-report"),
    
]
