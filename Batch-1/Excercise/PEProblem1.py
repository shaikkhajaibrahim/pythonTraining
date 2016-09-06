Sum = 0
for n in range(0,1000):
	if ((n + 1) % 3 == 0) or ((n + 1) % 5 == 0):
		Sum += n + 1
print(Sum)