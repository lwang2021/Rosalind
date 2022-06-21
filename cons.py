from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio.Seq import Seq

sequences = []
longest = ""

for seq_record in SeqIO.parse("/Users/lwang/Downloads/" + input("file name: "), "fasta"):
    sequences.append(str(seq_record.seq))

a = ["0"] * len(sequences[0])
t = ["0"] * len(sequences[0])
c = ["0"] * len(sequences[0])
g = ["0"] * len(sequences[0])
for i in sequences:
    for k in range(len(i)):
        letter = i[k]
        if letter == "A":
            a[k] = str(int(a[k]) + 1)
        elif letter == "T":
            t[k] = str(int(t[k]) + 1)
        elif letter == "C":
            c[k] = str(int(c[k]) + 1)
        elif letter == "G":
            g[k] = str(int(g[k]) + 1)

for i in range(len(a)):
    largest = int(a[i])
    lett = "A"
    if int(t[i]) > largest:
        largest = int(t[i])
        lett = "T"
    if int(c[i]) > largest:
        largest = int(c[i])
        lett = "C"
    if int(g[i]) > largest:
        largest = int(g[i])
        lett = "G"
    longest += lett

print(longest)
print("A: " + " ".join(a))
print("C: " + " ".join(c))
print("G: " + " ".join(g))
print("T: " + " ".join(t))