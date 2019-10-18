#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program som tel ulike ord på tekstfiler.
@author: nmidd
"""


def stripp(ordliste):
    """
    Fjernar eit utval teikn frå alle ord i ei liste
    """
    rusk = ',.;:!?"\'|()[]{}\t\n '
    for i in range(len(ordliste)):
        ordliste[i] = ordliste[i].strip(rusk)


def les_ordliste(filnamn):
    """
    Returnerer ei liste over orda på fila med namn filnamn
    """
    with open(filnamn, 'r') as lesefil:
        tekst = lesefil.read()
    ordliste = tekst.split()
    stripp(ordliste)
    return ordliste



def main():

    ordliste = les_ordliste('uib.txt')
    n_ord = len(ordliste)
    ordmengd = set(ordliste)
    n_ulike = len(ordmengd)
    print('Fila uib.txt har %d ord.'
          % n_ord)
    print('Fila uib.txt har %d ulike ord.'
          % n_ulike)


main()