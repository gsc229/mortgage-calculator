import math
import re
import json

def calculateLoan(principal, downpayment, yearly_rate, years):
  """ Returns the monthly payment, total payment, and total interest given principal, downpayment, yearly interest rate and number of years  """
  
  if type(principal) == str:
    principal = principal.strip("$")

  if type(downpayment) == str:
    downpayment = downpayment.strip("$")

  if type(yearly_rate) == str:
    yearly_rate.strip("%")

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