# The Odd Appearing element
arr = [1, 1, 2, 2, 1, 1, 2, 2, 13, 1, 1, 40, 40, 13, 13]
size = len(arr)


frequencies = dict()
for i in range(size):
    if arr[i] not in frequencies:
        frequencies[arr[i]] = 1
    else:
        frequencies[arr[i]] += 1

sortData = sorted(frequencies.items(), reverse=True, key=lambda x: x[1])
odd = 0
for data in sortData:
    if data[1] % 2 != 0:
       odd = data[1] 
print(odd)