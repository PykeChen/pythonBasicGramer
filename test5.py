""" 实例005：三数排序
题目 输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析 练练手就随便找个排序算法实现一下，偷懒就直接调函数。 """

# numStr = input('输入三个整数，格式:1, 2, 3\n')
# numbs = numStr.split(',')

# data2 = [int(i) for i in numbs]
# print(data2)

# 冒泡排序，从小到大排序


def mopaoSort(datas):
    for i in range(len(datas)):
        minValue = datas[i]
        minIndex = i
        for j in range(i+1, len(datas)):
            if datas[j] < minValue:
                minValue = datas[j]
                minIndex = j
        tmpValue = datas[i]
        datas[i] = minValue
        datas[minIndex] = tmpValue


# 快速排序，从小到大排序
def quickSort(datas):
    if len(datas) <= 1:
        return datas
    i, j = 0, len(datas)-1
    keyValue = datas[i]
    # 将keyVlaue作为关键数据，将<keyValue的都放在左边，将>keyValue的都放在右边
    while i < j:
        # 从j--开始找<keyValue的，然后进行对调
        while j > i:
            if datas[j] < keyValue:
                tmp = datas[i]
                datas[i] = datas[j]
                datas[j] = tmp
                break
            j = j-1
        # 从i++开始找>keyVlaue的, 然后进行对调
        while j > i:
            i = i+1
            if datas[i] > keyValue:
                tmp = datas[i]
                datas[i] = datas[j]
                datas[j] = tmp
                break
    return quickSort(datas[:i]) + [datas[i]] + quickSort(datas[i+1:])

# 分而治之+递归


def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


data2 = [19, 48, 5, 7, 20, 45, 369, 100, 24, 69, 234]
# mopaoSort(data2)
data3 = quickSort(data2)
print(data3)
