def selectionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1]= arr[j]
            j-=1
            arr[j+1] = key
    return arr
arr = [1,3,5,2,6,9,11,7]
print(selectionSort(arr))
def insertionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
                arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=j=k=0
        while i < len(L) and j < len(R):
            if (L[i]<R[j]):
                arr[k] = L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        while i <len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k]=R[j]
            j+=1
            k+=1
        return arr

arr = [1,3,5,2,6,9,11,7]
print(mergeSort(arr),"this is my ans")