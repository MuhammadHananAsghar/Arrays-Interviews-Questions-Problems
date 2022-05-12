# Print all distinct elements of a given array
arr = [1, 2, 3, 3, 4, 5, 5]
size = len(arr)
freq = {}
single = True
distinctElements = []

for i in range(size):
    if arr[i] not in freq:
        freq[arr[i]] = 1
    else:
        freq[arr[i]] += 1

for key, value in freq.items():
    if value == 1:
        distinctElements.append(key)

print("Distinct Elements are___")
for item in distinctElements:
    print(item, end=" ")
print()