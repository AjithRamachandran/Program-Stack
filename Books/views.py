from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import book
from django.template import loader
from django.http import HttpResponse

class IndexView(ListView):
	model = book
	template_name = 'books/index.html'
	context_object_name = 'book_list'
	paginate_by = 12

	def get_queryset(self):
		return book.objects.all()

class BookSearchView(ListView):
	template_name = 'books/index.html'
	model = book
	context_object_name = 'book_list'

	def get_queryset(self):
		name = self.request.GET.get('q')
		if name != None:
			object_list = book.objects.filter(name__icontains=name)
		else:
			object_list = book.objects.filter(name__icontains=name)
		return object_list

class DetailView(DetailView):
	model = book
	template_name = 'books/details.html'

def donatePage(request):
	return render(request,'books/donate.html')