def maxprofit(arr):
    buy = min(arr)
    return max(arr[arr.index(buy) :]) - buy


print(maxprofit([7, 6, 4, 3, 1]))
