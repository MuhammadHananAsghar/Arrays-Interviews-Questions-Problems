# Triplets with sum is zero
arr = [0, -1, 2, -3, 1]
size = len(arr)

triplets = []
for i in range(size-1):
    for j in range(i+1, size):
        for k in range(j+1, size):
            if abs(arr[i]+arr[j]+arr[k]) == 0:
                triplets.append([arr[i],arr[j],arr[k]])

print(f"Triplets are: {triplets}")