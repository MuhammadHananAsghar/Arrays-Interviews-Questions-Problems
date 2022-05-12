# Find sum with given subarray (Handling Negative)
arr = [10, 2, -2, -20, 10]
size = len(arr)
gsum = -10
idx, jdx = 0, 0

for i in range(size-1):
    for j in range(i+1, size):
        sliced = arr[i:j]
        if gsum == sum(sliced):
            idx, jdx = i, j
            break

print(f"Given sum value {gsum} equal to the subarray between {idx} and {jdx-1}.")