# Search and element in a sorted and rotated array
def getPivot(arr):
    index, value = 0,0
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            pass
        else:
            index, value = i, arr[i]
            break
    return index, value

def binarySearch(keyValue, mLst):
    low = 0
    high = len(mLst)-1
    while low <= high:
        mid = low + (high - low) // 2
        if keyValue == mLst[mid]:
            return mid
        elif keyValue > mLst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [3, 4, 5, 1, 2]
pivotIndex, _ = getPivot(arr)
leftArray = arr[:pivotIndex+1]
rightArray = arr[pivotIndex+1:]
element = 1
indexValue = 0

if element > arr[0]:
    indexValue = binarySearch(element, leftArray)
    print(f"Element {element} is found at {indexValue} index in Left Array {leftArray}.")
else:
    indexValue = binarySearch(element, rightArray)
    print(f"Element {element} is found at {indexValue} index in Right Array {rightArray}.")
