def avgMean(meanlist):
    if len(meanlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    mean = sum(meanlist) / len(meanlist)
    return mean

def avgmedian(medianlist):
    if len(medianlist) == 0:
        raise ValueError("Illegal empty list")
    pass
    medianlist.sort()
    if len(medianlist) % 2 == 1:
        middle = int(len(medianlist) / 2)
        median = medianlist[middle]
    else:
        middle1 = int(len(medianlist) / 2)
        middle2 = middle1 - 1
        median = (medianlist[middle1] + medianlist[middle2]) / 2
    return median


def avgvariance(variancelist):
    count = 0
    mean = sum(variancelist) / len(variancelist)

    for i in range(len(variancelist)):
        count += (mean - (variancelist[i]))**2
    variance = count / len(variancelist)
    return variance

