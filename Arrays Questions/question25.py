arr = [6, 1, 4, 3, 1, 7]
size = len(arr)


ix = 0
jx = size - 1
minSteps = 0

while ix < jx:
    if arr[ix] == arr[jx]:
        print(f"Left {arr[ix]} and right {arr[jx]} elements are same.")
        print(f"Array: {arr}")
        ix += 1
        jx -= 1
    elif arr[ix] > arr[jx]:
        jx -= 1
        arr[jx] += arr[jx+1]
        print(f"Left {arr[ix]} is greater then right {arr[jx]}.")
        print(f"Merging:{arr[jx]} and {arr[jx+1]}, Array: {arr}")
        minSteps += 1
    else:
        ix += 1
        arr[ix] += arr[ix-1]
        print(f"Left {arr[ix]} is less then right {arr[jx]}.")
        print(f"Merging:{arr[ix]} and {arr[ix-1]}, Array: {arr}")
        minSteps += 1

