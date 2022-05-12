# Sum of elements in the array
arr = [15, 12, 13, 10]
size = len(arr)

sum = 0
for i in range(size):
    sum += arr[i]

print(f"""
Input: {arr}
Output: {sum}
""")