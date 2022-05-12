# Sum of array elements using recursion
arr = [15, 12, 13, 10]
size = len(arr)

def recurrSum(arr, n):
    if n == 0:
        return 0

    return (recurrSum(arr, n-1)+arr[n-1])

print(recurrSum(arr, size))