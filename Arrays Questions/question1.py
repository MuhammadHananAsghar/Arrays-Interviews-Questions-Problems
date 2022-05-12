# Longest Span with same sum
arr1 = [0, 1, 0, 0, 0, 0]
arr2 = [1, 0, 1, 0, 0, 1]
maxLen = 0

for i in range(len(arr1)):
    sumArr1, sumArr2 = 0, 0
    for j in range(i, len(arr2)):
        sumArr1 += arr1[j]    
        sumArr2 += arr2[j]

        if (sumArr1 == sumArr2):
            length = j - i + 1
            print(f"i={i}, j={j}, length={length}, maxlength={maxLen}")
            if length > maxLen:
                maxLen = length  


print("The maximum length is {}.".format(maxLen))