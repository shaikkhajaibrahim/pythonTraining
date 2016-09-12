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


list1 = [1, 2, 3]
print("list before change", list1)
change(list1)
print("list after change", list1)

print(intrest(10000, 1, 6))

print(intrest(rate=6, principle=100000, time=2))

print(intrest(10000, 1))

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print(add())

mul = lambda arg1, arg2: arg1 * arg2

print(mul(10, 2))

printMul = lambda arg: print(arg)

printMul(mul(10, 2))
