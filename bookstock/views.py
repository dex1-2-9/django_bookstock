from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	title = 'Welcome to VERY basic Book Management System'
	context = {
	"title": title,
	}
	return render(request, "home.html", context)

@login_required
def list_item(request):
	title = 'Books Management'
	form = StockSearchForm(request.POST or None)
	queryset = Stock.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
		"form": form
	}
	if request.method == 'POST':
		queryset = Stock.objects.filter(category__icontains=form['category'].value(),
										item_name__icontains=form['item_name'].value(),
										last_updated__range=[
											form['start_date'].value(),
											form['end_date'].value()
										])

	context = {
		"form": form,
		"title": title,
		"queryset": queryset,
}

	return render(request, "list_item.html", context)

@login_required
def add_items(request):
	form = StockCreateForm(request.POST or None)
	title="Register Book"
	if form.is_valid():
		form.save()
		messages.success(request, 'Book registered!')
		return redirect('/list_item')	
	context = {
		"form": form,
		"title": title,
	}
	return render(request, "add_items.html", context)

@login_required
def update_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	form = StockUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = StockUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully updated book named' + ' ' + str(queryset).upper())
			return redirect('/list_item')

	context = {
		'form':form
	}
	return render(request, 'add_items.html', context)

@login_required
def delete_items(request, pk):
	queryset = Stock.objects.get(id=pk)
	#queryset_show = Stock.objects.all()
	if request.method == 'POST':
		messages.success(request, 'Successfully deleted book named' + ' ' + str(queryset).upper())
		queryset.delete()
		return redirect('/list_item')
	return render(request, 'delete_items.html')