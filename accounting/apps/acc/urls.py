from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('product-purchase/', views.get_product, name='product-purchase'),
    path('expenses-by-type/', views.evaluate, name='expenses-by-type'),
    path('results/', views.evaluate, name='results'),
    path('services/', views.get_services, name='services'),
    path('contacts/', views.get_contacts, name='contacts'),
    # path('income/', views.get_services, name='income'),
    # path('expenses/', views.get_services, name='expenses'),
    # path('student/', views.get_student, name='student'),
]