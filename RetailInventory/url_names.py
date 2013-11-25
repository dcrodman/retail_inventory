"""Module with constants for URL names used for page redirects for each
application view."""
from django.core.urlresolvers import reverse

DASHBOARD = 'dashboard'
# Stock Module URLS
STOCK_OVERVIEW = 'stock_overview'
PRODUCT_SEARCH = 'product_search'
CUSTOMER_SEARCH = 'customer_search'
SERVICE_PRODUCTS = 'service_products'
# Employee Module URLS
ADD_EMPLOYEE = 'add_employee'
EMPLOYEE_DETAILS = 'employee_details'
SEARCH_EMPLOYEE = 'search_employee'
# Transaction Module URLs
TRANSACTION_OVERVIEW = 'transaction_overview'
SALES_OVERVIEW = 'sales_overview'
RECEIPT_SEARCH = 'receipt_overview'


# Shortcut URLS for resolving reverse matches.

def dashboard_url():
  return reverse(DASHBOARD)

def stock_overview_url():
  return reverse(STOCK_OVERVIEW)

def product_search_url():
  return reverse(PRODUCT_SEARCH)

def service_products_url():
  return reverse(SERVICE_PRODUCTS)

def customer_search_url():
  return reverse(CUSTOMER_SEARCH)

def add_employee_url():
  return reverse(ADD_EMPLOYEE)

def employee_details_url():
  return reverse(EMPLOYEE_DETAILS)

def search_employee_url():
  return reverse(SEARCH_EMPLOYEE)

def transaction_overview_url():
  return reverse(TRANSACTION_OVERVIEW)

def sales_overview_url():
  return reverse(SALES_OVERVIEW)

def receipt_search_url():
  return reverse(RECEIPT_SEARCH)
