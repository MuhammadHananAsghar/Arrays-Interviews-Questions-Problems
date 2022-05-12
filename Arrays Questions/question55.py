# Smallest and Second smallest element in the array
from cgitb import small
import sys

arr = [12, 13, 1, 10, 34, 1]
size = len(arr)

def getMinElem(arr):
    size = len(arr)
    smallest = sys.maxsize
    for i in range(size-1):
        if arr[i+1] > arr[i]:
            if arr[i] < smallest:
                smallest = arr[i]
    return smallest

def nullElem(arr, x, size):
    for i in range(size):
        if arr[i] == x:
            arr[i] = None

    arr = [elem for elem in arr if elem is not None]
    return arr

firstSmallest = getMinElem(arr)
tempArr = nullElem(arr, firstSmallest, size)
secondSmallest = getMinElem(tempArr)

print(f"First smallest element is {firstSmallest} and second smallest element is {secondSmallest}.")
