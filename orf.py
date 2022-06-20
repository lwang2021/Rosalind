from Bio.SeqUtils import GC
from Bio import SeqIO
from Bio.Seq import Seq

sequences = []
proteins = []

for seq_record in SeqIO.parse("/Users/lwang/Downloads/" + input("file name: "), "fasta"):
    sequence = seq_record.seq

sequences.append(sequence)
sequences.append(sequence[1:-2])
sequences.append(sequence[2:-1])
sequences.append(sequence.reverse_complement())
sequences.append(sequence.reverse_complement()[1:-2])
sequences.append(sequence.reverse_complement()[2:-1])

for seq in sequences:
    seq = seq.translate()
    start = False
    current = []
    for letter in seq:
        if letter == "M":
            current.append("")
            start = True
        elif letter == "*":
            if start:
                for i in current:
                    if i in proteins:
                        continue
                    proteins.append(i)
            start = False
            current = []
        if start:
            for k in range(len(current)):
                current[k] += letter

for i in proteins:
    print(i)