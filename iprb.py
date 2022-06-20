homoDom = int(input("Homozygous dominant: "))
hetero = int(input("Heterozygous: "))
homoRec = int(input("Homozygous recessive: "))
Total = homoDom + hetero + homoRec

recProb = (homoRec/Total) * ((homoRec - 1)/(Total - 1))
recHeteroProb = ((hetero/Total) * (homoRec/(Total - 1))) / 2
heteroRecProb = ((homoRec/Total) * (hetero/(Total - 1))) / 2
heteroProb = ((hetero/Total) * ((hetero - 1)/(Total - 1))) / 4

totalProb = 1 - (heteroProb + recHeteroProb + recProb + heteroRecProb)

#prob = 1 - (totalProb / (Total * (Total - 1)))

print(totalProb)