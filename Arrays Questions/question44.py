# Number of pairs such that x^y > y^x
arr = [2, 1, 6]
Y = [1, 5]
pairs = []


for x in arr:
    for y in Y:
        if (x**y) > (y**x):
            pairs.append([x, y])

print(pairs)