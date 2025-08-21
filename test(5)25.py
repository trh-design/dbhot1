# 汽车类
class Car(object):
    def __init__(self, color,speed, type):
        self.color = color
        self.speed = speed
        self.type = type
    def move(self):
        print("汽车开始跑了")
        

# BMW_X9 对象
BMW_X9 = Car("red", 80, "F4")
print(BMW_X9.color, BMW_X9.speed, BMW_X9.type)
BMW_X9.move()

# AUDI_A9 对象
AUDI_A9 = Car("black", 100, "S3")
print(AUDI_A9.color, AUDI_A9.speed, AUDI_A9.type)
AUDI_A9.move()