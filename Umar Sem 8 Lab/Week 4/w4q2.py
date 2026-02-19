def ascending_func(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def descending_func(arr):
    if len(arr) <=1: return arr
    pivot=arr[0]
    left=[x for x in arr[1:] if x>pivot]
    right=[x for x in arr[1:] if x<=pivot]
    return descending_func(left)+[pivot]+descending_func(right)

arr=[45,12,78,34,23,90,11]
ascending=ascending_func(arr.copy())
descending=descending_func(arr.copy())

print("Original List:",arr)
print("Ascending Order (Bubble Sort):",ascending)
print("Descending Order (Quick Sort):",descending)
