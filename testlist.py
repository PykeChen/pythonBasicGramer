""" 字符串列表转换为数字列表的方式"""
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print('size = ', len(queue))

datas = ['3', '4', '5', '9']
print(datas)
# 方式1
data2 = [int(i) for i in datas]
print(data2)

# 方式2
data3 = list(map(int, datas))
print(data3)

data = ['a', 'b', 'c']
data2 = [1, 2, 4]
newData = [(x, y) for x in data for y in data2]
print(newData)

# 嵌套列表表达式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])
