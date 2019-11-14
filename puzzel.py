def isgoal(a,b):
    for i in range(3):
        for j in range(3):
            if a[i][j]!=b[i][j]:
                return False
    return True

def swap(a,b):
    return(b,a)

def h(a,b):
    cost=0
    for i in range(3):
        for j in range(3):
            if a[i][j]!=b[i][j] and a[i][j]!=0:
                cost+=1
    return cost

def printmat(a):
    for i in range(3):
        for j in range(3):
            print(a[i][j],end=" ")
        print()

def copymat(a):
    c=[[0 for i in range(3)]for j in range(3)]
    for i in range(3):
        for j in range(3):
            c[i][j]=a[i][j]
    return c


def astar(a,b,g,bi,bj):
    if isgoal(a,b):
        print("Done")
        return
    
    au=[]
    ad=[]
    al=[]
    ar=[]
    moves={"up":-1,"down":-1,"left":-1,"right":-1}
    g+=1
    if bi+1<3: #down
        ad=copymat(a)
        ad[bi][bj],ad[bi+1][bj]=swap(ad[bi][bj],ad[bi+1][bj])
        moves["down"]=g+h(ad,b)
    if bi-1>=0:#up
        au=copymat(a)
        au[bi][bj],au[bi-1][bj]=swap(au[bi][bj],au[bi-1][bj])
        moves["up"]=g+h(au,b)
    if bj+1<3:#right
        ar=copymat(a)
        ar[bi][bj],ar[bi][bj+1]=swap( ar[bi][bj],ar[bi][bj+1])
        moves["right"]=g+h(ar,b)
    if bj-1>0:#left
        al=copymat(a)
        al[bi][bj],al[bi][bj-1]=swap(al[bi][bj],al[bi][bj-1])
        moves["left"]=g+h(al,b)
    min=10**9
    nextmove=""
    for m in moves:
        if moves[m]>-1 and moves[m]<min:
            nextmove=m
            min=moves[m]
    next=[]
    if nextmove=="up":
        next=au
        bi-=1
        bj=bj
    if nextmove=="down":
        next=ad
        bi+=1
        bj=bj
    if nextmove=="right":
        next=ar
        bj+=1
    if nextmove=="left":
        next=al
        bj-=1
    print("next move and cost function")
    printmat(next)
    print(nextmove,moves[nextmove])
    astar(next,b,g,bi,bj)
    
############################################ Driver code    ###################################################################################
a=[[0 for i in range(3)]for j in range(3)]
bi=0
bj=0
print("Enter initial state:")
for i in range(3):
    x=list(map(int,input().split()))
    for j in range(3):
        a[i][j]=x[j]
        if a[i][j]==0:
            bi=i
            bj=j

b=[[0 for i in range(3)]for j in range(3)]
print("Enter Goal state:")
for i in range(3):
    x=list(map(int,input().split()))
    for j in range(3):
        b[i][j]=x[j]
printmat(b)
astar(a,b,0,bi,bj)
