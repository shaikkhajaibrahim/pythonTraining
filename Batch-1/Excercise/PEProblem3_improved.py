number = 600851475143
# largest prime factor
index = number // 2

while index > 0:
    # Check whether the number is prime if its a factor
    if number % index == 0:
        primeIndex = 2
        isPrime = True
        while primeIndex < index // 2:
            if index % primeIndex == 0:
                isPrime = False
                break

            primeIndex += 1

        if isPrime:
            print("largest prime factor is : ", index)
            break

    index -= 1
