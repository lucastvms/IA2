#########################################LETRA

def isL(L):
    isL=0
    if(L[0][0] and L[1][0] and L[2][0]  and L[3][0] and L[3][1] and L[3][2] and L[3][3]):
        isL = 1
    return isL

def isnL(L):
    isnL=0
    if (L[0][1] or L[0][2] or L[0][3] or L[1][1] or L[1][2] or L[1][3] or L[2][1] or L[2][2] or L[2][3] ):
        isnL = 1
    return isnL

L = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,1]]

C = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,1,1,1]]

I = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]

print("\nC")
for i in range(0, 4):
    print(C[i])

print("\nL")
for i in range(0,4):
    print(L[i])

print("\nI")
for i in range(0, 4):
    print(I[i])

print("\n")

char = C
if isL(char) and not(isnL(char)):
    print("it's a L")
else:
    print("it's not a L")

char = L
if isL(char) and not(isnL(char)):
    print("it's a L")
else:
    print("it's not a L")

char = I
if isL(char) and not(isnL(char)):
    print("it's a L")
else:
    print("it's not a L")
