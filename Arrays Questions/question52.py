# Sort an array in waveform

arr = [3, 6, 5, 10, 7, 20]
size = len(arr)
sortedArr = sorted(arr)
tempArr = sortedArr.copy()

for i in range(0, size-1, 2):
    temp = sortedArr[i]
    sortedArr[i] = sortedArr[i+1]
    sortedArr[i+1] = temp

print(tempArr, sortedArr)
