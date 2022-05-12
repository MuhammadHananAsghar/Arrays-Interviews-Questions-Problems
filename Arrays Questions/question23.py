import sys

# Two elements whose sum in closet to zero
arr = [1, 60, -10, 70, -80, 85]
size = len(arr)
minDist = sys.maxsize
numOne, numTwo = 0, 0

for i in range(size):
    for j in range(i+1, size):
        sum = abs(arr[i] + arr[j])

        if sum < minDist:
            minDist = sum
            numOne, numTwo = arr[i], arr[j]


print(f"Minimum sum is {minDist} which is between {numOne} and {numTwo}.")
