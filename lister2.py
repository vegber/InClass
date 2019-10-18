#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demonstrerer ulike operasjonar på lister
@author: nmidd
"""


def finn_alle(liste, verdi):
    """
    Returnerer liste med indeksane til alle
    forekomstar av verdi i liste
    """
    indeksliste = []
    for i in range(len(liste)):
        if liste[i] == verdi:
            indeksliste.append(i)
    return indeksliste


def lag_kort_liste(liste):
    """
    Lagar og returnerer kortversjon av liste,
    der alle element er med berre ein gong
    """
    kort_liste = []
    for verdi in liste:
        if verdi not in kort_liste:
            kort_liste.append(verdi)
    return kort_liste


def fjern_duplikate(liste):
    """
    Fjernar multiple forekomstar av element i liste
    """
    i = 1
    while i < len(liste):
        verdi = liste[i]
        if verdi in liste[:i]:
            liste.pop(i)
        else:
            i += 1


def main():
    # Testar funksjonen finn_alle:
    resultat = ['Rosenborg', 'Brann',
                'Molde', 'Brann', 'Kristiansund']
    funn = finn_alle(resultat, 'Brann')
    for indeks in funn:
        print('Brann står i posisjon %d i resultatlista'
              % (indeks + 1))

    # Testar funksjonen lag_kort_liste
    kort_liste = lag_kort_liste(resultat)
    print(kort_liste)


"""
    # Testar funksjonen fjern_duplikate:
    resultat = ['Rosenborg', 'Brann',
                'Brann', 'Haugesund', 'Rosenborg']
    print(resultat)
    fjern_duplikate(resultat)
    print(resultat)
    """

main()
