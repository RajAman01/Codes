a = int(input("Enter the start Value:"))
b = int(input("Enter the end value"))
while (a < b):
    flag = 0
    for i in range(2, int(a / 2), 1):
        if (a % i == 0):
            flag = 1
            break
    if flag == 0:
        print(a, end=" ")
    a = a + 1

        