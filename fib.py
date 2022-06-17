months = int(input("months: "))
escalation = int(input("escalation: "))
n = 0
offspring = []

while n <= months:
    if len(offspring) <= 2:
        offspring.append(1)
    else:
        newvalue = offspring[-1] + offspring[-2] * escalation
        offspring.append(newvalue)
    n += 1

print(offspring[-1])