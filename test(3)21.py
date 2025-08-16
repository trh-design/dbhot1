<<<<<<< HEAD
octal_number = '52'
decimal_number = int(octal_number, 8)       # 八进制转换为十进制
binary_number = bin(decimal_number)         # 十进制转换为二进制
hexadecial_number = hex(decimal_number)       # 十进制转换为十六进制

print ('八进制数: ', octal_number)
print ('转换为十进制: ', decimal_number)
print ('转换为二进制:', binary_number)
print ('转换为十六进制: ',hexadecial_number)
=======
import statistics

data = [10,20,30,40]
interval = 10
median = statistics.median_grouped(data, interval)
print(median)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
