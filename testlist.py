""" 字符串列表转换为数字列表的方式"""

datas = ['3', '4', '5', '9']
print(datas)
# 方式1
data2 = [int(i) for i in datas]
print(data2)

# 方式2
data3 = list(map(int, datas))
print(data3)