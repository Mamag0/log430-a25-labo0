"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(1, 2) == 3
    assert my_calculator.addition(-1, 1) == 0
    assert my_calculator.addition(-1, -1) == -2

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(2,4) == 2
    assert my_calculator.subtraction(2,2) == 0
    assert my_calculator.subtraction(2,1) == 1

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2,4) == 8
    assert my_calculator.multiplication(2,0) == 0
    assert my_calculator.multiplication(2,-1) == -2

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(4,2) == 2
    assert my_calculator.division(4,0) == "Erreur : division par zéro"
    assert my_calculator.division(4,-2) == -2