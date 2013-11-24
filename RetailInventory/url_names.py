"""Module with constants for URL names used for page redirects for each
application view."""
from django.core.urlresolvers import reverse

DASHBOARD = 'dashboard'
# Stock Module URLS
STOCK_OVERVIEW = 'stock_overview'
PRODUCT_SEARCH = 'product_search'
# Employee Module URLS
ADD_EMPLOYEE = 'add_employee'
EMPLOYEE_DETAILS = 'employee_details'
SEARCH_EMPLOYEE = 'search_employee'


# Shortcut URLS for resolving reverse matches.

def dashboard_url():
  return reverse(DASHBOARD)

def stock_overview_url():
  return reverse(STOCK_OVERVIEW)

def product_search_url():
  return reverse(PRODUCT_SEARCH)

def add_employee_url():
  return reverse(ADD_EMPLOYEE)

def employee_details_url():
  return reverse(EMPLOYEE_DETAILS)

def search_employee_url():
  return reverse(SEARCH_EMPLOYEE)