L = [1,4,2,6,7,9,2,12]

def mini(L):

    mini = L[0]
    i_mini = 0
    for i in range(len(L)):
        if L[i] < mini :
            mini = L[i]
            i_mini = i
    return i_mini


def tri_par_selection(L) :
    for i in range(len(L)) :

        i_mini = mini(L[i:])+i
        #print(i_mini)
        L[i_mini],L[i] = L[i],L[i_mini]
    return L


L = [1,4,2,6,7,9,2,12]
print(tri_par_selection(L))
#pokemmo
#france.ioi