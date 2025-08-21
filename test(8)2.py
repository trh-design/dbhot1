x = 10
if x > 5:
    raise Exception('x 不能大于5。x 的值为: {}'.format(x))

file = open('.test_runoob.txt', 'w')
try:
    file.write('hello world')
finally:
    file.close()