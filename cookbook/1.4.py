import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# getting the smallest item is log N complexity
heapq.nlargest(3, nums)
heapq.nsmallest(3, nums)

portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
cheap

# advice if you need just the single smallest or largest use this
# however if you need enough element that it gets close to n just
# sort and slice
