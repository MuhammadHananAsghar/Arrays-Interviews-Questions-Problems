# Replace every element to the greatest element of right side
# [16, 17, 4, 3, 5, 2]
arr = [14, 20, 12, 15, 8, 9, 1, 2, 1]
size = len(arr)
temp = arr.copy()

for i in range(size):
    for j in range(i, size):
        if arr[j] > arr[i]:
            arr[i] = arr[j]

    if i == (size-1):
        arr.pop(0)
        arr.append(-1)
    
print(f"Modified array of {temp} is {arr}.")