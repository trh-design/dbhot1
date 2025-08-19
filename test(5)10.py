name = "RUNOOB"

# 接受用户收入
# name = input("输入你的名字: \n\n")

lngth = len(name)
l = ""

for x in range(0, lngth):
    c = name[x]
    c = c.upper()
    
    if (c == "A"):
        print("..######..\n..#....#..\n..######..", end= "")
        print("\n..#....#..\n..#....#..\n\n")
        
    elif (c == "B"):
        print("..######..\n..#....#..\n..######..", end= "")
        print("\n..#....#..\n..#....#..\n\n")
        
    