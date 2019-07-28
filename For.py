print('start')
print('start one({1}), end({0})'.format('cpy', 'cry'))

numbers = 1, 2, 3, 4
L = []

# 逆向遍历
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i], end=' ')

print('\n', '-'*10)

for i, v in enumerate(numbers):
    print(i, v)


def composeNumber(numbers):
    for i, v in enumerate(numbers):
        print(f'One for nest index = {i}, value  = {v}')
        for j in range(i+1, len(numbers)):
            print(f'tow for nest index = {j}, value  = {numbers[j]}')
            for k in range(j+1, len(numbers)):
                print(f'three for nest index = {k}, value  = {numbers[k]}')
                print(f'compose i = {i}, j  = {j}, k = {k}, lastValue = ' +
                      str(v) + str(numbers[j]) + str(numbers[k]))
                L.append(str(v) + str(numbers[j]) + str(numbers[k]))
                L.append(str(v) + str(numbers[k]) + str(numbers[j]))
                L.append(str(numbers[k]) + str(v) + str(numbers[j]))
                L.append(str(numbers[k]) + str(numbers[j]) + str(v))
                L.append(str(numbers[j]) + str(numbers[k]) + str(v))
                L.append(str(numbers[j]) + str(v) + str(numbers[k]))


composeNumber(numbers)

for i, v in enumerate(L):
    print(f'==== {v}')


prices = [1, 2, 4, 5]
pt = [[0 for _ in range(2)] for i in prices]
pt2 = [[0] for _ in range(2) for i in prices]
pt3 = [[[0 for _ in range(2)] for _ in range(2)] for i in prices]
print(pt)
print(pt2)
print(pt3)


word1 = 'workd1'
for i in word1[:3]:
    print(i)

for i in range(1, 3):
    print(i)
