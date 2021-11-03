def maxProfitForStocks(arr):
    buy = 999999
    profit = 0
    for stock in arr:
        sell = stock
        profit = max(sell - buy, profit)
        buy = min(sell, buy)
    return profit


arr = [12,11,15,3,10]

print(maxProfitForStocks(arr))