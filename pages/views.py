from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import math
import re
import json
from pages.loanCalculator import calculateLoan

# Create your views here.
def renderCalculator(request):
  context = {
    "values": request.GET
  }
  return render(request, 'pages/loan_calculator.html', context)


def calculate_loan(request):
  print(f"request: { request.GET }")
  amount = request.GET['amount']
  downpayment = request.GET['downpayment']
  yearly_rate = request.GET['interest']
  years = request.GET['term']

  if not amount:
    context = {
      "amount_error": "Please Specify the amount Loan Amount.",
      "values": request.GET
    }
    return render(request, 'pages/loan_calculator.html', context)
  
  if not downpayment:
    downpayment = 0
  
  if downpayment and float(downpayment) >= float(amount):
    context = {
      "downpayment_error": "Down payment must be smaller than prinicipal",
      "values": request.GET
    }
    return render(request, 'pages/loan_calculator.html', context)

  if not yearly_rate:
    context = {
      "interest_error": "Please Specify a Yearly Interest Rate.",
      "values": request.GET
    }
    return render(request, 'pages/loan_calculator.html', context)

  if not years:
    context = {
      "term_error": "Please specify the number of years",
      "values": request.GET
    }
    return render(request, 'pages/loan_calculator.html', context)


  print(f"P: {amount}, r: {yearly_rate}, t: {years}")

  result = calculateLoan(amount, downpayment, yearly_rate, years)

  if 'no_json' in request.GET:

    context = {
      "monthly_payment": result['monthly_payment'],
      "total_interest": result['total_interest'],
      "total_payment": result['total_payment'],
      "values": request.GET
    }

    print(f"context: { context } ")

    return render(request, 'pages/loan_calculator.html', context)

  else:

    data = {
      "monthly payment": result['monthly_payment'],
      "total interest": result['total_interest'],
      "total payment": result['total_payment'],
    }

    return JsonResponse(data)