# Array Rotation
arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)
d = 2
temp = arr[:d]

for i in range(size):
    if i > d-1:
        index = abs(i-d)
        swap = arr[i]
        arr[index] = swap

arr = arr[:-2]+temp
print("After Rotation: ",arr)
