# Closet pair from two sorted arrays
import sys

arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
value = 50

closest = sys.maxsize
numOne, numTwo = 0, 0

for x in arr1:
    for y in arr2:
        sum = abs(x + y)
        diff = abs(value - sum)
        if diff < closest:
            closest = diff
            numOne, numTwo = x, y

print(numOne, numTwo, closest)