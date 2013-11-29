from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from RetailInventory import url_names
from store import views

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='schedule/')),
    url(r'^managers/$', views.ManagerOverviewView.as_view(), 
        name=url_names.MANAGER_OVERVIEW),
    url(r'^add_shift/$', views.AddShiftView.as_view(),
        name=url_names.ADD_SHIFT),
    url(r'^schedule/$', views.ScheduleView.as_view(),
        name=url_names.VIEW_SCHEDULE)
)
