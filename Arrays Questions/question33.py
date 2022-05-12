# triplets with sum less than x
arr = [5, 1, 3, 4, 7]
size = len(arr)
x = 12
triplets = []

for i in range(size - 1):
    for j in range(i+1, size):
        for k in range(j+1, size):
            sum = abs(arr[i]+arr[j]+arr[k])
            if x > sum:
                triplets.append([arr[i], arr[j], arr[k]])


print(triplets, len(triplets))
