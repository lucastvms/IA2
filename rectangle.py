#find the limits able for research of our matrix
#defines which row and column to search between 0x5, because our search goes from min to max-1
def Limits(R):
    if R["row"]-1 >= 0:
        i1=R["row"]-1
    else:
        i1=0
    if R["row"]+R["r"]+1 <= 5:
        i2=R["row"]+R["r"]+1
    else:
        i2=5

    if R["col"]-1 >= 0:
        j1=R["col"]-1
    else:
        j1=0
    if R["col"]+R["c"]+1 <= 5:
        j2=R["col"]+R["c"]+1
    else:
        j2=5

    return {"minR": i1, "maxR": i2, "minC": j1, "maxC": j2}

#finds a rectangle 1x2, gives it the first position as a parameter for NotR
def oneXtwo(A):
    sum=0
    for j in range(0,5):
        for i in range(0,5):
            if A[i][j]==1 and j+1<=4:
                if A[i][j+1]:
                    R={"row": i, "col": j, "r": 1, "c": 2}
                    #print(R)
                    sum+=NotR(A,R,2)
    #print ("aqui", sum)
    return sum

#finds a rectangle 2x3, gives it the first position as a parameter for NotR
def twoXthree(A):
    sum=0
    for j in range(0,5):
        for i in range(0,5):
            if A[i][j]==1 and i+1<=4 and j+2<=4:
                if A[i][j+1] and A[i][j+2] and A[i+1][j] and A[i+1][j+1] and A[i+1][j+2]:
                    R={"row": i, "col": j, "r": 2, "c": 3}
                    #print(R)
                    sum+=NotR(A,R,6)
    #print ("aqui", sum)
    return sum

#finds a rectangle 3x4, gives it the first position as a parameter for NotR
def threeXfour(A):
    sum=0
    for j in range(0,5):
        for i in range(0,5):
            if A[i][j]==1 and i+2<=4 and j+3<=4:
                if A[i][j+1] and A[i][j+2] and A[i][j+3] and A[i+1][j] and A[i+1][j+1] and A[i+1][j+2] and A[i+1][j+3]\
                        and A[i+2][j] and A[i+2][j+1] and A[i+2][j+2] and A[i+2][j+3]:
                    R={"row": i, "col": j, "r": 3, "c": 4}
                    #print(R)
                    sum+=NotR(A,R,12)
    #print ("aqui", sum)
    return sum

#finds if it's not a rectangle: Matrix, First position and size of the rectangle, Occupied positions
def NotR(A, R, S):
    L=Limits(R)
    #print(L)
    sum=0
    for j in range(L["minC"],L["maxC"]):
        for i in range(L["minR"],L["maxR"]):
            #print(i,j,A[i][j])
            sum+=A[i][j]
    #print("aqui2:",sum)

    if(sum==S):
        return 1
    else:
        return 0


#main
A=[[1,1,1,1,0],
   [1,1,1,1,0],
   [1,1,1,1,0],
   [0,0,0,0,0],
   [1,0,1,1,0]]

print("\nMatrix A")
print("Possui",oneXtwo(A), "retângulo 1x2")
print("Possui",twoXthree(A), "retângulo 2x3")
print("Possui",threeXfour(A), "retângulo 3x4")


B=[[1,1,1,0,0],
   [1,1,1,0,0],
   [0,0,0,0,0],
   [1,1,0,0,0],
   [0,0,0,1,1]]

print("\nMatrix B")
print("Possui",oneXtwo(B), "retângulo 1x2")
print("Possui",twoXthree(B), "retângulo 2x3")
print("Possui",threeXfour(B), "retângulo 3x4")


C=[[1,1,1,1,1],
   [1,0,1,1,1],
   [1,1,0,0,0],
   [0,0,1,1,1],
   [1,0,1,1,1]]

print("\nMatrix C")
print("Possui",oneXtwo(C), "retângulo 1x2")
print("Possui",twoXthree(C), "retângulo 2x3")
print("Possui",threeXfour(C), "retângulo 3x4")

#print(A[1][1:3])
