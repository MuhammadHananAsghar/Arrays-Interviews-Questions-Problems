# Find there a given sum in the sorted array
arr = [11, 15, 6, 8, 9, 10]
size = len(arr)
given_sum = 16

def checkSum(arr, size):
    for i in range(size-1):
        for j in range(i+1, size):
            sum = abs(arr[i] + arr[j])
            if sum == given_sum:
                return True
    return False

print(checkSum(arr, size))