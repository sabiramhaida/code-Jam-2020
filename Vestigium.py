def repeatedElementInLine(L,n):
    for i in range(n-1):
        if (L[i] in L[i+1:]):  return True
    return False

def repeatedElementInCol(C,n):
    for i in range(n-1):
        if (C[i] in C[i+1:]): return True
    return False

import collections as cl
for t in range(int(input())):
    n = int(input())
    k, r, c = 0, 0, 0
    colonnes = [[] for _ in range(n)]
    for i in range(n):
        Ligne = list(map(int,input().split()))
        k += Ligne[i]
        if(repeatedElementInLine(Ligne,n)):
            r+=1
        for i in range(n):
            colonnes[i].append(Ligne[i])
    for i in range(n):
        if(repeatedElementInCol(colonnes[i],n)):
            c+=1
    print('Case #{}: {} {} {}'.format(t+1,k, r, c))

        

