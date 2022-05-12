# Find an elements that appears more than n/k times
arr = [3, 1, 2, 2, 1, 2, 3, 3]
size = len(arr)
k = 4

times = size//k
freq = {}

for i in range(size):
    if arr[i] not in freq:
        freq[arr[i]] = 1
    else:
        freq[arr[i]] += 1

nums = []
for key, value in freq.items():
    if value > times:
        nums.append(key)

print(f"""
Input: {arr}
Output: {nums}
""")