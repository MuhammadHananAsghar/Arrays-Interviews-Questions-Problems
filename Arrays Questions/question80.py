# Find a element such that all elements are divisble by it
arr = [25, 20, 5, 10, 100]
size = len(arr)

def divisbility(arr, value):
    divisible = False
    for i in range(len(arr)):
        if (arr[i] % value) == 0:
            divisible = True
        else:
            divisible = False
            break
    return divisible

for i in range(size):
    check = divisbility(arr, arr[i])
    if check:
        print(f"{arr[i]} is complete divisible.")
        break
    