# Reverse and array or string
arr = [1, 2, 3, 4, 5]
tempArr = arr.copy()
size = len(arr)

for i in range(size//2):
    temp = arr[i]
    arr[i] = arr[size-i-1]
    arr[size-i-1] = temp

print(f"""
Input: {tempArr}
Output: {arr}
""")