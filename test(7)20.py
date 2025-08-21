from collections import deque

# 创建一个新队列
queue = deque()

# 向队尾添加元素
queue.append('a')
queue.append("b")
queue.append('c')

print("队列状态:", queue)

first_element = queue.popleft()
print("移除的元素:", first_element)
print("队列状态:", queue)

front_element = queue[0]
print("队首元素:", front_element)

is_empty = len(queue) == 0
print("队列是否为空:", is_empty)

size = len(queue)
print("队列大小:", size)