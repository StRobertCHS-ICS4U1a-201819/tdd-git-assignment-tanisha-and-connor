import pytest
from statTools import *



def test_mean_basic1():
    assert(avgMean([30, 10, 20, 40, 50]) == 30)
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
    assert(avgmedian([1, 2, 3, 4, 10]) == 3)
def test_median_basic2():
    assert(avgmedian([2, 4, 5, 10, 20]) == 5)
def test_median_unsorted():
    assert(avgmedian([100, 4, 21, 75, 34]) == 34)
def test_median_empty():
    with pytest.raises(ValueError) as errmsg:
        avgmedian([])
    assert ("Illegal empty list" == str(errmsg.value))
def test_median_evenlist():
    assert(avgmedian([500, 5, 65, 70, 100, 200]) == 85)
def test_mean_corner():
    assert(avgmedian([0]) == 0)
def test_median_negative():
    assert(avgmedian([-5, -30, -1, 0]) == -3)
def test_median_one():
    assert(avgmedian([4]) == 4)
def test_median_decimal():
    assert(avgmedian([-5, 3, 4, 10]) == 3.5)


def test_variance_basic1():
    assert(avgvariance([45, 20, 15, 75, 100]) == 1054)
def test_variance_basic2():
   assert(avgvariance([0, 20, 40, 20]) == 200)
def test_varinace_empty():
    with pytest.raises(ValueError) as errmsg:
        avgvariance([])
    assert("Illegal empty list" == str(errmsg.value))
def test_variance_corner():
    assert(avgvariance([0]) == 0)
def test_variance_one():
    assert(avgvariance([100000]) == 0)
def test_variance_negative():
    with pytest.raises(ValueError) as errmsg:
        avgvariance([-50, -100, 20])
    assert("Illegal negative mean" == str(errmsg.value))
def test_variance_negative2():
    assert(avgvariance([-2, 4, 8, 10]) == 21)
def test_variance_decimal():
    assert(avgvariance([3, 4]) == 0.25)
def test_variance_repeating():
    assert(avgvariance([20, 20, 20, 20, 20, 20, 20]) == 0)


def test_standarddev_basic1():
    assert (deviation([45, 20, 15, 75, 100]) == 32.46536616149585)
def test_standarddev_basic2():
    assert (deviation([0, 20, 40, 20]) == 14.142135623730951)

