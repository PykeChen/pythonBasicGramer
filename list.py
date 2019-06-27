prices = [2, 4, 1, 6]
prices2 = [4, 6, 7, 9]
print(prices[-3:])
print(prices[:-1])
for i, j in zip(prices[1:], prices[:-1]):
    print(i, j)
print('--'*10)
for i, j in zip(prices, prices2[:-1]):
    print(i, j)
