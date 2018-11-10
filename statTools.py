def avgMean(meanlist):
    if len(meanlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    mean = sum(meanlist) / len(meanlist)
    return mean

def median(medianlist):
    if len(medianlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    medianlist.sort()
    middle = int(len(medianlist) / 2)
    median = medianlist[middle]
    return median