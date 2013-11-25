from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper

class SearchView(View):
  """Generic class designed to simplify implementing Views that allow users
  to perform field-level searches on a table for tuples with specific values.
  """

  def getViewURL(self):
    """Returns a fully qualified URL for this View."""
    raise NotImplementedError('No GET url specified')

  def getPageTitle(self):
    """Returns the title for the page."""
    raise NotImplementedError('Page title is not defined')

  def getTableName(self):
    """Returns the name of the SQL table on which to query."""
    raise NotImplementedError('Table name is not defined')

  def get(self, request):
    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable(self.getTableName())

    query_params = {}
    for field in fields:
      if field in request.GET:
        query_params[field] = request.GET[field]
    helper.close()

    context = {
        'title' : self.getPageTitle(),
        'fields' : fields,
        }
    return render(request, 'table_search.html', context)

  def post(self, request):
    table_name = self.getTableName()
    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable(table_name)

    query_params = {}
    for field in fields:
      if field in request.POST and len(request.POST[field]) > 0:
        query_params[field] = request.POST[field]

    if len(query_params) > 0:
      query_str = 'select * from %s where ' % (table_name)
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
        'title' : '%s Results' % self.getPageTitle(),
        'fields' : fields,
        'results' : results
        }
      return render(request, 'search_results.html', context)
    else:
      # No query specified; bounce them back to GET.
      return HttpResponseRedirect(self.getViewURL())