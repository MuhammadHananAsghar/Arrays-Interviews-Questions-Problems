# Pythagorean Triplet
# [3, 1, 4, 6, 5]
arr = [3, 1, 4, 6, 5]
size = len(arr)
tripletFound = False

for i in range(size):
    for j in range(i+1, size):
        for k in range(j+1, size):
            a, b, c = arr[i]**2, arr[j]**2, arr[k]**2
            if (a == b + c) or (b == a + c) or (c == a + b):
                print("Pythagoreous Triplet is: {}".format([arr[i], arr[j], arr[k]]))
