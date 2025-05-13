def chercheD(e,L):
    g = 0
    d = len(L)
    while g <= d :
        m = (g+d)//2
        if L[m] == e :
            return m
        elif e > L[m] :
            g = m+1
        else :
            d = m-1
T = [1,2,3,4,5,6,7,8,9,10]
#print(chercheD(7,T))


def dichotomie_rec(val,tab,g,d) :
    millieu = (g+d)//2
    if val == tab[millieu] :
        return millieu
    elif g ==d :
        return False
    else :
        if val > tab[millieu] :
            return dichotomie_rec(val, tab,millieu+1 , d)
        else :
            return dichotomie_rec(val, tab , g , millieu-1 )
T = [1,2,3,4,5,6,7,8,9,10]
print(dichotomie_rec(7, T, 0, len(T)))