# Find subarray with sum is zero
arr = [-3, 2, 3, 1, 6]
size = len(arr)
present = False

for i in range(size-1):
    for j in range(i+1, size):
        sliced = arr[i:j]
        if sum(sliced) == 0:
            present = True
            break
        else:
            present = False

if present:
    print("Subarray found with zero sum.")
else:
    print("Subarray not found with zero sum.")