from django.shortcuts import render
from django.views.generic.base import View

from RetailInventory.url_names import *

class DashboardView(View):
  """Class defining the main dashboard view."""
  
  def get(self, request):
    context = {
        'title' : 'Dashboard',
        'stock_overview' : stock_overview_url(),
        'product_search' : product_search_url(),
        'add_employee' : add_employee_url(),
        'employee_details' : employee_details_url(),
        'search_employees' : search_employee_url()
      }
    return render(request, 'dashboard.html', context)