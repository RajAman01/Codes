# You are given a sorted array containing both negative and positive values.
# Resort the array taking absolute value of negative numbers.
# Your complexity should be O(n)

def rreArrange(arr, n):
    i = -1
    for j in range(n):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    pos, neg = i + 1, 0

    while n > pos > neg and arr[neg] < 0:
        arr[neg], arr[pos] = arr[pos], arr[neg]
        pos += 1
        neg += 2
    return arr


def printArr(arr, n):
    for i in range(n):
        print(arr[i])


arr = [-8, -5, -3, -1, 3, 6, 9]
print(rreArrange(arr, len(arr)))
print(printArr(arr, len(arr)))
