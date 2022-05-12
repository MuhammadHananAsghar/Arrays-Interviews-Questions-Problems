# Delete an element from the array
arr = [3, 1, 2, 5, 90]
size = len(arr)
x = 2


temp = []
for i in range(size):
    if arr[i] != x:
        temp.append(arr[i])

print("After Deletion: ", temp)