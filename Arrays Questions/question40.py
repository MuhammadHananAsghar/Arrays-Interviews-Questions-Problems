# Find the largest pair sum in the unsorted array
arr = [12, 34, 10, 6, 40]
size = len(arr)

def getIndex(num, arr):
    for index, item in enumerate(arr):
        if item == num:
            return index
    return None

firstMax = max(arr)
arr.pop(getIndex(firstMax, arr))
secondMax = max(arr)
sum = firstMax + secondMax
print(f"Largest pairs are {firstMax} and {secondMax} having sum {sum}.")
