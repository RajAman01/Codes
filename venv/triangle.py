row = 6
def revderseTri(row):
    k = 2*row - 2
    for i in range(0,row):
        for j in range(0,k):
            print(end=" ")
        k = k-2
        for j in range(0,i+1):
            print("* ",end="")
        print("")
#revderseTri(row)
def triangle(row):
    m = (2*row)-2
    for i in range(0,row):
        for j in range(0,m):
            print(end=" ")
        m = m - 1
        for j in range(0,i+1):
            print("* ",end="")
        print(" ")
triangle(row)