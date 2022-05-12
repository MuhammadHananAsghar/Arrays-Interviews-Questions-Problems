# Stock Buy Sell to Maximize Profit
# [100, 180, 260, 310, 40, 535, 695]
# [1, 5, 2, 3, 7, 6, 4, 5]
arr = [100, 180, 260, 310, 40, 535, 695]
size = len(arr)

buy, sell = [], []
buyFlag, sellFlag = False, False

for i in range(size):
    if (arr[i] < arr[i-1]) and ((i+1 == size) or (arr[i] < arr[i+1])) and (not buyFlag):
        if i == size-1:
            continue
        buy.append(arr[i])
        sellFlag = False
        buyFlag = True

    if (arr[i] >= arr[i-1]) and ((i+1 == size) or (arr[i] > arr[i+1])) and (not sellFlag):
        sell.append(arr[i])
        sellFlag = True
        buyFlag = False


for b,s in zip(buy, sell):
    print(f"Buy at the price of {b} and sell at the price of {s}.")
