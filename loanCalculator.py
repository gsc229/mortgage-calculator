import math
import re

principal = input("What is the loan amount?")
downpayment = input("What is the downpayment?")
yearly_rate = input("What is the interest rate?\n (%, i.e. 5.5% or 5.5 = .055, .5% or .5 = .0055)").strip("%")
years = input("How many years is the loan?")


# principal = 100000
# downpayment = 20000
# yearly_rate = ("5.5%").strip("%")
# years = 30

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