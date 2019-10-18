

pris = float(input("Ordiner pris"))
rabpris = float(input("Rabattert pris: "))
grense = float(input("Rabattgrense: "))
kvantum = float(input("Kvantum: "))
kundenr = int(input("Kundenr: "))

betaling = kvantum * pris
if kundenr < 100:
    if kvantum > grense / 2:
        betaling = grense/2 * pris + (kvantum - grense / 2) * rabpris
elif kvantum > grense:
        betaling = grense * pris + (kvantum - grense) * rabpris
print(" Til betaling: %.f NOK" % betaling)