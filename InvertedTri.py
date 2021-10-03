def invertedTri(row):
    k = 2 * row - 2
    for i in range(row, -1, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k = k + 1
        for j in range(0, i + 1):
            print("*", end=" ")
        print("")


row = 9
invertedTri(row)
