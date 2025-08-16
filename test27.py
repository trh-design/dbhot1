# 简单计算器程序

# 定义函数来执行加法
def add(x,y):
    return x + y

# 定义函数来执行减法
def subtract(x,y):
    return x - y

# 定义函数来执行乘法
def multiply(x,y):
    return x * y 

# 定义函数来执行除法
def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "除数不能为零"
    
# 主程序循环
while True:
    print("\n选择一个运算:")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("5.退出")
    
    choice = input("输入选项编号: ")
    
    if choice in ('1','2','3','4'):
        num1 = float(input("输入第一个数: "))
        num2 = float(input("输入第二个数: "))
        
        if choice == '1':
            print(f"结果：{add(num1,num2)}")
        elif choice == '2':
            print(f"结果: {subtract(num1,num2)}")
        elif choice == '3':
            print(f"结果: {multiply(num1,num2)}")
        elif choice == '4':
            print(f"结果: {divide(num1,num2)}")
    elif choice == '5':
        print("退出程序.")
        break
    else:
        print("无效的选项，请重新输入.")