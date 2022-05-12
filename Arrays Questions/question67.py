# Subarray with given sum
arr = [1, 4, 20, 3, 10, 5]
size = len(arr)
gsum = 33
idx, jdx = 0, 0

for i in range(size-1):
    for j in range(i+1, size):
        sliced = arr[i:j]
        if gsum == sum(sliced):
            idx, jdx = i, j
            break

print(f"Given sum value {gsum} equal to the subarray between {idx} and {jdx-1}.")