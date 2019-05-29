from itertools import groupby


def checkValueType(value):
    if isinstance(value, int):
        return 'int'
    elif isinstance(value, str):
        return 'str'
    elif isinstance(value, tuple):
        return 'tuple'
    else:
        return 'other'


datas = [1, 3, 4, 5, 'a', 'b', 'c']

print(type(datas))
print(type(datas[0]))
print(str(type(datas[0]) == type(1)))

newData = groupby(datas, key=checkValueType)
for key, collectData in newData:
    print(key, collectData)
