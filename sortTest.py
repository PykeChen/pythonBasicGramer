""" 实例004：这天第几天
题目 输入某年某月某日，判断这一天是这一年的第几天？

程序分析 特殊情况，闰年时需考虑二月多加一天： """

dateFormat = input('输入某年某月某日,格式:2018-10-10\n')

daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysOfMonthIfEvenYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dates = dateFormat.split('-')
year = int(dates[0])
month = int(dates[1])
day = int(dates[2])

ifEvenYear = (year % 4) == 0

if(ifEvenYear):
    listChoose = daysOfMonthIfEvenYear
else:
    listChoose = daysOfMonth

dayNums = 0

for i in range(month-1):
    dayNums += listChoose[i]

dayNums += day

print('This is the ', dayNums, 'th days of this year')

