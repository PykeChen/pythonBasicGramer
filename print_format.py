
import math
value1 = 34
value2 = 'Test'

print('This is a {1}, value is {0}'.format(value1, value2))

# :后输出格式
print('This is a {1:6}, value is {0:.3f}'.format(value1, value2))

print(f'This is a {value2}, value is {value1}')
# :后输出格式
print(f'This is a {value2:9}, value is {value1:.2f}')
# 可以使用关键字参数
print('The story of {0}, {1}, and {other}.'.format(
    'Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'
      .format(table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 使用%来格式化字符串
stfValue = 23.234324342
print('The value of pi is approximately %5.3f.' % stfValue)
