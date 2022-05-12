# Move all zeros to end
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
size = len(arr)
nums, zeros = [], []

for index, item in enumerate(arr):
    if item == 0:
        zeros.append(0)
    else:
        nums.append(item)

target = nums+zeros

print(f"""
Input: {arr}
Output: {target}
""")