

styrke = float(input("Gje vindstyrke (km/h): "))

if styrke >= 117.0:
    print("Orkan. ")
elif styrke >= 76.0:
    print("Storm.")
elif styrke >= 40.0:
    print("kuling")
elif styrke >= 12.0:
    print("Bris. ")
elif styrke >= 0.0:
    print(" Lite vind. ")
else:
    print("Feil: negativ vind")


