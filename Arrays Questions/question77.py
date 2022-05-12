# Increasing subsequence of three with maximum product
arr = [6, 7, 8, 1, 2, 3, 9, 10]
size = len(arr)
maxProd = 0
maxSeq = None

def checkAscending(arr):
    check = False
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            check = True
        else:
            check = False
            break
    return check

for i in range(size-1):
    for j in range(i+1, size):
        for k in range(j+1, size):
            prod = arr[i]*arr[j]*arr[k]
            checkSeq = checkAscending([arr[i], arr[j], arr[k]])
            if checkSeq and (prod > maxProd):
                maxProd = prod
                maxSeq = [arr[i], arr[j], arr[k]]
                print(checkAscending([arr[i], arr[j], arr[k]]), prod, maxProd, maxSeq)


print(f"""
Input: {arr}
Output: {maxSeq} having product value {maxProd}.
""")