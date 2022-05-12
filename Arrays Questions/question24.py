# Count Minimum steps to get desired array

# 1. Get the desiredArr array.
# 2. Set output as 0.
# 3. Check if all the elements given are even, then divide all the elements by 2 and increase the output by 1.
# 4. Get all of the odd elements, make them even by decrease their value by 1.
# 5. For every decrement, increase the value of output by 1.
# 6. We get all zeros in desiredArr array, after completing all the steps.
# 7. Return output.

target = [16, 16, 16]
size = len(target)
numSteps = 0

def getEvenCount(arr):
    evenCount = 0
    for item in arr:
        if item % 2 == 0:
            evenCount += 1
    return evenCount

def getZeroCount(arr):
    zeroCount = 0
    for item in arr:
        if item == 0:
            zeroCount += 1
    return zeroCount

while True:
    print(target)
    zeros = getZeroCount(target)
    if zeros == size:
        break

    evens = getEvenCount(target)
    if evens == size:
        for i in range(size):
            if target[i]%2 == 0:
                target[i] = target[i] // 2
        numSteps += 1

    for i in range(size):
        if target[i] % 2 != 0:
            target[i] = target[i] - 1
            
            numSteps += 1
    


print(numSteps)


# while True:
#     print(target)
#     for i in range(size):
#         if (target[i] % 2 != 0):
#             break

#         if target[i] == 0:
#             zeroCount += 1
        
#         evenCount += 1

#     if zeroCount == size:
#         break
    
#     if evenCount == size:
#         print("Even")
#         for i in range(size):
#             if target[i]%2 == 0:
#                 target[i] = target[i] / 2

#         numSteps += 1

#     print(target)

#     for i in range(size):
#         if target[i]%2 != 0:
#             target[i] = target[i] - 1
#         numSteps += 1

#     print(target)

