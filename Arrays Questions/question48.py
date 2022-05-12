# Minimum subarray to which to which we sort to make full array sort
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
size = len(arr)

start = None
for i in range(size-1):
    if arr[i+1] < arr[i]:
        start = [arr[i], i]
        break

end = None
for j in range(size-1, -1, -1):
    if arr[j-1] > arr[j]:
        end = [arr[j], j]
        break

print(f"Sort subarray from {start[1]} to {end[1]} indexes.")