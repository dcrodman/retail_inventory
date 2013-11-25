from django.conf.urls.defaults import patterns, include, url
from django.views.generic import RedirectView

from transactions import views
from RetailInventory.url_names import *

urlpatterns = patterns('',
  url(r'^$', RedirectView.as_view(url='overview/')),
  url(r'^overview/$', views.TransactionOverviewView.as_view(),
      name=TRANSACTION_OVERVIEW),
    url(r'^sales_overview/$', views.SalesOverviewView.as_view(),
      name=SALES_OVERVIEW),
  url(r'^receipt_search/$', views.ReceiptSearchView.as_view(),
      name=RECEIPT_SEARCH),
)
