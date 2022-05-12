# Search in unsorted array
arr = [25, 65, 6, 24, 86, 34]
size = len(arr)
x = 24
foundFlag = 0

for i in range(size):
    if x == arr[i]:
        foundFlag = i
        break

print(f"Element {x} is found at the index of {foundFlag} in array {arr}.")