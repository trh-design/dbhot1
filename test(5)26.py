# Person 类
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def play(self):
        print("我可以玩")
        
# Article类
class Article(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def func(self):
        print("我可以放东西")
        
# Fruits 类
class Fruits(object):
    def __init__(self, color, width):
        self.color = color
        self.width = width
    def eat(self):
        print("我可以被吃")
        
        
# lisi
lisi = Person("李思", 18)
print(lisi.name, lisi.age)
lisi.play()

# desk
desk = Article(80, 100)
print(desk.width, desk.height)
desk.func()

# apple
apple = Fruits("red", 10)
print(apple.color, apple.width)
apple.eat()