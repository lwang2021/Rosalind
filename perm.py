import random
import math

length = int(input("Permutation length: "))
test = []
factorial = math.factorial(length)
lst = [[]] * factorial

def permutation():
    for i in range(len(lst)):
        createPermutation(i)
        

def createPermutation(i):
    test = []
    for j in range(length):
        rand = random.randint(1, length)
        while rand in test:
            rand = random.randint(1, length)
        else:
            test.append(rand)
    if test in lst:
        createPermutation(i)
    else:
        lst[i] = test

permutation()

print(factorial)
for i in lst:
    sequence = ""
    for j in i:
        if j == i[-1]:
            sequence += str(j)
        else:
            sequence += str(j) + " "
    print(sequence)