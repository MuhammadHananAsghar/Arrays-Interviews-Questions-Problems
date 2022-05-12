# Maximum of all subarrays of size k using sliding window technique
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
size = len(arr)
k = 4
maxarray = []

for i in range(size):
    temp = []
    if (k + i) <= size:
        for j in range(i, k+i):
            temp.append(arr[j])
        maxarray.append(max(temp))

print(f"""
Input: {arr}
Output: {maxarray}
""")
