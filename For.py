print('start')
print('start one({1}), end({0})'.format('cpy', 'cry'))

numbers = 1, 2, 3, 4
L = []

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
