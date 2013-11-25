from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper
from RetailInventory import url_names
from search_handler import SearchView

class StockOverviewView(View):
  """Class to represent the stock overview page, which presents the option
  of viewing all stock in the store's inventory."""

  def get(self, request):
    helper = InventoryDBHelper()
    headers = helper.getColumnsForTable('products')

    helper.execute('select * from products')
    products = [product for product in helper]
    helper.close()

    context = {
        'title' : 'Stock Overview',
        'headers' : headers, 
        'products' : products
        }
    return render(request, 'stock/stock_overview.html', context)

class ProductSearchView(SearchView):

  def getViewURL(self):
    return url_names.product_search_url()

  def getTableName(self):
    return 'products'

  def getPageTitle(self):
    return 'Product Search'
