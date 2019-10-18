n = int(input("Antal observasjonar: "))
talliste = []
for i in range(n):
    tal = float(input("%3d. observasjon: "
                % (i + 1)))
    talliste.append(tal)
summen = sum(talliste)
snitt = summen/n
print()
print("%s %7s" % ("Verdi", "avvik"))
for tal in talliste:
    avvik = tal - snitt
    print("%7.2f %7.2f" % (tal, avvik))
