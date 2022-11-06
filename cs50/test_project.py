import pytest
from project import calculate_margin, calculate_expected,calculate_chisquare
def test_calculate_margin():
    data = {
        'Male Swimmer':23,
        'Male Nonswimmer':15,
        'Female Swimmer':30,
        'Female Nonswimmer':10,
    }

    levels = {
        'Gender':['Male','Female'],
        'Swimming':['Swimmer','Nonswimmer']
    }


    assert calculate_margin(data,levels) == {
        'Female':40,
        'Male':38,
        'Swimmer':53,
        'Nonswimmer':25
    }
def test_calculate_chisquare():

    observed = {
        'Male Swimmer': 23,
        'Male Nonswimmer': 15,
        'Female Swimmer': 30,
        'Female Nonswimmer': 10,
    }
    expected = {
        'Male Swimmer': 25.8205128,
        'Male Nonswimmer': 12.1794872,
        'Female Swimmer': 27.1794872,
        'Female Nonswimmer': 12.8205128,
    }

    assert calculate_chisquare(observed,expected) ==('1.8745','Not significant')

def test_calculate_expected():
    data = {
        'Male Swimmer': 23,
        'Male Nonswimmer': 15,
        'Female Swimmer': 30,
        'Female Nonswimmer': 10,
    }

    margin = {
        'Female':40,
        'Male':38,
        'Swimmer':53,
        'Nonswimmer':25
    }

    assert calculate_expected(data,margin) == {
        'Male Swimmer': margin['Male']*margin['Swimmer']/78,
        'Male Nonswimmer': margin['Male']*margin['Nonswimmer']/78,
        'Female Swimmer': margin['Female']*margin['Swimmer']/78,
        'Female Nonswimmer': margin['Female']*margin['Nonswimmer']/78,
    }



