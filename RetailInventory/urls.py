from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from dashboard import views
import url_names

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/dashboard')),
    url(r'^dashboard/$', views.DashboardView.as_view(), 
        name=url_names.DASHBOARD)
)
