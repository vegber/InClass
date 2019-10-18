# coding=utf-8
def skriv(talliste):
    """
    :param talliste:
    :return:
    """
    for i in range(len(talliste)):
        print("%3d %7.2f" % (i, talliste[i]))


def store_avvik(talliste):
    """
    :param talliste:
    :return:
    """
    summen = sum(talliste)
    n = len(talliste)
    snitt = summen / n
    print("Store avvik frå gjennomsnittet på %7.2f"
          % snitt)
    for tal in talliste:
        avvik = tal - snitt
        if abs(avvik) > abs(snitt) / 2:
            print("%7.2f %7.2f" % (tal, avvik))


def to_like(talliste):
    """
    :param talliste:
    :return:
    """
    i = 0
    while i < len(talliste) - 1:
        if talliste[i] == talliste[i + 1]:
            return i
        i += 1
    return -1


def main():
    n = int(input("Antal observasjonar: "))
    talliste = []
    for i in range(n):
        tal = float(input("%3d. observasjon: "
                          % (i + 1)))
        talliste.append(tal)

    skriv(talliste)
    store_avvik(talliste)
    pos = to_like(talliste)

    if pos >= 0:
        print("Elementene i posisjonane %d og %d er begge lik %.1f" %
              (pos, pos + 1, talliste[pos]))
    else:
        print("Lista har ikkje to etterfylgjande element")
