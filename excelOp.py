# -*- coding: utf-8 -*-
import xlrd

# 打开文件
workbook = xlrd.open_workbook(
    r'/Users/cpy/python_proj/BasicGrammar/demoDoc.xlsx')

# 获取所有sheet
print(workbook.sheet_names())

# 根据sheet索引或者名称获取sheet内容
sheet = workbook.sheet_by_index(0)
sheet2 = workbook.sheet_by_name('工作表1')

# sheet的名称，行数，列数
print(sheet.name, sheet.nrows, sheet.ncols, sheet.number)

# 获取整行和整列的值（数组）
rows = sheet.row_values(2)
cols = sheet.col_values(1)


def replaceSpace(values):
    newTmp = values.replace('\xa0', '')
    return newTmp


newRows = [replaceSpace(i) for i in rows]
newCols = [replaceSpace(i) for i in cols]


print('rows_2', newRows)
print('cols_2', newCols)
