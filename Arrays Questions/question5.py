# Leaders is array
arr = [12, 23, 9, 6, 8, 5, 6]
size = len(arr)
leaders = set()
leader = None

for i in range(size):
    for j in range(i, size):
        if arr[i] > arr[j]:
            leader = arr[i]
        
        if arr[i] < arr[j]:
            leader = None
            break
        

    if i == (size-1):
        leader = arr[i]
    
    if leader:
        leaders.add(leader)

print("Leaders are: {}".format(sorted(leaders, reverse=True)))    