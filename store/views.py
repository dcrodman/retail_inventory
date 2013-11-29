from datetime import date, timedelta

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper
from RetailInventory import url_names

def storeHours():
  """Generates a list of times the store is open.

  Returns:
    List of these times as strings with the format "00:00 AM|PM".
  """
  times = []
  for i in range(8, 22):
    if i < 12:
      times.append('%d:00 AM' % i)
    elif i == 12:
      times.append('12:00 PM')
    else:
      times.append('%d:00 PM' % (i - 12))
  return times


class ManagerOverviewView(View):

  def get(self, request):
      helper = InventoryDBHelper()
      helper.execute('select employee_id, name, position, contact ' +
          'from employees where position = "manager"')
      results = [result for result in helper]
      fields = helper.getColumnsForTable('employees')
      fields.remove('manager')

      context = {
        'title' : 'Store Managers',
        'fields' : fields,
        'results' : results
        }
      return render(request, 'search_results.html', context)


class AddShiftView(View):

  def get(self, request):
    helper = InventoryDBHelper()
    helper.execute('select name from employees')
    employees = [employee[0] for employee in helper]

    today = date.today()
    dates = []
    dates.append(today.strftime('%m-%d'))
    # Option to schedule 2 weeks out.
    for i in range(1, 15):
      future_date = today + timedelta(i)
      dates.append(future_date.strftime('%m-%d'))

    success = True if 'success' in request.GET else False

    context = {
      'title' : 'Add Shift',
      'employees' : employees,
      'times' : storeHours(),
      'dates' : dates,
      'success' : success
    }
    return render(request, 'store/add_shift.html', context)

  def post(self, request):
    helper = InventoryDBHelper()

    fields = helper.getColumnsForTable('employee_shifts')
    fields.remove('employee_id')
    for field in request.POST:
      if field not in request.POST or len(request.POST[field]) < 1:
        return HttpResponse(400)

    helper.execute('select employee_id from employees where name = "%s"' %
        request.POST['employee'])
    employee_id = [employee[0] for employee in helper][0]

    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    shift_date = date.today().strftime('%Y') + '-' + request.POST['date']

    helper.execute('insert into employee_shifts values(%d, "%s", "%s", "%s")' %
        (employee_id, shift_date, start_time, end_time))
    helper.commit()
    helper.close()

    url = url_names.add_shift_url() + '?success=true'
    return HttpResponseRedirect(url)


class ScheduleView(View):

  def get(self, request):
    view_date = None
    if 'view_date' in request.GET:
      view_date = request.GET['view_date'].replace('"', '')
    else:
      view_date = date.today().strftime('%Y-%m-%d')

    helper = InventoryDBHelper()
    helper.execute('call get_schedule("%s")' % view_date)
    shifts = [shift for shift in helper]
    helper.close()

    other_dates = []
    today = date.today()
    for i in range(0, 15):
      future_date = today + timedelta(i)
      other_dates.append(future_date.strftime('%Y-%m-%d'))

    context = {
      'title' : 'View Schedule',
      'shifts' : shifts,
      'other_dates' : other_dates,
      'schedule_url' : url_names.view_schedule_url(),
      }
    return render(request, 'store/schedule.html', context)
