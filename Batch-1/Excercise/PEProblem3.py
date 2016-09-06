import math

N = 21
maxPrimeVal = math.sqrt(N)
Primes = [2]
n = 1
# Create Recursive Primes List
while Primes[-1] < maxPrimeVal:
    n += 2
    cont = 0  # Counts How many primes were done
    for p in Primes:
        if p > math.sqrt(n):
            cont = len(Primes)
            break
        if n % p == 0:
            break
        else:
            cont += 1
    if cont == len(Primes):
        Primes.append(n)
# Now Get the ones that fit with N
PrimesforN = []
for p in Primes:
    if N % p == 0:
        PrimesforN.append(p)
print(max(PrimesforN))
