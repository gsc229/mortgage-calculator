import math

principal = input("How much is the loan?")
downpayment = input("What is the downpayment?")
rate = input("What is the interest rate?")
time = input("How many years is the loan?")

print(f"P: {principal}, r: {rate}, t: {time}")

principal = float(principal)
rate= (float(rate[:-1]) / 100)
time = int(time)

print(f"P: {principal}, r: {rate}, t: {time}")

A = principal *  math.pow((1 + rate) , time)

print(f"A:{A}")