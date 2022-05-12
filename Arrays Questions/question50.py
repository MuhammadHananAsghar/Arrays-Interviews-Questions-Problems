# pair whose sum is closet to x
import sys

arr = [10, 22, 28, 29, 30, 40]
size = len(arr)
x = 54

closest = sys.maxsize
numOne, numTwo = 0, 0
for i in range(size-1):
    for j in range(i+1, size):
        sum = abs(arr[i] + arr[j])
        diff = abs(sum - x)
        if diff < closest:
            closest = diff
            numOne, numTwo = arr[i], arr[j]

print(f"Sum of pair {numOne} and {numTwo} is closet to value {x}.")