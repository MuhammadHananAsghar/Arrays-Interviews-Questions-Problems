# Cyclically rotate an array by one
arr = [1, 2, 3, 4, 5]
size = len(arr)

temp = []
last = arr[size-1]
temp.append(last)
for i in range(size-1):
    temp.append(arr[i])

print(temp)