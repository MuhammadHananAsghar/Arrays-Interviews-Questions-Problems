# Find the missing element in the array
arr = [1, 2, 3, 4, 5, 6, 7, 9]
size = len(arr)
total = int((size + 1) * (size + 2) / 2)

for i in range(size):
    total -= arr[i]
print("Missing element is {}. ".format(total))