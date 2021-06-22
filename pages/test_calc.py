import os
from django.test import TestCase
from pages.loanCalculator import calculateLoan
from pages.bulkCalculate import calculateLoans
from django.urls import reverse, resolve
from pages.views import calculate_loan

# Create your tests here.
class TestCalc(TestCase):
  
  def test_loan_calculator_takes_strings(self):

    amount = "100000"
    downpayment = "20000"
    interest = "5.5"
    term = "30"

    result = calculateLoan(amount, downpayment, interest, term)
    
    self.assertEqual(result['monthly_payment'], 454.23)
    self.assertEqual(result['total_payment'], 163523.23)
    self.assertEqual(result['total_interest'], 83523.23)

  def test_loan_calculator_takes_integers(self):

    amount = 100000
    downpayment = 20000
    interest = 5
    term = 30

    result = calculateLoan(amount, downpayment, interest, term)
    
    self.assertEqual(result['monthly_payment'], 429.46)
    self.assertEqual(result['total_payment'], 154604.63)
    self.assertEqual(result['total_interest'], 74604.63)

  def test_loan_calculator_takes_floats(self):

    amount = 100000.00
    downpayment = 20000.00
    interest = 5.000000
    term = 30.0000

    result = calculateLoan(amount, downpayment, interest, term)
    
    self.assertEqual(result['monthly_payment'], 429.46)
    self.assertEqual(result['total_payment'], 154604.63)
    self.assertEqual(result['total_interest'], 74604.63)

  def test_loan_calclualtor_returns_correct_data_shape(self):
    amount = "100000"
    downpayment = "20000"
    interest = "5.5"
    term = "30"

    result = calculateLoan(amount, downpayment, interest, term)

    self.assertEqual('monthly_payment' in result, True)
    self.assertEqual('total_payment' in result, True)
    self.assertEqual('total_interest' in result, True)

  def test_loan_calculator_removes_dollar_sign_from_amount_and_downpayment(self):
    amount = "$100000.00"
    downpayment = "$20000.00"
    interest = "5.5"
    term = "30"

    result = calculateLoan(amount, downpayment, interest, term)
    
    self.assertEqual(result['monthly_payment'], 454.23)
    self.assertEqual(result['total_payment'], 163523.23)
    self.assertEqual(result['total_interest'], 83523.23)


  def test_bulk_calculator_chages_bytes_to_strings(self):

    result = {}

    with open('loanData.txt', 'r') as f:
      f_contents = f.readlines()
      f_contents = [bytes(string, 'utf-8') for string in f_contents] # data will be sent as bytes through the file upload
      result = calculateLoans(f_contents)
      
    self.assertTrue("data" in result)
    self.assertTrue("rejected" in result)
    self.assertEqual(len(result["data"]), 5)
    self.assertEqual(len(result['rejected']), 1)

  def test_bulk_calculator_case_insensitive(self):
    result = {}

    with open('loanData.txt', 'r') as f:
      f_contents = f.readlines()
      # turns the lines to upper case and then to bytes
      f_contents = [bytes(string.upper(), 'utf-8') for string in f_contents] # data will be sent as bytes through the file upload
      
      print(f_contents)
      result = calculateLoans(f_contents)
      print(result)
    self.assertTrue("data" in result)
    self.assertTrue("rejected" in result)
    self.assertEqual(len(result["data"]), 5)
    self.assertEqual(len(result['rejected']), 1)



  def test_calculate_loan_url(self):

    reverseUrl = reverse("calculate_loan")

    self.assertEqual(resolve(reverseUrl).func, calculate_loan)
    self.assertEqual(reverseUrl, "/calculate")