import MySQLdb

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from RetailInventory import url_names
from db_helper import InventoryDBHelper
from overview_handler import TableOverview
from search_handler import SearchView
from pydoc import Helper

class AddEmployeeView(View):
  """View responsible for allowing administrators to add new employees."""
  
  def get(self, request):
    employee_positions = ['Specialist', 'Mentor', 'Genius','Manager']
    
    helper = InventoryDBHelper()
    idx = helper.getIndexOfColumnForTable(column='name', table='employees')

    helper.execute('select * from employees where position = "manager"')
    managers = [mgr[idx] for mgr in helper]

    helper.execute('select address from contacts')
    contacts = [contact[0] for contact in helper]
    helper.close()
    
    success = True if 'success' in request.GET else False
    missing_name = True if 'form_error' in request.GET else False

    context = {
        'title' : 'Add Employee',
        'contacts' : contacts,
        'positions' : employee_positions,
        'managers' : managers,
        'success' : success,
        'missing_name' : missing_name
        }
    return render(request, 'employees/add_employee.html', context)
  
  def post(self, request):
    helper = InventoryDBHelper()
    
    if 'name' not in request.POST or len(request.POST['name']) < 1:
      url = url_names.add_employee_url() + '?form_error=true'
      return HttpResponseRedirect(url)
    name = helper.escape_string(request.POST['name']).replace('"', '')
    position = helper.escape_string(request.POST['position'])
    manager = helper.escape_string(request.POST['manager'])
    
    # Naive assumption that the passed string corresponds to a manager. Just a
    # shortcut for now, this should be done by id.
    helper.execute(
        'select employee_id from employees where name = "%s"' % manager)
    manager_id = helper.first()[0]
    if not manager_id:
      return HttpResponse(status=412)

    helper.execute('insert into employees (name, position, manager) ' +
        'values ("%s", "%s", %d);' % (name, position, manager_id))
    helper.commit()
    helper.close()

    url = url_names.add_employee_url() + '?success=true'
    return HttpResponseRedirect(url)


class EmployeeDetailsView(TableOverview):
  """View responsible for displaying employee details."""
  
  def getPageTitle(self):
    return 'Employee Overview'

  def getTableName(self):
    return 'employeedetails'


class SearchEmployeeView(SearchView):
  """View responsible for allowing a user to search for an employee by 
  some detail (field name).
  """
  
  def getViewURL(self):
    return url_names.search_employee_url()

  def getTableName(self):
    return 'employees'

  def getPageTitle(self):
    return "Search Employees"

class AddContactView(View):

  def get(self, request):
    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable('contacts')
    helper.close()

    success = missing = db_error = None
    if 'success' in request.GET:
      success = request.GET['success']
    if 'missing' in request.GET:
      missing = request.GET['missing']
    if 'db_error' in request.GET:
      db_error = request.GET['db_error']

    context = {
      'title' : 'Add Contact',
      'fields' : fields,
      'success' : success,
      'missing' : missing,
      'db_error' : db_error
      }
    return render(request, 'employees/add_contact.html', context)

  def post(self, request):
    url = url_names.add_contact_url()

    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable('contacts')
    safer_fields = {}
    for field in fields:
      if field not in request.POST or request.POST[field] == '':
        url = url + '?missing=' + field
        return HttpResponseRedirect(url)
      else:
        # Simple method of preventing unexpected behavior if the user decides
        # to add quotes onto each of the fields.
        safer_fields[field] = request.POST[field].replace('"', '')
        safer_fields[field] = helper.escape_string(safer_fields[field])

    try:
      helper.execute(
          'insert into contacts values("%s", "%s", "%s", "%s", "%s")' % (
          safer_fields['address'],
          safer_fields['email'],
          safer_fields['phone'],
          safer_fields['city'],
          safer_fields['state'])
          )
    except MySQLdb.MySQLError as e:
      # Terrible way to pass a DB error, but for the sake of laziness/project
      # simplicity it's going to stay like this for now.
      url = url + '?db_error=%s' % e
      return HttpResponseRedirect(url)
    helper.close()

    url = url + '?success=true'
    return HttpResponseRedirect(url)
