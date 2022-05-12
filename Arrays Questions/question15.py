# a[] with sum x

arr = [1, 4, 45, 6, 10, -8]
size = len(arr)
x = 37

for i in range(size):
    for j in range(i+1, size):
        if (arr[i]+arr[j]) == x:
            print(f"Pairs found [{arr[i]}, {arr[j]}].")
            break