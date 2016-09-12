def change(mylist):
    mylist[1] = 100
    return


def intrest(principle, time, rate=3):
    "This method will be used to calculate simple intrest"
    intrestAmount = float(principle) * float(time) * float(rate) / 100.0
    return intrestAmount


def add(*vartuple):
    sum = 0
    for var in vartuple:
        sum += int(var)

    return sum