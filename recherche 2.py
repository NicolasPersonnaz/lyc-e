from random import randint
from timeit import default_timer as timer

L = [randint(0, 99999) for i in range(99999)]  # pour la créer
L.sort()  # pour la trier

def recherche(L, x):
    debut = timer()
    i = 0
    j = len(L) - 1
    c = 0  # compteur
    while i <= j:
        m = (i + j) // 2
        if L[m] == x:
            c = c + 1
            fin = timer()
            print(fin - debut)
            return c
        elif L[m] > x:
            j = m - 1
            c = c + 1
        else:
            i = m + 1
            c = c + 1
    fin = timer()
    print(fin - debut)
    return "-1"

recherche(L, 500)
