sequence1 = input("sequence 1: ")
sequence2 = input("sequence 2: ")
n = 0

for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
        n += 1

print(n)