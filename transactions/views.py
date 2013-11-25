from django.shortcuts import render
from django.views.generic.base import View

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