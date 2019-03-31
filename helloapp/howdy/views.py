from django.views.generic import TemplateView,ListView
from django.template import loader
from django.views import generic
from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse_lazy

from .models import Person


class IndexView(generic.ListView):
	template_name ='howdy/index.html'
	context_object_name ='all_name'
	
	def get_queryset(self):
		return Person.objects.all()
 


