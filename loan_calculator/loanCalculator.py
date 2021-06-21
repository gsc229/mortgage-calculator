import math
import re
import json

def calculateLoan(principal, downpayment, yearly_rate, years):
  principal = float(principal) - float(downpayment)
  yearly_rate =  (float(yearly_rate) / 100)
  years = int(years)
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


# while True:

#   principal = input("What is the loan amount?")
#   downpayment = input("What is the downpayment?")
#   yearly_rate = input("What is the interest rate?\n (%, i.e. 5.5% or 5.5 = .055, .5% or .5 = .0055)").strip("%")
#   years = input("How many years is the loan?")
#   blank = input()

#   result = calculateLoan(principal, downpayment, yearly_rate, years)

#   print(f"result: { result }\n")

