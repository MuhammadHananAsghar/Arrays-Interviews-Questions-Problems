# Count pairs with given sum
arr = [1, 5, 7, -1]
size = len(arr)
value = 6
pairs = []

for i in range(size-1):
    sum = abs(arr[i] + arr[i+1])
    if sum == value:
        pairs.append([arr[i], arr[i+1]])

print(f"""
Input: {arr}
Output: {pairs}
""")