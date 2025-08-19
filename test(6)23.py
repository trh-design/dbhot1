import random
x = [18, 93, 40, 87, 18, 82, 30, 12, 67, 85, 10, 24, 86, 81, 67, 19, 70, 46, 74, 65]
a = x[1::2]
b = x[0::2]
b.sort(reverse = True)
x[0::2] = b
print(x)