def is_odd(n):
    return n % 2 == 1

tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

import math
def is_sqr(x):
    return math.sqrt(x) % 1 == 0

tmplist = filter(is_sqr, range(1, 101))
newlist = list(tmplist)
print(newlist)

class A:
    pass
class B(A):
    pass

print(issubclass(B, A))

import math

print("math.pow(100, 2) : ", math.pow(100, 2))
print("pow(100, 2) : ", pow(100, 2))
print("math.pow(100, -2) : ", math.pow(100, -2))
print("math.pow(2, 4) : ", math.pow(2, 4))
print("math.pow(3, 0) : ", math.pow(3, 0))

lst = [1, 2, 3]
for i in iter(lst):
    print(i)

class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x
    
    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

class A(object):
    bar = 1
    def func1(self):
        print('foo')
    @classmethod
    def func2(cls):
        print('func2')
        print(cls.bar)
        cls().func1()

A.func2()

hash('test')