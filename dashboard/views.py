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
        'customer_search' : customer_search_url(),
        'service_product_overview' : service_products_url(),
        'add_employee' : add_employee_url(),
        'employee_details' : employee_details_url(),
        'search_employees' : search_employee_url(),
        'add_contact' : add_contact_url(),
        'transaction_overview' : transaction_overview_url(),
        'sales_overview' : sales_overview_url(),
        'receipt_search' : receipt_search_url(),
        'manager_overview' : manager_overview_url(),
        'add_shift' : add_shift_url()
      }
    return render(request, 'dashboard.html', context)
