from random import random
from matplotlib import pyplot


def lag_nedbor(n_stadar, n_dagar, sannsyn, maks):
    """
    lagar og returnar matrise med tilfeldige nedborskvanta på
    n_stadar stadar over n _dagar. Sannsynet for nedbor er gitt med
    parameteren sannsyn, og teoretisk stoorste
    nedboorskvantum er gitt med maks
    :param n_stadar:
    :param n_dagar:
    :param sannsyn:
    :param maks:
    :return:
    """
    nedboor = []
    for stad in range(n_stadar):
        nedboor.append([])
        for dag in range(n_dagar):
            regnversdag = random()
            if regnversdag <= sannsyn:
                # Nedbor registert denne dagen
                regn = random() * maks
                nedboor[stad].append(regn)
            else:
                nedboor[stad].append(0.0)
    return nedboor


def les_nedbor(n_stadar, n_dagar):
    """

    :param n_stadar:
    :param n_dagar:
    :return:
    """
    nedbor = []
    for stad in range(n_stadar):
        nedbor.append([])
        print("Nedboor (mm) på stad %d: " % (stad + 1))
        for dag in range(n_dagar):
            innlest = float(input("\tDag %d: " % (dag + 1)))
            nedbor[stad].append(innlest)
    return nedbor


def skriv_nedboor(nedboor):
    """

    :param nedboor:
    :return:
    """
    print("       ", end="")
    for dag in range(len(nedboor)):
        print("Stad%2d" % (dag + 1), end="")
    print()

    for stad in range(len(nedboor)):
        print("Stad%2d" % (stad + 1), end="")
        for dag in range(len(nedboor[stad])):
            print("%6.1f" % nedboor[stad][dag], end="")
        print()


def skriv_snitt_stad(nedboor):
    """
    Reknar ut og skriv ut total og
    gjennomsnittleg nedbor for kvar stad
    :param nedboor:
    :return:
    """
    n_stadar = len(nedboor)
    for stad in range(n_stadar):
        summen = sum(nedboor[stad])
        n_dagar = len(nedboor[stad])
        if n_dagar > 0:
            snitt = summen / n_dagar
            print('Totalnedboor på stad %d: %.1f' % (stad + 1, summen))
            print('Gjennomsnittsnedboor på stad %d: %.1f' % (stad + 1, snitt))


def skriv_snitt_dag(nedboor):
    """

    :param nedboor:
    :return:
    """
    n_stadar = len(nedboor)
    if n_stadar > 0:
        n_stadar = len(nedboor[0])
        for dag in range(n_dagar):
            summen = 0.0
            for stad in range(n_stadar):
                summen += nedboor[stad][dag]
            snitt = summen / n_stadar
            print('Totalnedboor på dag %d: %1.f' % (dag + 1, summen))
            print('Gjennomsnittsnedboor på dag %d: %1.f' % (dag + 1, snitt))


def plott(nedboor):
    """

    :param nedboor:
    :return:
    """
    for stad in range(len(nedboor)):
        pyplot.plot(nedboor[stad])
    pyplot.show()


def teikn_histogram(liste, tittel):
    """
    teiknar histogram som svarar til verdiane i liste.
    Tittelen på histogrammet er gitt med parameteren tittel.
    :param liste:
    :param tittel:
    :return:
    """
    n_stadar = len(liste)
    for stad in range(n_stadar):
        pyplot.bar('Stad ' + str(stad + 1), liste[stad])
    pyplot.title(tittel)
    pyplot.show()


def teikn_hist_maks(nedboor):
    """
    Teiknar histogram over maksimalt
    nedboorskvatum for kvar stad
    Returnerar ei liste over verdiane i histogrammet
    :param nedboor:
    :return:
    """
    n_stadar = len(nedboor)
    maksliste = [None] * n_stadar
    for stad in range(n_stadar):
        maks = max(nedboor[stad])
        maksliste[stad] = maks
    teikn_histogram(maksliste, 'Maksimalt nedboor')
    return maksliste


def teikn_hist_tot(nedboor):
    """

    :param nedboor:
    :return:
    """
    n_stadar = len(nedboor)
    totliste = [None] * n_stadar
    for stad in range(n_stadar):
        maks = max(nedboor[stad])
        totliste[stad] = maks
    teikn_histogram(totliste, 'Maksimalt nedboor')
    return totliste


def finn_kor_maks(nedboor, dag):
    """
    Returnerer indeksen til staden der
    det regna mest på oppgitt dag

    :param nedboor:
    :param dag:
    :return:
    """
    stad_maks = -1
    maks = -1
    n_stadar = len(nedboor)
    for stad in range(n_stadar):
        regn = nedboor[stad][dag]
        if regn > maks:
            stad_maks = stad
            maks = regn
    return stad_maks


def teikn_kake(nedboor):
    """
    Teiknar kakediagram over kor ofte
    kvar stad er den med mest nedboor
    :param nedboor:
    :return:
    """
    n_stadar = len(nedboor)
    if n_stadar > 0:
        n_dagar = len(nedboor[0])
        frekvens = [0] * n_stadar
        tekst = ['Stad '] * n_stadar
        for stad in range(n_stadar):
            tekst[stad] += str(stad + 1)
        for dag in range(n_dagar):
            stad = finn_kor_maks(nedboor, dag)
            frekvens[stad] += 1
        pyplot.pie(frekvens, labels = tekst)


n_stadar = int(input('Talet på stadar: '))
n_dagar = int(input('Talet på dagar: '))
nedboor = lag_nedbor(n_stadar, n_dagar, 0.7, 50.9)
print()
skriv_nedboor(nedboor)
skriv_snitt_stad(nedboor)
plott(nedboor)
teikn_hist_tot(nedboor)
teikn_hist_maks(nedboor)
teikn_kake(nedboor)
