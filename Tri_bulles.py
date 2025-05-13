def tri_bulles(T) :
    n = len(T)
    for i in range(n, 0 , -1) :
        for j in range(i-1) :
            if T[j] > T[j+1] :
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
Test = [1,4,2,5,9,10]
print(tri_bulles(Test))


'''
def tri_bulles(T):
    n = len(T)
    for i in range(...,....,-1):
        for j in range(i):
            if T[j] > T[...]:
                .... = T[j]
                T[j] = T[...]
                T[j+1] = temp
    return T


Test = [1,4,2,5,9,10]
print(tri_bulles(Test))
'''