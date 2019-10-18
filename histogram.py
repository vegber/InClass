

from matplotlib import pyplot

n = int(input("Antal observerte artar: "))
for i in range(n):
    art = input("Observert art: ")
    observasjonar = int(input("Antal observasjonar av " + art + ": "))
    farge = "pink"
    if art.startswith("blaa"):
        farge = "blue"
    elif art.startswith("graa"):
        farge = "grey"
    elif art.startswith("svart"):
        farge = "black"
    elif art.startswith("groon"):
        farge = "green"
    elif art.startswith("rood"):
        farge = "red"
    elif art.startswith("gul"):
        farge = "yellow"
    pyplot.bar(art, observasjonar, color=farge)
pyplot.show()


