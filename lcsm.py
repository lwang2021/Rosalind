file_name = "/Users/lwang/Downloads/" + input("file name: ")
f = open(file_name)
file = f.readlines()
n = 0
dna = []
possible = []
longest = ""

for i in file:
    i = i.strip("\n")
    if ">Rosa" in i:
        dna.append("")
    else:
        dna[-1] = dna[-1] + i

def compare(string1, string2):
    for i in range(len(string1)):
        k = 2
        while k + i < len(string1):
            sub = string1[i:i + k]
            if sub in string2:
                possible.append(sub)
            k = k + 1

def count(sub):
    m = 0
    for letter in sub:
        m = m + 1
    return m

compare(dna.pop(0), dna.pop(0))

for sequence in dna:
    for sub in possible:
        if not sub in sequence:
            possible.remove(sub)

for sub in possible:
    if count(sub) > len(longest):
        longest = sub

print(longest)