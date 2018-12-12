"""
Definition of urls for servicelocal.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from app import views

# Uncomment the next lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^api/', views.LoadLogsAPIView.as_view()),
    url(r'^', include(admin.site.urls)),
]
