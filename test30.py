card = []
del_name = None


# 启动程序时默认调用的方法，显示主界面
def choose():
    print("**********************************************************\n欢迎使用【名片管理系统】v1.0")
    inputnum = input("\n请选择操作: \n1, 新建名片\n2, 显示全部\n3, 查询名片\n\n0, 退出系统\n*************************************************")
    if inputnum == "1":
        create_cards()
    elif inputnum == "2":
        display_all()
    elif inputnum == "3":
        search_card()
    elif inputnum == "0":
        exit()
    else:
        print("您输入的数字有误！")
        
        
# 新建名片
def create_cards():
    global cards   
    print("以下操作将为您新建一个名片:")
    name = input("请输入您的姓名:")
    tel = int(input("请输入您的电话:"))
    qq = int(input("请输入您的QQ:"))
    email = int(input("请输入您的邮件:"))
    print("------------------------\n您的名片信息为: \n姓名: %s\n电话: %d\nQQ: %d\n邮件: %s" % (name, tel, qq, email))
    cards.append([name, tel, qq, email])
    input_q = input("------------------------\nTip: 输入 q 即可返回主界面")
    if input_q == 'q':
        choose()
    else:
        print("输入有误！默认为您跳转到主界面！")
        choose()
        

# 显示全部名片信息
def display_all():
    global cards
    for index in cards:
        print("------------------------\n姓名: %s\n电话: %d\nQQ: %d\n邮件: %s" % (index[0], index[1], index[2], index[3]))
    input_q = input("---------------------------\nTip: 输入: q 即可返回主界面")
    if input_q == 'q':
        choose()
    else:
        print("输入有误！默认为您跳转到主界面！")
        choose()
        
        
# 查询用户
def search_card():
    global cards
    global del_name
    input_name = str(input(("请输入您要查询的用户姓名：")))
    del_name = input_name  #将要查询的用户名保存到全局变量del_name中，方便之后做删除操作
    isexist = False
    for index in range(len(cards)):
        if input_name == str(cards[index][0]):
            print("------------------------\n查询的用户信息如下: \n姓名: %s\n电话: %dQQ: %d\n邮件: %s" %(
                cards[index][0], cards[index][1], cards[index][2], cards[index][3]))
            isexist = True  #记录是否查询到该用户
            inputnum = int(input("------------选择操作------------\n1, 修改名片\n2, 删除名片"))
            if inputnum == '1':
                del cards[index]   # 这里定义对一个用户名片的修改操作为删除原来的所有信息，让用户重新输入
                edit_card()
            elif inputnum == '2':
                del_card
            else:
                pr = input("您已输入多次错误！自动为您退出系统！")
                exit
        else:
            continue
        
    if isexist == False:  # for循环结束后仍为Falsa的话，代表为查询到相应用户名的用户
        print("未查询到该用户信息！")
        input_q = input("------------------------\nTip: 输入 q 可返回主界面")
        if input_q == 'q':
            choose()
        else:
            choose()
            
            
# 修改用户信息
def edit_card():
    print("------------------------\n请重新输入名片信息: ")
    name = input("请输入您的姓名: ")
    tel = input("请输入您的电话: ")
    qq = input("请输入您的QQ: ")
    email = input("请输入您的邮件: ")
    print("------------------------\n您的名片信息为: \n姓名: %s\n电话: %d\nQQ: %d\n邮件: %s" % (name, tel, qq, email))
    card.append([name,tel,qq,email])
    input_q = input("------------------------\nTip: 输入 q 即可返回主界面")
    if input_q == 'q':
        choose()
    else:
        print("输入有误！默认为您跳转到主界面！")
        choose()
        
        
def del_card():
    global cards
    global del_name
    for index in range(len(cards)):
        if del_name == str(cards[index][0]):
            del cards[index]
            print("成功删除用户信息！")
            input_q = input("------------------------\nTip: 输入 q 即可返回主界面")
            if input_q == 'q':
                choose()
            else:
                print("输入有误！默认为您跳转到主界面！")
                choose()


choose()  # 程序启动时就会调用该方法显示主界面