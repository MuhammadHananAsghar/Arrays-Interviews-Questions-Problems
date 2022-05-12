# Reversal Alghorithum
arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)
d = 2
temp = arr.copy()

def reverse(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


def rotate(arr, d):
    if d == 0:
        return
    n = len(arr)
    d = d % n

    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)


rotate(arr, d)
print(temp, arr)