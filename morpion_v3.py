#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Jeu de Morpion v3 : 2 joueurs humains
# JJDides juin 2015

''' STRUCTURE DE DONNEES
    Plateau est une liste de 9 entiers, représentant les 3 x 3 cases de la grille de Morpion
    Plateau[i] contient 0 pour une case vide, 1 ou 2 pour une case occupée par joueur1 ou joueur2 '''

### FONCTIONS ###

# fonction créant un plateau de jeu vide
# Résultat : une liste de 9 entiers
def nouveau() :
    Pl = [0] * 9
    return Pl

### FONCTIONS IHM ###

# fonction affichant le plateau de jeu
# Donnée : une liste de 9 entiers (0 si case vide, 1 ou 2 si case occupée par joueur 1 ou 2)
def affiche(Pl) :
    # cases[] : liste de 9 caractères à afficher ('.' si case vide, 'O' ou 'X' si case occupée par joueur 1 ou 2)
    cases = ['.'] * 9
    for i in range(len(Pl)) :
        if Pl[i] == 1 : cases[i] = 'O'
        elif Pl[i] == 2 : cases[i] = 'X'
    print('\n  1 2 3')
    print('1',cases[0],cases[1],cases[2])
    print('2',cases[3],cases[4],cases[5])
    print('3',cases[6],cases[7],cases[8],'\n')

# fonction qui convertit n° de ligne + n° de colonne en rang de case du Plateau
# donnée : 2 entiers, de 1 à 3, les n° de ligne l et de colonne c
# résultat : 1 entier, de 0 à 8, le rang de la case c,l dans le plateau
def num_case(l, c) :
    return 3*(l-1)+c-1

# fonction qui permet à un joueur de choisir une case du plateau
# résultat : un entier case, le rang de la case du plateau choisie
def saisie_case() :
    c = int(input("N° de colonne :"))   # numéros de colonne (1,2,3)
    l = int(input("N° de ligne :"))     # numéros de ligne (1,2,3)
    while not c in range(1,4) or not l in range(1,4) :
        print('Saisie incorrecte : entrer des n° entre 1 et 3 !')
        c = int(input("N° de colonne :"))
        l = int(input("N° de ligne :"))
    print('Il joue en C',c,'L',l)
    return num_case(l,c)

# fonction qui permet à un joueur de choisir une case du plateau pour y déposer un pion
# données : une liste Pl de 9 entiers (0,1,2), l'état du plateau de jeu
#           un entier jo, le n° du joueur (1,2)
# résultat : un entier coup, le rang de la case du plateau choisie
def saisie_coup(Pl) :
    coup = saisie_case()
    # après avoir choisi une case, on verifie qu'elle est n'est pas déjà occupée
    while not coup_possible(Pl, coup) :
         print('Case déjà occupée : refaire un choix !')
         coup = saisie_case()
    return coup

### FONCTIONS D'EVALUATION ###

# fonction déterminant si un joueur a gagné la partie
# Donnée : une liste de 9 entiers (le plateau de jeu)
# Résultat : un entier (0 si pas de gagnant, 1 ou 2 si joueur 1 ou 2 a gagné)
def qui_gagne(Pl):
    gagnant = 0
    if (Pl[0]!=0 and Pl[0]==Pl[3]==Pl[6]): gagnant=Pl[0]
    if (Pl[1]!=0 and Pl[1]==Pl[4]==Pl[7]): gagnant=Pl[1]
    if (Pl[2]!=0 and Pl[2]==Pl[5]==Pl[8]): gagnant=Pl[2]
    if (Pl[0]!=0 and Pl[0]==Pl[1]==Pl[2]): gagnant=Pl[0]
    if (Pl[4]!=0 and Pl[4]==Pl[5]==Pl[3]): gagnant=Pl[3]
    if (Pl[7]!=0 and Pl[7]==Pl[8]==Pl[6]): gagnant=Pl[6]
    if (Pl[0]!=0 and Pl[0]==Pl[4]==Pl[8]): gagnant=Pl[0]
    if (Pl[2]!=0 and Pl[2]==Pl[4]==Pl[6]): gagnant=Pl[2]
    return gagnant

# fonction booléenne qui détermine si la partie est gagnée
# donnée : une liste de 9 entiers (0,1,2), l'état du plateau de jeu
# résultat : un booléen, vrai si un des 2 joueurs a gagné la partie
def gagne(Pl) :
    res = qui_gagne(Pl)
    return (res == 1) or (res == 2)

# fonction booléenne qui teste si le plateau est rempli
# retourne faux s'il reste une case libre, vrai sinon
def plein(Pl) :
    # calcul du produit des cases du plateau, nul au moins une case est vide
    prod = 1
    for i in range(len(Pl)) :
        prod  = prod * Pl[i]
    return (prod != 0)

# fonction booléenne qui vérifie si un coup est possible sur une case
# donnée : une liste Pl d'entiers (0,1,2), le plateau de jeu
#          un entier, le n° de la case
# résultat : un booléen, vrai si la case est vide
def coup_possible(Pl, n) :
    return (Pl[n] == 0)

# fonction INUTILISEE qui construit la liste des coups possibles
# donnée : une liste Pl de 9 entiers (0,1,2), l'état du plateau de jeu
# résultat : une liste d'entiers (0..8), les rangs des cases encore vide
def coups_possibles(Pl) :
    res = []
    for i in range(len(Pl)) :
        if Pl[i] == 0 : res.append(i)
    return res

# fonction qui détermine le joueur qui va jouer
# donnée : une liste Pl de 9 entiers (0,1,2), l'état du plateau de jeu
# résultat : un entier, le n° du jouer qui va jouer
def suivant(Pl) :
    j1, j2 = 0, 0   # nombre de pions déjà posés par chaque joueur
    for i in range(len(Pl)) :
        if Pl[i] == 1 : j1 += 1
        if Pl[i] == 2 : j2 += 1
# joueur1 ayant commencé, si j1=j2 : c'est à joueur1 de jouer,
#                         si j1=j2+1 : c'est à joueur2
    if j1 == j2 : return 1
    else : return 2


### PROGRAMME PRINCIPAL ###

### Initialisations
Plateau = nouveau()
joueur = 1  # joueur 1 commence
affiche(Plateau)

### Tours de jeu
while not gagne(Plateau) and not plein(Plateau) :   # tant qu'aucun joueur n'a gagné et que la plateau n'est pas rempli
    print('Au joueur', joueur,'de jouer : ', end='')
    if joueur == 1 : print('il a les pions "O" ...')
    else : print('il a les pions "X" ...')
    coup = saisie_coup(Plateau)             #   le joueur choisit une case du plateau
    Plateau[coup] = joueur                  #   et y place son pion
    affiche(Plateau)
    joueur = suivant(Plateau)               # on change de joueur

### Affichage du résultat de la partie
if gagne(Plateau) :
    print("Le joueur",qui_gagne(Plateau),"gagne la partie !")
else :
    if plein(Plateau) :
        print("Grille pleine et match nul !")