def func(start, end):
    count = 0
    sum = 0
    for index in range(start, end + 1):
        if index % 3 == 0 and index  % 7 == 0:
            count = count + 1
            sum = sum + index
        else:
            continue
    return count, sum


f = func(2, 100)  # 求2-100之间符合要求的数，可以打印看着符合要求的数有 21, 42, 63, 84四个
print(f)  # (4, 210)