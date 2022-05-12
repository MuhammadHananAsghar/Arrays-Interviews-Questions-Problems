# Equilibrium Index of an array
arr = [-7, 1, 5, 2, -4, 3, 0]
size = len(arr)

def sumOfList(arr):
    sum = 0
    for item in arr:
        sum += item
    return sum

equilibriumIndices = []

for i in range(size):
    if i > 0:
        curr_index = i
        previousElements = [arr[x] for x in range(curr_index)]
        nextElements = [arr[y] for y in range(curr_index+1, size)]
        
        if sumOfList(previousElements) == sumOfList(nextElements):
            equilibriumIndices.append(curr_index)

print(equilibriumIndices)