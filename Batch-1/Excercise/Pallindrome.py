print('Enter any number')
number = 9999
while number >= 1000:
    reverseNumber = 0
    tempAssignment = number
    while tempAssignment != 0:
        lastDigit = tempAssignment % 10
        reverseNumber = reverseNumber * 10 + lastDigit
        tempAssignment //= 10

    if reverseNumber == number:
        print(number)

    number -= 1
    # print(str(number) + " is palindrome")
