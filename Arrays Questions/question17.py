# Floor and Ceiling in Sorted Array
arr = [1, 2, 8, 10, 10, 12, 19]
size = len(arr)
sorted = sorted(arr)

x_value = 20
floor, ceil = None, None

for idx, item in enumerate(arr):
    if item == x_value:
        floor, ceil = item, item
        break
    elif item < x_value:
        floor = item
    elif item > x_value:
        ceil = item
        break
    else:
        pass

str = ""
if floor is None:
    str += "Floor doesn't exist in array, "

if floor:
    str += f"floor = {floor}, "

if ceil:
    str += f"ceil = {ceil}. "

if ceil is None:
    str += "ceil doesn't exists in array."
str = f"For the value of x = {x_value}, "+str
print(str)