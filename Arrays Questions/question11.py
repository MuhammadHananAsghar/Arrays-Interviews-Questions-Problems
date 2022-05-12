# Find a Peak Elements
# [5, 10, 20, 15]
arr = [10, 20, 15, 2, 23, 90, 67]
size = len(arr)
peakElems = set()


for i in range(1, size-1):
    if (arr[i] > arr[i-1]) and (arr[i] > arr[i+1]):
        peakElems.add(arr[i])

print("Peak Elements in the array are: {}".format(peakElems))