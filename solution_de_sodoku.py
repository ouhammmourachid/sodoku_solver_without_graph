# ------------------------------la regle 1--------------------------------------
def valeurpossible(L,i,j,n,m):
    if L[i][j][n][m]==0:
        a=[]
        for h in range(3):
            for s in range(3):
                a+=[L[i][j][h][s]]
        for s in range(3):
            a+=L[i][s][n]
        for s in range(3):
            for f in range(3):
                a+=[L[s][j][f][m]]
        return [i for i in range(1,10) if i not in a]
    else :
        return []
def rule1(L):
    return [[[[valeurpossible(L,i,j,n,m) for m in range(3)]for n in range(3)]for j in range(3)]for i in range(3)]
# -------------------------la regle 2-------------------------------------------
def rule2(L,H):
    for i in range(3):
        for j in range(3):
            for n in range(3):
                for m in range(3):
                    if len(H[i][j][n][m])==1:
                        L[i][j][n][m]=H[i][j][n][m][0]
    return L
#--------------------------la regle 3-------------------------------------------
def ligne(L,i,j):
    H=rule1(L)
    for h in range(1,10):
        s=0
        for a in range(3):
            for b in range(3):
                for c in H[i][a][j][b]:
                    if c==h:
                        s+=1
                        B,D=a,b
        if s==1:
            L[i][B][j][D]=h
    return L
def colone(L,i,j):
    H=rule1(L)
    for h in range(1,10):
        s=0
        for a in range(3):
            for b in range(3):
                for c in H[a][i][b][j]:
                    if c==h:
                        s+=1
                        A,B=a,b
        if s==1:
            L[A][i][B][j]=h
    return L
def rule3(L):
    for i in range(3):
        for j in range(3):
            L=ligne(L,i,j)
            L=colone(L,i,j)
    return L
#---------------------------la regle 4------------------------------------------
def ligne1(H,i,j,n):
    for y in range(1,10):
        h=False
        for a in range(3):
            if y in H[i][n][j][a]:
                h=True
        if h==True:
            for a in range(3):
                A=[f for f in range(3) if f!=j]
                h=False
                for e in A:
                    for a in range(3):
                        if y in H[i][n][e][a]:
                            h=True
            if h==False:
                A=[ f for f in range(3) if f!=n]
                for e in A:
                    for a in range(3):
                        if y in H[i][e][j][a]:
                            H[i][e][j][a]=[f for f in H[i][e][j][a] if f!=y]
    return H
def colone1(H,i,j,n):
    for y in range(1,10):
        h=False
        for a in range(3):
            if y in H[i][n][a][j]:
                h=True
        if h==True:
            for a in range(3):
                A=[f for f in range(3) if f!=j]
                h=False
                for a in range(3):
                    for e in A:
                        if  y in H[i][n][a][e]:
                            h=True
            if h==False:
                A=[f for f in range(3) if f!=i]
                for e in A:
                    for a in range(3):
                        H[e][n][a][j]=[f for f in H[e][n][a][j] if f!=y]
    return H
def rule4(H):
    for i in range(3):
        for j in range(3):
            for n in range(3):
               H=ligne1(H,i,j,n)
               H=colone1(H,i,j,n)
    return H

#------------------------la regle 4---------------------------------------------
def ligne2(H,i,j):
    for x in range(1,10):
        for y in range(x+1,10):
            A=[x,y]
            s=0
            for a in range(3):
                for b in range(3):
                    if A==H[i][a][j][b]:
                        s+=1
            if s>=2:
                for a in range(3):
                    for b in range(3):
                        if A!=H[i][a][j][b]:
                            H[i][a][j][b]=[ f for f in H[i][a][j][b] if f!=x and f!=y]
    return H
def colone2(H,i,j):
    for x in range(1,10):
        for y in range(x+1,10):
            A=[x,y]
            s=0
            for a in range(3):
                for b in range(3):
                    if A==H[a][i][b][j]:
                        s+=1
            if s>=2:
                for a in range(3):
                    for b in range(3):
                        if A!=H[a][i][b][j]:
                            H[a][i][b][j]=[ f for f in H[a][i][b][j] if f!=x and f!=y]
    return H
def rule6(H):
    for i in range(3):
        for j in range(3):
            H=ligne2(H,i,j)
            H=colone2(H,i,j)
    return H
#---------------------la regle 5------------------------------------------------
def colone3(H,i,j):
    for x in range(1,10):
        for y in range(x+1,10):
            for z in range(y+1,10):
                A=[x,y,z]
                s=0
                for a in range(3):
                    for b in range(3):
                        if A==H[a][i][b][j]:
                            s+=1
                if s>=3:
                    for a in range(3):
                        for b in range(3):
                            if A!=H[a][i][b][j]:
                                H[a][i][b][j]=[ f for f in H[a][i][b][j] if f!=x and f!=y and f!=z]
    return H
def ligne3(H,i,j):
    for x in range(1,10):
        for y in range(x+1,10):
            for z in range(y+1,10):
                A=[x,y,z]
                s=0
                for a in range(3):
                    for b in range(3):
                        if A==H[i][a][j][b]:
                            s+=1
                if s>=3:
                    for a in range(3):
                        for b in range(3):
                            if A!=H[i][a][j][b]:
                                H[i][a][j][b]=[ f for f in H[i][a][j][b] if f!=x and f!=y and f!=z]
    return H
def rule7(H):
    for i in range(3):
        for j in range(3):
            H=ligne3(H,i,j)
            H=colone3(H,i,j)
    return H
