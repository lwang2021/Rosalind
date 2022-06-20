import Bio
from Bio.Seq import Seq

file = open(input("file = "))
sequence = file.readlines()[0].strip('\n')
proteins = str(Seq(sequence).translate(to_stop=True))

print(proteins)