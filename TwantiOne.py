"""Skal lage spele Tjueein
spelaren startar med 0 poen g
spelaren trekkjer eit kort (1-13) i kvar omgang så lenge han/ho vil spela
ve3rdien på kortet blir lagt til poengsummen
dersom poengsummen blir større enn 32 blir har justert til 0, og spelete blir avslutta"""



from random import randint
from matplotlib import pyplot


spelar = input(("Navn på spelar: "))
farge = input(" %s sin farge (eng.): " % spelar)
beste_spelar = ""
storst = -1
while len(spelar) > 0:
    poeng = 0
    ferdig = False
    while not ferdig:
        svar = input("Du har %d poeng. Fleire kort? (j/n)"
                   % poeng)
        if svar[0].lower() == "j":
            kort = randint(1, 13)
            print("%s trakk %d. " % (spelar, kort))
            poeng += kort
            if poeng > 21:
                poeng = 0
                ferdig = True
        else:
            ferdig = True
    print("%s fekk %d poeng. " % (spelar, poeng))
    pyplot.bar(spelar, poeng)
    if poeng > storst:
        beste_spelar = spelar
        storst = poeng
    spelar = input("Namn på neste spelar: ")
    if len(spelar) > 0:
        farge = input("%s sin farge (eng.): " % spelar)

print("Beste spelar var %s med %d poeng."
      % (beste_spelar, storst))
pyplot.show()