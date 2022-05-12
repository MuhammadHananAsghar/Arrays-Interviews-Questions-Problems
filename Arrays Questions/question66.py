# Find the element that appears once
arr = [7, 3, 5, 4, 5, 3, 4]
size = len(arr)
freq = {}
single = True

for i in range(size):
    if arr[i] not in freq:
        freq[arr[i]] = 1
    else:
        freq[arr[i]] += 1

for key, value in freq.items():
    if value == 1:
        single = True
        break
    else:
        single = False

if single:
    print(f"{key} appears once in array.")
else:
    print("Nothing appears once.")