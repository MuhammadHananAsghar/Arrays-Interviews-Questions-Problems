# Find value if we doubles after every successful search in array
arr = [2, 4, 5, 6, 7]
size = len(arr)
k = 3

idx = 0
while 1:
    if arr[idx] == k:
        k = k * 2
        idx = 0

    idx += 1
    if idx == size-1:
        break
    

print(f"Value of K after all: {k}")