from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper
from RetailInventory import url_names
from overview_handler import TableOverview
from search_handler import SearchView

class StockOverviewView(TableOverview):
  """Class to represent the stock overview page, which presents the option
  of viewing all stock in the store's inventory."""

  def getPageTitle(self):
    return 'Stock Overview'

  def getTableName(self):
    return 'products'


class ProductSearchView(SearchView):

  def getViewURL(self):
    return url_names.product_search_url()

  def getTableName(self):
    return 'products'

  def getPageTitle(self):
    return 'Product Search'


class CustomerSearchView(SearchView):

  def getViewURL(self):
    return url_names.customer_search_url()

  def getTableName(self):
    return 'customers'

  def getPageTitle(self):
    return 'Customer Search'


class ServiceProductsView(TableOverview):

  def getPageTitle(self):
    return 'Servie Products'

  def getTableName(self):
    return 'serviced_products'