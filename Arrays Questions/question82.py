# Find largest no that is not perfect square
import math

arr = [16, 20, 25, 2, 3, 10]
size = len(arr)
maxnum = 0

for i in range(size):
    root = math.sqrt(arr[i])
    if int(root + 0.5) ** 2 != arr[i]:
        if arr[i] > maxnum:
            maxnum = arr[i]

print(f"{maxnum} is the largest not perfect square element in the array.")