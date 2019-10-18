from random import randint
from colorama import Fore, Back, Style


def finn_hoogder(n_soor, n_aust):
    """
    Genererar og returnerar matrise med n_soor*n_aust
    tilfeldige hoogder i intervallet[0, 500]
    :param n_soor:
    :param n_aust:
    :return:
    """
    hoogder = [None] * n_soor
    for soor in range(n_soor):
        hoogder[soor] = [None] * n_aust
        for aust in range(n_aust):
            hoogder[soor][aust] = randint(0, 500)
    return hoogder


def teikn(hoogde, fargar, grenser):
    """
    Skriv ut ein pixel med farge som funksjon av hoogd
    :param hoogde:
    :param fargar:
    :param grenser:
    :return:
    """
    farge = fargar[0]
    for i in range(len(grenser)):
        if hoogde >= grenser[i]:
            farge = fargar[i + 1]
    print(farge, end='')


def teikn_kart(hoogder, fargar, grenser):
    """
    Teiknar kart med farge som funksjon av hoogd
    :param hoogder:
    :param fargar:
    :param grenser:
    :return:
    """
    for soor in range(len(hoogder)):
        for aust in range(len(hoogder[soor])):
            teikn(hoogder[soor][aust], fargar, grenser)
        print()


def main():
    """

    :return:
    """
    pixel = chr(9608)
    print(Style.BRIGHT)
    blaa = Fore.BLUE + pixel
    groon = Fore.GREEN + pixel
    gul = Fore.YELLOW + pixel
    raud = Fore.RED + pixel

    fargar = [blaa, groon, gul, raud]
    grenser = [1, 200, 400]
    hoogder = finn_hoogder(20, 50)
    teikn_kart(hoogder, fargar, grenser)
    print(Style.RESET_ALL)


main()
