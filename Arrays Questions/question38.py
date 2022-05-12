# Maximum Product in array of integers
arr = [1, 4, 3, 7, 6, 0]
size = len(arr)
maxProd, numOne, numTwo = 0, 0, 0

for i in range(size-1):
    for j in range(i+1, size):
        prod = abs(arr[i]*arr[j])

        if prod > maxProd:
            maxProd = prod
            numOne, numTwo = arr[i], arr[j]


print(f"Maximum product is {maxProd} of {numOne} and {numTwo}.")