# Minimum Difference between two elements if larger element is after smaller element
arr = [2, 3, 10, 6, 4, 8, 1]
sortedArr = sorted(arr)
size = len(arr)
maxDiff = arr[1] - arr[0]
numOne, numTwo = 0, 0

for i in range(size):
    for j in range(i+1, size):
        diff = abs(sortedArr[j]-sortedArr[i])
        if diff > maxDiff:
            maxDiff = diff
            numOne, numTwo = sortedArr[j], sortedArr[i]



print(maxDiff, numOne, numTwo)

