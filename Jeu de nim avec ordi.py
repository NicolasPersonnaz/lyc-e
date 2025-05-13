def plateau(n) :
# fonction affichant un plateau de n bâtons
    print("| " * n)


def choix(n):
# fonction retournant un nombre e de batons à prélever après contrôle de la saisie du choix du joueur j sur un plateau de n bâtons
    if n > 3 : max = 3
    else : max = n      # max : maximum de bâtons prélevables
    message = "Combien de batons le joueur 1 prend il ?"

    e = int(input(message))
    while not e in range(1, max+1) :
        e = int(input(message))
    return e


def nbp(b):
    if b == 0:
        e = 2
    elif b ==1 :
        e = 3
    elif b == 2 :
        e = 2
    else:
        e = 1
    return e


### Programme principal
b = 0
n=15
plateau(n)
while n > 1 :

    e = nbp(b)
    n = n - e
    plateau(n)
    print(n)
    e = choix(n)
    b = e
    n = n-e
    plateau(n)
    print(n)

print("Le joueur 1 a perdu")