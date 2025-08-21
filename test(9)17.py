x =object

print(dir(x))

i = 0 
seq = ['one', 'two', 'three']
for element in seq:
    print(i, seq[i])
    i += 1

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

a, b, c =(input("请输入三角形的三边长: ").split())
a= int(a)
b= int(b)
c= int(c)

p = (a + b + c)/2

s = (p*(p-a)*(p-b)*(p-c))**0.5

print("三角形面积为: ".format(s, '.2f'))