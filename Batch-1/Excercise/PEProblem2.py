# Generate Fibonacci Sequence
FibSeq = [1, 2]
actnum = 2
while actnum < 4000000:
    actnum = FibSeq[-2] + FibSeq[-1]
    FibSeq.append(actnum)
# Now take the sum of the even numbers
Sum = 0
for n in FibSeq:
    if n % 2 == 0:
        Sum += n
print(Sum)
