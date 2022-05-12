# Third Largest Element in the array
arr = [1, 14, 2, 16, 10, 20]
size = len(arr)

def getIndex(value, arr):
    for index, item in enumerate(arr):
        if item == value:
            return index
    return -1

arr.pop(getIndex(max(arr), arr))
arr.pop(getIndex(max(arr), arr))
thirdMax = max(arr)
print(thirdMax)