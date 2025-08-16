binary_number = '10101'
decimal_number = int(binary_number, 2)     #二进制转换为十进制
octal_number = oct(decimal_number)         #十进制转换为八进制
hexadecimal_number = hex(decimal_number)   #十进制转换为十六进制

print('二进制数:', binary_number)
print('转换为十进制:', decimal_number)
print('转换为八进制:', octal_number)
print('转换为十六进制:', hexadecimal_number)