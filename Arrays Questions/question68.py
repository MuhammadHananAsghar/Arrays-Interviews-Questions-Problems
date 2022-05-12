# Merge an array of size of (n) to another array (m+n)
arr1 = [2, None, 7, None, None, 10, None]
arr2 = [5, 8, 12, 14]

idx = 0

for index, item in enumerate(arr1):
    if (item is None) and (idx < len(arr2)):
        arr1[index] = arr2[idx]
        idx += 1

print(arr1)