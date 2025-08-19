# 家具类
class HouseItem:
    def __init__(self, Item_name, Item_area):
        self.Item_name = Item_name  # 家具名称
        self.Item_area = Item_area  # 家具地点
        
        
    def __str__(self):
        return "[%s] 占地 %0.2f 平方米" % (self.Item_name, self.Item_area)   # 返回家具名以及该家具的占地面积
     
# 房子类
class House:
    def __init__(self, h_type, h_area):
        self.h_type = h_type  # 房子类型
        self.h_area = h_area  # 房子总地点
        self.Item_list = []  # 房子中家具的列表
        
        self.free_area = h_area  # 初始时房子剩余面积等于总面积
        
        
    def __str__(self):
        print("-"*50)
        return ("户型: [%s]\n总面积 %.2f平方米， 剩余[%0.2f]平米\n已装家具: %s" % (self.h_type, self.h_area, self.free_area, self.Item_list))
    
    # 该方法实现了将家具安装到房子中
    def add_Item(self, item):
        # 1. 判断家具面积是否大于剩余面积
        if item.Item_area > self.free_area:
            print("%s 太大了！装不到你的房子内！" % item.Item_name)
            return
        
        # 2. 把家具装入家具列表中
        self.Item_list.append(item.Item_name)
        
        # 3. 计算房子的 剩余面积 = 剩余面积 - 家具面积
        self.free_area -= item.Item_area
        
        
#1. 创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 19.5)

print(bed)
print(chest)
print(table)

#2. 创建房子家具
my_home = House("两室一厅", 60)

my_home.add_Item(bed)
my_home.add_Item(chest)
my_home.add_Item(table)
print(my_home)