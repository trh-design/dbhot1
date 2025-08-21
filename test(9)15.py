print("abs(-40) :", abs(-40))
print("abs(100.10) :", abs(100.10))

numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))

numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =', numbers1)

numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =', numbers2)

numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbes3 =', numbers3)

numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =', numbers1)

numbers2 = {'x': 4, 'y': 5}
print('numbers =', numbers2)

numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =', numbers3)

print("min(80, 100, 1000)", min(80, 100, 1000))
print("min(-20, 100, 400)", min(-20, 100, 400))
print("min(-80, -20, -10)", min(-80, -20, -10))
print("min(0, 100, -400)", min(0, 100, -400))

all(['a', 'b', 'c', 'd'])

hex(255)