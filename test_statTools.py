import pytest
from statTools import *

def test_mean_basic1():
    assert(avgMean([10, 20, 30, 40, 50]) == 30)
def test_mean_basic2():
    assert(avgMean([5, 10, 15, 50]) == 20)
def test_mean_empty():
    with pytest.raises(ValueError) as errmsg:
        avgMean([])
    assert("Illegal empty list" == str(errmsg.value))
def test_mean_corner():
    assert (avgMean([0,1000]) == 500)
def test_mean_negative():
    assert(avgMean([-200, -100, 0, 5, 500]) == 41)
def test_mean_decmials():
    assert(avgMean([2.0, 9, 5.5, 2.1]) == 4.65)

def test_median_basic1():
    assert(median([1, 2, 3, 4, 10]) == 3)
def test_median_basic2():
    assert(median([2, 4, 5, 10, 20]) == 5)