# Find duplicates in 0(n) time and 0(1) space
arr = [1, 2, 3, 1, 3, 6, 6]
size = len(arr)
nums = dict()

for i in range(size):
    if arr[i] not in nums:
        nums[arr[i]] = 1
    else:
        nums[arr[i]] += 1

print(f"""
Input: {arr}
Output: {[num for num, value in nums.items() if value==2]}
""")