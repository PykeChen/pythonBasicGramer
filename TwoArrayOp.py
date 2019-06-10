# 数组操作

# map进行转换
lineResult = [[1, 2, 3, 4], [5, 6, 7, 8]]
lastPrintStr = [["value="+str(unit) for unit in line] for line in lineResult]
print(lastPrintStr)

# 整合成单个数组
lastPrintStr2 = ["value=" + str(one) for line in lineResult for one in line]
print(lastPrintStr2)

# 每4个整合成一个单独的数组
lastPrintStr3 = [lastPrintStr2[i:i+4] for i in range(0, len(lastPrintStr2), 4)]
print(lastPrintStr3)
