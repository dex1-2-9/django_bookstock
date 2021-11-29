from django.contrib import admin
from .models import *
from .forms import StockCreateForm

# Register your models here.

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   # Creating form according to StockCreateForm .. in /forms.py
   form = StockCreateForm
   # Adding filter - category filter etc.
   list_filter = ['category'] 
   # Searching in admin panel
   search_fields = ['category', 'item_name']



admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Kategorie)