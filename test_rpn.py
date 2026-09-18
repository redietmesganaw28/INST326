# Rediet Mesganaw 

import pytest 
from rpn import evaluate 

# edge cases 
def test_single_int():
    assert evaluate("3") == pytest.approx(3.0)

def test_single_float():
    assert evaluate("1.23") == pytest.approx(1.23)

def test_negative_num():
    assert evaluate ("-4") == pytest.approx(-4.0)
    
def test_two_digit():
    assert evaluate ("55") == pytest.approx(55.0)
  
# happy cases 
  
def test_addition():
    assert evaluate ("1 2 +") == pytest.approx(3.0)

def test_subtraction():
    assert evaluate ("11 5 -") == pytest.approx(6.0)
    
def test_multiplication():
    assert evaluate ("5 2 *") == pytest.approx(10.0)
    
def test_division():
    assert evaluate ("25 5 /") == pytest.approx(5.0)
    
def test_three_numbers_two_ops():
    assert evaluate ("5 4 3 + *") == pytest.approx(35.0)
    
def test_two_numbers_middle_op():
    assert evaluate ("11 4 + 2 *") == pytest.approx(30.0)
    