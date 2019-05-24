# 1.构造函数重载的问题
# 2.静态方法
# $ 3.


class TestCls:
    a = 100
    b = [1, 2, 3, 4]

    @staticmethod
    def testStaticMethod(a):
        print(a)

    def testMethods(self, b):
        for i in b:
            print(i)

    def testMethodCall(self, method):
        method()


class TestClas2:

    bb = 10

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def methodsTst(self, arg):
        print(f'TestClas2 methodsTst {arg}')

# 派生类


class DerivedClas(TestClas2):

    def __init__(self):
        TestClas2.__init__(self, 101, 102)
        print('DerivedClas init ')

    def methodsTst(self, arg):
        super().methodsTst(arg)
        super(DerivedClas, self).methodsTst(arg)
        TestClas2.methodsTst(self, arg)
        print(f'DerivedClas methodsTst {arg}')


derivedInstance = DerivedClas()
print('I see', derivedInstance.x, derivedInstance.y)
derivedInstance.methodsTst('override methods')

# test1
instanceCls2 = TestClas2("234", 234324)
print(instanceCls2.x, instanceCls2.y)

# instanceCls3 = TestClas2("construct *argc")

# test2
instanceClas = TestCls()
methodDelegate = instanceClas.testMethods
methodDelegate([6, 7, 8])
instanceClas.a = 200

instanceCls3 = TestCls()
print(f'instanceClas.a = {instanceClas.a}')


def methodsTst():
    print('I just test')


instanceClas.testMethodCall(methodsTst)

# test3
instanceClas.testMethods(instanceClas.b)
TestCls.testMethods(instanceClas, instanceClas.b)
TestCls.testStaticMethod(instanceClas.a)
