# Find Fixed Point in the array
# [-10, -5, 0, 3, 7]
arr = [-10, -5, 3, 4, 7, 9]
size = len(arr)
fixedPoint = -1

for i in range(size):
    if i == arr[i]:
        fixedPoint = i

print(f"Fixed point in this array is: {fixedPoint}")