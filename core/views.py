from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City

class indexView(TemplateView):
	template_name = 'core/index.html'

class searchView(ListView):
	model = City
	context_object_name= 'cities'
	template_name = 'core/search_r.html'


	def get_queryset(self):
		query = self.request.GET.get('q')
		return City.objects.filter(name__icontains=query)
