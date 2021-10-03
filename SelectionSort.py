A = [64, 89, 100, 20, 1]


def SelectionSort(A):
    for i in range(len(A)):
        min_index = i
        for j in range(i + 1, len(A)):
            if A[min_index] > A[j]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A


print(SelectionSort(A))
def select(arr):
    for i in range(len(arr)):
        mid_index = i
        for j in range(i+1,len(arr)):
            if arr[mid_index]>arr[j]:
                mid_index=j
            arr[j],arr[mid_index]=arr[mid_index],arr[j]
            return arr
