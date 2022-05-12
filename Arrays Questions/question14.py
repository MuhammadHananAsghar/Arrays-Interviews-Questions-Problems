# Segregate 0s and 1s in an array
from click import pass_context


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
size = len(arr)
zeros, ones = [], []

for i in range(size):
    if arr[i] == 1:
        ones.append(1)
    else:
        zeros.append(0)

seg_arr = zeros+ones
print(f"Segregation of {arr} is {seg_arr}.")