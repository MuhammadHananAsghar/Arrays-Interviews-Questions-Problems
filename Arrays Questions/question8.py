# Number Occuring Odd Number of Times
from itertools import count


arr = [1, 2, 3, 2, 3, 1, 1]
size = len(arr)
countings = {}

for i in range(size):
    if arr[i] in countings:
        countings[arr[i]] += 1
    else:
        countings[arr[i]] = 1

oddNoTimes = [no for no in countings.keys() if countings[no]%2!=0][0]
print(f"{oddNoTimes} occurs odd number of times.")