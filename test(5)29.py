class Pistol:
    def __init__(self, pname):
        self.pname = pname
        self.count = 3  # 默认初始有3枚子弹
        
    # 枪能够发射子弹
    def Launch(self):
        if self.count <= 0:
            print("[%s]没有子弹了!!!" % self.pname)
            return
        else:
            self.count = self.count - 1
            print("[%s]成功发射一枚子弹! 还剩[%s]枚子弹! " % (self.pname, self.count))
            
    # 枪装填子弹
    def add_Bullets(self):
        self.count = self.count + 1
        print("为[%s]装填子弹!!此时有[%s]枚子弹!" % (self.pname, self.count))
        
        
class Soldiers:
    def __init__(self, name):
        self.name = name
        self.gun = None  # gun最后由创建类实例赋值！！
        
    def fire(self):
        # 此时没抢
        if self.gun == None:
            print("士兵[%s]没有枪哦，无法射击！" % self.name)
            return
        else:
            print("士兵[%s]开火" % self.name)
            self.gun.Launch()
            
            
p = Pistol("AK47")
s = Soldiers("许三多")
s.gun = p  #重要!!! 士兵类中的gun由此赋值!!!
s.fire()
s.fire()
s.fire()
s.fire()
p.add_Bullets()