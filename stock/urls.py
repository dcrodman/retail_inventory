from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

from stock import views

from RetailInventory.url_names import *

urlpatterns = patterns('',
  url(r'^$', redirect_to, {'url' : 'overview/'}),
  url(r'^overview/$', views.StockOverviewView.as_view(), name=STOCK_OVERVIEW),
  url(r'^product_search/$', views.ProductSearchView.as_view(), 
      name=PRODUCT_SEARCH)
)
