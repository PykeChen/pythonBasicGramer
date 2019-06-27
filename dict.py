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

node2 = {}
node2.setdefault("2", {1, 3, 4})
node2.setdefault(3, {3, 3, 4})
print(node2)

node = {1: {'This is me', 3}, "2": {'THIS 2'}, 'node2': {"This 3"}}
if "2" in node:
    value = node.get("99", "SBSSS")
    print(value)
    # node.setdefault()
keValue = node.pop("2")
print(keValue)

dict22 = {(1, 2): 1, (4, 5): 1}
if (7, 5) in dict22:
    print("(1, 2) is in it")

list1 = ['oath', 'abo']
list1.sort()
print(list1)