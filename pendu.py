
mot1 = "binaire"
mot2 = mot1[0] +"_"*(len(mot1)-1)
mot3 = ""
def recalcule(mot2,l):
    mot3 = ""
    for i in range(len(mot1)):
        if mot1[i] == l :
            mot3 += l
        else :
            mot3 += mot2[i]
    return mot3
mot1 = "binaire"
mot2 = mot1[0] +"_"*(len(mot1)-1)
print(mot2)
def pendu():
    mot1 = "binaire"
    mot2 = mot1[0] +"_"*(len(mot1)-1)
    nb = 0
    while mot1 != mot2 and nb < 6 :
        l = input("choisi une lettre")
        if not l in mot1 :
            nb += 1
            print(nb,"erreur")
        else :
            mot2 = recalcule(mot2, l)
            print(mot2)
        if nb > 6 :
            print("tu as perdu")
            return
    if mot1 == mot2 :
        print("bravo tu as gagné en ",nb,"erreurs")
    else :
        print("tu as perdu en ",nb,"coups")
    return
pendu()