from django.test import TestCase
from pages.loanCalculator import add, calculateLoan

# Create your tests here.
class TestCalc(TestCase):
  
  def test_percent(self):
    assert 2 == 2