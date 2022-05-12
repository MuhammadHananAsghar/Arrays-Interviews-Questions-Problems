# Shuffle an Array
import random

arr = [12, 34, 17, 90, 67, 23]
size = len(arr)
output = []


while True:
    rnd = random.choice(arr)
    if rnd not in output:
        output.append(rnd)
    
    if len(output) == size:
        break

print(f"""
Input: {arr}
Output: {output}
""")