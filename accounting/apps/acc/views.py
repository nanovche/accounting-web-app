from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *


def index(request):
    return render(request, 'acc/index.html')


def get_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data["product_name"]
            price = form.cleaned_data["price"]
            quantity = form.cleaned_data["quantity"]

            product = Product(name=name, price=price, quantity=quantity)
            product.save()

            return HttpResponseRedirect('')
    else:
        form = ProductForm()

    return render(request, 'acc/product-purchase.html', {'form': form})


def get_services(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():

            type_of_service = form.cleaned_data["type_of_service"]
            price = form.cleaned_data["price"]
            quantity = form.cleaned_data["quantity"]
            starting_date = form.cleaned_data["starting_date"]
            ending_date = form.cleaned_data["ending_date"]

            service = Service(type_of_service=type_of_service, price=price, quantity=quantity,
                              starting_date=starting_date, ending_date=ending_date)
            service.save()

            return HttpResponseRedirect('')
    else:
        form = ServiceForm()

    return render(request, 'acc/services.html', {'form': form})


def evaluate(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['product_name']
            product = Product.objects.get(name=name)
            total = product.price * product.quantity

            return render(request, 'acc/results.html', {'total': total})
    else:
        form = EvaluationForm()

    return render(request, 'acc/expenses-by-type.html', {'form': form})


def get_student(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'acc/results.html', context)


def get_contacts(request):
    context = { 'name': 'Мартин Нанов',
                'phone': '0879017037',
                'email':  'nanov_95@mail.bg',
                'city': 'Мездра',
                'address': 'Родопи 8'}
    return render(request, 'acc/contacts.html',  context)