# Convert an array to reduced form
arr = [10, 40, 20, 60, 5, 8]
size = len(arr)

sortedArr = sorted(arr)
ranks = {}
for index, item in enumerate(sortedArr):
    if item not in ranks:
        ranks[item] = index
output = [ranks[item] for item in arr]
print(output)