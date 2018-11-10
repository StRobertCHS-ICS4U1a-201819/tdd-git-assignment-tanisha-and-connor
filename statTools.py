def avgMean(mylist):
    if len(mylist) == 0:
        raise ValueError("Illegal empty list")
    pass
    mean = sum(mylist) / len(mylist)
    return mean