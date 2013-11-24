from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to

from RetailInventory import url_names
import views

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url' : 'search/'}),
    url(r'^add/$', views.AddEmployeeView.as_view(), 
        name=url_names.ADD_EMPLOYEE),
    url(r'^details/$', views.EmployeeDetailsView.as_view(),  
        name=url_names.EMPLOYEE_DETAILS),
    url(r'^search/$', views.SearchEmployeeView.as_view(),
        name=url_names.SEARCH_EMPLOYEE),
)
