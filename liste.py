from random import randrange, choice

def recherche(e,L) :
    for i in range(len(L)):
        if e == L[i] :
            return i
    return False

def compte(e,L) :
    c=0
    for i in range(len(L)):
        if e == L[i] :
            c = c + 1
    return c

L = [1,2,4,5,7,123,6543]


def maxi(L):
    m = L[0]
    for i in range(len(L)):
        if L[i] > m :
            m = L[i]
    return m

print(maxi(L))


def mini(L):
    if len(L)>0:

        m = L[0]
        for i in range(len(L)):
            if L[i] < m  :
                m = L [i]
        return m
    else : return -1


def moyenne(L):
    m = 0
    for i in range (len(L)) :
        m = L[i] + m
    return m / len(L)

def sansdoublon(L) :
    L2 = []
    for i in range(len(L)) :
        if not L[i] in L2 : L2 += [L[i]]
    return L2
tirage = []
L = [randrange(1,50) for i in range(8) ]
for i in range(6) :
     L2 = []
     for i in range(len(L)) :
        if not L[i] in L2 : L2 += [L[i]]
print(L2)
num = choice(L)
tirage += [num]
sansdoublon(L)

#L = [randrange(1,50) for i in range(8) ]
recherche(10,L)
#print(L)