import math
import re
import json

def calculateLoan(principal, downpayment, yearly_rate, years):
  """ Returns the monthly payment, total payment, and total interest given principal, downpayment, yearly interest rate and number of years  """
  
  if type(principal) == str:
    principal = re.findall(r"[-+]?\d*\.\d+|\d+", principal)[0]

  if type(downpayment) == str:
    downpayment = re.findall(r"[-+]?\d*\.\d+|\d+", downpayment)[0]

  if type(yearly_rate) == str:
    yearly_rate = re.findall(r"[-+]?\d*\.\d+|\d+", yearly_rate)[0]

  principal = float(principal) - float(downpayment)
  yearly_rate =  (float(yearly_rate) / 100)
  years = float(years)
  n_months = years * 12
  monthly_interest = yearly_rate / 12

  monthly_payment = principal * (monthly_interest * (1 + monthly_interest) ** n_months) / ((1 + monthly_interest) ** n_months - 1)
  total_payment = monthly_payment * n_months
  total_interest = total_payment - principal

  result = {
    "monthly_payment": round(monthly_payment, 2),
    "total_interest": round(total_interest, 2),
    "total_payment": round(total_payment, 2) 
  }

  return result

def amortizationSchedule(principal, downpayment, yearly_rate, years):
  if type(principal) == str:
    principal = re.findall(r"[-+]?\d*\.\d+|\d+", principal)[0]

  if type(downpayment) == str:
    downpayment = re.findall(r"[-+]?\d*\.\d+|\d+", downpayment)[0]

  if type(yearly_rate) == str:
    yearly_rate = re.findall(r"[-+]?\d*\.\d+|\d+", yearly_rate)[0]

  principal = float(principal) - float(downpayment)
  yearly_rate =  (float(yearly_rate) / 100)
  years = float(years)
  n_months = years * 12
  monthly_interest = yearly_rate / 12

  monthly_payment = principal * (monthly_interest * (1 + monthly_interest) ** n_months) / ((1 + monthly_interest) ** n_months - 1)


  schedule = []

  while True:

    interest_payment = (principal * yearly_rate) / 12
    principal_payment = monthly_payment - interest_payment
    principal = principal - principal_payment

    if principal < 0: break

    result = {
      "interest_payment": round(interest_payment, 2),
      "principal_payment": round(principal_payment, 2),
      "balance": round(principal, 2)
    }

    schedule.append(result)
  print(schedule)
  return schedule