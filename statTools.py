"""
-----------------------------------------------------------
Name:		statTools.py
Purpose:
functions that calculate statistical data

Author:	Dong.C

Created: 11/11/2018
-----------------------------------------------------------
"""


def avgMean(meanlist):
    """
    function used to calculate mean given a list of integers

    :param meanlist: list of integers to calculate mean
    :return: the mean
    """
    # returns error if there is an empty list
    if len(meanlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    # calculates mean
    mean = sum(meanlist) / len(meanlist)
    return mean


def avgmedian(medianlist):
    """
    function used to calculate median given a list of integers

    :param medianlist: list of integers to calculate mode
    :return: the mode
    """
    # returns error for empty list
    if len(medianlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    # sorts list
    medianlist.sort()
    # calculates median for odd amount of numbers in list
    if len(medianlist) % 2 == 1:
        middle = int(len(medianlist) / 2)
        median = medianlist[middle]
    # calculates median for even amount of numbers in list
    else:
        middle1 = int(len(medianlist) / 2)
        middle2 = middle1 - 1
        median = (medianlist[middle1] + medianlist[middle2]) / 2
    return median


def avgvariance(variancelist):
    """
    function used to calculate variance given a list of integers

    :param variancelist: list of integers to calculate variance
    :return: the variance
    """
    count = 0
    # returns error for an empty list
    if len(variancelist) == 0:
        raise ValueError("Illegal empty list")
    pass
    # returns error if the mean is negative
    if avgMean(variancelist) < 0:
        raise ValueError("Illegal negative mean")
    pass
    # calculates variance
    for i in range(len(variancelist)):
        count += (avgMean(variancelist) - (variancelist[i])) ** 2
    variance = count / len(variancelist)
    return variance


def deviation(devlist):
    """
    function used to calculate standard deviation given a list of integers

    :param devlist: list of integers to calculate standard deviation
    :return: the standard deviation
    """
    standard_deviation = avgvariance(devlist) ** 0.5
    return standard_deviation
