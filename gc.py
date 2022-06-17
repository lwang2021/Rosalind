from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio.Seq import Seq
sequences = []
percents = []
ids = []
longestid = ""
longest = 0

for seq_record in SeqIO.parse("/Users/lwang/Downloads/" + input("file name: "), "fasta"):
    ids.append(seq_record.id)
    string = seq_record.seq
    sequences.append(string)

for sequence in sequences:
    percents.append(GC(sequence))

for i in range(len(percents)):
    percent = percents[i]
    if percent > longest:
        longestid = ids[i]
        longest = percent

print(percents)
print(longestid)
print(longest)