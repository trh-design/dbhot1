class C(object):
    @staticmethod
    def f():
        print('runoob');

C.f();
cobj = C()
cobj.f()

result = eval("2 + 3 * 4")
print(result)

x = 10
result = eval("x + 5")
print(result)

namespace = {'a' : 2, 'b' : 3}
result = eval("a + b", namespace)
print(result)

x = 10
expr = """
z = 30
sum = x + y + z
print(sum)
"""
def func():
    y = 20
    exec(expr)
    exec(expr, {'x': 1, 'y': 2})
    exec(expr, {'x': 1, 'y': 2}, {'y': 3, 'z': 4})

func()

code = '2 + 2'
result = eval(code)
print(result)

code = 'result = 2 + 2'
local_vars = {}
exec(code, globals(), local_vars)
result = local_vars['result']
print(result)

code = '2 + 2'
global_vars = {}
exec(code, global_vars)
result = global_vars['result']
print(result)