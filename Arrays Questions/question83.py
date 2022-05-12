# Minimum swaps required to sort binary array
arr = [0, 0, 1, 0, 1, 0, 1, 1]
size = len(arr)
swaps = 0

i = 0
while 1:
    if (arr[i] == 1) and (arr[i+1] == 0) and (i < size-1):
        # print(arr[i], arr[i+1])
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        i = 0
        swaps += 1
        # print(arr)
    i += 1
    if i == size-1:
        break

print(f"{swaps} swaps required to swap {arr}.")