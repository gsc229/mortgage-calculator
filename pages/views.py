from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
import math
import re
import json
from pages.loanCalculator import calculateLoan
from pages.bulkCalculate import calculateLoans
from pages.models import Document
from pages.forms import UploadFileForm


# Create your views here.
def renderCalculator(request):
  context = {
    "values": request.GET
  }
  return render(request, 'pages/loan_calculator.html', context)


def calculate_loan(request):
  print("POST: " ,request.POST)
  amount = request.POST['amount']
  downpayment = request.POST['downpayment']
  yearly_rate = request.POST['interest']
  years = request.POST['term']

  if not amount:
    context = {
      "amount_error": "Please Specify the amount Loan Amount.",
      "values": request.POST
    }
    return render(request, 'pages/loan_calculator.html', context)
  
  if not downpayment:
    downpayment = 0
  
  if downpayment and float(downpayment) >= float(amount):
    context = {
      "downpayment_error": "Down payment must be smaller than prinicipal",
      "values": request.POST
    }
    return render(request, 'pages/loan_calculator.html', context)

  if not yearly_rate:
    context = {
      "interest_error": "Please Specify a Yearly Interest Rate.",
      "values": request.POST
    }
    return render(request, 'pages/loan_calculator.html', context)

  if not years:
    context = {
      "term_error": "Please specify the number of years",
      "values": request.POST
    }
    return render(request, 'pages/loan_calculator.html', context)


  print(f"P: {amount}, r: {yearly_rate}, t: {years}")

  result = calculateLoan(amount, downpayment, yearly_rate, years)

  if 'no_json' in request.POST:

    context = {
      "monthly_payment": result['monthly_payment'],
      "total_interest": result['total_interest'],
      "total_payment": result['total_payment'],
      "values": request.POST
    }

    return render(request, 'pages/loan_calculator.html', context)

  else:

    data = {
      "monthly payment": result['monthly_payment'],
      "total interest": result['total_interest'],
      "total payment": result['total_payment'],
    }

    return JsonResponse(data)

def bulk_calculate(request):

  print(request.POST)

  # Handle file upload
  if request.method == 'POST' and 'bulk_data' in request.FILES:

    file = request.FILES['bulk_data']
    f_lines_list_bytes = file.readlines()
    
    # Calcualte the loans:
    results = calculateLoans(f_lines_list_bytes)
    print(f"results: { results }")
    if 'send_json' in request.POST:
      for i, result in enumerate(results['data']):
        updated = {
          "monthly payment": result['monthly_payment'],
          "total interest": result['total_interest'],
          "total payment": result['total_payment'],
        }
        results['data'][i] = updated
      return JsonResponse(results)
    else:
      return render(request, 'pages/bulk_calculate.html', results)
      


  return render(request, 'pages/bulk_calculate.html')