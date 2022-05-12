# Find a pair with given difference
arr = [5, 20, 3, 2, 50, 80]
size = len(arr)
n = 78
numOne, numTwo = 0, 0

for i in range(size-1):
    for j in range(i+1, size):
        diff = abs(arr[i] - arr[j])
        if diff == n:
            numOne, numTwo = arr[i], arr[j]

print(f"Number found with the difference of {numOne} and {numTwo}")