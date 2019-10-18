
from math import sqrt

fra = int(input("Nedre grense (medrekna): "))
til = int(input("Oovre grense (ikkje medrekna): "))
summen = 0.0
if fra % 2 == 0:
    fra += 1
for radikand in range(fra, til, 2):
    rot = sqrt(radikand)
    summen += rot
print("Summen av kvadratroottene: %.2f" % summen)

