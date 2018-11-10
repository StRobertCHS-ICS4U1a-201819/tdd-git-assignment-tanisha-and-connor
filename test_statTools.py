import pytest
from statTools import *

def test_mean_basic1():
    assert(avgMean([10, 20, 30, 40, 50]) == 30)
