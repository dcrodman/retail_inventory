from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper
from RetailInventory import url_names

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

class ProductSearchView(View):
  """Class to allow an employee to search for a particular product. In order to
  save time (be lazy) and avoid using Ajax requests with JS, POSTs will
  redirect to this same page with column arguments in the GET args that will
  cause the form to be rendered with results instead of a form."""

  def get(self, request):
    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable('products')

    query_params = {}
    for field in fields:
      if field in request.GET:
        query_params[field] = request.GET[field]
    helper.close()

    context = {
        'title' : 'Product Search',
        'fields' : fields,
        }
    return render(request, 'stock/product_search.html', context)

  def post(self, request):
    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable('products')

    query_params = {}
    for field in fields:
      if field in request.POST and len(request.POST[field]) > 0:
        query_params[field] = request.POST[field]

    if len(query_params) > 0:
      query_str = 'select * from products where '
      for field in query_params:
        # Remove quotes to prevent them from breaking queries. No column names
        # in products should include quotes, but this should be done with
        # regex anchors at some point to avoid making that assumption.
        field_name = field.replace('"', '')
        field_value = query_params[field].replace('"', '')
        query_str += '%s = "%s" and ' % (field_name, field_value)

      # Use string slicing to remove the final "and" plus its extra space.
      helper.execute(query_str[:-5])
      results = [result for result in helper]
      helper.close()

      context = {
        'title' : 'Search Results',
        'fields' : fields,
        'results' : results
        }
      return render(request, 'stock/search_results.html', context)
    else:
      # No query specified; bounce them back to GET.
      return HttpResponseRedirect(url_names.product_search_url())
