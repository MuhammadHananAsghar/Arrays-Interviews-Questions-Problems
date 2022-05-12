# Union and Intersection
arr1 = [1, 2, 4, 3, 6, 7]
arr2 = [1, 2, 3, 5, 4, 7]

union = set()

for i in range(len(arr1)):
    union.add(arr1[i])

for j in range(len(arr2)):
    union.add(arr2[j])

print("Union of both arrays: {}".format(union))
        

intersection = set()
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            intersection.add(arr1[i])

print("Intersection of both arrays: {}".format(intersection))