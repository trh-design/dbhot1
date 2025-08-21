import operator

x = 10
y = 20

print("x:", x,", y:", y)
print("operator.lt(x,y):", operator.lt(x,y))
print("operator.gt(y,x):", operator.gt(x,y))
print("operator.eq(x,x):", operator.eq(x,x))
print("operator.ne(y,y):", operator.ne(y,y))
print("operator.le(x,y):", operator.le(x,y))
print("operator.ge(y,x):", operator.ge(y,x))
print()

x = "Google"
y = "Runoob"

print("x:", x, ",y:", y)
print("operator.lt(x,y):", operator.lt(x,y))
print("operator.gt(y,x):", operator.gt(y,x))
print("operator.eq(x,x):", operator.eq(x,x))
print("operator.ne(y,y):", operator.ne(y,y))
print("operator.le(x,y):", operator.le(x,y))
print("operator.ge(y,x):", operator.ge(y,x))