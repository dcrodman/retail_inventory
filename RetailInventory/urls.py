from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from dashboard import views
from employees import urls as employee_urls
from stock import urls as stock_urls
from transactions import urls as transaction_urls
from store import urls as store_urls

import url_names

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/dashboard')),
    url(r'^dashboard/$', views.DashboardView.as_view(), 
        name=url_names.DASHBOARD),

    url(r'^stock/', include(stock_urls)),
    url(r'^employees/', include(employee_urls)),
    url(r'^transactions/', include(transaction_urls)),
    url(r'^store/', include(store_urls))
)
