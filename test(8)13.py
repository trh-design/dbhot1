class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name, self.age))

class student:
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g
    def speak(self):
        print("%s 说: 我 %d 岁了， 我再读 %d 年级。" %(self.name, self.age, self.grade))


s = student('kem', 10, 60, 3)
s.speak()

class speaker:
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s, 我是一个演说家， 我演讲的主题是 %s" %(self.name, self.topic))

class sample(speaker, student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self, n , a, w, g)
        speaker.__init__(self, n, t)

test = sample("Tim", 25, 80, 4, "python")
test.speak()