#----------------------la regle 6 ----------------------------------------------
def melinge1(H,i,j):
    for x in range(1,10):
        for y in range(x+1,10):
            s0,s1,s2=0,0,0
            for a in range(3):
                for b in range(3):
                    if y in H[i][a][j][b]:
                        s2+=1
                        if x in H[i][a][j][b]:
                            s0+=1
                    if x in H[i][a][j][b]:
                        s1+=1
            if s0==2 and s1==2 and s2==2:
                for a in range(3):
                    for b in range(3):
                        if x and y in H[i][a][j][b]:
                            H[i][a][j][b]=[x,y]
    return H
def melinge2(H,i,j):
    for x in range(1,10):
        for y in range(x+1,10):
            s0,s1,s2=0,0,0
            for a in range(3):
                for b in range(3):
                    if x in H[a][i][b][j]:
                        s1+=1
                        if y in H[a][i][b][j]:
                            s0+=1
                    if y in H[a][i][b][j]:
                        s2+=1
            if s0==2 and s1==2 and s2==2:
                for a in range(3):
                    for b in range(3):
                        if x and y in H[a][i][b][j]:
                            H[a][i][b][j]=[x,y]
    return H
def rule8(H):
    for i in range(3):
        for j in range(3):
            H=melinge1(H,i,j)
            H=melinge2(H,i,j)
    return H
#-----------------the program compelt-------------------------------------------
def comllite1(L,i,j):
    a=True
    A=[]
    for a in range(3):
        for b in range(3):
            if L[i][j][a][b] not in A:
                A+=[L[i][j][a][b]]
    if len(A)!=9:
        a=False
    return a
def comllite2(L,i,j):
    a=True
    A=[]
    for a in range(3):
        for b in range(3):
            if L[a][i][b][j] not in A:
                A+=[L[a][i][b][j]]
    if len(A)!=9:
        a=False
    return a
def morcom(L,i,j):
    a=True
    A=[]
    for a in range(3):
        for b in range(3):
            if L[i][j][a][b] not in A:
                A+=[L[i][j][a][b]]
    if len(A)!=9:
        a=False
    return a
def test(L):
    a=True
    for i in range(3):
        for j in range(3):
            if comllite1(L,i,j)==False or comllite2(L,i,j)==False or morcom(L,i,j)==False:
                a=False
                break
    return a
def sodoku(L,H):
    for i in range(10):
        L=rule2(L,H)
        H=rule1(L)
    if test(L)==False:
        for i in range(10):
            L=rule2(L,rule1(L))
            L=rule3(L)
        if test(L)==False:
            for i in range(10):
                H=rule4(rule1(L))
                L=rule2(L,H)
            if test(L)==False:
                for i in range(10):
                    H=rule6(rule4(rule1(L)))
                    L=rule2(L,H)
                if test(L)==False:
                    for i in range(10):
                        H=rule7(rule6(rule4(rule1(L))))
                        L=rule2(L,H)
                    if test(L)==False:
                        for i in range(10):
                            H=rule8(rule7(rule6(rule4(rule1(L)))))

    return L
def shaire(H):
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if len(H[a][b][c][d])==2:
                        return H[a][b][c][d]
                        break
def shaire1(H):
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    if len(H[a][b][c][d])==2:
                        return a,b,c,d
                        break
def lastplan(L):
    L=sodoku(L,rule1(L))
    H=rule8(rule7(rule6(rule4(rule1(L)))))
    if test(L)==False:
        for i in shaire(H):
            e1,e2,e3,e4=shaire1(H)
            H[e1][e2][e3][e4]=[i]
            A=L
            L=sodoku(L,H)
            if test(L)==True:
                break
    return L
def sodokufinale(L):
    L=sodoku(L,rule1(L))
    for i in range(10):
        if test(L)==False:
            L=lastplan(L)
    return L
#-----------------chow sodoku---------------------------------------------------
def sochow(A):
    return ' | '+str(A[0])+' '+str(A[1])+' '+str(A[2])
def allchow(L):
    print('---------------------------')
    for i in range(3):
        print(sochow(L[i][0][0])+sochow(L[i][1][0])+sochow(L[i][2][0])+' |')
        print(sochow(L[i][0][1])+sochow(L[i][1][1])+sochow(L[i][2][1])+' |')
        print(sochow(L[i][0][2])+sochow(L[i][1][2])+sochow(L[i][2][2])+' |')
        print('---------------------------')
#--------------------------------------examples de sodok------------------------

L=[[[[7, 0, 0], [0, 0, 3], [1, 0, 8]], [[0, 0, 0], [0, 4, 0], [5, 0, 0]], [[0, 0, 0], [0, 0, 2], [0, 0, 0]]], [[[0, 0, 1], [0, 0, 0], [6, 9, 7]], [[0, 0, 9], [6, 0, 8], [4, 0, 0]], [[5, 6, 4], [0, 0, 0], [8, 0, 0]]], [[[0, 0, 0], [3, 0, 0], [0, 0, 0]], [[0, 0, 2], [0, 7, 0], [0, 0, 0]], [[6, 0, 9], [1, 0, 0], [0, 0, 5]]]]
L=[[[[0, 0, 1], [6, 3, 0], [0, 7, 5]], [[0, 0, 8], [0, 0, 0], [0, 0, 0]], [[4, 0, 0], [0, 7, 8], [2, 0, 9]]], [[[0, 0, 0], [0, 8, 0], [0, 2, 0]], [[0, 0, 0], [3, 5, 0], [6, 9, 0]], [[0, 0, 0], [0, 0, 4], [0, 0, 5]]], [[[0, 5, 2], [0, 0, 8], [1, 6, 0]], [[0, 0, 0], [0, 0, 7], [0, 0, 0]], [[3, 0, 1], [6, 0, 0], [0, 4, 7]]]]