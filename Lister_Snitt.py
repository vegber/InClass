n = int(input("Antal data input: "))

summen = 0.0
for i in range(n):
    tal = float(input(" %3d. tal: " % (i + 1)))
    summen += tal
snitt = summen / n
print("Gjennomsnitt: ", snitt)
