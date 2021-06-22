import re
from io import BytesIO
from pages.loanCalculator import calculateLoan



def findNumbers(line):
  # regex will find and extract all int or float numbers
  if re.findall(r"[-+]?\d*\.\d+|\d+", line):
    return round(float(re.findall(r"[-+]?\d*\.\d+|\d+", line)[0]), 2)

# context manager with open (best practice)
def calculateLoans(f_contents):
  calculationsList = []
  rejects = []
  varSet = {}
  f_contents = [line.decode("utf-8").strip() for line in f_contents]
  for line in f_contents:
    if len(line):
      if re.findall(r"amount", line):
        varSet["amount"] = findNumbers(line)
      if re.findall(r"interest", line):
        varSet["interest"] = findNumbers(line)
      if re.findall(r"downpayment", line):
        varSet["downpayment"] = findNumbers(line)
      if re.findall(r"term", line):
        varSet["term"] = findNumbers(line)
    else:
      if varSet["amount"] is None or varSet["interest"] is None or varSet["term"] is  None:
        rejects.append(varSet)
        varSet = {}
      else:
        calculationsList.append(varSet)
        varSet = {}
  

  calculations = [ calculateLoan(varSet["amount"], varSet["downpayment"], varSet["interest"], varSet["term"]) for varSet in calculationsList ]
  
  return {
    'data': calculations,
    'rejected': rejects
  }


