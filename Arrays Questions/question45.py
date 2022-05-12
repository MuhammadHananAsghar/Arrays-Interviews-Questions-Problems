arr = [5, 6, 7, 8, 9, 10]
size = len(arr)
key = 9


def binarySearch(arr,  low, high, key):
    mid =  (low + high) // 2
    if (high < low):
        return -1
    
    if (key == arr[mid]):
        return mid
    
    if (key < arr[mid]):
        return binarySearch(arr, low, (mid-1), key)
    return binarySearch(arr, (mid+1), high, key)

print(binarySearch(arr, 0, size-1, key))