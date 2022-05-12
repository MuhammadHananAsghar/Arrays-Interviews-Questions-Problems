# Common elements in three sorted arrays

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [5, 5, 10, 20]


def itemFound(value, arr):
    found = False
    for item in arr:
        if value == item:
            found = True
            return found
    return found

temp = []
for item in arr1:
    if itemFound(item, arr2):
        temp.append(item)
commons = []
for item in arr3:
    if itemFound(item, temp):
        commons.append(item)

print(f"""
Inputs: {arr1}, {arr2}, {arr3}
Output: {commons}
""")