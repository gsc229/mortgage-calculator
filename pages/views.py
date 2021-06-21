from django.shortcuts import render
from django.http import HttpResponse
import math
import re

# Create your views here.
def index(request):
  return render(request, 'pages/index.html')

def loan_calculator(request):
  return render(request, 'pages/loan_calculator.html')


def calculate_loan(request):

  principal = request.principal
  downpayment = request.downpayment
  yearly_rate = request.yearly_rate.strip("%")
  years = request.years

  print(f"P: {principal}, r: {yearly_rate}, t: {years}")

  principal = float(principal) - float(downpayment)
  yearly_rate =  (float(yearly_rate) / 100)
  years = int(years)
  n_months = years * 12
  monthly_interest = yearly_rate / 12

  print(f"P: {principal}, t: {years}, n_months: { n_months }, r: {yearly_rate}, monthly_interest: { monthly_interest }")

  monthly_payment = principal * (monthly_interest * (1 + monthly_interest) ** n_months) / ((1 + monthly_interest) ** n_months - 1)
  total_payment = monthly_payment * n_months
  total_interest = total_payment - principal

  result = {
    "monthly payment": round(monthly_payment, 2),
    "total interest": round(total_interest, 2),
    "total payment": round(total_payment, 2) 
  }

  print(f"result: { result } ")

  return render(request, 'pages/loan_calculator.html', result)