def plateau(n) :
# fonction affichant un plateau de n bâtons
    print("| " * n)

def ordi(n,j):
    m=1
    m%4==1
    e = int(input(1))

def choix(n,j):
# fonction retournant un nombre e de batons à prélever après contrôle de la saisie du choix du joueur j sur un plateau de n bâtons
    if n > 3 : max = 3
    else : max = n      # max : maximum de bâtons prélevables
    message = "Combien de batons le joueur", j, "prend il ?"
    e = int(input(message))
    while not e in range(1, max+1) :
        e = int(input(message))
    return e

def suivant(j) :
# fonction retournant le n° du joueur suivant le joueur  j
    if j ==1 :
         return 2
    else :
         return 1




### Programme principal
n=15
j=1
plateau(n)
while n > 1 :
    e = choix(n,j)
    n = n-e
    plateau(n)
    j = suivant(j)
    print(n)

print("Le joueur",j," a perdu")