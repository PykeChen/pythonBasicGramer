import sys


def testException(x, y):
    try:
        divisionValue = x / y
        print('divisionValue = ', divisionValue)
    except ZeroDivisionError:
        print('division zero error')
    except ArithmeticError:
        print('ArithmeticError')
    except Exception as error:
        print('args = ', error.args)
        print('exc_info = ', sys.exc_info())
        print('exception~~~', error)
    else:
        print('123213')
    finally:
        print('execute after')


testException(1, 2)

testException(1, '2')
