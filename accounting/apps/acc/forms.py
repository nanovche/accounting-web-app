from django import forms

from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity']


class ServiceForm(forms.Form):
    type_of_service = forms.CharField(
        widget=forms.RadioSelect(choices=Service.SERVICE_CHOICES))
    price = forms.DecimalField(max_digits=8, decimal_places=5, widget=forms.NumberInput)
    quantity = forms.DecimalField(max_digits=10, decimal_places=5)
    starting_date = forms.DateField(widget=forms.SelectDateWidget)
    ending_date = forms.DateField(widget=forms.SelectDateWidget)


# class StudentForm(forms.Form):
#     year_in_school = forms.ChoiceField(label='years', widget=forms.RadioSelect)


class EvaluationForm(forms.Form):
    product_name = forms.CharField(label='Product', max_length=100)


