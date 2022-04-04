prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# often operations are done by keys not values
min(prices)

# work around
min_price = min(zip(prices.values(), prices.keys()))
min_price

# can tell it what key to use
min_price = min(prices, key=lambda k: prices[k])
min_price
