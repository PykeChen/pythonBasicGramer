matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(list(zip(*matrix)))

prices = [1, 3, 4, 5]
pt = [[[0 for _ in range(2)] for _ in range(2)] for i in prices]
print(prices[-1])