from django import forms
from django.forms import fields
from .models import *

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
	    category = self.cleaned_data.get('category')
	    if not category:
		    raise forms.ValidationError('This field is requifred')
	    return category


    def clean_item_name(self):
	    item_name = self.cleaned_data.get('item_name')
	    if not item_name:
		    raise forms.ValidationError('This field is required')
	    return item_name

class StockSearchForm(forms.ModelForm):
    #export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=True)
    end_date = forms.DateTimeField(required=True)
    class Meta:
        model = Stock
        fields = ['category', 'item_name','start_date','end_date']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']
