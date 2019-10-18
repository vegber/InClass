#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Handterer artsobservasjonar lagra på fil
@author: nmidd
"""

from os import chdir


def summer(streng):
    """
    Returnerer summen av alle tal i strengen streng
    """
    liste = streng.split()
    summen = 0
    for ordet in liste:
        if ordet.isdigit():
            summen += int(ordet)
    return summen


def lag_totaloversikt(observasjonar, analyse, filnamn):
    """
    Les artsobservasjonar frå fila med namn filnamn i katalogen observasjonar.
    Skriv talet på observasjonar av kvar art på fila filnamn i katalogen analyse.
    """
    chdir(observasjonar)
    lesfil = open(filnamn, 'r')
    liste = lesefil.readlines()
    lesefil.close()
    chdir(analyse)
    with open(filnamn, 'w') as skrivefil:
        for streng in liste:
            total = summer(streng)
            art = streng.split()[0]
            skrivefil.write(art + ' ' + str())

def main():
    lag_totaloversikt('/Users/nmidd/Observasjonar',
                      '/Users/nmidd/Analyse/',
                      'fugl.txt')


main()
