<<<<<<< HEAD
# -*- coding : UTF-8 -*-

# Filename : test py
# author by : www.runoob.com

# 获取用户输入十进制数
dec = int(input("输入数字: "))

print("十进制数为: ", dec)
print("转换为二进制是: ", bin(dec))
print("转换为八进制是: ", oct(dec))
print("转换为十六进制是:", hex(dec))
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
