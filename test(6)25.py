values = [11, 22, 33, 44, 55, 66, 77, 88, 99]
result_dict = {'key1':[1], 'key2':[2]}

for value in values:
    if value > 66:
        result_dict['key1'].append(value)
    elif value < 66:
       result_dict['key2'].append(value)
print(result_dict)