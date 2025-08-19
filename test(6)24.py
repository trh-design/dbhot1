list = [33, 26, 75, 50, 39, 79, 80, 62, 56, 75, 42, 95, 54, 100, 98, 4, 59, 25, 96, 17]
i =len(list) - 1
while i >= 0:
    if list[i] % 2 != 0:
        list.pop(i)
    i -= 1
print(list)