<<<<<<< HEAD
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def topologicalSortUtil(self,v,visited,stack):
        
        visited[v] = True
        
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
                
        stack.insert(0,v)
        
    def topologicalSort(self):
        visited = [False]*self.V       
        stack =[]
        
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
                
        print (stack)
        
g= Graph(6)
g.addEdge(5,2);
g.addEdge(5,0);
g.addEdge(4,0);
g.addEdge(4,1);
g.addEdge(2,3);
g.addEdge(3,1);

print ("拓扑排序结果是:")
g.topologicalSort()
=======
# -*- coding : UTF-8 -*-

# Fiename : test.py   
# author by : www.runoob.com 

# 最简单的
print(max(1,2))
print(max('a','b'))

# 也可以对列表和元组使用
print(max([1,2]))
print(max([1,2]))

# 更多实例
print("80,100,1000 最大值为: ", max(80,100,1000))
print("-20,100,400 最大值为: ", max(-20,100,400))
print("-80,-20,-10 最大值为: ", max(-80,-20,-10))
print("0,100,-400 最大值为:", max(0,100,-400))
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
