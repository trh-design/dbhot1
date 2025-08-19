class Person:                    
    def __init__(self, name ,weight):
        self.name = name 
        self.weight = weight 
        
    def __str__(self):
        return "[%s]的当前体重是 %.1f KG " % (self.name, self.weight)
    
    def running(self):
        print("跑了一次步 ! ")
        self.weight = self.weight - 0.5
        
    def eatting(self):
        print("吃了一次饭 ! ")
        self.weight = self.weight + 1
        
        
p = Person('小明', 120)
print(p)
p.running()
p.running()
print(p)
p.eatting()
print(p)