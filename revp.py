sequence = input("sequence =")
answer = []

def createPalindrome(sequenceSub):
    newsequence = ""
    for letter in sequenceSub:
        if letter == "A":
            newsequence = "T" + newsequence
        if letter == "C":
            newsequence = "G" + newsequence
        if letter == "G":
            newsequence = "C" + newsequence
        if letter == "T":
            newsequence = "A" + newsequence
    return newsequence

for i in range(len(sequence)):
    k = 4
    while k < 13 and i + k <= len(sequence):
        splice = sequence[i:k + i]
        if splice == createPalindrome(splice):
            answer.append([i + 1, k])
        k = k + 1

for i in range(len(answer)):
    """"
    location = answer[i][0]
    if i + 1 == len(answer):
        print(str(location) + " " + str(answer[i][1]))
        break
    elif location == answer[i+1][0]:
        continue
    """
    print(str(answer[i][0]) + " " + str(answer[i][1]))