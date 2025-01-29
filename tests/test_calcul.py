import pytest
from src.calcul import addition, soustraction

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0

def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(0, 0) == 0


def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0
