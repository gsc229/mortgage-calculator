from loanCalculator import getAmortizationSchedule, calculateLoan



keepcalculating=True

while keepcalculating:

  principal = input("What is the loan amount?")
  downpayment = input("What is the downpayment?")
  yearly_rate = input("What is the interest rate?\n (%, i.e. 5.5% or 5.5 = .055, .5% or .5 = .0055)").strip("%")
  years = input("How many years is the loan?")
  blank = input()

  result = calculateLoan(principal, downpayment, yearly_rate, years)

  print(f"result: { result }\n")

  getAmortizationSchedule(principal, downpayment, yearly_rate, years)

  willContinue = input("Make another calculation? (type: 'Yes' or hit Enter)")
  keepcalculating = willContinue == "Yes" or  willContinue == "Y" or willContinue == "yes" or willContinue == "y"