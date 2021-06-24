from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderCalculator, name='loan_calculator'),
    path('calculate', views.calculate_loan, name='calculate_loan'),
    path('bulk-calculate', views.bulk_calculate, name='bulk_calculate'),
    path('amortization-schedule', views.amortization_schedule, name='amortization')
]

