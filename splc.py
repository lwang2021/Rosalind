from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio.Seq import Seq

sequences = []

for seq_record in SeqIO.parse("/Users/lwang/Downloads/" + input("file name: "), "fasta"):
    string = str(seq_record.seq)
    sequences.append(string)

base = str(sequences.pop(0))

for i in sequences:
    base = base.replace(i, "")

base = str(Seq(base).translate(to_stop=True))

print(base)
