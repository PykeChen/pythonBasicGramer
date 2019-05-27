""" 字典--表达式练习 """

dictDemo = dict([('key1', 1), ('key2', 2), ('key3', 3),
                 ('key4', 4), ('key5', 5), ('key6', 6)])
print(dictDemo['key1'], dictDemo['key2'])

if 'key1' in dictDemo:
    print('key1 in the dict key ')

for i in dictDemo.values():
    print(i)

print(dictDemo.values())

print(dictDemo['key1'])


dictOne = dict(sape=4139, guido=4127, jack=4098)
print(dictOne['sape'])


    