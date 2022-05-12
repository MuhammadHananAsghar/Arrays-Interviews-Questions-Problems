# Program to find largest element in the array
arr = [20, 10, 20, 4, 100]
size = len(arr)

largest = 0
for i in range(size):
    if arr[i] > largest:
        largest = arr[i]

print(f"""
Input: {arr}
Output: {largest}
""")