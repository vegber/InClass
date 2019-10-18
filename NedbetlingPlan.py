

belop = float(input("Lånebeløp (NOK): "))
startaar = int(input("Startår: "))
rente = float(input("Årleg rente (%): "))
betaling = float(input((
    "Årleg betling av adrag og renter (NOK): ")))

if betaling > belop * rente / 100.0:
    balanse = belop
    aar = startaar
    while balanse > 0.0:
        print("%4d: %10.2f" % (aar, balanse))
        balanse += balanse * rente / 100.0
        balanse -= betaling
        aar += 1
else:
    print("For liten innbetaling. ")

