li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
i = 0
sum = 0
sum1 = 1
i = 0
while True:
    sum = li[i]
    if sum1 < sum:
        print(li[i])
        break
    else:
        sum1 += i
        i += 1

