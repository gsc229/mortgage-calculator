from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loan-calculator', views.loan_calculator, name='loan_calculator')
]

