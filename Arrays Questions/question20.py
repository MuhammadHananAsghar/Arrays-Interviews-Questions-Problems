import sys

# Minimum distance between any two elements
# [1, 5, 3, 19, 18, 25]
# [30, 5, 20, 9]
arr = [1, 19, -4, 31, 38, 25, 100]
size = len(arr)
numOne, numTwo = 0, 0
minDist = sys.maxsize

for i in range(size):
    for j in range(i+1, size):
        diff = abs(arr[i] - arr[j])
        if diff < minDist:
            minDist = diff
            numOne, numTwo = arr[i], arr[j]

print(f"""Input: {arr}
Output: {minDist}
Minimum difference is between {numOne} and {numTwo}.""")