try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open ('file log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论一场是否都会执行。')