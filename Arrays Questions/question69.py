# Four elements that given sum is equal
arr = [10, 2, 3, 4, 5, 9, 7, 8]
size = len(arr)
given_sum = 23
one, two, three, four = 0, 0, 0, 0

for i in range(size-1):
    for j in range(i+1, size):
        for k in range(j+1, size):
            for m in range(k+1, size):
                sum = abs(arr[i]+arr[j]+arr[k]+arr[m])
                if sum == given_sum:
                    one, two, three, four = arr[i], arr[j], arr[k], arr[m]
                    break
    
print("Numbers are: ", one, two, three, four)