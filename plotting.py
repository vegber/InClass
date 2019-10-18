from matplotlib import pyplot
from random import random


def lag_tilfeldig_liste(n):
    """

    :param n:
    :return:
    """
    tilfeldig = [None]*n
    for i in range(n):
        tilfeldig[i] = random()
    return tilfeldig


def akkumuler(liste):
    """
    Erstattar alle liste[i] med liste[0] +... liste[i]
    :param liste:
    :return:
    """
    summen = 0.0
    for i in range(len(liste)):
        summen += liste[i]
        liste[i] = summen


def lag_akkumulert(liste):
    """
    lagar og returnerar liste med
    akkumulerte verdiar i liste

    :param liste:
    :return:
    """
    # Kopier lista:
    kopi = list(liste)
    akkumuler(kopi)
    return kopi


def lag_glattta(liste, vekt):
    """
    Lagar og returnerar liste med glatta verdia i liste,
    der vekta på kvart naboelement er lik vekt
    :param liste:
    :param vekt:
    :return:
    """
    n = len(liste)
    glatta_liste = list(liste)
    if n > 1:
        verdi = (1-vekt)*liste[0] + vekt*liste[1]
        glatta_liste[0] = verdi
        for i in range(1, n-1):
            verdi = vekt * liste[i-1] \
                + (1-2*vekt) * liste[i] \
                + vekt * liste[i + 1]
            glatta_liste[i] = verdi
        verdi = vekt * liste[n-2] + (1 - vekt) * liste[n - 1]
        glatta_liste[n-1] = verdi
        return glatta_liste


def main():
    observasjon = lag_tilfeldig_liste(10)
    pyplot.plot(observasjon, 'y')
    akkumulert = lag_akkumulert(observasjon)
    pyplot.plot(akkumulert, 'b')
    glatta_observasjonar = lag_glattta(observasjon, 0.2)
    pyplot.plot(glatta_observasjonar, 'r')
    pyplot.show()


main()
