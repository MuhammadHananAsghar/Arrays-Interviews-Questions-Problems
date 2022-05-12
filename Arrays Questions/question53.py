# Search in an almost sorted array
arr = [10, 3, 40, 20, 50, 80, 70]
size = len(arr)
key = 40


def binarySearch(arr, key):
    low = 0
    high = size-1

    while (low <= high):
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        if (mid > 0) and (arr[mid - 1] == key):
            return (mid - 1)

        if (mid < size-1) and (arr[mid + 1] == key):
            return (mid + 1)

        if key > arr[mid]:
            low = mid + 2
        
        else:
            high = mid - 2
    
    return -1

print(binarySearch(arr, key))