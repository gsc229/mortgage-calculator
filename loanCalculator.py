import math

# principal = input("How much is the loan?")
# downpayment = input("What is the downpayment?")
# yearly_rate = input("What is the interest rate?")
# years = input("How many years is the loan?")

principal = 100000
downpayment = 20000
yearly_rate = "5.5%"
years = 30

print(f"P: {principal}, r: {yearly_rate}, t: {years}")

principal = float(principal) - float(downpayment)
yearly_rate = (float(yearly_rate[:-1]) / 100)
years = int(years)
n_months = years * 12
montly_inerest = yearly_rate / 12

print(f"P: {principal}, t: {years}, n_months: { n_months }, r: {yearly_rate}, montly_inerest: { montly_inerest }")

monthly_payment = principal * (montly_inerest * (1 + montly_inerest) ** n_months) / ((1 + montly_inerest) ** n_months - 1)
total_payment = monthly_payment * n_months
total_interest = total_payment - principal

monthly_payment = round(monthly_payment, 2)
total_payment = round(total_payment, 2)
total_interest = round(total_interest, 2)

print(f"monthly payment: { monthly_payment }, total interest: { total_interest }, total payment { total_payment } ")


