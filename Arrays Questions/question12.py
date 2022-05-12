# Count Strictly Increasing Subarrays
# [1, 4, 3]
# [1, 2, 3, 4]
arr = [1, 2, 2, 4]
size = len(arr)
subArrays = list()

def checkArrayisStrictlyIncreasing(arr):
    cnt = False
    for index in range(len(arr)-1):
        if arr[index] < arr[index+1]:
            cnt = True
        else:
            cnt = False
            break
    return cnt

for i in range(size):
    for j in range(i, size+1):
        sliced = arr[i:j]
        sliced_length = len(sliced)
        if sliced_length > 1:
            if checkArrayisStrictlyIncreasing(sliced):
                subArrays.append(sliced)

print(f"Strictly Increasing Subarrays are {subArrays}.")
