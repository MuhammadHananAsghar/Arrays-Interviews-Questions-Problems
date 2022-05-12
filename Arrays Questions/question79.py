# Product Array Puzzle
arr = [10, 3, 5, 6, 2]
size = len(arr)

def product(arr):
    prod = 1
    for item in arr:
        prod = prod * item
    return prod

output = []

for i in range(size):
    current_element = arr[i]
    temp = arr.copy()
    temp.pop(i)
    output.append(product(temp))    
    print(current_element, temp)

print(f"""
Input: {arr}
Output: {output}
""")