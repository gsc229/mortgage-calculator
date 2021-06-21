from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate', views.calculate_loan, name='calculate_loan'),
    path('loan-calculator', views.loan_calculator, name='loan_calculator')
]

