# Rotation Count in sorted array
import sys
arr = [15, 18, 2, 3, 6, 12]
size = len(arr)
mini = sys.maxsize
count = 0

for i in range(size):
    if arr[i] < mini:
        mini = arr[i]
        count = i

print(f"Minimum counts is {count}.")
