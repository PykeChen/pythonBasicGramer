""" 实例003：完全平方数
题目 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

程序分析 因为168对于指数爆炸来说实在太小了，所以可以直接省略数学分析，用最朴素的方法来获取上限: """


import math


def checkIsInteger(b):
    diff = math.floor(b) - b
    if diff == 0:
        return True
    else:
        return False


for i in range(1, 1000):
    newInt1 = i + 100
    newInt2 = i + 168
    # check if the tow number is total square
    number1 = math.sqrt(newInt1)
    number2 = math.sqrt(newInt2)
    if checkIsInteger(number1) and checkIsInteger(number2):
        print('check the number', i, number1, number2)

# 方法二
n = 0
while (n+1)**2-n*n <= 168:
    n += 1

for i in range(n+1):
    print('NUMB', i, str((i+100) ** 0.5), str(int((i+100) ** 0.5)))
    if ((i + 100)**0.5 == int((i + 100)**0.5) and (i+168)**0.5
            == int((i+168)**0.5)):
        print(i)
