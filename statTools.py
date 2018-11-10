def avgMean(meanlist):
    if len(meanlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    mean = sum(meanlist) / len(meanlist)
    return mean

def median(medianlist):
    length = len(medianlist)
    middle = int(length / 2)
    median = medianlist[middle]
    return median