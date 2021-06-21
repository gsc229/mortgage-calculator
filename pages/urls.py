from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderCalculator, name='loan_calculator'),
    path('calculate', views.calculate_loan, name='calculate_loan')
]

