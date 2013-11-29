from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper
from RetailInventory import url_names
from overview_handler import TableOverview
from search_handler import SearchView

class TransactionOverviewView(TableOverview):

  def getPageTitle(self):
    return 'Transaction Overview'

  def getTableName(self):
    return 'receipts'

class SalesOverviewView(TableOverview):

  def getPageTitle(self):
    return 'Employee Sales Overview'

  def getTableName(self):
    return 'employeesales'


class ReceiptSearchView(SearchView):

  def getViewURL(self):
      return url_names.receipt_search_url()

  def getTableName(self):
    return 'receipts'

  def getPageTitle(self):
    return 'Search Receipts'


class POSView(View):

  def get(self, request):
    helper = InventoryDBHelper()

    # Only allow users to ring out items available for sale.
    helper.execute('select name from products where bucket = "sellable"')
    products = [product[0] for product in helper]

    helper.execute('select name from employees')
    employees = [employee[0] for employee in helper]

    helper.execute('select name from customers')
    customers = [customer[0] for customer in helper]
    helper.close()

    error = None
    if 'error' in request.GET:
      error = request.GET['error']
    success = True if 'success' in request.GET else False

    context = {
      'title' : 'Point of Sale',
      'customers' : customers,
      'products' : products,
      'employees' : employees,
      'success' : success,
      'error' : error
      }
    return render(request, 'transactions/pos.html', context)

  def post(self, request):
    total = 0.0
    error_url = url_names.pos_view_url() + "?error=%s"
    try:
      total = float(request.POST['total'])
    except:
      return HttpResponseRedirect(
          error_url % "Please enter valid decimal total.")

    helper = InventoryDBHelper()
    # Serial numbers wouldn't be selected by the customer, so we're just
    # going to choose the first product they want and use that serial.
    pdct = helper.escape_string(request.POST['product'].replace('"', ''))
    helper.execute(
        'select model, serial_number from products ' +
        'where name = "%s" limit 0, 1' % pdct
      )
    product = [product for product in helper][0]

    cstr = helper.escape_string(request.POST['customer'].replace('"', ''))
    helper.execute(
        'select customer_id from customers where name = "%s"' % cstr)
    customer = [int(customer[0]) for customer in helper]

    empl = helper.escape_string(request.POST['employee'].replace('"', ''))
    helper.execute(
        'select employee_id from employees where name = "%s"' % empl)
    employee = [int(employee[0]) for employee in helper]

    helper.execute('call transact_product("%s", "%s", %d, %d, %f, 1)' %
        (product[0], product[1], customer[0], employee[0], total))
    helper.commit()
    helper.close()

    return HttpResponseRedirect(url_names.pos_view_url() + '?success=true')
