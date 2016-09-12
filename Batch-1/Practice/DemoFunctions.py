def myprint(value):
    "This prints a passed string"
    print("*******************")
    print(value)
    print("*******************")
    return


def square(number):
    "This return square of number"
    return number * number


def isPrime(number):
    "This returns T if number is prime else False"
    index = 2
    prime = True
    while index < (number // 2):
        if number % index == 0:
            prime = False
            break

        index += 1

    return prime


myprint("Hello How are you")
myprint(square(4))
number = 600851475143
# largest prime factor
index = number // 2

while index > 0:
    # Check whether the number is prime if its a factor
    if number % index == 0:
        if isPrime(index):
            print("largest prime factor is : ", index)
            break

    index -= 1
