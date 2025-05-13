"""fonction tri_insertion(L)
Données : L ← liste d’entiers
n ← taille de la liste
Pour k allant de 1 à n-1 faire
j ← k
Tant que j > 0 et L[j-1] > L[j] faire
On échange L[j-1] et L[j]
j ← j – 1
retourner L
"""




def tri_insertion(L) :
    n = len(L)
    for k in range(1, n) :
        j = k
        while j > 0 and L[j-1] > L[j] :
            L[j],L[j-1] = L[j-1],L[j]
            j = j - 1
    return L

L = [1,2,9,4,7,6]
print(tri_insertion(L))
