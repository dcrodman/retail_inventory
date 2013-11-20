from django.shortcuts import render
from django.views.generic.base import View

class DashboardView(View):
  """Class defining the main dashboard view."""
  
  def get(self, request):
    return render(request, 'dashboard.html')
