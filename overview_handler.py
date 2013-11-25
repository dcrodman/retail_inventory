from django.shortcuts import render
from django.views.generic.base import View

from db_helper import InventoryDBHelper
from search_handler import SearchView

class TableOverview(View):

  def getTableName(self):
    raise NotImplementedError('Table name not specified')

  def getPageTitle(self):
    raise NotImpelemtedError('Page title not specified')

  def get(self, request):
    table_name = self.getTableName()
    helper = InventoryDBHelper()
    fields = helper.getColumnsForTable(table_name)
    helper.execute('select * from %s' % (table_name))

    results = [result for result in helper]
    helper.close()

    context = {
      'title' : self.getPageTitle(),
      'fields' : fields,
      'results' : results
      }
    return render(request, 'search_results.html', context)