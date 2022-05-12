# Minimum element in the sorted and rotated array
import sys

arr = [5, 6, 1, 2, 3, 4]
size = len(arr)
minElem = sys.maxsize

for i in range(size):
    if arr[i] < minElem:
        minElem = arr[i]

print(f"{minElem} is minimum element in {arr}.")