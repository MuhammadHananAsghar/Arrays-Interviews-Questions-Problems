# Sort even in ascending order and Odd in descending order
arr = [1, 2, 3, 5, 4, 7, 10]
size = len(arr)

odd = []
even = []

for i in range(size):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])

arr = sorted(odd, reverse=True)+sorted(even)
print(arr)