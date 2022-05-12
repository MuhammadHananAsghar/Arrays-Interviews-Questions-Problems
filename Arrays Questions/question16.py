# Print missing elements that lie in range 0-99
arr = [88, 105, 3, 2, 200, 0, 10]
size = len(arr)
boolArray = [False for _ in range(100)]

for item in arr:
    if (item >= 0) and (item <= 99):
        boolArray[item] = True

boolArraySize = len(boolArray)
ix = 0
while (ix < boolArraySize):
    if boolArray[ix] == False:
        jx = ix + 1
        while (jx < boolArraySize) and (boolArray[jx] == False):
            jx += 1
        if ix+1 == jx:
            print(f"{ix}")
        else:
            print(f"{ix}-{jx-1}")
        ix = jx
    else:
        ix += 1