# Number of Occurences in the sorted array
# [1, 1, 2, 2, 2, 2, 3], x = 2
arr = [1, 1, 2, 2, 2, 2, 3]
size = len(arr)
x = 1


frequencies = {}
for i in range(size):
    if arr[i] not in frequencies:
        frequencies[arr[i]] = 1
    else:
        frequencies[arr[i]] += 1
occurs = 0
for item in frequencies.items():
    if item[0] == x:
        occurs = item[1]

print(f"Number {x} occurs {occurs} times.")