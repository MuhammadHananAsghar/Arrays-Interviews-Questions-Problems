# Minimum distance between two numbers

x, y  = 3, 6
arr = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
distance = max(arr)

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if (x == arr[i] and y == arr[j]) or (y == arr[i] and x == arr[j]):
            if distance > abs(i-j):
                distance = abs(i-j)


print("Minimum distance between {} and {} is {}.".format(x, y, distance))