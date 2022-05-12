# Array to Ziig-Zag Function

arr = [4, 3, 7, 8, 6, 2, 1] 
size = len(arr)
flag = True

for i in range(size-1):
    if flag:
        if arr[i] > arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
        
    else:
        if arr[i] < arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
    
    flag = bool(1 - flag)

    print(arr)


