hexadecimal_number = '2a'
decimal_number = int(hexadecimal_number, 16)  # 十六进制转换为十进制
binary_number = bin(decimal_number)             # 十进制转换为二进制
octal_number = oct(decimal_number)              # 十进制转化为八进制

print('十六进制数: ', hexadecimal_number)
print('转换为十进制: ', decimal_number)
print('转换为二进制: ', binary_number)
print('转换为八进制:', octal_number)