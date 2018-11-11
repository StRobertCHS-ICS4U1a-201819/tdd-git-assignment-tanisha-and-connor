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
    assert (avgMean([0]) == 0)
def test_mean_negative():
    assert(avgMean([-200, -100, 0, 5, 500]) == 41)
def test_mean_decmials():
    assert(avgMean([2.0, 9, 5.5, 2.1]) == 4.65)
def test_mean_one():
    assert(avgMean([5]) == 5)


def test_median_basic1():
    assert(median([1, 2, 3, 4, 10]) == 3)
def test_median_basic2():
    assert(median([2, 4, 5, 10, 20]) == 5)
def test_median_unsorted():
    assert(median([100, 4, 21, 75, 34]) == 34)
def test_median_empty():
    with pytest.raises(ValueError) as errmsg:
        median([])
    assert ("Illegal empty list" == str(errmsg.value))
def test_median_evenlist():
    assert(median([500, 5, 65, 70, 100, 200]) == 85)
def test_mean_corner():
    assert(median([0]) == 0)
def test_median_negative():
    assert(median([-5, -30, -1, 0]) == -3)
def test_median_one():
    assert(median([4]) == 4)