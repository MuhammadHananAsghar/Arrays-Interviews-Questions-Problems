# Triplet that sum to a given value
arr = [12, 3, 4, 1, 6, 9]
size = len(arr)
sum = 24


triplets = []
for i in range(size-1):
    for j in range(i+1, size):
        for k in range(j+1, size):
            if abs(arr[i]+arr[j]+arr[k]) == sum:
                triplets.append([arr[i],arr[j],arr[k]])

print(f"Triplets are: {triplets}")