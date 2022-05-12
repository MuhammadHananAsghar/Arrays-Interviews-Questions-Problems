# Find lost element from the duplicated array

arr1 = [1, 4, 5, 7, 9]
arr2 = [4, 5, 7, 9]

for item in arr1:
    if item in arr2:
        pass
    else:
        print(f"{item} is missing from second array.")
        break
