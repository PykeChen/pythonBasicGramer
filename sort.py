from operator import itemgetter, attrgetter

data = [('a', 6), ('e', 2), ('f', 2), ('a', 4), ('d', 21), ('c', 9)]

print(sorted(data))

print(sorted(data, key=itemgetter(0)))

# print(sorted(data, key=attrgetter()))

print(sorted(data, key=itemgetter(0), reverse=True))

print(sorted(data, key=itemgetter(0, 1), reverse=True))

print('---------------')
# 使用装饰-排序-去装饰的旧方法


class Item:
    def __init__(self, name, age):
        self.name = name
        self.age = age


datas = [Item('a', 6), Item('e', 2), Item('f', 2),
         Item('a', 4), Item('d', 21), Item('c', 9)]


print(datas.sort())


newData = sorted(datas, key=attrgetter('name'), reverse=True)
for i in newData:
    print(i.name, i.age)
print('===========')


decorated = [(item.name, i, item) for i, item in enumerate(datas)]
sortDecorated = sorted(decorated, key=itemgetter(0, 1), reverse=True)
unDecorated = sorted([item for name, i, item in sortDecorated],
                     key=attrgetter('name'), reverse=True)
for i in unDecorated:
    print(i.name, i.age)

