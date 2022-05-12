# Majority Element in array

arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
size = len(arr)
half = size // 2
majorityElem = None

for i in range(size):
    nTimes = 0
    for j in range(i, size):
        if arr[i] == arr[j]:
            nTimes += 1
    
    if nTimes > half:
        majorityElem = arr[i]

print(f"Majority Element is: {majorityElem}")