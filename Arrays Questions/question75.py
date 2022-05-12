# First repeating element in the array
arr = [10, 5, 3, 4, 3, 5, 6]
size = len(arr)

freq = {}
for i in range(size):
    if arr[i] not in freq:
        freq[arr[i]] = 1
    else:
        freq[arr[i]] += 1

for key, value in freq.items():
    if value == 2:
        print(f"{key} is the first repeating element.")
        break