import random

print("Random number from range(100):",random.choice(range(100)))
print("Random number from list:",random.choice([1,2,3,4,5,6,7,8,9]))
print("Random character from string: ",random.choice('Python Programming Language') )

# randrange(start,stop,step)

print('randrange(2,100,2): ',random.randrange(2,100,2) )

#shuffle
numbers=[20,24,17,32]
random.shuffle(numbers)
print("Reshuffled list :",numbers)

random.shuffle(numbers)
print("Reshuffled  again list :",numbers)
