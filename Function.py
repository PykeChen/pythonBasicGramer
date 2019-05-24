
valueBefore = 10
array = [2, "4", 5]


def testFunParamsValue(x):
    x = 100


def modifyFunParamsValue(x):
    x[1] = 444


testFunParamsValue(valueBefore)

print('valueAfter' + str(valueBefore))
modifyFunParamsValue(array)

for i in array:
    print('arrary value ' + str(i))
