# Rearrange array in maximum and minimum form
arr = [1, 2, 3, 4, 5, 6, 7]
size = len(arr)
temp = []
start = 0
end = size-1

for i in range(size):
    if arr[end] not in temp:
        temp.append(arr[end])
    if arr[start] not in temp:
        temp.append(arr[start])
    start += 1
    end -= 1
    if start > end:
        break

print(f"""
Input: {arr}
Output: {temp}
""")