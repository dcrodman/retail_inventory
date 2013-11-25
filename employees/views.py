from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from RetailInventory import url_names
from db_helper import InventoryDBHelper

class AddEmployeeView(View):
  """View responsible for allowing administrators to add new employees."""
  
  def get(self, request):
    employee_positions = ['Specialist', 'Mentor', 'Genius','Manager']
    
    helper = InventoryDBHelper()
    idx = helper.getIndexOfColumnForTable(column='name', table='employees')

    helper.execute('select * from employees where position = "manager"')
    managers = [mgr[idx] for mgr in helper]
    helper.close()
    
    success = True if 'success' in request.GET else False
    missing_name = True if 'form_error' in request.GET else False

    context = {
        'title' : 'Add Employee',
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
    name = helper.escape_string(request.POST['name'])
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


class EmployeeDetailsView(View):
  """View responsible for displaying employee details."""
  
  def get(self, request):
    helper = InventoryDBHelper()
    headers = helper.getColumnsForTable('employeedetails')
    helper.execute('select * from employeedetails')
    employees = [employee for employee in helper]
    helper.close()

    context = {
        'title' : 'Employee Details',
        'headers' : headers,
        'employees' : employees,
        }
    return render(request, 'employees/employee_details.html', context)


class SearchEmployeeView(View):
  """View responsible for allowing a user to search for an employee by 
  some detail (field name).
  """
  
  def get(self, request):
    context = {
        'title' : 'Search Employees'
        }
    return render(request, 'employees/employee_search.html', context)