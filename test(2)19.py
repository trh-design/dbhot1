<<<<<<< HEAD
def reverseArray(arr, start,end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
        
def leftRotate(arr, d):
    n = len(arr)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
    
def printArray(arr):
    for i in range(0, len(arr)):
        print (arr,[i], end='')
        
arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2)
printArray(arr)
=======
from pyecharts import options as opts  
from pyecharts.charts import Bar

# 准备数据
x_data = ['一月', '二月', '三月', '四月', '五月']
y_data = [10,20,15,25,30]

# 创建柱状图
bar_chart = Bar()
bar_chart.add_xaxis(x_data)
bar_chart.add_yaxia("销售额:",y_data)

# 配置全局属性
bar_chart.set_global_opts(
    title_opts = TitleOpts(title="月度销售额柱状图", subtitle="副标题"),
    xaxis_opts=opts.AxisOpts(name="月份")
)
>>>>>>> 97e04fd8f1a7712f6dcc21b0461796cd8cd10568
